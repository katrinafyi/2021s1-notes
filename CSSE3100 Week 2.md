# Control flow
Recall that using backwards reasoning, we start from the bottom and use the weakest precondition needed to satisfy the postcondition after executing a particular statement. This can be written as
```
precondition = wp(statement, postcondition)
```
in the Hoare triple of the form
```
{ precondition }
statement;
{ postcondition }
```

## Sequential composition
```
{ y < 10 }
{ forall x :: y < 10 }
var x;
{ y < 10 }
x := y;
{ x < 10 }
y := 0;
{ x < 10 }      wp(z:=x, z<10)
z := x;
{ z < 10 }
```

More generally,
```
wp(S; T, Q) = wp(S, wp(T, Q))
```

## Conditional control flow
```
if B { S } else { T }
```
We need to consider both branches depending on the condition. For example,
```
wp(if x % 2 == 0 { y := y + 3; } else { y := y - 1; }, y == 4)
= (x % 2 == 0 ==> y + 3 == 4)
  && (x % 2 != 0 ==> y - 1 == 4)
```
More generally,
```
wp(if B { S } else { T }, Q) =
    (b ==> wp(S, Q)) && (!B ==> wp(T, Q))
```

## Implications
An implication can be replaced with a disjunction.
$$
A \implies B \iff \neg A \vee B
$$
We can also simplify predicates with
$$
A \implies (B \implies C) \iff (A \wedge B) \implies C.
$$

# Method calls

Given a method
```c
method M(x: X) returns (y: Y)
    requires P
    ensures R
{
    body
}
```
we need to prove that `P ==> wp(body, R)`.

Methods are opaque. That is, we reason about them only in terms of their specifications, not their implementations.

Given a method M with requires P ensures R and postcondition Q, the weakest precondition needed to imply Q is:

```c
wp(t := M(E), Q) = P[x\E] && forall y' :: R[x,y \ E,y'] ==> Q[t\y'].
```

Intuitively,
$$
\begin{aligned}
&\text{method precondition with argument} \\
&\wedge~\operatorname*{forall} r':: \text{method postcondition with }r' \implies \text{following postcondition}.
\end{aligned}
$$

## One-point rule
```c
(forall y :: y == E ==> P) <==> P [y\E]
```