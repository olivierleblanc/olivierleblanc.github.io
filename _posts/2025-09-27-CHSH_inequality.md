---
layout: post
title: CHSH inequality
date: 2025-09-26 08:12:00-0400
description:
tags: quantum
categories: maths
giscus_comments: true
related_posts: true
pretty_table: true
toc:
    sidebar: left
---

$$
\newcommand{\ol}{\overline}
\newcommand{\sqrtt}{\frac{1}{\sqrt 2}}
\newcommand{\tinv}[1]{\frac{1}{#1}}
\newcommand{\win}{\text{win}}
\newcommand{\bb}{\mathbb}
$$

In physics, the [Clauser–Horne–Shimony–Holt (CHSH) inequality](https://en.wikipedia.org/wiki/CHSH_inequality) can be used in the proof of Bell's theorem, which states that certain consequences of entanglement in quantum mechanics cannot be reproduced by local hidden-variable theories.

## Classical states
{:data-toc-text="Classical states"}

As illustrated in Fig. 1, let us consider two persons, `Alice` and `Bob`, who have each two independent observables $A,\bar{A}$ and $B,\bar{B}$ with possibles outcomes $\pm 1$.

<center>
    <img src="/assets/img/posts/CHSH_inequality.png" alt="CHSH inequality" width="250px">
</center>
<div class="caption">
    Fig. 1: Alice and Bob have each two classical independent bits to measure. 
</div>

We define the variable

$$
    \begin{equation} \label{eq:S}
        S = \langle AB \rangle + \langle \bar{A}B \rangle + \langle A\bar{B} \rangle + \langle \bar{A}\bar{B} \rangle.
    \end{equation}
$$

The usual form of the CHSH inequality is 

$$
    \begin{equation} \label{eq:CHSH_ineq}
        |S| \leq 2.
    \end{equation}
$$

Expliciting all possible combinations of Alice' and Bob's observables in Table 1, it is easy to verify \eqref{eq:CHSH_ineq} in the classical case.
Indeed,

$$
    \begin{align}
    \begin{split}
        S &= \big| \braket{AB} + \braket{A\bar{B}} + \braket{\bar{A}B} - \braket{\bar{A}\bar{B}} \big| \\
        &= \big| \braket{A(B+\bar{B}) + \bar{A}(B-\bar{B})} \big| \\
        &= 2
    \end{split}
    \end{align}
$$

if the only outcomes are $\pm 1$ and cannot be in between.

<center>
    Table 1: All possible combinations of Alice and Bob measurements in the classical case. 
</center>

|  $$A$$  |  $$\bar{A}$$  |  $$B$$  |  $$\bar{B}$$  |  $$A(B+\bar{B})$$  |  $$\bar{A}(B-\bar{B})$$ |
|  :-:  |  :-:  |  :-:  |  :-:  |     :-:      |      :-:      |
|   -1   |   -1   |   -1   |   -1   |        2      |        0       |
|   -1   |   -1   |   -1   |    1   |        0      |        2       |
|   -1   |   -1   |    1   |   -1   |        0      |       -2       |
|   -1   |   -1   |    1   |    1   |       -2      |        0       |
|   -1   |    1   |   -1   |   -1   |        2      |        0       |
|   -1   |    1   |   -1   |    1   |        0      |       -2       |
|   -1   |    1   |    1   |   -1   |        0      |        2       |
|   -1   |    1   |    1   |    1   |       -2      |        0       |
|    1   |   -1   |   -1   |   -1   |       -2      |        0       |
|    1   |   -1   |   -1   |    1   |        0      |        2       |
|    1   |   -1   |    1   |   -1   |        0      |       -2       |
|    1   |   -1   |    1   |    1   |        2      |        0       |
|    1   |    1   |   -1   |   -1   |       -2      |        0       |
|    1   |    1   |   -1   |    1   |        0      |       -2       |
|    1   |    1   |    1   |   -1   |        0      |        2       |
|    1   |    1   |    1   |    1   |        2      |        0       |

## Quantum states
{:data-toc-text="Quantum states"}

In the more general quantum case, illustrated in Fig. 2, we write 

$$
    \begin{equation}
        \ket{\psi} = a \ket{00} + b \ket{01} + c \ket{10} + d \ket{11} = \begin{bmatrix}
            a \\ b \\ c \\ d
        \end{bmatrix}
    \end{equation}
$$
any general 2-qbit quantum state, with $|a|^2+|b|^2+|c|^2+|d|^2 =1$.
Now, in contrast to the classical case, $A,\bar{A},B,\bar{B}$ are all bases for measuring the same state $\ket{\psi}$ shared by Alice and Bob. 
They are given by

$$
    \begin{align}
    \begin{split}
        A &= Z = \begin{bmatrix}
            1 & 0 \\ 0 & -1
        \end{bmatrix} \\
        \bar{A} &= X = \begin{bmatrix}
            0 & 1 \\ 1 & 0 
        \end{bmatrix} \\
        B &= \sqrtt (Z+X) = \sqrtt \begin{bmatrix}
            1 & 1 \\ 1 & -1
        \end{bmatrix} \\
        \bar{B} &= \sqrtt (Z-X) = \sqrtt \begin{bmatrix}
            1 & -1 \\ -1 & -1
        \end{bmatrix}
    \end{split}
    \end{align}
$$

<center>
    <img src="/assets/img/posts/CHSH_inequality2.png" alt="CHSH inequality2" width="250px">
</center>
<div class="caption">
    Fig. 2: Alice and Bob have each two observables of the 2-qbit quantum state $\ket{\psi}$.
</div>

We remind the definition in \eqref{eq:S} of the variable 

$$
    \begin{equation*} 
        S = \langle AB \rangle + \langle \bar{A}B \rangle + \langle A\bar{B} \rangle + \langle \bar{A}\bar{B} \rangle.
    \end{equation*}
$$

In quantum algebra, the statistical expectation of the output of the observables $AB$ can be computed as

$$
    \begin{align} \label{eq:AB}
    \begin{split}
        \braket{AB} &= \braket{\psi | A \otimes B | \psi} \\
        &= \begin{bmatrix}
            a & b & c & d
        \end{bmatrix} \sqrtt \begin{bmatrix}
            1 & 1 & & \\
            1 & -1 & & \\
            & & -1 & -1 \\
            & & -1 & 1
        \end{bmatrix}
        \begin{bmatrix}
            a \\ b \\ c \\ d
        \end{bmatrix} \\
        &= \sqrtt \begin{bmatrix}
            a & b & c & d
        \end{bmatrix} \begin{bmatrix}
            a+b \\ a-b \\ -c-d \\ -c + d 
        \end{bmatrix} \\
        &= \sqrtt (a^2-b^2-c^2+d^2).
    \end{split}
    \end{align}
$$

And, we similarly obtain

$$
    \begin{align}
        \braket{\bar{A}B} &= \sqrtt (2ad+2bc) \label{eq:A_B} \\
        \braket{A\bar{B}} &= \sqrtt (a^2-b^2-c^2+d^2) \label{eq:AB_} \\
        \braket{\bar{A}\bar{B}} &= \sqrtt (-2ad-2bc). \label{eq:A_B_}
    \end{align}
$$

Injecting \eqref{eq:AB}-\eqref{eq:A_B_} into \eqref{eq:S} yields

$$
    \begin{align} \label{eq:S_quantum}
    \begin{split}
        S &= \frac{2}{\sqrt 2} (a^2-b^2-c^2+d^2+2ad+2bc) \\
        &= \frac{2}{\sqrt 2} [(a+d)^2-(b-c)^2].
    \end{split}
    \end{align}
$$

From \eqref{eq:S_quantum}, we can distinguish different situations.
Firstly, the simplest case $a=1$, which is a `classical state`, gives $S=\frac{2}{\sqrt 2}$ and satisfies the CHSH inequality \eqref{eq:CHSH_ineq}.
However, choosing $a=d=\sqrtt$ gives the entangled state 

$$
    \begin{equation}
        \ket{\psi} = \ket{\Phi^+} = \sqrtt (\ket{00} + \ket{11})
    \end{equation}
$$

and $S=2\sqrt{2} > 2$ and `breaks the CHSH inequality`!