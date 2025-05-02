# Properties of Cosets
#theorem Let $C$ be a linear $(n,k)$-code and $u,v$ be distinct elements of $\mathbb Z_2^n$. Then,
1. $u \in C + u$,
2. $u + v \in C \iff u \in C + v\iff C+u = C+v$,
3. the cosets partition $\mathbb Z_2^n$, so $\mathbb Z_2^n = \cup_{u}(C+u)$ and either $C+u=C+v$ or $(C+u)\cap(C+v) = \emptyset$,
4. $|C+u|=|C|$,
5. there are $2^{n-k}$ different cosets of $C$ each of size $2^k$, and
6. the code $C$ is a coset.

# Decoding Linear Codes
#lemma Let $C$ be a linear code with parity check matrix $H$. Then, $(uH = vH) \iff (C+u=C+v)$.

#proof Assume $uH=vH$ then $(u+v)H=0$ which occurs iff $u+v \in C$, which by theorem above is if and only if $C+u = C+v$.

Suppose $C$ is a linear $(n,k)$-code and suppose $v \in C$ is transmitted, while $w$ is received. That is, $v+e=w$ where $e$ is th error pattern. Then, $w+e=v$ and $C+w=C+e$. This means the coset containing $e$ also contains the received word $w$. If we can find what error pattern this is, we can determine what the original codeword could have been.

#definition A **coset leader** is a word of minimal weight in a particular coset (it may not be unique).

Under the assumption of IMLD, we can decode a received word $w$ and codeword $v$. If the coset $C+w$ has a unique coset leader $e$, IMLD implies that $v=w+e$ was the transmitted word and we can decode it to $v$. 

If a coset has more than one coset leader, IMLD will *fail* for all words in that codeset.