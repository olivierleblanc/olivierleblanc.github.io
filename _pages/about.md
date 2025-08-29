---
layout: about
title: about
permalink: /
subtitle: <a href='#'>Affiliations</a>. Address. Contacts. Motto. Etc.

profile:
  align: right
  image: moi_souriant.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Andenne, Belgium</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: true
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

Welcome to my homepage! :wave:

### About Me

I am from Belgium :belgium:

I earned my BSc in electromechanical engineering, MSc in electrical engineering, and PhD in applied maths to computational imaging.

My interests range from machine learning, data engineering to 
computational optimization, and high performance computing.

In my spare time I enjoy practicing sport :soccer: :tennis:, learning new languages :france: :spain: :netherlands:, and sometimes playing piano.

### Previous research

My research was about drawing on signal processing insights to reduce the computational cost of machine learning methods; see more on my research page. Don't hesitate to also check out my list of publications and related code.

I worked within [Institute of Signal Processing Group (ISPG)](https://ispgroup.gitlab.io) and my research topic is *GeneCI: Physically-Driven and Generative Neural Networks for Computational Imaging*.

The goal of my research project is to tackle computational imaging (CI) applications that suffer both from the ill-posedness of the imaging process and high computational and memory complexities. I decided to focus on fluorescent lensless endoscopy (LE) with ultra thin multicore optical fibers (MCF), extending the work of Stephanie Guérit, a recently graduated PhD student of my current supervisor, Prof. <a href="https://laurentjacques.gitlab.io">Laurent Jacques</a>.
    
* ###  What is Lensless Endoscopy and what challenges does it raise?
The lensless endoscope (LE) is a promising device to acquire in vivo 
images at a cellular scale. The challenges raised by LE are twofold: (i) first, the miniaturization of this endoscope (its cross section amounts to a few hundreds of microns) prevents it from direct imaging using a lens, both for manufacturing and nonlinear optical effects issues (ii) second, the light actually captured by the device represents a small fraction of the initially  emitted light, either by direct reflection or fluorescence (occurring when the biological sample captures part of the energy of the incoming light and re-emits it at another larger wavelength). Hence, one requires to provide sufficient illumination power combined with a sensitive enough light sensor to hope for satisfying image reconstruction. 
These issues make LE still an open-problem for provable recovery and real-time usage in concrete biomedical applications, compared to more matured applications such as MRI, confocal microscopy and refraction tomography.

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

I'm doing my PhD at UCLouvain (Université catholique de Louvain, the university in Louvain-la-Neuve, Belgium). More precisely, I am affiliated to the ICTEAM research institute, and within it, the Electrical Engineering department (ELEN). 

### Besides research...
I'm doing sport almost everyday. I'm playing soccer and tennis. I also often go to the gym with friends.

Very curious and passionate by science, I regularly watch videos on YouTube which vulgarize many science subjects, either very technical or also about philosophy, economy, history, ... On a smaller measure, I like reading some non-fiction stuff similar to the videos I watch.

Working daily on my pc, I'm listening to music all day, with the type depending on the period (mostly rock, electro and rap).

I'm currently self learning piano :)

<!-- Write your biography here. Tell the world about yourself. Link to your favorite [subreddit](http://reddit.com). You can put a picture in, too. The code is already in, just name your picture `prof_pic.jpg` and put it in the `img/` folder.

Put your address / P.O. box / other info right below your picture. You can also disable any of these elements by editing `profile` property of the YAML header of your `_pages/about.md`. Edit `_bibliography/papers.bib` and Jekyll will render your [publications page](/al-folio/publications/) automatically.

Link to your social media connections, too. This theme is set up to use [Font Awesome icons](https://fontawesome.com/) and [Academicons](https://jpswalsh.github.io/academicons/), like the ones below. Add your Facebook, Twitter, LinkedIn, Google Scholar, or just disable all of them. -->
