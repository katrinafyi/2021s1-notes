# Coding Theory
What is a code, how do we develop them, and what properties do we expect? We will construct various codes and study their properties.

The goal of **coding theory** is to digitise information so it can be transmitted electronically and recovered later. The importance is the information may be transmitted through a noisy or unreliable channel, so the code should be able to detect and (ideally) correct the errors.

![](Pasted%20image%2020210226125249.png)

A **message text** is a vector or **word** of length $k$ containing elements from some alphabet $A$. For binary codes, $A = \mathbb Z_2 = \{0, 1\}$. The space of all possible message words is denoted $M = A^k$ (this is just the Cartesian product of $A$ and itself $k$ times).

An **encoding function** $f : A^k \to A^n$ **encodes** a message word to a **codeword**, assuming $n \ge k$. For binary codes, $f : \mathbb Z_2^k \to \mathbb Z_2^n$.

As a slight abuse of notation, the space of all codewords $f(M) = C$ is said to be the **code** with **code length** $n$. This code which takes a message of length $k$ and encodes it to a codeword of length $n$ is called an $(n,k)$-code.

## Codes
Requirements of a code:
- fast encoding of message information (it should work in realtime),
- easy transmission of encoded message (over some channel),
- fast decoding of codeword,
- detection of errors (because the channel is noisy),
- correct of errors if possible, and
- maximise transfer of information per unit time (efficient).

Here, the second point is the easiest to deal with; we can just take $A = \mathbb Z_2$ and use binary codes. This will be the case in this course.

## Formal specification

$$
\mathbb Z_2 = \{0,1\} \quad \mathbb Z_2^k = \{(x_1, \ldots, x_k) ~|~ x_1, \ldots, x_k \in \mathbb Z_2\}.
$$
Binary operations of addition and multiplication are defined on $\mathbb Z_2$ in the usual way; + behaves like XOR and \* behaves like AND.

Addition in $C \subseteq Z_2^n$ is defined as *componentwise* addition where $+$ is addition modulo 2.

We will often write $x_1x_2 \ldots x_n$ or $(x_1x_2\ldots x_n)$ to represent the vector $(x_1, \ldots, x_n)$.

If the set of codewords is $C = f(A^k)$, then the number of codewords is $|C| = |A^k| = |A|^k$ and this means _all_ received words are potentially codewords. This means no error can ever be detected or corrected (it would be mistaken as another codeword received with no errors).

In error correction codes, the encoding function adds redundancy so errors can be detected and possibly corrected. We take $n = k+r$ where $r>0$, with $r$ redundant/check digits added to a message while encoding to a codeword.

One example of this is adding a **parity check digit**. Specifically, let $M = \mathbb Z_2^k$ and $C \subseteq Z_2^{k+1}$ such that
$$
f(x_1, \ldots, x_k) = (x_1, \ldots, x_k, x_{k+1})
$$
where
$$
x_{k+1} = x_1 + \cdots + x_k \pmod 2.
$$
This $C$ is called a **parity check code**. This is very simple but is widely used in practice. For example, the last digit of barcodes is a parity check code.

**Example.** The largest possible message space and parity check code where $k=3$ is below. $M$ is the set of original messages of length 3, and $C$ is the set of codewords of length 4.
```
M   x4
000 0
001 1
010 1
011 0
100 1
101 0
110 0
111 1
```
We can see that $001$ is encoded to $0011$. If we receive $0010$, we know some error has occurred because the parity check does not match. Assuming exactly one error, the original codeword could have been $0000, 0011, 0110,$ or $1010$ (it is impossible to tell which one).

If we know an error has occurred, we can ask for the message to be resent (e.g. barcode), but this is not good enough for real-time situations like music playback.

## Hamming weight

For $v \in \mathbb Z_2^n$, the **(Hamming) weight** of $v$ is defined to be
$$
\|v\| = \sum_{i=1}^n v_i,
$$
that is, the number of entries in $v$ which are $1$ (note addition here is *not *under modulo 2).

**Example.** Let $C$ be a code of length $8$. If $v = 00011011$ and $w=10101011$, then $\|v\| = 4$ and $\|w\|=5$.

**Lemma.** For all $v, w \in \mathbb Z_2^n$, $v+w$ is a word containing a $1$ in position $i$ if $v_i \ne w_i$ and $0$ otherwise. 

**Proof.** $w = (w_1, \ldots, w_n), v = (v_1, \ldots, v_n)$ so the sum is
$$
v+w = (w_1 + v_1, \ldots, w_n + v_n)
$$
Note that $w_i+v_i = 1 \iff w_i \ne v_i$ according to definition of addition in $\mathbb Z_2$ so the result holds.

## Hamming distance

The **Hamming distance** between $v, w \in \mathbb Z_2^n$ is the number of positions in which $v$ and $w$ differ. 

**Lemma.** For $v, w \in \mathbb Z_2^n$, $d(v, w) = \|v+w\|$.
**Proof.** According to the earlier lemma, $v+w$ has a one if and only if $v$ and $w$ differ at that position. Therefore, the number of $1$s in $v+w$ is exactly the number of positions which differ.

## Overview

We take messages from some message space $M = \mathbb Z_2^k$ and add redundancy by mapping it to a codeword in a code space $C \subset \mathbb Z_2^n$. Because not all $n$-length binary words are valid codewords, this allows us to detect errors. Potentially, we can also correct errors by finding the valid codeword which is "closest" to what we received.

![](Pasted%20image%2020210226134947.png)