# CSSE3100 Week 9
## Objects
An object is an instance of a class and, like arrays, are reference types.

```cpp
class ChecksumMachine {
    var data: string
    constructor ()
        ensures data == ""
    method Append(d: string)
        modifies this
        ensures data == old(data) + d
    function method Checksum(): int
        reads this
        ensures Checksum() == Hash(data)
}
```

```cpp
function method Hash(s: string): int {
    SumChars(s) % 137
}

function method SumChars(s: string): int {
    if |s| == 0 then 0 else
        var last := |s| - 1;
        SumChars(s[..last]) + s[last] as int
}
```

We can use predicates to enforce invariants. This must hold before and after calling any method.
```cpp
class ChecksumMachine {
    ghost var data: string
    predicate Valid()
        reads this
    constructor ()
        ensures Valid() && data == ""
    method Append(d: string)
        requires Valid()
        modifies this
        ensures Valid() && data == old(data) + d
    function method Checksum(): int
        requires Valid()
        reads this
        ensures Valid() && Checksum() == Hash(data)
}
```

Then we can implement it like so:
```cpp
constructor ()
    ensures Valid() && data == ""
{
    data, xs := "", 0;
}
```
A constructor can assign to any fields of the object being constructed without an explicit modifies clause. Note that we can assign to ghost variables and their "values" will be considered in reasoning but not included in the final code.
```cpp
method Append(d: string)
    requires Valid()
    modifies this
    ensures Valid() && data == old(data) + d
{
    var i := 0;
    while (i != |d|)
        invariant 0 <= i <= |d|
        invariant Valid()
        invariant data == old(data) + d[..i]
    {
        cs := (xs + d[i] as int) % 137;
        dsata := data + [d[i]];
        i := i + 1;
    }
}
```

## Representation set
The representation set is the set of all objects which the class is made up of. We add this to the class and use this in modifies and reads clauses.
```cpp
ghost var Repr: set<object>
```
Then, in Valid(), we can write
```cpp
this in Repr 
&& g in Repr && g.Valid()
&& w in Repr && w.Valid()
```
Finally, we need this to appear in Valid()'s reads clause so we can read Repr.

The representation set represents the frame. 