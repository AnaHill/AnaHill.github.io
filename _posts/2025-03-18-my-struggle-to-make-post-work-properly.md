---
layout: post
title: "My struggles to make posts work properly"
date: 2025-03-23
# last_modified_at: 2025-03-23
categories: [demonstration]
tags: [GitHub Pages, Jekyll, debug]
---

In this post, I'll be documenting my journey to make these blog posts, like this, work probably. Originally, idea was to demonstrate how a markdown file is converted to a blog post. But, because of problems reported below, this turned to be documentation of the problem. Let's see if I find any solution! Please do not hesitate to contact me if you would have any tips that could help me!

There are probably many problems with these blog post pages, but where I noticed it first was headings, they are just not implemented as they should. So, let's deep dive into the problem!

# This is H1 title text
Above text is written as `# This is H1 title text`. If working properly, it should use H1 level style based on theme I have applied, currently merlot. Example, how this `H1` text should look can be found e.g. on my main page like [H1 level anahill.github.io/#-explore-more](https://anahill.github.io/#-explore-more "anahill.github.io/#-explore-more"). Same goes lower level `H2`heading, example how it should look like is  
[anahill.github.io/work.html#-own-projects](https://anahill.github.io/work.html#-own-projects "anahill.github.io/work.html#-own-projects")


## H2 level heading
Above, is H2 title text starting with two `##`.
https://anahill.github.io/work.html#-own-projects

# How to apply H1 level text in blog post: use html
Above line is created with `#` tag, so it should use header level 1 style. You can see the difference if you use the following code

```html
<h1 style="font-size: 2.2em; color: #600000; font-weight: bold;">
    This is H1 title text with `h1` tag and attributes written in html 
</h1>
```


<h1 style="font-size: 2.2em; color: #600000; font-weight: bold;">
This is H1 title text with `h1` tag and attributes written in html 
</h1>





<!-- 
## Second level heading
Typically, I use this in my blog post; title in layout is 'reserver' for "H1 level headings". 
-->

### Third level heading
Outcome is like this when make heading with three `###`. Currently, it is the same as higher level headings.

#### Fourth last time
Same goes this: style.css should now include definition for also forth level headings `####`, but you can see the outcome.

# 📝 Blogging
To start blogging with GitHub Pages, I recommend to check out my previous post on [How to start blogging using GitHub Pages]({% post_url 2025-03-01-learn-write-posts %}).

📝 Have a great time with GitHub Pages! 😊

## <span id="ref"> Find out more </span>
- GitHub Pages [documentation](https://pages.github.com/)

--- 
