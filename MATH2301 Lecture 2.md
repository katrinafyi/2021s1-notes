Now that we have identities, we'd like to get to inverses. However as an intermediate step, we will look at cancellation. This is not quite the same as inverses.
# Cancellation
As a rough example, cancellation is just saying $xa = ya$ (or $ax = ay$) implies $x = y$ for some binary operation, i.e. we can cancel the $a$. Note that we do not require $a$ has an inverse.

#example We can cancel $a = \begin{bmatrix}1 & 2 \\ 0 & 0 \end{bmatrix}$ in the expression $xa = \begin{bmatrix}2 & 4 \\ 0 & 0 \end{bmatrix} = ya$ to get $x = y = 2$. Note that $a$ is not invertible. however, we would not be able to cancel $A = [1\ 2]$ and $x = [1\ 2]^\top, y = [5\ 0]^\top$ since $Ax = Ay$ but clearly $x \ne y$.

#example If $a = 0$, then no cancellation is possible.

If we can _always_ cancel an element $a$, then we call the element that cancels $a$ the **inverse** of $a$. For $(\mathbb R,+)$, this is $-a$ and for $(\mathbb R, \cdot)$ this is $a^{-1} = 1/a$ for $a \ne 0$.

#definition Let $(S, *)$ have an identity $e$. Then *an* inverse of $a$ is $b \in S$ such that 
$$
a * b = b * a = e.
$$
#definition An element with an inverse is said to be **invertible**.

#theorem Let $(S, *)$ have an identity with $*$ being associative. If $a \in S$ is invertible, then its inverse is unique.
#proof Let $b, c$ be inverses of $a$. 
$$
b = e * b = (c * a) * b = c * (a * b) = c * e = c\qquad \blacksquare
$$
Note associativity is required; if you have a non-associative operation, you can potentially have multiple inverses. This could be weakened with a left or right inverse, but we will stick with a single "inverse".

As a (ill-formed) question, what are the "nicest" algebraic objects? 
Things like $\mathbb Q$, $\mathbb R$, and $\mathbb C$, because they satisfy all our axioms. We can multiply, add, subtract, and be commutative and associative.

# Field
#definition A **field** is $(S, +, \cdot)$ such that 
- $+, \cdot$ are associative and commutative,
- there are additive and multiplicative identities (typically 0 and 1), 
- if $a \ne 0$, there exists $a^{-1}$,
- for all $a \in S$, there exists $-a$, and
- distributivity: for $a, b, c, \in S$, we have $a \cdot (b + c) = a \cdot b + a \cdot c$  and $(b + c) \cdot a = b \cdot a + c \cdot a$.

Note that the last property holds by commutativity but we write it because we will deal with non-commutative fields later.

#example $\mathbb Q, \mathbb R, \mathbb C$ are fields but $\mathbb Z$ is not because $2^{-1} \notin \mathbb Z$. If we take $\mathbb Q + \sqrt 2 \mathbb Q$, this is also a field.

#exercise Show that the rationals plus root is a field. This is very similar to showing $\mathbb C = \mathbb R + i \mathbb R$ is a field.

Recall that identities are unique (we showed this in [[MATH2301 Lecture 1]]).

#theorem For $(S, +, \cdot)$ with $0$ being the identity under $+$, with $+$ and $\cdot$ associative, distributive, and additive inverses, then $a \cdot 0 0 \cdot a = 0$ for all $a \in S$.

#proof $a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0$ then cancel $a \cdot 0$ to get $0 = a \cdot 0$ and similarly for the other direction. This makes use of distributivity and the additive inverse of $a \cdot 0$.

#example The field with 1 element, $0 = 1$. In fact, if the additive and multiplicative identities are the same, the field must have exactly one element. A proof of this is if $0 = 1$ in some field $F$, then $0 = a \cdot 0 = a \cdot 1 = a$ for all $a$. Hence, $F = \{0\}$.

#example The *quaternions* are an "extension" of $\mathbb C$ with two additional imaginary variables $j, k$ such that $i^2 = j^2 = k^2 = -1$. Elements are of the form $a + bi + cj + dk$ for $a, b, c, d \in \mathbb R$. Multiplication is extended by
$$
i \cdot j = k,\ j \cdot i = -k,\ j \cdot k = i,\ k \cdot j = -1,\ k \cdot i = j,\ i \cdot k = -j.
$$
#exercise This satisfies all of the field axioms except for $\cdot$ being commutative. This a type of a skew field or division ring.