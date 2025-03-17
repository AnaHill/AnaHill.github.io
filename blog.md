---
layout: list_pages
title: "📝 A-J Mäki's Blog Posts"
permalink: /blog/
---

> 😎 Nerd your day! 🤓 

## 📝 Blog Archive  
Here you can find all my blog posts, sorted by date.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>  
      <em>({{ post.date | date: "%B %d, %Y" }})</em>
    </li>
  {% endfor %}
</ul>

---

## 🏷️ Tags  

Here are the topics I frequently write about:

<ul>
  {% for tag in site.tags %}
    <li><strong>{{ tag[0] }}</strong> ({{ tag[1] | size }} posts)</li>
  {% endfor %}
</ul>

## this is test: can't make tags-links working properly
<p>
  <strong>Tags:</strong>
  {% for tag in site.tags %}
    <a href="{{ site.baseurl }}/tags#{{ tag | slugify }}" style="color:blue;">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
  {% endfor %}
</p>


