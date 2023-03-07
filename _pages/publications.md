---
layout: single
permalink: /publications/
title: Publications
years: [2023, 2022, 2020]
---
<!-- _pages/publications.md -->
<div class="publications">
  {%- for y in page.years %}
    <h2 class="year">{{y}}</h2>
    {% bibliography -f papers -q @*[year={{y}}]* %}
  {% endfor %}
</div>