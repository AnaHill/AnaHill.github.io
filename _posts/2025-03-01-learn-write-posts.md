---
layout: post
title: "How to start blogging using GitHub Pages (my first post!)"
categories: [blog]
---
This is my first blog post to describe how to combine Jekyll and GitHub Pages. Briefly, you should
1. add `_post` folder
2. where you should add a markdown file named as `YEAR-MONTH-DAY-title.md`, for example this post is named as `2025-03-01-learn-write-posts.md` and write your content

Remember to start all your blog post files with the front matter that sets a layout or other meta data, example [this blog post file](https://github.com/AnaHill/AnaHill.github.io/blob/main/_posts/2025-03-01-learn-write-posts.md?plain=1) starts with the following 
```
---
layout: post
title: "How to start blogging using GitHub Pages (my first post!)"
categories: [blog]
---
```

I had problems to have any theme applied to blog post (I used merlot theme in my main page). In this case, you can
1. add `_layouts` folder if you do not have it already 
2. add `post.html` file there with the proper content, see example below


My [post.html](https://github.com/AnaHill/AnaHill.github.io/blob/main/_layouts/post.html) includes following 
```html
{% raw %}
---
layout: default
---

<article class="post">
  <h1>{{ page.title }}</h1>
  <p><em>Published on {{ page.date | date: "%B %d, %Y" }}</em> 
    (<a href="{{ site.url }}/">back to main page</a>)</p>
  <div class="content">
    {{ content }}
  </div>
</article>

{% endraw %}

```

You can create list of your (blog) post with the following command, see more info on [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/). 
I have included following code in my <a href="{{ site.url }}/"> main page</a> to list my blog posts

```html
{% raw %}
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
{% endraw %}
```

## References used
- [GitHub Docs to add content with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
- [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/) 
- and some help from ChatGPT 😎🤖
