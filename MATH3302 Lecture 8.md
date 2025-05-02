#theorem Suppose $C$ be a linear $(n,k)$-code. Then, $G$ is a generating matrix and $H$ is a parity check matrix for $C$ if and only if
- $G$ is $k \times n$ and $H$ is $n \times (n-k)$ and $GH=0$, 
- the *rows* of $G$ are linearly independent and form a basis for $C$, 
- the *columns* of $H$ are linearly independent and form a basis for $C^\perp$.

Further, for a parity check matrix $H$ with no zero rows and no repeated rows, then
- no single row of $H$ is linearly dependent, 
- all rows are different, so no set of two rows of $H$ are dependent, 
- a set of three rows can only be dependent if one row of $H$ is the sum of two others.

#theorem Let $H$ be a parity check matrix for a linear $(n,k)$-code $C$. Then $C$ has distance $\delta$ if and only if every set of $\delta-1$ rows of $H$ is linearly independent and there exists a set of $\delta$ rows of $H$ that is linearly dependent.

#proof Let $S = \{r_{i1}, \ldots, r_{is}\}$ be a non-empty set of rows of $H$ of minimal cardinality s.t. $S$ is linearly dependent. This implies that the sum of the vectors is zero.

Assume $C$ has distance $\delta$, so there exists $v \in C$ such that $\|v\| = \delta$.

Let $R=\{r_{i1}, \ldots, r_{ir}\}$ be a set of rows of $H$ such that $r_{ij}\in R$ if $v_j=1$. This is the set of rows where the corresponding bit in $v$ is 1. Then, $|R| = \|v\| = \delta$. Since $vH=0$, the sum of the rows in $R$ is 0, so $R$ is a linearly dependent set of size $\delta$. Because $S$ is the smallest such set, $\delta \ge |S|$.

We also create $w = (w_1, \ldots, w_n)$ where $w_j = 1$ iff $r_{ij} \in S$. Then, $\|w\| = |S| > 0$ and $wH$ is the sum of the linearly dependent vectors, which means $wH = 0$. Therefore, $w \in C \setminus \{0\}$ and by definition of distance, the distance is at most $\delta \le \|w\| = |S|$.

# Cosets

If $C$ is a linear code and $e$ occurs in transmission, then the set of all possible received words is 
$$
C + e =\{c + e ~|~ c \in C\}.
$$
If $e = 0$, then this is just $C$. Otherwise, this will change the code.

For linear codes, the set $\mathbb Z_2^n$ can be partitioned into subsets of the form $C + e$ which are called cosets.

#definition Suppose $C$ is a linear $(n,k)$-code and $u \in \mathbb Z_2^n$. The **coset** of $C$ containing $u$ is the set $C + u = \{c + u \mid c \in C\}$. This is the set of all possible received words $c + u$.

This is called "containing $u$" because $0 \in C$ and so $u \in C + u$.

#example Let $C = \{000,111\}$ and $u_1=111, u_2=011$. Then,
$$
C + 111 = \{111,000\}, \quad C + u_2 = \{011,100\}.
$$