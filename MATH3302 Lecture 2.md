# Encoding and decoding

Let $C$ be a code and $w$ be a received code word. **Incomplete maximum likelihood decoding (IMLD)** is the principle that if there is a *unique* codeword $c \in C$ such that $d(w, c) < d(w, v)$ for all $v \in C \setminus \{c\}$, then we decode $w$ to $c$. 

If there are codewords of equal minimum distance, we cannot decide and the decoding fails.

In this course, we will assume IMLD is always being used.

## Error detection

For code $C$, assume the codeword $c \in C$ has been transmitted and word $w$ is received. For words $c$ and $w$, the **error pattern** is defined to be $e = c+w$ (arithmetic modulo 2). If this is non-zero, then some error has occurred.

#lemma For code $C$, codeword $c \in C$, and received word $w$, the number of errors occurring in transmission is $\|e\|$ where $e = c+w$.

#definition Code $C$ is able to detect an error pattern $e$ in transmission if $e \ne 0$ and $c + e \notin C$ for any $c \in C$. 

Of course, if $w = c+e \in C$, then IMLD fails because $c+e$ will be the closest codeword and that error cannot be detected.

#definition A code $C$ is called a $t$-**error detecting** code if it detects all non-zero error patterns of weight at most $t$ and does not detect at least one error pattern of weight $t+1$.

#definition Given $M = \mathbb Z_2^k$, an $m$-**fold repetition code** is formed by taking each message $v \in M$ and concatenating $m$ copies of $v$ to form $c \in C$.

**Example.** Consider the 3-fold code with $k=3$ and codeword $c=010010010$ with the addition of all weight 1 error patterns. We can see these errors are detected because they are not in $C$.
![](Pasted%20image%2020210226140856.png)

In this case, we have $|M| = 2^3 = 8$ and $|C| = 8$. However, $|\mathbb Z_2^9| = 2^9$ which is much larger than 8.

In this case of $C \subseteq \mathbb Z_9$, we can think of each codeword being the centre of a sphere. Words of distance 1 from a codeword $c$ will fall inside a sphere of radius 1 centred at $c$, similarly for radius 2, etc.

However here, $d(000000000, 010010010) = 3$ which means there is some error pattern which when applied to $000000000$ makes the received word 2 distance from two codewords.

This means this 3-fold code can detect 1 or 2 errors but can only reliably correct single errors.

## Minimum distance of a code
#definition Let $C$ be a binary $(n,k)$-code. The **minimum distance** $\delta$ of a code is the smallest distance between pairs of distinct codewords. That is,
$$
\delta = \min_{v \ne w}d(v,w) = \min_{v \ne w}\|v+w\|, \quad \forall v, w \in C.
$$
Sometimes, it is useful to include this in our notation so we write a $(n,k)$-code with minimum distance $\delta$ as a $(n,k,\delta)$-code.

**Example.** The minimum distance of the code $C = \{000, 111\}$ is 3 which is $\|000 + 111\| = 3$.
![](_attachments/Pasted%20image%2020210226150839.png)
We can imagine the balls of radius 1 around the codewords. Because the balls of distance 1 around each codeword do not intersect, there is a unique closest codeword for error patterns of weight 1. This is not the case for error weights 2.
![](Pasted%20image%2020210226151043.png)

#theorem If $C$ is a code with minimum distance $\delta$, then $C$ is a $(\delta-1)$-error *detecting *code.

#proof Let $c \in C$ and $e$ be a non-zero error pattern with $\|e\|< \delta$. Then, $d(c, c+e) = \|c + (c + e)\| = \|e\|<\delta$. Since $\delta$ is the *minimum* distance of the code, then this received message is $c + e \notin C$ and $C$ detects $e$.

Further, since $C$ has minimum distance $\delta$, there exists $v, w \in C$ such that $d(v,w) = \delta$. Let $e = v+w$, noting that $\|e\| = \delta$, then $v+e = w \in C$ and there is an error of weight $\delta$ that $C$ will not detect.

Note that _some_ error patterns of weight $\delta$ might be detected but not all.

#lemma A code $C$ does not detect an error pattern $e$ if and only if there exists $v, w \in C$ such that $e =v+w$.

#proof Assume we have $v, w \in C$ and $e = v+w$. However, $v + e$ is a code word so if $v$ was transmitted and $w$ received, so $C$ will not detect the error $e$. This argument holds in reverse as well.

## Error correction
Recall that error correction will follow IMLD, correcting to a unique *codeword* with the minimum distance.

#definition A code $C$ is said to be $t$-**error correcting** if it corrects all non-zero error patterns of weight at most $t$, and does not correct at least one error pattern of weight $t+1$.

#definition A code $C$ **corrects** error pattern $e \ne 0$ to $v \in C$ if 
$$
d(v + e, v) < d(v + e, w), \quad \forall w \in C \setminus \{v\}.
$$
This means that there is a unique codeword $v$ which is closest to the received message $v+e$.

#lemma Assume $C$ is a code, $v \in C$ and $e \ne 0$ is an error pattern, where $v$ is transmitted but $w = v+e$ is received. Code $C$ will successfully correct error pattern $e$ if and only if $\|v + v' + e\| \ge \|e\|$, for all $v' \in C \setminus \{v\}$.

#proof By definition, we correct to $v$ if, for all $v' \in C \setminus \{v\}$,
$$
d(v+e, v') > d(v+e, v).
$$
Using the definition of distance,
$$
\|v + v' + e \| d(v+e, v') > d(v+e, v) = \|v + e + v\| = \|e\|
$$
and the result follows. $\blacksquare$

#theorem Let $C$ be a code with minimum distance $\delta$. Then, $C$ can correct all non-zero error patterns with weight $< \delta / 2$, and there is at least one error pattern of weight $\lceil \delta / 2\rceil$ which $C$ cannot correct.

#proof First, we will prove the pattern corrects successfully. Let $e$ be any non-zero error pattern with $\|e\|< \delta/2$. Suppose $c \in C$ is transmitted and $w = c+e$ is received. Proceed by contradiction; assume that $w$ cannot be corrected to $c$. That is, $\exists\ c' \in C \setminus \{c\}$ with $d(w, c') \le d(c, w)$, then
$$
\begin{aligned}
0 < d(c, c') &\le d(c, w) + d(w, c') && \text{(triangle inequality)} \\ 
&\le 2\,d(c,w) && \text{(by assumption)} \\ 
&= 2\|c + w\| = 2 \|c + (c + e)\| = 2 \| e\| < \delta.
\end{aligned}
$$
However, this contradicts the fact that $\delta$ is the minimum distance of the code. Therefore, $c$ is the unique codeword with minimum distance from $w$ so the error pattern $e$ can be corrected to $w$.

Now, we need to prove there exists at least one error pattern with weight $\lceil \delta /2\rceil$ which cannot be corrected. By definition of $\delta$, there exists $c, c' \in C$ such that $d(c, c') = \delta$. Let $e = c + c'$ and let $e=e_1+e_2$ where $\|e_1\| = \lceil \delta / 2 \rceil$ and $\|e_2\| = \lfloor \delta / 2 \rfloor$ (we can do this because for all integer $\delta$, $\lceil \delta / 2 \rceil + \lfloor \delta / 2 \rfloor = \delta$).

Consider $w = c + e_1$. Then,
$$
\begin{aligned}
w + c' &= c + e_1 + c' \\ 
&= c + e_1 + (e + c) \\ 
&= c + e_1 + e_1 + e_2 + c \\ 
&= e_2
\end{aligned}
$$
Therefore, $d(w, c) = \|w+c\| = \|e_1\| = \lceil \delta / 2 \rceil$ and $d(w, c') = \|e_2\|=\lfloor \delta/2 \rfloor$ and so, the error pattern $e_1$ with codeword would correct it to $c'$ instead of the original $c$ so IMLD cannot correct this.

#corollary If $C$ is a code with minimum distance $\delta$, then $C$ is a $\lfloor (\delta-1)/2\rfloor$-error correcting code.