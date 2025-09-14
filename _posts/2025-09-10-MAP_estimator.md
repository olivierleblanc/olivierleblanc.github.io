---
layout: post
title: Viewing a Lagrangian inverse problem as a MAP estimator
date: 2025-09-09 08:12:00-0400
description: and the Bayesian point estimators
tags: optimization
categories: maths
giscus_comments: true
related_posts: true
---

$$
\newcommand{\bs}{\boldsymbol}
\newcommand{\ud}{\mathrm{d}} 
\newcommand{\Rbb}{\mathbb{R}}
\newcommand{\Cbb}{\mathbb{C}}
\newcommand{\tinv}[1]{\frac{1}{#1}}
\newcommand{\indep}{\perp \!\! \perp}
$$

In the following derivations, we show that the typical regularised inverse 
problem to recover a quantity $\bs x \in \Rbb^N$ from noisy observations of the form 
$\bs y = \bs{Hx} + \bs n \in \Cbb^M$ with additive noise $\bs n \in \Cbb^M$ corresponds to the *maximum a posteriori* (MAP) estimator when a prior distribution $$p(\bs x) = e^{-\theta \| \bs{\Psi x} \|_1}$$ is assumed on the 
data:

$$
\begin{align}
    \hat x_{\text{MAP}} &= \mathrm{argmax}_{\bs x}~ p(\bs x|\bs y) = \mathrm{argmax}_{\bs x}~ \frac{p(\bs y|\bs x) p(\bs x)}{p(\bs y)} 
    \underset{p(\bs y) \indep \bs x}{=}
    \mathrm{argmax}_{\bs x}~ p(\bs y|\bs x) p(\bs x) \\
    &= \mathrm{argmax}_{\bs x}~ e^{-\tinv 2 \|\bs y-\bs{Hx}\|_2^2} e^{-\theta \|\bs{\Psi x}\|_1} 
    = \mathrm{argmax}_{\bs x}~ e^{-\tinv 2 \|\bs y-\bs{Hx}\|_2^2 -\theta \|\bs{\Psi x}\|_1} \\
    &= \mathrm{argmax}_{\bs x}~ \log \big(e^{-\tinv 2 \|\bs y-\bs{Hx}\|_2^2 -\theta \|\bs{\Psi x}\|_1} 
    \big) \\
    &= \mathrm{argmin}_{\bs x}~ \underbrace{\tinv 2 \|\bs y-\bs{Hx}\|_2^2}_{\text{Data fidelity}} 
    + \underbrace{\theta \|\bs{\Psi x}\|_1}_{\text{Regularization}}.
\end{align}
$$

Additionnally, we define *Bayesian point estimators* that arise from the
decision ``what point $\hat{\bs x} \in \Rbb^N$ summarises $\bs x|\bs y$ best?''. The optimal decision under uncertainty is 

$$
\begin{equation*}
    \hat{\bs x}_L = \mathrm{argmin}_{\bs u \in \Rbb^N}~ \mathbb{E}[L(\bs u,\bs x)|\bs y] = \mathrm{argmin}_{\bs u \in \Rbb^N}~ \int L(\bs u,\bs x) p(\bs x|\bs y) \ud \bs x
\end{equation*}
$$

where the loss $L(\bs u,\bs x)$ measures the "dissimilarity" between $\bs u$ and $\bs x$.

General desiderata:
- $L(\bs u,\bs x) \ge 0,~ \forall \bs u, \bs x \in \Rbb^N$,
- $L(\bs u,\bs x)=0 \Leftrightarrow \bs u=\bs x$, 
- $L$ strictly convex w.r.t. $\bs u$ (for estimator uniqueness).

**<u>Example:</u>**

The *minimum mean square error* (MMSE) estimator, taking $$L(\bs u,\bs x) = \|\bs u-\bs x\|_2^2$$, is obtained as:

$$
\begin{align*}
\begin{split}
    \hat{\bs x}_{\text{MMSE}} &= \mathrm{argmin}_{\bs u}~ \int \|\bs u-\bs x\|_2^2 p(\bs x|\bs y) \ud \bs x \\
    &\Leftrightarrow \int (\hat{\bs x}_{\text{MMSE}}-\bs x) p(\bs x|\bs y) \ud \bs x=0 \\
    &\Leftrightarrow \hat{\bs x}_{\text{MMSE}} \underbrace{\int p(\bs x|\bs y) \ud \bs x}_{=1}
    = \int \bs x p(\bs x|\bs y) \ud \bs x \\
    &\Leftrightarrow \hat{\bs x}_{\text{MMSE}} = \mathbb{E}[\bs x|\bs y].
\end{split}
\end{align*}
$$