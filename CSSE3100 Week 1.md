
Dafny precedence can be remembered by the shorter operators bind first. 
There are also universal quantifiers "forall x" and existential quantifiers "exists x".

The **program state** refers to program variables. Note that not all program variables are in scope from the start.

This is useful because of something called **Flyod logic**. Instead of reasoning about individual states, we reason about predicates which capture ranges of states.

If the precondition does not hold, we don't care what happens. This can be expressed precisely as the preconditions imply the postconditions.

We will not be learning forward reasoning in this course. The less obvious way is to do backwards reasoning.

For predicates $P$, $Q$ and program $S$, the **Hoare triple** { P } S { Q } says that if $S$ is started in any state satisfying $P$, then $S$ will not crash and will terminate in some state satisfying $Q$. 

Forward reasoning constructs the strongest postcondition. That is the postcondition which implies all of the others. We say $A$ is stronger then $B$ of $A \implies B$.

With backwards reasoning we derive the weakest precondition possible. This allows it to be implied by the most potential preconditions.

### Weakest precondition for variable declaration
The weakest precondition of declaration just adds a forall quantifier. This is often combined with an assignment.
```c
{ forall x :: Q }
var x;
{ Q }
```

### Weakest precondition for assignment
Given `{ ? } x := E { Q }`, we construct `?` by replacing each x in Q with E, denoted $Q[x\E]$. For example, with
```
{ ? } y := a + b { y >= 25 }
```
the `{?}` should be $a + b \ge 25$.

**Example.** Consider swapping two variables. We will introduce *logical variables* which aren't present in the program but will aid in reasoning.
```
{ x == X && y == Y}

{ y == Y && x == X }
tmp := x;
{ y == Y && tmp == X }
x := y;
{ x == Y && tmp == X }
y := tmp;
{ x == Y && y == X }
```
The last step is to show that the given precondition implies the weakest required precondition. Here, that is trivially true.

**Example.** Consider version 2 of swap.
```
{ x == X && y == Y }

{ y-(y-x) + (y-x) == Y && y-(y-x) == X }
x := y - x;
{ y-x + x == Y && y-x == X }
y := y - x;
{ y + x == Y && y == X }
x := y + x;
{ x == Y && y == X }
```
The constructed precondition does, in fact, simplify to $y == Y && x == X$. We are also allowed to strengthen the conditions as we go backwards (but not weaken them!). 

### Simultaneous assignments
Dafny allows several assignments in one statement. For example,
```
x, y := x + y, x - y;
```
This means all the right-hand sides are computed before any variables are assigned. 