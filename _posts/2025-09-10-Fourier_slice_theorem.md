---
layout: post
title: Simple proof of the Fourier-slice theorem
date: 2025-09-09 08:12:00-0400
description: 
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
\newcommand{\so}{\sin (\theta)} % sin(theta)
\newcommand{\co}{\cos (\theta)} % cos(theta)
$$

> **Definition. (Radon transform)** 
> The Radon transform $$\cl R \{f\}$$ of $f: \Rbb^2 \rightarrow \Rbb$ is 
> $$
>    \begin{equation} \label{eq:radon}
>        \cl R \{f\}(t, \theta) = \intfty \intfty f(x,y) \delta(t-x \co - y \so) \ud x \ud y,
>    \end{equation}
> $$
> for $t \in \Rbb$ and $0\le \theta < \pi$.

<center>
    <img src="/assets/img/posts/fourier_slice_theorem.png" alt="fourier-slice" width="500px">
</center>
<div class="caption">
    Fig. 1: Illustration of the Fourier-slice theorem. 
</div>

We wish to prove the *Fourier-Slice Theorem* reminded in p.37 of {% cite adcock %} 

$$
\begin{equation} \label{eq:fourier_slice}
    \cl{F}_1 \big\{ \cl R \{ f \} \big\} (\omega, \theta) = \cl F \{ f \} (\omega \co, \omega \so),~~~~\omega \in \Rbb,~ \theta \in [0,2\pi)
\end{equation}
$$

Where $\cl F$ denotes the 2-D Fourier transform and $\cl F_1$ 
is the 1-D Fourier transform with respect to the first component. 

*proof*.

Using \eqref{eq:radon} and the definition of the Fourier transform, the left term of \eqref{eq:fourier_slice} writes as

$$
\begin{align} \label{eq:left}
    \cl{F}_1 \big\{ \cl R \{ f \} \big\} (\omega, \theta) &= \intfty \left( \intfty \intfty f(x,y) \delta(t-x \co -y \so) \ud x \ud y \right) e^{-\im \omega t} \ud t \\
    &= \intfty \intfty f(x,y) \big( \intfty \delta(t-x \co -y \so) e^{-\im \omega t} \ud t \big) \ud x \ud y \\
    &= \intfty \intfty f(x,y) \big( \intfty \delta(t-x \co -y \so) e^{-\im \omega (x \co+y\so)} \ud t \big) \ud x \ud y \\
    &= \intfty \intfty f(x,y) e^{-\im \omega (x \co+y\so)} \underbrace{\big(\intfty \delta(t-x \co -y \so) \ud t \big)}_{=1}  \ud x \ud y \\
    &= \intfty \intfty f(x,y) e^{-\im \omega (x \co+y\so)} \ud x \ud y \\
    &= \cl F \{ f \} (\omega \co, \omega \so)
\end{align}
$$

which proves \eqref{eq:fourier_slice}. □

## References
{% bibliography %}