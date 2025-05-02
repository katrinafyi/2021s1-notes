
## Introduction

**Linear algebra** can be thought of as the study of matrices, vector spaces, and "flat" objects. That is, objects without curvature. We can solve a lot of problems using linear algebra.

All the operations we want to do in linear algebra can be reduced to linear equations. We can exploit nice properties which they have. A linear equation is solved by "something that looks flat".

**Number theory** is the study of prime numbers and what numbers divide other numbers. By using prime numbers and their properties, we can build up other interesting objects to help us study the relation between different numbers.

In fact, the famous Riemann hypothesis with a million prize is related to the distribution of prime numbers. Another famous open problem is can you find two prime numbers which differ by exactly two? For example, 3 and 5, then 5 and 7 satisfy this but when is the next pair? As numbers become large, they're less likely to be prime and so it becomes harder to find prime numbers.

The twin prime conjecture says that you can find arbitrarily large prime numbers whose difference is two. This is not something we'll talk too much about in this course (or at all).

**Abstract algebra** is about generalising properties of things we understand to apply to various algebraic objects. For example, functions, polynomials, and others. This is a great help in particle physics. For example, the symmetries of a square. What are the ways we can label this up to symmetry? This would be like describing this particle system in terms of things we can control which change the system.

We're going to start with basic addition and multiplication then apply this to more complex problems to understand symmetries and similar things. We like to generalise stuff --- to find properties and find what the fundamental building blocks are to build out.

## How to generalise?

We want to find the smallest assumptions which are required to describe all of the properties we want.

**Example.** With $\mathbb R$, the set of real numbers, we can add, subtract, multiply, and divide. We also know that add and subtract are opposites, and multiply and divide are opposite operations (except involving zero). Also, we can add/multiply in any order (associativity). We can also reorder our addition or multiplication (commutativity). We can also distribute multiplication across addition. We have identity elements.

These are the fundamental properties we want, which we call **axioms**. We have these with the reals. The rational and complex number sets also satisfy these axioms.

The natural numbers $\mathbb N = \{1, 2, 3, \ldots\}$ and the integers $\mathbb Z = \{\ldots, -1, 0, 1, \ldots\}$ do not. For example, there is no multiplicative inverse for 2 since 1/2 is not an integer. We don't have an additive identity in $\mathbb N$ since we do not include 0 as a natural number.

Something we will want to do is see if these axioms hold for other sets with particular binary operations. 

A **binary operation** on a set $S$ is a function $* : S \times S \to S$. In usual function notation, we might write this as $*(a, b) = *((a, b))$ but usually denote this as $a * b$. We often denote a set with a binary operation by $(S, *)$. If we have multiple binary operations $*_1, *_2, \ldots, *_k$, we can write this as $(S, *_1, \ldots, *_k)$.

**Example.** Let $M_n(F)$ be the set of $n \times n$ matrices with entries from some field $F$ and let $\mathcal F_A$ be the set of all functions $f : A \to A$. Binary operations on $M_n(\mathbb R)$ include addition, multiplication, and $[X, Y] := XY-YX$. On $\mathcal F_A$, we have composition $(f \circ g)(x) = f(g(x))$ for all $x \in A$.

A binary operation is **associative**, if for all $a, b, c \in S$, we have $(a * b) * c = a * (b * c)$. What this allows us to do is not write parentheses to indicate the order we apply binary operations. For example, addition and multiplication of fields, and composition of functions.

Non-examples include the Lie bracket for matrices, and subtraction and division. Generally, the binary operations we consider will be associative.

A binary operation is **commutative** if for all $a, b \in S$, we have $a * b = b * a$. For example, addition and multiplication are commutative for the regular number-like fields but not for matrices. Also, composition on $\mathcal F_A$ is not commutative.

![](202102231327%20math2301%20theorem%20associativity)

![](202102231344%20math2301%20identities)