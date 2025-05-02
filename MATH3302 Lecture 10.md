#definition If $C$ is a linear $(n,k)$-code with parity check $H$ and $w \in \mathbb Z_2^n$, then the **syndrome** of $w$ is $wH$.

#lemma If $C$ is a linear $(n,k)$-code and $u, v$ are in the same coset of $C$, then $u$ and $v$ have the same syndrome.

#proof Assume $u,v$ are in the same coset so $u+v \in C$ and so $0=(u+v)H = uH+vH$ which implies $uH = vH$.

Therefore, knowing the syndrome $wH$ uniquely identifies the coset containing $w$ and the associated error pattern is in the same coset. Furthermore, if it has a unique coset leader, then we can use that as the error pattern to correct $w$.

Note that since the rank of $H$ is $n-k$, then $\{vH \mid v \in \mathbb Z_2^n\} = \mathbb Z_2^{n-k}$ because there are $2^{n-k}$ cosets and each syndrome uniquely specifies a coset.

#theorem Suppose $C$ is a linear $(n,k)$-code with parity check $H$ and $w,e \in \mathbb Z_2^n$. Then,
- $wH=0$ iff $w \in C$,
- $wH = eH$ iff $w$ and $e$ are in the same coset,
- $w$ is corrected with a unique coset leader $e_0$ if it exists from the coset containing $w$,
- if $e$ is the error pattern for a received word $w$, then $eH$ is the sum of the rows of $H$ corresponding to the positions where errors occured, and
- the $2^{n-k}$ words of length $n-k$ each occur as the syndrome of exactly one of the $2^{n-k}$ cosets.


#definition Assume that $\mathbb Z_2^n$ has been partitioned into cosets and the coset leaders have been ideitified. A table that matches the coset leaders with syndromes is called a **standard decoding array** (SDA).

# Decoding summary
Let $G$ and $H$ be generating and parity check matrices, respectively. For a received word $w$ of length $n$:
1. Compute the syndrome $wH$.
2. Using IMLD, the most likely error pattern is the coset leader of the syndrome's corresponding coset.
3. If the coset leader is unique, the most likely codeword is $c = w+e$ which we should decode to.