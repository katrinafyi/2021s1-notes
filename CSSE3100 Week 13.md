# CSSE3100 Week 13

## Revision
Weakest precondition:
- basic backwards reasoning
- method calls
- branches

Recursion:
- termination metrics
    - lexicographic tuples

Loops:
- guard, invariant, decreases, invariant and negation of guard.
- termination metric (similar to recursion)

Loop design:
- postcondition
- wish for a variable of the required value
- replace a constant by variable
- what's yet to be done?
- use postcondition as invariant
- weaken postcondition (e.g. with `||`)

Arrays:
- specify preconditions and postconditions
- preconditions as weak as possible

Objects:
- representation set
- object invariants as Valid() predicate
- frame invariants

Data structures:
- abstract specification for client, in terms of ghost variables
- no concrete variables in specifications
- related via abstraction invariants in Valid() predicate

Exam: 
- open book
- don't bring in big pile of paper
- 5 questions, very similar to last year

### 2020 final exam
1. Weakest precondition of method, no loops.
    - Marks for rule in each line of code.
    - State why precondition implies postcondition.
    - Don't short cut rules.
    - Strengthening: all strengthening can be written as `&&`. Q is strengthened to P if $P \implies Q \wedge \neg (Q \implies P)$.
2. Loop weakest precondition proof.
    - Apply loop design tips.
    - Include termination.
3. Derive a program from its specification.
4. Specifying a method given a description.
    - Uses arrays.
    - Don't forget about aliasing.
    - Reads and writes.
5. Data structures.
    1. Specifying invariant and methods.