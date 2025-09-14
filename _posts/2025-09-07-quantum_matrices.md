---
layout: post
title: Quantum Pauli matrices
date: 2025-09-06 08:12:00-0400
description: 
tags: quantum
categories: maths
giscus_comments: true
related_posts: true
---

$$
\newcommand{\im}{\mathrm{i}\mkern1mu}
$$

The `Pauli` matrices are defined as

$$
\begin{equation}
    X = \begin{bmatrix}
        0 & 1 \\ 1 & 0
    \end{bmatrix},~~Y = \begin{bmatrix}
        0 & -\im \\ \im & 0
    \end{bmatrix},~~Z=\begin{bmatrix}
        1 & 0 \\ 0 & -1
    \end{bmatrix}.
\end{equation}
$$

Each of them defines a transformation of a qbit state. For instance,

$$
\begin{equation}
    X \ket{0} = \begin{bmatrix}
        0 & 1 \\ 1 & 0
    \end{bmatrix} \begin{bmatrix}
        1 \\ 0
    \end{bmatrix} = \begin{bmatrix}
        0 \\ 1
    \end{bmatrix} = \ket{1}.
\end{equation}
$$

Find more information [on Wikipedia](https://en.wikipedia.org/wiki/Pauli_matrices).