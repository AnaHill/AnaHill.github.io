---
layout: default
title: "📝 Blog Archive"
permalink: /blog/
---

# 📝 Blog Archive
Here you can find all my blog posts, sorted by date.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>  
      <em>({{ post.date | date: "%B %d, %Y" }})</em>
    </li>
  {% endfor %}
</ul>


<a href="{{ site.url }}" style="color:green;">
  <strong>⬅ Back to Main Page</strong>
</a> 
