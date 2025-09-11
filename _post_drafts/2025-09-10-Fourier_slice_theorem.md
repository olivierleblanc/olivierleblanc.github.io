---
layout: post
title: Simple proof of the Fourier-slice theorem
date: 2025-09-09 08:12:00-0400
description: Simple proof of the Fourier-slice theorem
tags:
categories: maths
giscus_comments: true
related_posts: true
---

$$
\newcommand{\im}{\mathrm{i}\mkern1mu}
\newcommand{\bs}{\boldsymbol}
\newcommand{\cl}{\mathcal}
\newcommand{\ud}{\mathrm{d}} % Infinitesimal part for integration
\newcommand{\Rbb}{\mathbb{R}}
\newcommand{\Cbb}{\mathbb{C}}
\newcommand{\tinv}[1]{\frac{1}{#1}}
\newcommand{\intfty}{\int_{-\infty}^\infty}
\newcommand{\iintfty}{\iint_{-\infty}^\infty}
\newcommand{\norm}[2]{\| #1 \|_{#2}}
\newcommand{\so}{\sin (\theta)} % sin(theta)
\newcommand{\co}{\cos (\theta)} % cos(theta)
$$

> **Definition. (Radon transform)** 
> The Radon transform $\cl R f$ of $f: \Rbb^2 \rightarrow \Rbb^2$ is 
> $$
>    \begin{equation}
>        \cl R \{f\}(t, \theta) = \int_{l_{t,\theta}} f \ud s = 
>        \intfty f(t \co-s \so, t\so + s \co) \ud s,
>    \end{equation}
> $$
>    for $t \in \Rbb$ and $0\le \theta < \pi$.

We wish to prove the *Fourier-Slice Theorem* reminded in p.37 of {% cite pomm24 %} \cite{Adcock}

$$
\begin{equation}
    \cl{F}_1 \cl R f (\omega, \theta) = \cl F f (\omega 
    \co, \omega \so),
    ~~\omega \in \Rbb,~ \theta \in [0,2\pi)
\end{equation}
$$

Where $\cl F$ denotes the 2-D Fourier transform and $\cl F_1$ 
is the 1-D Fourier transform with respect to the first component. 

*proof*.

The left term writes as

$$
\begin{equation*}
    \intfty \left( \intfty f(t \co-s \so, t \so + s \co) \ud s \right) 
    ~ e^{-\im \omega t} \ud t 
\end{equation*}
$$

The second writes 

$$
\begin{equation*}
    \iintfty f(t', \alpha) e^{-\im \omega \co t'} e^{-\im \omega \so \alpha} 
    \ud t' \ud \alpha
\end{equation*}
$$

With the following change of variable

$$
\begin{equation*}
\left\{ 
\begin{split}
    t' &\rightarrow t\co -s\so \\
    \alpha &\rightarrow t\so + \alpha \co \\ 
\end{split}
\right.
\end{equation*}
$$

Insert in the right term, we get 

$$
\begin{align*}
\begin{split}
    \iintfty f(t', \alpha) e^{-\im \omega \co t'} e^{-\im \omega \so \alpha} 
    \ud t' \ud \alpha &\rightarrow \iintfty f(t\co-s\so, t\so+s\co)
    e^{-\im \omega \co (t\co-\cancel{s\so})} \\
    & e^{-\im\omega \so 
    (t\so+\cancel{s\co})} [\ud t \co 
    - \ud s\so] [\ud t\so + \ud s \co] \\
    &= \iintfty f(t\co-s\so, t\so+s\co) e^{-\im \omega t} \\
    & [\ud^2 t \so\co 
    +\ud t \ud s (\co^2+\so^2) - \ud^2 s \so\co ] \\
    &= \iintfty f(t\co-s\so, t\so+s\co) e^{-\im \omega t} \ud t \ud s 
\end{split}
\end{align*}
$$

Which concludes the proof. □