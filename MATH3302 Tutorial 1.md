   

# Question 8 2018
1.  0.997^5 = 0.9851
2.  (1-0.997) \* 0.997^4 = 0.003
3.  X
4.  Binom(5, 1) \* (1-0.997) \* 0.997^4

# Question 2
Suppose we have an e-error correcting binary code with code words of length n, transmitted through a BSC with reliability $p$. What is the probability of an error passing uncorrected through the BSC given that an error has occurred?

The probability of correcting an error given one has occurred is the probability of the error being weight $\le e$ divided by the probability of an error, so
$$
\frac{1-\sum_{i=0}^e \binom ni (1-p)^ip^{n-i}}{1-p^n}.
$$
Probability of any errors is just the probability of not all correct.

# Question 3
i) a: yes, b: yes, c: no.
ii) a: no. b: yes.

# Question 6
For binary codewords $u, v$,
$$
\|u+v\| = \|u\| + \|v\| - 2\|y\|
$$
where $y = u \cap v$.

Let $B$ be a linearly independent basis for $V$. Let $u, v \in B$ . Suppose $\|u\|$ is even and $\|v\|$ is even. Then, $u+v \in V$ and $\|u+v\|$ must be even.

Suppose $\|u\|$ is even and $\|v\|$ is odd. Then, $u+v \in V$ and $\|u+v\|$ is odd.