---
title:  About
page_title: About
layout: single
permalink: /about/
author_profile: false
comments: false
---

Welcome to my homepage! :wave:

### About Me

I earned my BSc in electromechanical engineering and MSc in electrical engineering.

<!-- Throughout my studies I was involved in several science projects that 
used large amounts of data to discover patterns and model phenomena.

My interests range from machine learning, data engineering to 
computational optimization, and high performance computing.

In my spare time I enjoy taking walks, learning new languages, 
drawing, and sometimes playing the guitar. -->

I am a PhD student at UCLouvain in Louvain-la-Neuve under the supervision of [Pr. Laurent Jacques](https://uclouvain.be/en/directories/laurent.jacques). Find my complete cursus and more about me here.

### Research

My research is about drawing on signal processing insights to reduce the computational cost of machine learning methods; see more on my research page. Don't hesitate to also check out my list of publications and related code.

I work within Institute of Signal Processing Group (ISPG) and my research topic is *GeneCI: Physically-Driven and Generative Neural Networks for Computational Imaging*.

The goal of my research project is to tackle computational imaging
(CI) applications that suffer both from the ill-posedness of the imaging 
process and high computational and memory complexities. I decided to 
focus on fluorescent lensless endoscopy (LE) with ultra thin multicore 
optical fibers (MCF), extending the work of Stephanie Guérit, a recently 
graduated PhD student of my current supervisor, Prof. <a href="https://laurentjacques.gitlab.io">Laurent Jacques</a>.
    
* ###  What is Lensless Endoscopy and what challenges does it raise?
The lensless endoscope (LE) is a promising device to acquire in vivo 
images at a cellular scale. The challenges raised by LE are twofold: (i) first, the miniaturization 
of this endoscope (its cross section amounts to a few hundreds of microns) 
prevents it from direct imaging using a lens, both for manufacturing 
and nonlinear optical effects issues (ii) second, the light actually
captured by the device represents a small fraction of the initially 
emitted light, either by direct reflection or fluorescence (occurring 
when the biological sample captures part of the energy of the incoming 
light and re-emits it at another larger wavelength). Hence, one requires 
to provide sufficient illumination power combined with a sensitive 
enough light sensor to hope for satisfying image reconstruction. 
These issues make LE still an open-problem for provable recovery and
real-time usage in concrete biomedical applications, compared to more 
matured applications such as MRI, confocal microscopy and refraction 
tomography.

<center>
<img
    src="/assets/images/LEMCF.png"
    alt="microdicom-preview"
    caption="MicroDicom Preview"
    width="600px"
/>
<figcaption> Figure 1: Working principle of a lensless endoscope viewed as an interferometric machine (legend: SLM: spatial
light modulator; MCF: multicore optical fiber). </figcaption>
</center>

* ### What problems do I focus on?
Here are some axes I'm considering for my PhD research:
      
    * interferometric Lensless Endoscopy:
        Including the physical constraints of a LE, I refined the sensing 
        model for a 2D object, introducing the physics of electromagnetic 
        wave propagation, more precisely the Rayleigh-Sommerfeld equation 
        in the Far-Field assumption, for now. This new model called
        Interferometric Lensless Endoscopy (ILE) brings multiple advances both in a theoretical
        and practical point of view. 

        <center>
        <img
            src="/assets/images/schema.png"
            alt="microdicom-preview"
            caption="MicroDicom Preview"
            width="600px"
        />
        <figcaption> Figure 2: Working principle of a lensless endoscope viewed as an interferometric machine (legend: SLM: spatial
        light modulator; MCF: multicore optical fiber). </figcaption>
        </center>
      
    * Tomographic lensless endoscopy: LE is so far limited 
        to the observation of planar objects perpendicular to the optical 
        fiber distal end (see Fig. 1); and this is still the
        case with the ILE model described above. I plan to extend this 
        modality to tomographic LE (TLE), namely to the estimation 
        of a biological sample volume (the density of
        fluorophore) by collecting the light re-emitted under a controlled 
        illumination pattern.
        Depending on what can be done in 3D with the ILE model, 
        I will either model the forward acquisition using a 3D extended 
        ILE model or with a physically-driven neural network (NN),
        where the NN activation functions represent light-matter interaction, 
        and the NN weights correspond to a discrete 3D representation 
        of the sample. 
       
    * Improved TLE modeling with generative networks: 
        TLE crucially depends on (i) an accurate model for the illumination 
        pattern used to probe the biological sample, and (ii) a
        suitable representation of the sample volume to regularize the 
        related inverse problem. I will tackle the first point by learning 
        the transformation of the wave front operated by the MCF,
        using a supervised (or inferent) generative network (s-GN) learned 
        in an offline calibration  stage. The second point will be 
        solved by leveraging unsupervised GNs (u-GNs) and their
        highly compressed latent space representation. 
        These appealing alternatives to analytical representations of images 
        (such as sparse wavelet representation or low-rank models) will
        be learned with generative adversarial networks or variational 
        autoencoders.

### Affiliations
I am funded by the Belgian "Fonds National de la Recherche Scientifique" (F.R.S.-FNRS), which granted me 4 years of research funding as "Aspirant FNRS", starting in October 2020.

I'm doing my PhD at UCLouvain (Université catholique de Louvain, the university in Louvain-la-Neuve, Belgium). More precisely, I am affiliated to the ICTEAM research institute, and within it, the Electrical Engineering department (ELEN). Finally, I am a member of the Image and Signal Processing Group (ISPGroup), active in UCLouvain.

### Besides research...
I'm doing sport almost everyday. I'm playing soccer and tennis. I also often go to the gym with friends.

Very curious and passionate by science, I regularly watch videos on YouTube which vulgarize many science subjects, either very technical or also about philosophy, economy, history, ... On a smaller measure, I like reading some non-fiction stuff similar to the videos I watch.

Working daily on my pc, I'm listening to music all day, with the type depending on the period (mostly rock, electro and rap).

I'm currently self learning piano :)

### Curriculum Vitae
- 2015-2018: Bachelors degree in engineering sciences (UCLouvain), options in electricity and mechanics, cum laude.
- 2018-2020: Masters degree in electrical engineering (UCLouvain), option in signal processing, magna cum laude.
- Master thesis: "Comparison between the walking droplet and the electron behaviour inside a chaotic stadium cavity", with Benoît Hackens (download).
- 2020-: PhD student (UCLouvain); Research Fellow at F.R.S.-FNRS (ASP - ASPIRANT FNRS).