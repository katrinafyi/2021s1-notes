# Dual codes
#definition Vectors $v$ and $w$ in $\mathbb Z_2^n$ are said to be **orthogonal** if $v \cdot w=0$.

#definition The **dual** of $S$ is defined as 
$$
S^\perp = \{v \mid v \cdot s = 0,~ \forall s \in S\}.
$$

#lemma For any non-empty set $S \subset \mathbb Z_2^n$, the set $S^\perp$ is a vector space (linear code).

#proof $0 \in S^\perp$ so it is non-empty. For all $v, w \in S^\perp$ and $s \in S$, $(v+w)\cdot s = v\cdot s + w \cdot s = 0$ so $v+w \in S^\perp$. Therefore, $S^\perp$ is a linear code.

#definition If $C \subseteq \mathbb Z_2^n$ is a code, then the set $C^\perp$ is called the dual code of $C$.

#lemma Suppose $C$ is a linear code of length $n$, $S$ is a basis with dimension $k$ and $G$ is the generating matrix, then the dual code $C^\perp$ is the null space of $G$.

#proof By definition, the null space of $G$, $\operatorname*{NS}(G)$, is the set of vectors $y$ such that $Gy=0$. Since $S$ is a basis, $y \in \operatorname*{NS}(G)$ implies $c \cdot y^\top=0$ for all $c \in C$. Therefore, $y \in C^\perp$.

Conversely, if $x \in C^\perp$ then $s\cdot x = 0$ for all $s \in S$. Therefore, $Gx^\top = 0$ and so $x^\top \in \operatorname*{NS}(G)$.

#lemma If $S \subseteq \mathbb Z_2^n$, then $\langle S \rangle^\perp=S^\perp$.

#proof Assume $v \in \langle S \rangle^\perp$. Note that $S \subseteq \langle S \rangle$. Therefore, if $v$ is orthogonal to all vectors in the span of $S$, it is surely orthogonal to anything in $S$.

Assume $v \in S^\perp$. Then, $v \cdot w =0$ for all $w \in S$. However, we can write $w \in \langle S \rangle S$ as a linear combination of elements in $S$. Therefore, $v \cdot w = v \cdot w_1 +\cdots+ v \cdot w_s=0$ where $w_i \in S$. Thus, $v \in \langle S \rangle^\perp$.

#theorem Suppose $C \subseteq \mathbb Z_2^n$ is a linear code. Then, the dual code $C^\perp$ is a linear code and if $C = \langle S \rangle$ then $C^\perp = S^\perp$.

#theorem Suppose $C \subseteq Z_2^n$ is a linear code of length $n$. Then, $\operatorname*{dim} C + \operatorname*{dim}C^\perp = n$.

#proof This follows from $\operatorname*{rank}G + \operatorname*{rank} \operatorname*{NS}G = n$ for an $m \times n$ matrix $G$.

#lemma Suppose $V, W \subset \mathbb Z_2^n$ and $S, T$ are their respectives bases. If $s \cdot t=0$ for all $s \in S, t \in T$, then $v \cdot w = 0$ for all $v \in V$ and $w \in W$.

#lemma Let $C$ be a linear $(n,k)$-code with generating matrix $G$. Suppose $H$ is an $n \times (n-k)$ matrix with linearly independent columns. Then, the columns of $H$ form a basis for $C^\perp$ if and only if $GH=0$.

#proof Assume $H$ is a basis of $C^\perp$. Then, any column $h$ is in $C^\perp$ so $GH = 0$.

Assume $GH = 0$. Let $S$ be the span of columns of $H$. By definition of matrix multiplication, $g \cdot h^\top=0$ for all rows $g$ of $G$ and columns $h$ of $H$. With the above lemma, this means every vector in $S$ is orthogonal to every vector in $C$. Therefore, $S \subseteq C^\perp$. But since $H$ has rank $n-k$. this tells us $\operatorname*{dim} S = n-k = n-\operatorname*{dim} C = \operatorname*{dim}C^\perp$ so $S = C^\perp$.

#theorem A matrix $H$ is a parity check matrix for a linear code $C$ if and only if $H^\top$ is a generating matrix for the dual code $C^\perp$.

#proof Assume $H$ is a parity check matrix, then there exists $G$ where $GH=0$. Given rows of $G$ are a basis for $C$ and columns of $H$ are a basis of $C^\perp$, then $H^\top G^\top=0$. Now, the rows of $H^\top$ are a basis for $C^\perp$ and so $H^\top$ is a generating matrix for $C^\perp$. Additionally, $G^\top$ is the parity check matrix.