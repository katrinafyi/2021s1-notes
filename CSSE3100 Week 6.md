# Program derivation
## Integer square root

```cpp
method SquareRoot(N: nat) returns (r: nat)
    ensures r * r <= N < (r + 1) * < (r + 1)
```

We can break out specification into two conjunctions:
```
r * r <= N && N < (r + 1) * (r + 1)
```
We do this because part of the invariant will be the guard and part will be invariant. 
> **Technique 1.** Given a postcondition $A \wedge B$, choose an invariant as $A$ and the guard as $\neg B$.

> **Technique 2.** (Programming by wishing.) Suppose we have a quantity $Q$ with the intention of establishing and maintaining the invariant $Q=q$ for some expression $q$.

> **Technique 3.** Replace a constant by a variable. For a loop which needs to establish something in terms of a constant $C$, use a loop variable $k$ which changes until it equals $C$ and make the expression with $k$ a loop invariant.

> **Technique 4.** If we have a postcondition $p= F(n)$, we can add a "what's yet to be done" invariant of the form $p \odot F(n-i)=F(n)$ where $\odot$ is some kind of operation.

> **Technique 5.** Use the postcondition. To establish $Q$, we can make $Q$ a loop invariant. This is most useful when there are multiple postconditions.

> **Technique 6.** Weak the postcondition by disjoining a predicate $R$. For example, to establish $Q$ use a loop variant of $Q \vee R$.