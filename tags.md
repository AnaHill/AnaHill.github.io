---
layout: page
title: "Tags"
permalink: /tags/
---

## 🏷️ Tags  

{% for tag in site.tags %}
  - **{{ tag[0] }}** ({{ tag[1] | size }} posts)
{% endfor %}
