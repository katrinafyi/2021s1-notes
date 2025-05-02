# CSSE3100 Week 11

## Data structures

Consider a class which contains a lazy array. That is, an array which is not populated when it is constructed. The notation `T(0)` denotes a generic type with a default value, e.g. int.

```cpp
class LazyArray<T(0)> {
    ghost var Elements: seq<T>
    ghost const Repr: set<object>
    
    predicate Valid()
        reads this, Repr
        ensures Valid() ==> this in Repr
    
    constructor(length: nat, initial: T)
        ensures Valid() && fresh(Repr)
        ensures |Elements| == length
        ensures forall i :: 0 <= i < |Elements| 
            ==> Elements[i] == initial
}
```

We will also add a variable `ghost const N: nat` because the length of elements never changes. This will simplify code and ensure that the size of elements does not change. 

```cpp
const default: T
const a: array<T>
const b: array<int>
const c: array<int>
var n: int

predicate method IsUpdated(i: natint)
    requires 0 <= i < |Elements| == b.Length == c.Length
    requires 0 <= n <= |Elements|
    reqds this, b, c
{
    0 <= b[i] < n && c[b[i]] == i
}
```

```cpp
predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr && N == |Elements|
{
    // frame invariants
    ...
    // abstraction invariants
    && N == |Elements| == a.Length == b.Length == c.Length 
    && 0 <= n <= N
    && forall i :: 0 <= i < N 
        ==> Elements[i] == if IsUpdated(i) then a[i] else default
}
```

```cpp
constructor (length: nat, initial: T)
    ensure Valid() && fresh(Repr)
    ensures N == length && forall i :: 0 <= i < N
        ==> Elements[i] == initial
{
    N := length;
    Elements := seq(length, _ => initial);
    default := initial;
    a, b, c := new T[length], new int[length], new int[length];
    n := 0;
    Repr := {this, a, b, c};
}
```

We will also add a set of indices which have been updated, adding this to Valid()
```cpp
s == (set i | 0 <= i < N && IsUpdated(i)) && n == |s|
```