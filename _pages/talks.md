---
layout: single
permalink: /talks/
title: Talks
#img: assets/img/eusipco_talk.jpg
years: [2023]
---

<!-- {%- include figure_post.html 
    path="assets/img/eusipco_talk.jpg"
    size="100%"
    -%} -->

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f talks -q @*[year={{y}}]* %}
{% endfor %}

</div>
