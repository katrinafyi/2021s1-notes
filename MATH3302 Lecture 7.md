# Standard form for generating matrices
There are many distinct generating matrices for a linear code $C$. We would like some sort of canonical form for the generating matrix.

#definition Let $k \ne n$ and $G$ be a $k \times n$ generating matrix for a linear code $C$. The matrix $G$ is in **standard form** if $G = [I_k ~|~ X]$ where $I_k$ is the $k \times k$ identity matrix and $X$ is the remainder.

#definition If $C$ and $C'$ are both codes of length $n$ and dimension $k$, then $C$ and $C'$ are said to be **equivalent codes** if there exists a permutation of the $n$ bits such that each codeword of $C'$ is mapped to a unique codeword of $C$ (the same permutation must be used for all codewords).

With this in mind, any $(n,k)$-code $C'$ has an equivalent code $C$ with generating matrix $G$ in standard form such that
- the rows of $G$ are linearly independent, and
- for $c= mG \in C$, the first $k$ bits of $c$ are the message the the last $n-k$ bits are "check bits".

#theorem If $C$ is a linear code of length $n$ and dimension $k$ with generating matrix $G$ in standard form and a message $m$ is encoded, then the first $k$ bits of the codeword $c = mG$ are the message word $m$.

#theorem Any linear code $C$ is equivalent to a linear code having a generating matrix in standard form.

#proof Assume $G$ is a generating matrix in rref with rank $k$. Then, $G$ has $k$ non-zero rows and $k$ columns which have leading ones and zeros elsewhere. Permute these columns so $I_k$ is at the left gives us $G'$ for an equivalent code. This generating matrix will be in standard form.

# Parity check matrices

From now, assume all generating matrices are in standard form with $G = [I_k~|~X]$ where $X$ is some $k \times (n-k)$ binary matrix.

If we have $G$ in standard form, a parity check matrix is simply
$$
H = \begin{bmatrix}
X \\
I_{n-k}
\end{bmatrix}.
$$
Then, 
$$
GH = \begin{bmatrix}
I_k & X
\end{bmatrix}
\begin{bmatrix}
X \\ I_{n-k}
\end{bmatrix}
= X + X = 0
$$
because we are in a binary field so $X+X$ is zero.

In practice, we often construct $H$ then deduce $G$ and hence $C$ from $H$.

#example Given $S = \{11010,10001,01001,11000\}$ and let $C = \langle S \rangle$. We can find a basis for $S$ using RREF. We find that it has row rank $k=3$ and we can delete the row of zeros. This tells us the code has dimension $4$ and length 5.

We can find the generating and parity check matrices for an equivalent code and just need to reverse the transformation to obtain matrices for the original code. In general, block lengths are quite long because they are easy to work with.

#theorem If $C$ is a linear $(n,k)$-code with parity check matrix $H$, then $C = \{v \in \mathbb Z_2^n ~|~ vH=0\}$.

#proof Any codeword $v \in C$ can be written as a linear combination of $G$. That is, $mG$ for some $m$, so $mGH=0$ for all $v=mG \in C$.

#corollary If $C$ is a linear $(n,k)$-code with generating matrix $G$ and parity check matrix $H$ and $w$ is a received word such that $wH \ne 0$, then $w \notin C$.

#definition Let $x = (x_1, x_2, \ldots, x_n)$ be such that $xH = 0$, then this product gives us a set of $n-k$ **parity check equations** of the form
$$
x_1 h_{j1} + \cdots + x_n h_{jn} = 0
$$
for $j = n-k, \ldots, n$.