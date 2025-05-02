# CSSE3100 Week 12

We are creating a map.

```cpp
class Map<Data> {
    ghost var M: map<int, Data>
    ghost var Repr: set<object>
    
    predicate Valid()
        reads this, Repr
        ensures Valid() ==> this in Repr
    
    constructor() 
        ensures Valid() && fresh(Repr)
        ensures M == map[]
}
```

We will create an optional sum type:
```cpp
datatype Option<T> = None | Some(T)
```
This is needed when the type T is a primitive. Otherwise, we can append ? to get a nullable reference type.

```cpp
function method Lookup(key: int): Option<Data>
    requires Valid()
    reads Repr
    ensures key in M.Keys ==> Lookup(key) == Some(M[key])
    ensures key !in M.Keys ==> Lookup(key) == None
    
function method Add(key: int, value: Data)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures M == old(M)[key := value]
```

## Implementation
```cpp
ghost var M: map<int, Data>
ghost var Repr: set<objetc>
var root: Node?<Data>

class Node<Data> {
    ghost var M: map<int, Data>
    ghost var Repr: set<object>
    var key: int
    var value: Data
    var left: Node?<Data>
    var right: Node?<Data>
}
```

## Invariant
```cpp
predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
{
    this in Repr && 
    (|M.Keys| == 0 ==> root == null) &&
    (|M.Keys| != 0 ==> root in Repr
        && root.Repr <= Repr
        && this !in root.Repy
        && root.Valid() 
        && root.M == M)
}
```

Invariant for Node:
```cpp
predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
{
    this in Repr 
    && (left != null ==> left in Repr 
        && left.Repr <= Repr
        && this !in left.Repr
        && left.Valid() 
        && Less(left.M.Keys, {key}))
    && (right != null ==> [as above])
    && (left != null && right !+ null ==> left.Repr !! right.Repr)
    && M == Union(Union(map[key := value]), left), right)
}
```

Used to ensure left/right subtrees are all less/larger respectively.
```cpp
predicate Less(s: set<int>, b: set<int>) {
    forall x, y :: x in a && y in b ==> x < y
}
```

This performs a union of the map m and the map inside n, preferring m if the key appears in both.
```cpp
function Union<Data>(m: map<int, Data>, n: Node?<Data>): map<int, Data>
    reads n
{
    if n == null then m
    else map k | k in m.Keys + n.M.Keys :: if k in m.Keys then m[k] else n.M[k]
}
```

Node constructor
```cpp
constructor (key: int, value: Data)
    ensures Valid() && fresh(Data)
    ensures M == map[key := value]
    
function method Lookup(key: int): Option<Data>
    requires Valid() 
    reads Repr
    ensures key in M.Keys ==> Lookup(key) == Some(M[key])
    ensures key !in M.Keys ==> Lookup(key) == None
    
method Add(key: int, value: Data)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures M == old(M)[key := value]
    decreases Repr // need this explicitly.
    
method Remove(key: int)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
    ensures M == old(map k | k in M.Keys && k != key :: M[k])
```

Remove is more complicated because it actually returns a new node which may appear in the place of the node it was called on.

```cpp
method Remove(key: int) returns (n: Node?<Data>)
    requires Valid()
    modifies Repr
    ensures n != null ==> n.Valid() && n.Repr <= old(Repr)
    ensures var newMap :=
        old(map k | k in M.Keys ** k != key :: M[k]);
        (|newMap.Keys| == 0 ==> n == null)
        && (|newMap.Keys| != 0 ==> n != null && n.M == newMap)
```

## Iterators

```cpp
class Iterator<Data> {
    // note the non-ghost variable bst.
    const bst: Map<Data>
    ghost var RemainingKeys: set<int>
    
    predicate Valid()
        reads this, Repr
        ensures Valid() ==> this in Repr && bst.Valid() &&
            RemainingKeys <= bst.M.Keys

    constructor (bst: Map<Data>)
        requires bst.Valid()
        ensures Valid() && fresh(Repr - bst.Repr)
        ensures this.bst == bst && RemainingKeys == bst.M.Keys
}
```

```cpp
method GetNext() returns (r: Option<(int, Data)>)
    requires Valid()
    modifies Repr - bst.Repr
    ensures Valid()
    ensures match r
        case None => old(RemainingKeys) == RemainingKeys == {}
        case Some((k, val)) =>
            k in old(RemainingKeys) && bst.M[k] == val &&
            RemainingKeys == old(RemainingKeys) - {k}
```

Stack:
```cpp
datatype List<T> = Nil | Cons(T, List<T>)

var stack: List<Node<Data>>
```

```cpp
predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr && bst.Valid() &&
            RemainingKeys <= bst.M.Keys
{
    this in Repr && bst in Repr 
    && bst.Repr <= Repr 
    && this !in bst.Repr && bst.Valid() 
    && RemainingKeys <= bst.M.Keys 
    && SValid(stack, RemainingKeys)        
}
```

```cpp
// R is remaining keys
predicate SValid(st: List<Node<Data>>, R: set<int>)
    reads bst, bst.Repr
{
    match st
        case Nil => R == {}
        case Cons(node, next) => 
            node in bst.Repr && node.Repr <= bst.Repr
            && node.Valid()
            && (forall k :: k in node.M.Keys 
                ==> k in bst.M.Keys && bst.M[k] == node.M[k])
            // the node and everything to its right is in remaining keys
            var m := Union(map[node.key := node.value], node.right);
            m.Keys <= R && SValid(next, R - m.Keys)
}
```

```cpp
method Push(n: Node?<Data>)
    requires bst.Valid() && this !in bst.Repr
    requires SValid(stack, RemainingKeys)
    requires n != null ==> 
        n in bst.Repr && n.Repr <= bst.Repr && n.Valid()
    requires n != null ==>
        forall k :: k in n.M.Keys ==> 
            k in bst.M.Keys && bst.M[k] == n.M[k]
    requires n != null ==> RemainingKeys !! n.M.Keys
    modifies this
    ensures SValid(stack, RemainingKeys)
    ensures RemainingKeys == old(RemainingKeys)
        + if n == null then {} else n.M.Keys
{
    if (n != null) {
        stack := Cons(n, stack);
        ghost var m := Union(map[n.key := n.value], n.right);
        RemainingKeys := RemainingKeys + m.Keys;
        Push(n.left);
    }
}
```

Decreases clause needs to consider for if n is null, so we union it with an empty map.
```cpp
decreases set k | k in Union(map[], n)
```

```cpp
constructor (bst: Map<Data>)
    requires bst.Valid()
    ensures Valid() && fresh(Repr - bst.Repr)
    ensures this.bst == bst && RemainingKeys == bst.M.Keys
{
    this.bst := bst;
    stack, RemainingKeys := Nil, {};
    Repr := {this} + bst.Repr;
    new;
    Push()
}
```

```cpp
method GetNext() returns (r: Option<(int, Data)>)
{
    match stack
        case Nil => return None
        case Cons(node, next) => 
            r := Some((node.key, node.value));
            ghost var m :=
                Union(map[node.key := node.value], node.right);
            stack, RemainingKeys := next, RemainingKeys - m.Keys;
            Push(node.right);
}
```