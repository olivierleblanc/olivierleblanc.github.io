---
title: "Low-rank circulant matrices"
page_title: "Low-rank circulant matrices"
excerpt: ""
date: March 3, 2024
toc: true
toc_label: "Content"
toc_sticky: true
last_modified_at: March 3, 2024
og_image: /assets/images/posts/semantic-search/similarity-header.jpg
---

<!-- Load MathJax Configuration -->
<script src="/assets/js/mathjax-config.js"></script>

<!-- Load MathJax library -->
<script type="text/javascript" async 
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js">
</script>

> **Theorem.** 
> A circulant matrix $$\bs C \in \Cbb^{N\times N}$$ which has been generated using the DFT $$\bs u = \bs{Fv} \in \Cbb^N$$ (with $$\bs F$$ the DFT matrix) of a $$K$$-sparse vector $$\bs v \in \Cbb^N$$ is rank-$$K$$.

**Proof.** 
If $$\bs v$$ is $$K$$-sparse ($$\norm{}{\bs v}{0} \le K$$), it can be written as 

$$
\begin{equation} \tag{1} \label{eq:sparse}
    \bs v = \sum_{q=0}^{K-1} \rho_q \bs e_{p_q}.
\end{equation}
$$

Moreover, let $$T(\bs u)$$ be the operator that turns a vector $$\bs u \in \Cbb^N$$
into a circulant matrix, that is, in <em>modulo arithmetic</em> ($$u_{k-l} = u_{\modulo{k-l}{N}}$$)

$$
\begin{equation}
    (T(\bs u))_{k,l} = u_{k-l}
\end{equation} 
$$

We can write $$\bs C = T(\bs u) = T(\bs{Fv})$$. We also have $$u_a = \sum_{b=0}^{N-1} F_{a,b} v_b$$. The circulant matrix at index $$jk$$ can thus write 

$$
\begin{align} \tag{2} \label{eq:dev}
\begin{split}
    C_{jk} &= u_{j-k} = \sum_{l=0}^{N-1} F_{j-k,l}~ v_l 
    \underset{\eqref{eq:sparse}}{=} \sum_{l=0}^{N-1} F_{j-k,l} 
    \sum_{q=0}^{K-1} \rho_q \delta_{l,p_q} \\ 
    &= \sum_{q=0}^{K-1} \rho_q F_{j-k,p_q } 
    \underbrace{\sum_{l=0}^{N-1} \delta_{l,p_q}}_{=1} \\
    &= \sum_{q=0}^{K-1} \rho_q F_{j,p_q} F_{k,p_q}^*
\end{split}
\end{align}
$$

where the last line in Eq.~\eqref{eq:dev} is obtained thanks to the 
definition of the coefficients of the DFT matrix 
$$F_{jk} = e^{\frac{-\im 2\pi jk}{N}}$$. This is the critical property which 
allows this proof. Finally, the circulant matrix writes as 

$$
\begin{equation} \tag{3} \label{eq:not1}
    \bs C = \sum_{q=0}^{K-1} \rho_q \bs f[p_q] \bs f[p_q]^*
\end{equation}
$$

with $$\bs f [n] := \bs F_{:,n}$$, which makes it rank-$$K$$.

The circulant matrix $$\bs C$$ in \eqref{eq:not1} can also be equivalently represented as  

$$
\begin{equation} \tag{4} \label{eq:quasiSVD}
    \bs C = \begin{bmatrix}
        & & & \\
        & & & \\
        \bs f [p_0] & \bs f [p_1] & \dots \\
        & & & \\
        & & &
    \end{bmatrix} \begin{bmatrix}
        \rho_0 & & & \\
        & \rho_1 & & \\
        & & \rho_2 & \\ 
        & & & \ddots 
    \end{bmatrix} \begin{bmatrix}
        & & \bs f^*[p_0] & & \\
        & & \bs f^*[p_1] & & \\
        & & \vdots & & \\
    \end{bmatrix} = \bs{FP} \diag(\bs \rho) \bs P^* \bs F^*,
\end{equation}
$$

with $$\bs \rho \in \Rbb^K$$ containing the $$K$$ coefficients of the vector $$\bs v$$
which also shows $$\bs C$$ is rank-$$K$$.

<ul>Note:</ul> 
With the conventional writing $$\bs v = \sum_{l=0}^{N-1} v_l \bs e_l$$, a derivation similar
to \eqref{eq:dev} would lead to $$\bs C = \sum_{l=0}^{N-1} v_l \bs f[l] \bs f[l]^*$$. 

Thus

$$
\begin{equation} \label{eq:decomp}
\bs C = \bs F \diag( \bs v) \bs F^*    
\end{equation}
$$

We see that \eqref{eq:quasiSVD} is very close to the SVD defition: 
$$\bs C := \bs U \bs{\Sigma V}^*$$. The subtlety comes where the singular values in $$\bs \Sigma$$ are (i) all positive and (ii) aranged in descending order. 
(i) implies $$\bs C = \bs F \bs P |\diag(\bs \rho)| \bs P^* \tilde{\bs F}^*$$ where $$\tilde{\bs F}^*$$ is the Fourier matrix with each column $$i$$ multiplied by $$+1$$ or $$-1$$ depending on the sign of associated $$\rho_i$$. 
(ii) implies the selection matrix $$\bs P$$ must also contain permutation to ensure $$\bs \rho$$ is aranged in descending order. 

To synthetize, we have 

$$
\begin{align}
\bs C &= \bs F \diag (\bs v) \bs F^* \\
&= \bs F \diag(|\bs v|) \bs S \bs F^*\\
&= \bs F \bs P^* \diag(|\tilde{\bs v}|) \bs{PSF}^* \\
&= \bs{U\Sigma V}^*,
\end{align}
$$

with $$\bs S = \diag(\text{sign}(\bs v))$$, $$\bs P$$ is a permutation matrix such that 
$$\bs P |\bs v| = |\tilde{\bs v}|$$ and $$\tilde{v}_k \ge |\tilde{v}_{k+1}|$$, $$\bs \Sigma
= \diag(|\tilde{\bs v}|)$$, and the unitary matrices $$\bs U = \bs F \bs P^*$$, and 
$$\bs V = \bs F \bs S \bs P$$. By definition, this means that 
$$\bs U \bs \Sigma \bs V^*$$ is the SVD decomposition of $$\bs C$$. 

In fact, $$\bs U \bs \Sigma \bs V^* = \bs U \bs Z \bs \Sigma \bs Z^* \bs V^*$$
for any $$\bs Z = {\rm diag}(\bs z)$$ such that $$\bs Z \bs Z^* = \bs I$$ 
(that is, $$\bs z$$ is such that $$|z_k|=1$$). 
So we can choose $$\bs z$$ to make $$\bs U\bs Z$$ and $$\bs V \bs Z$$ real, 
as in J. Romberg developments. 

This proves a rank-$$K$$ circulant matrix contains only $$K$$ degrees of freedom, very less than a general rank-$$K$$ matrix containing $$(2K+1)N$$ DOFs. 

We also see a circulant matrix is hermitian if $$\bs v \in \Rbb^N$$ as $$\bs C^* = \bs F \diag(\bs v)^* \bs F^* = \bs F \diag(\bs v) \bs F^* = \bs C \Leftrightarrow \bs v = \bs v^*$$. 