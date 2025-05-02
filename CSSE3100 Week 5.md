# Loop invariants
An invariant must be true on entering a loop and must be true after every iteration of the loop (including when we exit the loop).

```cpp
{ J }
while B
    invariant J
{
    { B && J }
    ...
    { J }
}
{ J && !B }
```

Backwards reasoning works by transforming the loop's postcondition to J before the loop, where J is an invariant of the loop.

## Decreases
We need to prove that the termination metric decreases at the end of the iteration compared to the beginning. We also need to ensure that the metric is greater than or equal to zero because it is a termination metric.

```cpp
{ J }
while B
    invariant J
    decreases D
{
    { B && J }
    ghost var d := D;
    
    { J && d > D }
}
{ J && !B }
```