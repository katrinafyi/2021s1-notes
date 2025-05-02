# Shannon's Theorem
Let $C_1, C_2, \ldots$ be a family of $(n_i, k_i)$-codes where $n_1 < n_2 < \cdots$ all with rate $\ge r$ and where failure rate goes to $0$ as $n \to \infty$ (i.e. as length increases, number of uncorrectable errors go to zero).

#definition The **channel capacity** $R$ of a BSC is the supremum of all rates $r$ for which there exists a family of codes $C_1, C_2, \ldots$ as described above.

Intuitively, we want to transmit information across a BSE. We can transmit rates at close to but below $R$ with essentially no errors, but when we take rate above $R$, we cannot achieve this goal of no errors regardless of codeword length.

$R$ is the intrinsic limit of what is possible with this channel.

#theorem  (Shannon's Theorem) The channel capacity $R$ of a BSC with reliability $p$ exists and is given by 
$$
R = 1 + p \log_2 p + (1-p) \log_2(1-p).
$$

# Code Sizes
For given $n$, $k$, and $|delta$, what is the largest possible set of binary codewords? That is, can we construct a code with these parameters?

We could just take all $2^n$ vectors and all $2^k$ messages and try to distribute the messages in the codeword and analysing the resulting code. However, considering all $\binom {2^n}{2^k}$ is not practical.

#example Does there exist a binary $(n,k,\delta)$-code $C$ where $n=3, \delta=2, |C|=5$?

Suppose such a code exists, with $C = C_0 \cup C_1$ for $C_0$ codewords starting with 0 and $C_1$ starting with 1. Assume $|C_0| \ge 3$. Then, we might have 3 codewords of the form:
$$
0x_1x_2, \quad 0y_1y_2, \quad 0z_1z_2.
$$
Because we assumed $\delta=2$, we need $d(0x_1x_2, 0y_1y_2) \ge 2$ and the only way this is possible is if $x_1 \ne y_1$ and $x_2 \ne y_2$. By the same logic, we must also have $x_1 \ne z_1, x_2 \ne z_2$. However, because this is binary, this implies $y_1 = z_1$ and $y_2=x_2$ which contradicts the minimum distance.

Therefore, it is not possible to construct such a binary code. However, the analysis is quite tedious and even if it is possible, does not yield a workable code.

#theorem (Singleton Bound) Let $C$ be a binary $(n,k,\delta)$-code. Then, $|C| \le 2^{n-\delta+1}$. Further, if $|C| = 2^k$, then $n \ge k+\delta-1$.

#proof Take the set of codewords $C \subseteq \mathbb Z_2^n$. For each codeword of length $n$, delete the first $\delta-1$ bits. This can be thought of as a mapping $f : C \to \mathbb Z_2^{n-\delta+1}$. Since our code is of distance $\delta$, we can construct $f$ such that it is an injective function with distinct mapped truncated words. Thus, $|C| = |f(C)|$. Hence, $|C| \le 2^{n-\delta+1}$.

Now substituting $|C| = 2^k$ into the above gives us
$$
|C| = 2^k \le 2^{n-\delta+1} \iff k \le n-\delta+1\iff k+\delta-1 \le n.
$$

Furthermore in this case, $k \le n-\delta+1$ and dividing by $n$ then rearranging,
$$
\frac k n + \frac \delta  n \le 1 + \frac 1 n.
$$
This means that for large $n$, $k/n + \delta/n \le 1$ but we can rarely find codes which meet this bound so it is not very sharp.

In general, it is difficult to generate bounds for codes. Even for the case where the codes are a vector space, there are still many open questions. In 2008, researchers developed a construction for a $(40,20,\delta)$ linear code, but it is not known if the maximum Hamming distance $\delta$ is 9 or 10. Theoretical results imply $\delta \le 10$ but only codes with distance 9 have been constructed.

# Linear Algebra

#definition A **vector space** is an Abelian group $(V, +)$ and a scalar field $F$ with an operation of scalar multiplication of each element of $V$ by each element of $F$ such that for all $a, b \in F$ and $u, v \in V$, 
- $av \in V$, 
- $a(bv) = (ab)v$,
- $(a+b)c = av + bv$,
- $a(u+v) = au+av$, and
- $1v = v$.

In particular, we are interested in bases of vector spaces. Let $S = \{v_1, \ldots, v_s\} \subseteq V$. 

#definition $w$ is a **linear combination** of vectors in $S$ if there exists scalars $a_1, \ldots, a_s \in F$ such that 
$$
w = a_1 v_1 + \cdots + a_s v_s.
$$

#definition The set of all linear combinations of vectors in $S$ is denoted $\langle S \rangle$ and called the **linear span** of $S$.

If $S = \emptyset$, then $\langle S \rangle = \{0\}$.

#definition $S$ is said to be **linearly independent** if 
$$
a_1v_1 + \cdots + a_sv_s = 0 \implies a_1 = \cdots = a_s = 0.
$$
If $S$ is *not* linearly independent, then it is **linearly dependent**.

#definition A **basis** for a vector space $V$ is a subset $B$ of $V$ which spans $V$ and is linearly independent. The **dimension** of a vector space $V$ is the number of vectors in (any) basis of $V$.

#definition The **rank** of a matrix $A$ is the number of linearly independent rows of $A$ (for example, the number of non-zero rows after reduction by RREF).

#definition The **null space** of a matrix $A$, denoted $\operatorname*{NS}(A)$, is the set of vectors $v$ such that $Av = 0$.

#definition The **row space** of a matrix $A$ with rows $r_1, \ldots, r_n$ is the span of its rows $\langle r_1, \ldots, r_n\rangle$.

#theorem If $A$ is an $m \times n$ matrix, then
$$
\operatorname*{rank}(A) + \operatorname*{dim}(\operatorname*{NS}(A)) = n.
$$

# Linear Codes

The set of vectors $\mathbb Z_2^n$ forms a vector space over the field $F = \{0,1\}$ and the binary operations are modulo 2.

#definition A non-empty code $C$ is called a **linear code** if the sum of any two codewords is itself a codeword. That is, $v, w \in C \implies v+w \in C$.

Here, we work with non-trivial subspaces of $\mathbb Z_2^n$. That is, subspaces with at least one non-zero vector.

#example $C=\{0000,1010,0101,1111\}$ is a linear code but the code $C'=\{0000,1100,0101,1111\}$ is not.

#theorem The distance of a linear code $C$ is equal to the minimum weight among all non-zero codewords in $C$.

#proof Let $\delta > 0$ be the minimum distance. This implies there exists $v, w \in C$ such that $d(v,w)=\delta$. Because $C$ is linear, there exists $z$ such that $w+z=v$ and hence $\|z\|=\|v-w\| = d(v,w)=\delta$. Clearly, $0 \in C$. Thus, the distance from 0 to $c$ is $\|c+0\|=\|c\|$ for all $c \ne0$. This tells us $\delta \le \|c\|$ for all $c \ne 0$.

Next we will prove this is the minimum weight. Assume there is $u \in C$ where $\|u\|<\|z\| = \delta$. However, $0 \in C$ and $d(u,0)=\|u\|<\delta$ which contradicts the fact that minimum distance is $\delta$.