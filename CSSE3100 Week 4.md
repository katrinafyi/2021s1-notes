# Lemmas

Lemmas look like methods. A lemma is a property that we would like the verifier to use during its proofs.
```cpp
function method More(x: int): int {
    if x <= 0 then 1 else More(x - 2) + 3
}

lemma Increasing(x: int)
    ensures x < More(x)
```

Lemmas can be "called" just like methods. This signals to the verifier that at that point, the lemma holds. Lemmas without a body are used to specify something you know to be true and is not verified by the checker.

The body of a lemma should be used to convince Dafny that the lemma is true. This can be done via induction.
```cpp
lemma Increasing(x: int)
    ensures x < More(x)
{
    if x <= 0 {
        // base case is trivial.
    } else {
        Increasing(x-2);
    }
}
```

```cpp
lemma DivisionLemma(n: int, d: int)
    requires n > 0 && d > 1
    ensures n / d < n
{
    if n == 1 {} // proved automatically.
    else {
        DivisionLemma(n-1, d);
    }
}
```