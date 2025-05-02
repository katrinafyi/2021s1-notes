**Theorem.** For an associative binary operation $*$, then
$$
a_1 * a_2 * a_3 *\cdots *a_k
$$
does not depend on the way parentheses are inserted. That is, there is no ambiguity to state this operation without parentheses. This is something we've been informally using with real numbers but we can formalise it now.

**Proof.** $n=2$ is vacuous, and $n=3$ is by assumption of associativity. We prove the rest by (strong) induction. We assume this holds for all $m < k$. Then, we can parenthesize as
$$
(\ldots(a_1 * a_2)*a_3)*\cdots)*a_k.
$$
For any parenthesisation of $a_1* \cdots* a_k$, we can write this as $A * B$ with $A$ being some expressions, with $A$ containing the left $m$ operations and $B$ containing the operations involving $a_{m+1}$ to $a_k$. Since $A$ and $B$ are shorter, we can rewrite them without parentheses using our inductive hypothesis. 

Thus, we have 
$$
(a_1 * \cdots * a_m) * (a_{m+1} * (a_{m+2} *\cdots * a_k))
$$
and by associativity, the above is equal to
$$
((a_1 * \cdots * a_m) * a_{m+1}) * (a_{m+2} *\cdots * a_k)
$$
which is uniquely defined by assumption.