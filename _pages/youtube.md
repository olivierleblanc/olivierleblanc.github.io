---
layout: page
title: YouTube
permalink: /youtube/
description: Gallery of my favorite YouTube channels.
nav: false
nav_order: 3
display_categories: [science]
horizontal: false
---

<!-- pages/youtube.md -->
<div class="youtube">
{% if site.enable_youtube_categories and page.display_categories %}
  <!-- Display categorized youtube -->
  {% for category in page.display_categories %}
  <a id="{{ category }}" href=".#{{ category }}">
    <h2 class="category">{{ category }}</h2>
  </a>
  {% assign categorized_youtube = site.youtube | where: "category", category %}
  {% assign sorted_youtube = categorized_youtube | sort: "importance" %}
  <!-- Generate cards for each youtube -->
  {% if page.horizontal %}
  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for youtube in sorted_youtube %}
      {% include youtube_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for youtube in sorted_youtube %}
      {% include youtube.liquid %}
    {% endfor %}
  </div>
  {% endif %}
  {% endfor %}

{% else %}

<!-- Display youtube without categories -->

{% assign sorted_youtube = site.youtube | sort: "importance" %}

  <!-- Generate cards for each youtube -->

{% if page.horizontal %}

  <div class="container">
    <div class="row row-cols-1 row-cols-md-2">
    {% for youtube in sorted_youtube %}
      {% include youtube_horizontal.liquid %}
    {% endfor %}
    </div>
  </div>
  {% else %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for youtube in sorted_youtube %}
      {% include youtube.liquid %}
    {% endfor %}
  </div>
  {% endif %}
{% endif %}
</div>
