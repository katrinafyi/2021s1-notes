# Recursion
To reason about a method call, we can handle it like any other method call. The basic idea why this works is that method calls are opaque. We don't look at the code, we only look at the specification.

```c
method Mult(x: int, y: int) returns (r: int)
    requires 0 <= x && 0 <= y
    ensures r == x * y
{
    if (x == 0) {
        r := 0;
    } else {
        var x := Mult(x - 1, y);
        y := z + y;
    }
}
```

Consider this recursive function. The conditions are sound but it clearly does not terminate.
```c
method PartialId(x: int) returns (y: int)
    ensures y == x
{
    if x % 2 == 0 { y := x; } else { y := PartialId(x); }
}
```

# Correctness
For predicates P and Q and program S, the Hoare triple `{P} S {Q}` says that if S is started in any state that satisfies P, then S will not crash (or do other bad things) and will *terminate* in a state satisfying Q.

- **Partial correctness:** A program is partially correct if it gives the right result whenever it terminates.
- **Total correctness:** A program is totally correct if it always terminates with the correct result.

# Termination metric
We can add a clause to the method declaration like
```c
function Fib(n: nat): nat
    decreases n
{
    if n < 2 then n else Fib(n - 2) + Fib(n - 1)
}
```

## Well-founded orders
Termination metrics don't need to be natural numbers. Any set of values with a well-founded order can be used. That is, an order which is:
- irreflexive, so $a \succ a$ never holds,
- transitive, so $a \succ b$ and $b \succ c$ implies $a \succ c$, and 
- there is no infinite descending chain.

A termination metric is sometimes called a variant in literature.

## In Dafny
Dafny has a number of well-founded orders:
- bool, with true decreasing to false,
- int (non-negative),
- real (non-negative),
- set, with proper subsets, and
- seq, with consecutive proper subsequences getting shorter (e.g. $[a,b,c] \succ [b,c]$)

```c
function F(x: int): int {
    if x < 10 then x else F(x - 1)
    decreases x
}

function H(x: int): int {
    if x < -60 then x else H(x - 1)
    decreases x - 60
}
```

This can be tricky to come up with. We just need something which is decreasing each time. This is something like a count of the total number of recursive calls.

# Lexicographic Tuples

A lexicographic tuple is a tuple which is compare by comparing elementwise, left to right.

For example, $(4, 12) > (4, 11)$ but $(3, 100) < (4, 10)$. A tuple which is a prefix of another compares greater.

#example Suppose we have $n$ courses before graduation, numbered $n-1$ to $0$. The method
```c
method RequiredStudyTime(c: nat) returns (hours: nat)
```
returns the number of hours required to study course $c$.

Consider this function which simulates studying until graduation. Note that we can't do the same thing as earlier because we don't know how much RequiredStudyTime would increase the hours by.

![[Pasted image 20210309161646.png]]

#example Consider the Ackermann function. This is used to show that not every totally recursive function is primitive recursive. That is, it can't be implemented using loops with a fixed number of iterations. The question we'd like to ask is does this terminate.

In fact, yes with termination metric $(m,n)$. We can see that all recursive calls either decrease $m$, or for the inner call $\operatorname{Ack}(m,n-1)$ decreases $n$.

![[Pasted image 20210309162033.png]]

# Mutually recursive functions

Here, StudyPlan is called with a number which represents the number of courses completed. Learn is called with the number of courses completed and hours remaining in the current course.

We need the termination metric of the recursive calls to be greater than their recursive call. For example, in StudyPlan,
$$
40 - n \succ (40 - n, \operatorname{RequiredStudyTime}n).
$$

![[Pasted image 20210309162623.png]]

# Subcomputations

The following function calculates $2^n -1 $.
```c
function ExpLess1(n: nat): nat {
    if n == 0 then 0 else 2 * ExpLess1(n-1) + 1
}
```
Clearly, this terminates because it decreases $n$. What if we refactored the else branch into a function ExpLess2 which calculates $2^n-2$?

Then,
```c
function ExpLess1(n: nat): nat {
    if n == 0 then 0 else ExpLess2(n) + 1
}
```

However, the termination metric from ExpLess1 to ExpLess2 are both the same, $n \not\succ n$. To fix this, we can make the termination metric of ExpLess1 to be $(n,1)$ and the termination metric of ExpLess2 $(n,0)$.

# Default decreases

Dafny will choose a termination metric by default if nothing is specified. This defaults to all a function's arguments in the order specified.