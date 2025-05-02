# CSSE3100 Week 10
Representation set weirdness.

`new;` must be used in the constructor if some variables depend on earlier instance variables.

```cpp
...
predicate Valid()
reads this, Repr
ensures Valid() ==> this in Repr
```

When calling methods on sub-objects which can modify their representation set, we could violate the `g.Repr <= Repr` requirement. To fix this, we can just update Repr with new elements:
```cpp
Repr := Repr + g.Repr + w.Repr;
```

## Summary
```cpp
ghost var Repr: set<object>
```

```cpp
predicate Valid()
    reads this, Repr
    ensures Valid() ==> this in Repr
{
    this in Repr && ...
    // objects with simple frames:
    a in Repr && a.Valid() 
    // objects with dynamic frames:
    b in Repr && b.Repr <= Repr && this !in b.Repr && b.Valid() 
    
    a0 != a1 && {a0, a1} !! b0.Repr !! b1.Repr
}
```

```cpp
constructor() 
    ensures Valid() && fresh(Repr)
{
    ...
    new;
    Repr := {this, a, b} + b.Repr;
}
```

```cpp
function F(x: X): Y
    requires Valid()
    reads Repr
```

```cpp
method M(x: X) returns (y: Y)
    requires Valid()
    modifies Repr
    ensures Valid() && fresh(Repr - old(Repr))
```