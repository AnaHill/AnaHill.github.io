---
layout: default
title: "My struggles to make posts work properly"
date: 2025-03-23
last_modified_at: 2025-04-06
categories: [demonstration]
tags: [GitHub Pages, Jekyll, debug]
---

{% include blog-meta.html %}

> 😎 Nerd your day! 🤓  

## Update on April, 2025
I found a solution. Or at least a workaround; not perfect but ok. Basically, now all blog post are
- using default theme (instead of post that was used previously)
- metadata like "Published on" etc are included with `include blog-meta.html` command
- I include links to my blog list and main page in each blog post file
  - this is a bit bummer, and therefore my previously used "post.html" method, described [here](https://anahill.github.io/blog/learn-write-posts.html), would have been better

<!-- ![blog_post_workaround](/pics/posts/blog_post_workaround.png "Workaround to make blog post to use my default merlot theme")  -->
<figure style="text-align: center;">
  <img src="pics/post/blog_post_workaround.png" alt="Workaround to make blog post to use my default merlot theme">
  <figcaption><em>"Blog post workaround: 1) change layout from post to default, 2) include blog-meta.html, and 3) include links to my blog list and main page." </em></figcaption>
</figure>

## Previous text 

In this post, I'll be documenting my journey to make these blog posts, like this, work probably. Originally, idea was to demonstrate how a markdown file is converted to a blog post. But, because of problems reported below, this turned to be documentation of the problem. Let's see if I find any solution! Please do not hesitate to contact me if you would have any tips that could help me!

There are probably many problems with these blog post pages, but where I noticed it first was headings, they are just not implemented as they should. So, let's deep dive into the problem!

# This is H1 title text
Above text is written as `# This is H1 title text`. If working properly, it should use H1 level style based on theme I have applied, currently merlot. Example, how this `H1` text should look can be found e.g. on my main page like [H1 level anahill.github.io/#-explore-more](https://anahill.github.io/#-explore-more "anahill.github.io/#-explore-more"). 

Same goes lower level `H2`heading, example how it should look like is 
[anahill.github.io/work.html#-own-projects](https://anahill.github.io/work.html#-own-projects "anahill.github.io/work.html#-own-projects")

In the following pic, I try to demonstrate this: left side shows how headings should look when merlot theme is applied properly; right side the current state in this blog post.  
You do not need to be a sherlock to see the difference! 🤓 
![comparison_of_heading_](/pics/posts/compare_correct_headings_to_current_post.png "Properly applied headings on the left vs headings on this blog post (right)")

## H2 level heading
Above line is H2 title text starting with two `##`. 

# Check how H1 looks 
Above line is created with `#` tag, so it should use header level 1 style. You can see the difference if you use e.g. the following code.

```html
<h1 style="font-size: 2.2em; color: #600000; font-weight: bold;">
    This is H1 title text with `h1` tag and attributes written in html 
</h1>
```

Above code result following heading text.

<h1 style="font-size: 2.2em; color: #600000; font-weight: bold;">
This is H1 title text with `h1` tag and attributes written in html 
</h1>

After page is built, you can see the outcome; so yes, probably I could always manually apply html to each headings in my blog posts, but I do not want to do that.

![manual_h1_title](/pics/posts/manual_h1_title_outcome.png "how manually written h1 text is shown currently")

Let's test pure h1 element also, below I have written `<h1> Pure h1 element, no attributes included </h1>`.

<h1> Pure h1 element, no attributes included </h1>


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

<a href="{{ site.baseurl }}/blog/" style="color:green;"><strong>⬅ To My Blog list</strong></a><br>
<a href="{{ site.baseurl }}/" style="color:green"><strong>⬅ To My Main Page</strong></a>
