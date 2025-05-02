# Arrays
Arrays are references.
```cpp
var a := new string[20];
a[y] := "hello";
var b := a;
assert b[7] == "hello";
b[7] := "hi"; // modifies 'a' as well.
```
We can also create a new array using the "new" operator.

## Multidimensional arrays
```cpp
var m := new bool[3,10];
assert m.Length0 == 3 && m.Length1 == 10;
```

# Sequences
Arrays are *mutable reference* types. Sequences are immutable value types. We declare sequences with `seq<T>`.

```cpp
var s := [6,28,496];
assert s[2] == 496;
assert |s| == 3;
assert s + [8128] == [6, 28, 496, 8128];
```

We can also take slices using `a[2..4]` for example. This also works for taking slices of arrays.

## Linear search
Here, P is a predicate taking a T and returning a boolean.
```cpp
method LinearSearch0<T>(a: array<T>, P: T -> bool)
    returns (n: int)
    ensures 0 <= n <= a.Length
    ensures n == a.Length || P(a[n])
{
    n := 0;
    while n != a.Length
        invariant 0 <= n <= a.Length
    {
        if P(a[n]) {
            // return goes to the end of the method 
            // then we need to prove the postcondition.
            return; 
        }
        n := n + 1;
    }
}
```

To reason about "return", we just need the full postcondition immediately above the return.

However, this postcondition is not precise enough. The trivial program `n := a.Length` will satisfy the requirements. We need to add a quantifier of the form
```cpp
forall x: nat :: x >= 5 ==> Fib(x) >= 5
```

We will add this to our linear search:
```cpp
ensures n == a.Length ==>
    forall i :: 0 <= i < a.Length ==> ! P(a[i])
```

# Existential quantifier
There is an exists keyword which we use like
```cpp
exists x: int :: x >= 0 && Fib(x) == 144
```

In the context of linear search,
```cpp
method LinearSearch3<T>(a: array<T>, P: T -> bool) returns (n: int)
    requires exists i :: 0 <= i < a.Length && P(a[i])
    ensures 0 <= n < a.Length && P(a[n])
```