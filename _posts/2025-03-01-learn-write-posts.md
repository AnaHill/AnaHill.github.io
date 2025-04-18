---
layout: default
title: "How to start blogging using GitHub Pages"
date: 2025-03-01
last_modified_at: 2025-04-06
categories: [blogging]
tags: [GitHub Pages, Jekyll, blogging]
---

{% include blog-meta.html %}

> 😎 Nerd your day! 🤓  

## Update on April, 2025
Method described in next section is **not used anymore in my blog posts**. I just was not able to apply theme (merlot in this case) properly when using `post.html` approach. 
For the possible reasons, I have given a more detailed information in my [**another post**](/blog/my-struggle-to-make-post-work-properly.html "My struggles to make posts work properly"); here, I just let our 🤖 friend named as chat-GPT to answer. 

> That’s called a layout chaining technique, where `post.html` extends `default.html`. That part is totally fine in theory — but in practice, your **_layouts/post.html doesn't contain any actual HTML** content.
> 
> And here’s the issue: **Jekyll does not render the front matter from a layout file like a normal page/post**. Therefore, `layout: default` inside `post.html` is **ignored**.


## Previous version: using post.html
**Notice**: your theme might not work as planned, e.g. related to headings, if the following approach is applied.

--- 

In this **my first blog post** (oujee! 🤓😎), I describe how to combine Jekyll and GitHub Pages to make a blog post. Briefly, you should
1. add `_post` folder
2. where you should add a markdown file named as `YEAR-MONTH-DAY-title.md`, for example this post is named as `2025-03-01-learn-write-posts.md` and write your content

Remember to start all your blog post files with the front matter that sets a layout or other meta data, example [this blog post file](https://github.com/AnaHill/AnaHill.github.io/blob/main/_posts/2025-03-01-learn-write-posts.md?plain=1) starts with the following 
```
---
layout: post
title: "How to start blogging using GitHub Pages"
date: 2025-03-01
last_modified_at: 2025-03-03
categories: [blogging]
tags: [GitHub Pages, Jekyll, Blogging]
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
  {% if page.last_modified_at %}
    <em>&nbsp;(Updated on {{ page.last_modified_at | date: "%B %d, %Y" }})</em>
  {% endif %}
  </p>

  {% if page.tags %}
  <p>
    <strong>Tags:</strong>
    {% for tag in page.tags %}
      <span style="color:blue;">{{ tag }}</span>{% unless forloop.last %}, {% endunless %}
    {% endfor %}
  </p>
{% endif %}

  <div class="content">
    {{ content }}
  </div>
  
  <a href="{{ site.baseurl }}/blog/" style="color:green;">
    <strong>⬅ To My Blog list</strong>
  </a>
  <br>
  <a href="{{ site.baseurl }}/" style="color:green">
    <strong>⬅ To My Main Page</strong>
  </a>
</article>
{% endraw %}
```

You can create list of your post with the following command, see more info on [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/). I included following code in my <a href="{{ site.url }}/"> main page</a> to list only my recent blog posts; with parameter in the for-loop, `limit:5` you can control how many posts are listed. If you want to list all your post, like I have done in my blog archieve [page](https://anahill.github.io/blog/ "blog post listed"), just remove `limit:5` in the for loop row.

```html
{% raw %}
<ul>
  {% for post in site.posts limit:5 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>  
      <em>({{ post.date | date: "%B %d, %Y" }})</em>
    </li>
  {% endfor %}
</ul>
{% endraw %}
```

📝 Happy blogging! 😊

## References used
- [GitHub Docs to add content with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
- [Jekyll's documentation about posts](https://jekyllrb.com/docs/posts/) 
- and some help from ChatGPT 😎🤖

--- 
<a href="{{ site.baseurl }}/blog/" style="color:green;"><strong>⬅ To My Blog list</strong></a><br>
<a href="{{ site.baseurl }}/" style="color:green"><strong>⬅ To My Main Page</strong></a>