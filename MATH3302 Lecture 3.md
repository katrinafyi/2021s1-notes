Recall that efficiency was one of the important features of a code. We added redundancy to improve error detection and correction, but we would also like to minimise redundancy.

#definition Let $C$ be a $(n,k)$-code. When $n$ is constant, the $(n,k)$-code is called a **block code**.

We will assume codes here are block codes.

#definition The **rate** of a block $(n,k)$-code is defined to be $r = k/n$ which is the length of the message word divided by the length of the codeword.

#example For a message space of binary messages of length $k$ so $M = \mathbb Z_2^k$ and corresponding code $C$ of length $n$ and rate $r=k/n$, we have
$$
|C| = 2^k=2^{rn} \implies \log_2|C| = rn \iff r = \frac 1 n \log_2 |C|
$$

#definition The **information rate** of a $(n,k)$-code $C$ is given by
$$
I = \frac 1 n \log_2 |C|
$$
which is a measure of the proportion of "message information" each codeword. Note that $\log_2|C|$ is the number of bits needed to uniquely identify the codeword.

#example The information rate of a parity-check $(n,k)$-code is $1/(k+1) \log_2(2^{k})=k/(k+1)$. The information rate of a 3-fold $(n,k)$-code is $1/(3k)\log_2(2^k)=1/3$.

For a 3-fold code, we can detect 2 and correct 1 errors. A parity check code might detect one error but cannot correct any errors.

In practice, the properties we want need to be balanced against a variety of applications. For example, hard drives with large volumes, images for number plate recognition vs skin cancer recognition, mobile network bandwidth, or IoT applications.

# Binary Symmetric Channels
Given that we know the probability of an error occurring in a bit, we can lok at the reliability of a coding process.

Assuming:
- A codeword is transmitted in sequence one bit at a time across a channel.
- Errors occur in distinct positions (i.e. one position cannot have multiple errors).
- All errors are distributed uniformly, independently, with a fixed probability $p$.

Here, $p$ represents the probability of *correct transmission.* That is,
if $b$ is transmitted and $b'$ is received, then $b' = b+e$ where
$$
e = \begin{cases}
0, & \text{with probability }p, \\
1, & \text{with probability }q=1-p.
\end{cases}
$$

#definition A **binary symmetric channel (BSC)** is a channel which satisfies the above assumptions, and it is said to have **reliability** $p$.

What does it mean if $p=1$? Then, there will be no errors ever. If $p<0.5$, we can easily improve reliability by flipping the bits on the receiving end to obtain $p > 0.5$.

Let $C$ be an $(n,k)$-code with reliability $p$ and let $c \in C$. For any error pattern $e$, the probability of transmitting $c$ and receiving $w=c+e$ is given by
$$
P_p(c \to w) = p^{n-\|e\|}(1-p)^{\|e\|}.
$$
This denotes that a certain number of bits in the codeword (of length $n$) have changed and the remainder have been correctly transmitted. This assumes that error probabilities are independent, as written above.

#example Assume $C$ is an $(n,k)$-code and $c\in C$ is transmitted across a BSC with reliability $p=1-10^{-8} \approx 1$. What is the probability of no errors occurring in a transmission of 10000 bits?

The probability of no errors in 10000 bits is 
$$
p^{10000} = (1-10^{-8})^{10000} = 0.99990000499
$$
which is small-ish. We would like to do better than this by introducing redundancy.

#example Assume $C$ is a $(11,11)$-code (which cannot detect any errors) and $c \in C$ is transmitted across a BSC with reliability $p=1-10^{-8}$. What is the probability of at least one error occurring?

Recall that $(1+x)^n \sum 1+xn$ for small $|x|$ and $x$ and $n$ not too large.

Then, the probability of no errors is $p^{11} = (1-10^{-8})^11 \sim 1-11/10^8$ and so the probability of *at least* one error is
$$
1-(1-11/10^8) = 11/10^8.
$$

#example Assume $C$ is an $(11,11)$-code and $c \in C$ is transmitted across the same channel which can transmit $10^7$ bits per second. What is the expected frequency of undetected errors? What is the rate?
$$
P_p(\ge 1 \text{ error}) \times \frac{\text{transmited bits per second}}{\text{bits per codeword}} = \frac{11}{10^8} \times \frac{10^7}{11} \sim 0.1 \text{ errors per second}.
$$
The rate is $r=11/11=1$ but it cannot correct any errors and the reliability is quite poor.

#example Extending this by adding a parity check bit, assume $C$ is a parity check $(12,11)$-code and $c \in C$ is transmitted across the same BSC with rate $10^7$.

The probability of an undetected error is 
$$
1-P_p(0\text{ errors}) - P_p(1 \text{ error})
$$
No errors means the zero error pattern, so there is one possibility. With one error (of 12 bits), there are 12 possible patterns. Therefore, the probability of an error being undetected is
$$
1-\binom {12}0 p^{12}(1-p)^0 + \binom{12}1 p^{11}(1-p)^1 \sim 6.6 \times 10^{-15}.
$$
Now, 
$$
P_p(\ge 1 \text{ error}) \times \frac{\text{transmited bits per second}}{\text{bits per codeword}} = \frac{6.6}{10^{15}} \times \frac{10^7}{12} \sim 5.5\times 10^{-19} \text{ errors per second}
$$
which is approximately one undetected error every 6 years. The rate of this code is $r=11/12$.