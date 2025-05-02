# Bases for linear codes

Since a linear code is a vector space, the set of all codewords can be written as linear combinations of the basis.

#definition The **dimension** of a linear code $C$ is the number of vectors in a basis which spans the vector space of the code.

#example Are the vectors $\{1010,0101\}$ linearly independent? Yes, since there is no linear combination of them which equals zero. Now, we can use this as a basis for a linear code. This linear code is
$$
C = \{0000,1010,0101,1111\}
$$
which is length 4 and dimension 2 with size 4.

Let $C$ be a linear code and $B=\{b_1, \ldots, b_s\}$ be a basis for $C$. Then, for all $c \in C$, $c$ can be expressed as a linear combination of vectors in the basis. Let 
$$
G = \begin{bmatrix}
b_1 \\ b_2 \\ \vdots \\ b_s
\end{bmatrix}
$$
be a matrix with rows of the basis vectors. Then, $c$ can be written as
$$
c = \begin{bmatrix}
a_1 & \cdots & a_s
\end{bmatrix}G
$$
where $a_1, \ldots, a_s$ are the coefficients of the linear combination.

#example Let $C = \{0000,1010,1100,0110\}$. $C$ is a linear code because the sum of any two vectors is also a codeword. A basis for this is
$$
B=\{1100, 0110\} \implies G = \begin{bmatrix}
1&1&0&0 \\ 
0&1&1&0
\end{bmatrix}.
$$
We should verify that this is linearly independent.

#definition Let $G$ be a $k \times n$ matrix whose rows form a basis for a linear code $C$. Then, $G$ is said to be a **generating matrix** for $C$, where for each $c \in C$ there exists a $k \times 1$ vector $m$ such that
$$
c = mG.
$$
Here, $m$ is the message word. We encode messages by multiplying them with the generating matrix.

Notes:
- $C$ will be a linear $(n,k)$-code.
- Since the rows of $G$ are a basis of $C$, they must be linearly independent and the rank of $G$ is $k$.
- The matrix $G$ is not unique as $C$ may have many different bases.

#theorem A $k \times n$ matrix with $n \ge k$ is a generating matrix for a linear $(n,k)$ code if and only if the rows of $G$ are linearly independent (i.e. the rank of $G$ is $k$).

#theorem If $G$ is a generating matrix for a linear code $C$, then any matrix row-equivalent to $G$ is also a generating matrix.

#theorem If $m_1 G = c_1$ and $m_2 G = c_2$ where $c_1 = c_2$, then $m_1 = m_2$. That is, the encoding function $f(m) = mG$ is one-to-one.

#definition Let  $C$ be a linear $(n,k)$-code with $k \times n$ generating matrix $G$. A $n \times (n-k)$ matrix $H$ such that $GH = 0$ is called a **parity check** matrix for code $C$.

If we take a codeword and multiply it with $H$, we should get a zero vector if the codeword is in $C$.