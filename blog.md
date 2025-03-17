---
layout: list_pages
title: "📝 A-J Mäki's 😎 Nerd your day! 🤓 Blog Posts"
permalink: /blog/
---

> 😎 _Nerd your day!_ 🤓 

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

