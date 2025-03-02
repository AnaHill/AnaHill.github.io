---
layout: post
title: "How to start blogging using GitHub Pages (my first posts!)"
---
# How to write blog post using Jekyll and Github Pages
This is my first blog post to learn how to combine Jekyll and GitHub Pages.

Briefly,
1. add `_post` folder
2. where add a markdown file named as `YEAR-MONTH-DAY-title.md`, example this post `2025-03-01-learn-write-posts.md`

Then, I had problems to have any theme applied to blog post (I used merlot theme in my main page).

You can create list of your (blog) post with the following command, see more info on [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/). 

```html
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
```

References used
- [GitHub Docs to add content with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
- [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/) 
