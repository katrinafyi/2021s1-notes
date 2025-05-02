
**What is functional programming?**

- Programs in the functional paradigm are comprised of expressions which are themselves comprised of constants, names, and functions.
- Functions are expressions which apply to an input and can be reduced.
- Mathematical functions are pure and satisfy referential transparency.

**What is programming?**

- Programming is combining maching instructions into an algorithm to make it do _something_.
- Computable functions are those which are decidable by a Turing machine. All computing devices are essentially Turing machines.

**Language paradigms**

- Imperative: an explicit, ordered, sequence of commands written which instructs _how_ the computation takes place.
- Object-oriented: objects have their own internal state and public interfaces.
- Declarative: a structured query is written, so the result is specified rather than the method for computing it.
- Functional: the "instruction set" is limited to function creation and execution.

Functional programming is just another way of instructing the compiler to output machine code which performs a particular task.

### Definitions
A relation $R$ is a **function** when
$$
(a,y)\in R \wedge(a, z) \in R \implies y = z.
$$

Functions can be over functions. For example, $\mathcal R$ is a function.
$$
\mathcal R = \left\{ (R, \top) : (R \subset \mathbb N \times \mathbb N) \wedge R \text{ is a function} \right\}
\cup\left\{ (R, \bot) : (R \subset \mathbb N \times \mathbb N) \wedge R \text{ is not a function} \right\}
$$

### Functions vs `Functions`

Functions in imperative programming are not mathematical functions. A function which modifies a global variable easily demonstrates this. Consecutive but identical calls can return different things. This violates something called *referential transparency*.

An expression is called **referentially transparent** if it can be replaced with its corresponding value without changing the program's behaviour. An expression satisfying referential transparency is called **pure**. 

Functional programming is a *commitment* to *purity*.

Paul wants us to learn Haskell because most programming languages are semi-functional. He wants us to derive pleasure finding recursive solutions to problems.

### Lambda Calculus

We get to write symbols on the board which make us look like geniuses. Haskell is a lambda calculus.

A **lambda calculus** is a formal system in mathematical logic expressing computation with function abstractions and applicationsu sing variable binding and substitution.

The lambda calculus is *Turing complete* because it can simulate a turing machine.

The lambda calculus was introduced by Alonzo Church (a mentor and influence of Alan Turing) in the 1930s. 

Every program in Haskell can be translated into a lambda expression.

A lambda expression is yet another way of denoting functions. For example, with the function $ax^2+bx+c$ we can express in three ways:
- tuples: $R = \left\{ (x, ax^2+bx+c) : c \in \mathbb Q \right\}$.
- functional: $f(x) = ax^2 + bx + c$.
- lambda: $\lambda x.\ ax^2 + bx + c$.

Note that the lambda expression has no name. It is always an *anonymous function*. 

A **calculus** generally is an abstract theory developed in a formal way.

A **lambda calculus** is a formal logic for codifying computations which boils down to
- constructing $\lambda$-terms (or expressions), and 
- reducing $\lambda$-terms.

Haskell _is_ a lambda calculus.

The set of all **lambda terms** (or **lambda expressions**) is denoted  $\Lambda$ and can be generated as:
> Let $V$ be the set of all variables or names (stateless).
> - Variables: $x \in V \implies x \in \Lambda$.
> - Abstractions: $x \in V \wedge M \in \Lambda$
> TODO

**Binding/substitution**
When evaluating a function in the normal way, we _bind_ the name $x$ to some value $2$ when evaluating $f(2)$. In the lambda calculus, we can write this as
$$
(x^2 + x + a)[x:=2] = 2^2 + 2 + a
$$
Note that $a$ is not bound so it is a **free variable**.

**Reductions**
There are two reductions we can do on lambda terms.

Renaming a variables ($\alpha$-conversion): $(\lambda.xM[x]) \to (\lambda.yM[y])$.

Function application ($\beta$-reduction): $(\lambda x.M) E \to M[x:=E]$. This replaces a bound variable with the argument inside the body of the abstraction.

Two lambda expressions that are identical after $\alpha$-conversion (variable renaming) are said to be $\alpha$-equivalent.

**Rules for evaluating**
- Application has higher precedence than abstraction (we do application first). $\lambda x.A B$ means $\lambda x.(A B)$ and not $(\lambda x.A) B$.
- Application is left-associative. $A B C$ means $(A B) C$.
- Abstraction is right-associative. $\lambda x.A\ \lambda y.B$ means $\lambda x. (A \lambda y.B)$.

Example:
$$
\begin{aligned}
(\lambda x.\lambda y.xyy) (\lambda a.a)b &= (\lambda y.xyy)[x:=\lambda a.a]b &&\text{beta-reduction}\\ 
&= (\lambda y.(\lambda a.a)yy)b &&\text{bind} \\ 
&= ((\lambda a.a)yy)[y:=b] &&\text{beta-reduction}\\ 
&= (\lambda a.a)bb &&\text{bind}\\ 
&= (a)[a:=b]b &&\text{beta-reduction}\\ 
&= b b &&\text{bind}
\end{aligned}
$$

The **free variables** of an expression are those not bound by an expression. This can be defined indictively.

A **combinator** is a lambda expression with *no* free variables. They are called as such because they combine arguments. 

A term which cannot be reduced any further is said to be in **$\beta$-normal form**. This can be considered the fully executed functional program.

If a term cannot be reduced to a $\beta$-normal form, it is said to be divergent. As an example, the expression $(\lambda x.xx)(\lambda x.xx)$ diverges because
$$
\begin{aligned}
(\lambda x.xx)(\lambda x.xx) &= (\lambda y.yy)(\lambda x.xx) \\ 
&= (yy)[y:=\lambda x.xx]\\
&= (\lambda x.xx)(\lambda x.xx)
\end{aligned}
$$