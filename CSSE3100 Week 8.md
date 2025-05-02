# CSSE3100 Week 8

## Canyon Search

Given two arrays, finds the minimum distance from some value in the first array to some value in the second array.

```cpp
function method Dist(x: int, y: int): nat
{
    if x < y then y - x else x - y
}

method CanyonSearch(a: array<int>, b: array<int>) returns (d: nat)
    requires a.Length != 0 && b.Length != 0
    requires forall i,j :: 0 <= i < j < a.Length ==> a[i] <= a[j]
    requires forall i,j :: 0 <= i < j < b.Length ==> b[i] <= b[j]
    ensures exists i,j :: 
        0 <= i < a.Length && 0 <= j < b.Length
        && d == Dist(a[i], b[j])
    ensures forall i,j :: 
        0 <= i < a.Length && 0 <= j < b.Length
        ==> d <= Dist(a[i], b[i])
{
    d := Dist(a[0], b[0]);
    var m,n := 0,0;
    while (m < a.Length && n < b.Length)
        invariant exists i,j :: 
            0 <= i < n && 0 <= j < m
            && d == Dist(a[i], b[j])
    {
        
    }
}
```

## Modifying arrays
Our heap-allocated storage is passed by reference. We can add a `modifies` clause to specify that this modifies the variable.

This is maintained when assigning references to other variables.

The expression `old(E)` denotes the value of E upon entry to the method. This is useful when working with methods which modify their arguments. This only affects heap references in its expression argument.

If a new array is created, then the new array can be modified arbitrarily without a modifies clause. We can use `fresh(E)` to denote that E must be a newly allocated object.

If a function access the elements of an array, its specification must include a `reads` clause.

## Initialising arrays
```cpp
method InitArray<T>(a: array<T>, d: T)
    modifies a
    ensures forall i :: 0 <= i < a.Length ==> a[i] == d
{
    var n := 0;
    while (n != a.Length)
        invariant 0 <= n <= a.Length
        invariant forall i :: 0 <= i < n ==> a[i] == d
    {
        
    }
}
```

### Initialising matrices

```cpp
method InitMatrix<T>(a: array2<T>, d: T)
    modifies a
    ensures forall i,j :: 0 <= i < a.Length0 && 0 <= j < a.Length1 
        ==> a[i,j] == d
{
    var m := 0;
    while (m != a.Length0)
        invariant 0 <= m <= a.Length0
        
}
```

## Selection sort
```cpp
method SelectionSort(a: array<int>)
    modifies a
    ensures forall i,j :: 0 <= i < j < a.Length ==> a[i] <= a[j]
    ensures multiset(a[..]) == old(multiset(a[..]))
```
Here, multiset is used as an unordered set where values may occur more than once.