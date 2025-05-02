# CSSE3100 Question Index
## Questions
|✅|Q|Description|Notes|
|-|-|-|-|
||**Q1**|Recursive weakest precondition|<br/>$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$|
||**Q2**|Loop weakest precondition|<br/><br/>|
||**Q3**|Loop derivation|<br/><br/>|
||**Q4**|Method specification|<br/><br/>
| | **Q5** | Objects<br/>(a) class invariant, <br/>(b) methods|<br/><br/>

## Question Hints

### Question 1 &mdash; Recursive weakest precondition
- Include proof of **decreasing termination metric**!
- For each instruction, apply the rule given in the lectures for that instruction
    - Don't make up your own rule
    - Don't apply short-cut rules, even when the short-cut is "obviously" correct
- Justify any proof steps that aren't simple mathematical or logical simplifications. Always, justify strengthening steps. If in doubt, justify!
- Don't forget to **state/argue that the calculated weakest precondition is implied by the given precondition**.

Additional tips:
- $Q$ is **strengthened** to $P$ whenever $P \Rightarrow Q \wedge \neg (Q \Rightarrow P)$.
- All predicates in a wp proof are over the program state, i.e., inputs, outputs and local variables.
- Any time new information is added to a predicate, that is strengthening, e.g., $x = 0 \wedge y = 1$ is stronger than $x = 0$.
- All strengthening can be rewritten in terms of &&:
    - $n \ge 0$ can be strengthened to $n > 0$ (i.e., $n \ge 0 \wedge n \ne 0$)
    - $x = 0 \vee y = 1$ can be strengthened to $x = 0$ (i.e., $(x=0\vee y=1) \wedge (y \ne 1)$)

### Question 2 &mdash; Loop weakest precondition
- Use one of the **loop design techniques** to come up with the loop invariant using the postcondition of the loop – this is not always the postcondition of the method!
- Don't forget the tips from Question 1!
- Unless you are asked to satisfy "partial correctness" then you should include a termination proof, i.e., "correctness" means **"total correctness"**.

### Question 3 &mdash; Loop derivation

- Tips from Question 2 apply here.
- Follow the process from the lectures, e.g., always end the loop body with `n := n + 1` (where _n_ is your loop counter).
    - *Don't try to write the code first!*
- If asked to satisfy "partial correctness" then your program should still be totally correct, but you don't need to prove termination, i.e., a program that loops forever on some or all cases is *not* acceptable.

### Question 4 &mdash; Method specification
- Be careful not to underspecify, and think about **aliasing**.
    - Make use old() as needed.
- Don't make the precondition stronger than necessary
- If the specification is easier to write in a recursive fashion, define a recursive function and use that in the method specification.
- Don't forget **read and write frames**!

### Question 5 &mdash; Objects

- Follow the standard idiom for frame invariants, and specifications of constructors, functions and methods.
    - Think about whether they need to hold, e.g., input variables added to Repr won't be fresh and make changes to the idiom as required.
- Make sure **abstraction invariants** capture ALL relations between concrete and abstract variables.
- Don't forget about constraints between 2 abstract, or 2 concrete, variables.
- *Specifications should not refer to concrete variables!*