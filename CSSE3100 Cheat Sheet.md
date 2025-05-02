# CSSE3100 Cheat Sheet
## Weakest Preconditions
$\operatorname{wp}(E, Q)$ denotes the weakest precondition of **E** which can imply **Q**.

**Assignment**
```cpp
{ Q[x\E] } x := e { Q }
```

**Variable introduction**
```cpp
{ forall x :: Q } var x { Q }
```

**Sequences**
```cpp
(S; T, Q) = wp(S,  wp(T, Q))
```

**Conditional**
```cpp
{ (B ==> wp(S, Q)) && (!B ==> wp(T, Q))}
if B then S else T
{ Q }
```

**Method Call**
```cpp
method M(x: int) returns (y: int)
    requires P
    ensures R
```


Substitute variables and expressions for `E` and `x` where needed.
```
{ P && forall t :: R ==> Q}
t := M(E);
{ Q }
```

**Loops**
```js
{ J }
while B
    invariant J
    decreases D
{
    { B && J }
    ghost var d0 := D;
    ...
    { J }, { D < d0 }
}
{ J && !B }
```
## Implications
$$
\begin{aligned}
A &\implies B &\iff&\neg A \vee B \\ 
A &\implies \text{true} &\iff& \text{true} \\
A &\implies \text{false}&\iff& \neg A\\
\text{true} &\implies B& \iff & B \\ 
\text{false} &\implies B &\iff& \text{true}
\end{aligned}
$$
Additionally,
$$
A \implies (B \implies C)\quad \iff \quad(A \wedge B) \implies C.
$$
### One-point rule
If the implication restricts to a single point, we can substitute the value of that point into the expression.
$$
(\operatorname{forall }x:: y =E \implies P) \iff P[y\backslash E]
$$

### Implications with conjunctions
$$
\begin{aligned}
(A \vee B) &\implies C &\iff&(A \implies C) \wedge(B \implies C) \\ 
\operatorname{forall} x &::A \wedge B &\iff& (\operatorname{forall} x ::A) \wedge (\operatorname{forall} x ::B)
\end{aligned}
$$

### Extras
$$
\begin{aligned}
\neg (A \vee B) &&\iff& \neg A \wedge \neg B \\
\neg (A \wedge B) &&\iff& \neg A \vee \neg B \\\\
 (A \wedge B) \vee C &&\iff& (A \vee C) \wedge (B \vee C) \\
 (A \vee B) \wedge C &&\iff& (A \wedge C) \vee (B \wedge C) \\\\
A \wedge(A \implies B) &&\iff&A \wedge B
\end{aligned}
$$

## Termination Metrics
- **Partial correctness**: A program is partially correct if it gives the right result whenever it terminates.
- **Total correctness**: A program is totally correct if it always terminates and gives the right result. 

### Orders

| type        | $X \succ x$           | example  |
| ------------- |-------------| ----|
| bool      | $X, ~\neg x$ | true decreases to false (like ints) |
| int      | $X \ge 0,~ X > x$      |   non-negative less |
| real | $X \ge 0.0,~ x \le X - 1.0$      |    decreases by at least $1$ |
|set\<T\>|$x \subset X$|strict subset|
|seq\<T\>|$x$ is a consecutive subsequence of $X$ | $[a, b, c] \succ [b, c]$

**Tuples**
A tuple is compared element-wise. Shorter tuples compare _greater_ than longer tuples if they have the same prefix.

## Loops

- (1) **Look in the postcondition** (for the invariant and negation of the guard).
- (2) **Programming by wishing** (for a variable of a required value).
- (3) **Replace a constant** (in the postcondition) by a variable (to get the invariant).
- (4) (Thinking about) **What's yet to be done** (rather than what has been done).
- (5) **Use the postcondition** (as an invariant).
- (6) **Weaken the postcondition** (by disjoining (||) another predicate to get the invariant).

## Sequences
```js
var s := [6, 28, 496];
assert s[2] == 496;
assert |s| == 3;
assert s + [8128] == [6, 28, 496, 8128];

var p := [1, 5, 12, 22, 35]
assert p[2..4] == [12, 22];
assert p[..2] == [1, 5];
assert p[2..] == [12, 22, 35];

// array to sequence
a := new int[3];
a[0], a[1], a[2] := 6, 28, 496;
s, p := a[..], a[..2];
assert s == [6, 28, 496] && p == [6, 28];
```

## Maps
```js
// map<U, V>
var m := map[4 := 5, 5 := 6]
assert m[4] == 5;
```

```js
map i | 0 <= i < 10 :: 2*i
```


## Objects

```js
ghost var Repr: set<object>
```

```js
constructor ()
    ensures Valid() && fresh(Repr)
    { ... new; Repr := {this, a, b} + b.Repr; }
```


```js
function F(x: X): Y
    requires Valid()
    reads Repr
```

```js
method M(x: X) returns (y: Y)
    requires Valid()
    modifies Repr  // if mutating
    ensures Valid() && fresh(Repr – old(Repr))
```

