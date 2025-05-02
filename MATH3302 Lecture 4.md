Recall the assumptions of a BSC.

#example Calculate the probability that errors go undetected in a parity check $(3,2)$-code over a BSC with reliability $p$. Is there a possibility of some errors being detected?

The probability of no errors is just one minus the probability of at least one error occurring.

No errors occur with probability $p^3$. At least one error occurs with probability
$$
\begin{aligned}
1-p^3 &= (1-p)(3p^2+3p(1-p)+(1-p^2)) \\ 
&=q(3p^2+3pq+q^2)
\end{aligned}
$$
where $q=1-p$. 

Errors of weight exactly 1 can be detected so weight 2 errors will be undetected, with probability
$$
\binom 3 2 p^{3-2} (1-p)^2 = 3p(1-p) = 3pq^2.
$$
Hence, the probability of an undetected error given at least one error has occurred is
$$
\frac {3pq^2}{q(3p^2+3pq+q^2)} = \frac {q}{(p+q+q^2/3p)} < q < 1
$$
which means that at least some errors will be detected.

#example Consider instead the probability of decoding correctly an error in a particular message bit in a 3-fold $(3k,k)$-code over a BSC with reliability $p$. That is, what is the probability of correcting an error assuming one has occurred?

Recall that a 3-fold code has $\delta=3$ [MATH3302 Lecture 2#Minimum distance of a code](MATH3302%20Lecture%202%23Minimum%20distance%20of%20a%20code) and in deciding, we decode the the bit in the repetition which occurs most often. If there are no or one errors, the decoding will be correct. that is,
$$
\begin{aligned}
P  &= \binom {3}{0}p^{3-0}(1-p)^{0} + \binom 3 1 p^{3-1}(1-p)^1 \\ 
 &= p^3 + 3p^2 (1-p) = p^2(p+3(1-p)) \\ 
  &= p^2(3-2p) > p
\end{aligned}
$$
If $p>0.5$, then it is quite likely that we will be able to correct this error. However, we would like to do better because the rate is still quite bad ($r=1/3$).

# Formalising IMLD

Recall that IMLD is the concept that a received word $w$ is decoded to the codeword $c$ which minimises the Hamming distance between $c$ and $w$. Recall that $w=c+e$ where $e$ is an error pattern and $\|e\|$ is the weight of the error pattern.

#theorem Suppose $C$ is an $(n,k)$-code for use in BSC with reliability $0.5 < p < 1$. Let $c,c' \in C$ and let $w$ be any word of length $n$. Then,
$$
P_p(c \to w) \ge P_p(c' \to w) \iff d(c,w) \le d(c',w).
$$

#proof Since $0.5 < p < 1$, we know that $0 < q < p < 0.5$ and so $1 < p/(p-1)$. Let $c + w=e$ and $c'+w=e'$. 

We will prove the forward direction and assume $P_p(c \to w) \ge P_p(c' \to w)$. We rewrite this using the expressions for each probability, then
$$
\begin{aligned}
p^{n-\|e\|}(1-p)^{\|e\|} &\ge p^{n-\|e'\|}(1-p)^{\|e'\|}  \\ 
p^{-\|e\|}(1-p)^{\|e\|} &\ge p^{-\|e'\|}(1-p)^{\|e'\|}  \\ 
\left(\frac{1-p}{p}\right)^{\|e\|} &\ge \left(\frac{1-p}{p}\right)^{\|e'\|}  \\ 
1 &\ge \left( \frac {1-p}{p} \right)^{\|e'\|-\|e\|} \\ 
\iff \|e\| &\le \|e'\|
\end{aligned}
$$
because $1-p \le p$ and so $(1-p)/p \le 1$. Thus, $d(c,w) \le d(c',w)$.

The reverse implication is proved similarly. 

However, for large codes, finding the distance between all pairs of codewords is impractical. So we need to think about the design process then exploit these properties.

# Reliability
Let $C$ be an $(n,k,\delta)$-code transmitting over a BSC. One measure of reliability for $C$ is to determine the probabilities associated with the code's capacity to correct error patterns, some of which may have weight greater than $\lfloor (\delta-2)/2\rfloor$.

We will continue assuming IMLD so the received word is decoded to the closest codeword.

We will return to the 3-fold $(6,2,3)$-code. For all $c \in C$, $d(c+e_0,c) = 0$ for $\|e_0\|=0$. Also for $\|e_1\|=1$ and $d(c+e_1,c)=1$ we can correct these as well.

We know that error patterns of weight 3 cannot be decoded correctly because they correspond to other codewords. What about error patterns of weight 2?  

Intuitively, this 3-fold repetition can correct errors of weight two as long as they occur in different positions. We will separate the 6-digit error weight into 3 groups of 2:
$$
e=e_{11}e_{12}~ e_{21}e_{22}~e_{31}e_{32}.
$$
The error can be corrected if the two errors occur in different positions within the same or different groups. One error must occur in the left bit and the other must occur in the right bit. There are three choices for the left bit and given a left position, there are 3 choices for the right bit error position. This means there are $3 \times 3=9$ possible error patterns which are correctable.

![](Pasted%20image%2020210302121229.png)

If we transmit this over a BSC with reliability $p$, then the probability of at most 2 errors in codewords of length 6 is the sum of probabilities of 0, 1, and 2 errors:
$$
\begin{aligned}
p^6 + \binom 61p^5(1-p)^1 + \binom 62p^4(1-p)^2 
&= 
p^6 + 6p^5(1-p)^1 + 9p^4(1-p)^2  \\ 
&= p^4(2p-3)^2
\end{aligned}
$$