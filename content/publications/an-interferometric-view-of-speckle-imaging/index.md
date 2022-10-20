---
title: "An Interferometric view of Speckle Imaging"
author: ["Laurent Jacques"]
tags: ["rank-one projections", "interferometry", "lensless", "computational imaging"]
draft: false
#subtitle: ''
#summary: ''
authors: # One author per item "-"
- Olivier Leblanc
- Matthias Hofer
- Siddharth Sivankutty
- Hervé Rigneault
- Laurent Jacques
tags: # One keywords per item "-" with format - '"keyword"'
- '"rank-one projections"'
- '"interferometry"'
- '"lensless"'
- '"computational imaging"'
#categories: []
date: '2022-09-15'  #format: 'yyyy-mm-dd'
#featured: false
#draft: false
# Featured image
# To use, add an image named YY to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
#image:
#caption: ''
#focal_point: ''
#preview_only: false
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. YY references YY.
#   Otherwise, set Y.
#projects: []
publication_types:
#  - '0' = Uncategorized
#  - '1' = Conference paper
#  - '2' = Journal article
#  - '3' = Preprint / Working Paper
#  - '4' = Report
#  - '5' = Book
#  - '6' = Book section
#  - '7' = Thesis (v4.2+ required)
#  - '8' = Patent (v4.2+ required)
- '1'
#abstract: ''
publication: '*Workshop on Low-Rank Models and Applications -- LRMA 22*'
#url_pdf:
#url_code: '#'
#url_dataset: '#'
#url_poster: '#'
#url_project: ''
#url_slides: ''
#url_source: '#'
#url_video: '#'
#doi: ''
# custom links
links:
- name: Poster
  url: poster_LRMA22.pdf
#  name: arXiv
#  icon_pack: ai
#  url: https://arxiv.org/abs/ #add arxiv identifier here
- name: DIAL
  url: http://hdl.handle.net/2078.1/265610 #add dial handle or comment this out
---

**Abstract**: Lensless endoscopy (LE) with multicore fibers (MCF) enables fluorescent imaging of biological samples at cellular scale.  In this work, we show that the corresponding imaging process is tantamount to collecting multiple rank-one projections (ROP) of an Hermitian _interferometric_ matrix---a matrix encoding a subsampling of the Fourier transform of the sample image.  Specifically, each ROP of this matrix is achieved with the complex vector shaping the incident wavefront using a spatial light modulator (SLM), and, the image frequencies are taken at pairwise differences of the cores positions, allowing for as many frequencies as the square of the core number if there is no multiplicity.  As for typical compressive sensing (CS) applications, we demonstrate that the sampling rate is directly connected to the sample structure when the SLM is configured randomly. For instance, a sparse sample in the spatial domain induces a low rank interferometry matrix.  Interestingly, inspecting the separate dimensional conditions ensuring the specific restricted isometry properties of the two composing sensing models (the partial Fourier sampling of the interferometric matrix and the ROPs applied to it) in the observation of sparse images, we show in a simplified setting that a basis pursuit denoising (BPDN) program associated with an \\(\ell\_1\\)-fidelity cost provably provides a stable and robust image estimate.
