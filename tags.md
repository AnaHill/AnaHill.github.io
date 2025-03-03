---
layout: blog
title: "🏷️ Tags"
permalink: /tags/
---

# 🏷️ Tags in my posts

{% for tag in site.tags %}
  - **[{{ tag[0] }}](/tag/{{ tag[0] | slugify }}/)** ({{ tag[1] | size }} posts)
{% endfor %}


# Navigate

<a href="{{ site.baseurl }}/blog/" style="color:blue;">
  <strong>⬅ To My Blog list</strong>
</a>
<br>
<a href="{{ site.baseurl }}/" style="color:green">
  <strong>⬅ To My Main Page</strong>
</a>