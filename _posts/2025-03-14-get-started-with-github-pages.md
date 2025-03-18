---
layout: post
title: "Get Started With GitHub Pages"
date: 2025-03-14 
last_modified_at: 2025-03-18
categories: [webpage]
tags: [GitHub Pages, Jekyll, portfolio]
---

In this post, using my [**main page**](https://anahill.github.io/) as an example, I will explain how you can start with GitHub Pages and show how it is possible to create a FREE 🤑 work portfolio like [**mine**](https://anahill.github.io/work.html).

<span style="color:red"> *I do **not** try to invent the wheel 𖥞 again*. </span>  
So, check the 👉[links in the end](#ref); first three links will guide you to set up your portfolio...except please consider this one thing I recommend you to do: 

<span style="color:green; font-size: 1.2em;"> ⚠️ Use `index.md` for main page of GitHub Pages and `readme.md` for the main repo. **PERIOD.** </span>  
... trust me, you will thank me for this, but let me next explain how to set-up your main page properly.

## Step1: Create a repo (`username.github.io`) and set-up `index.md` and `readme.md` files
First, create a **public** repo named as `username.github.io`.

After you have created a repo (be sure that your **repo is public**, otherwise this wont't work!)
- add `index.md` file to your main folder 
- keep your `readme.md` minimal, I recommend to have there mainly a link to your main page when it is ready.

As an example, see `readme.md` and `index.md` in my repo
- my [repo page](https://github.com/AnaHill/AnaHill.github.io "https://github.com/AnaHill/AnaHill.github.io") shows what is written in `readme.md`
- whereas, my `index.md` is the code that will be deployed to Github Pages using Github actions
  - my`index.md` raw code can be check [here](https://github.com/AnaHill/AnaHill.github.io/blob/main/index.md?plain=1 "https://github.com/AnaHill/AnaHill.github.io/blob/main/index.md?plain=1") 
  - my `readme.md` mainly provides links to web pages, see below shortened example what `readme.md` could contain

```markdown
🌐 **Visit the live site**: [anahill.github.io](https://anahill.github.io/ "my personal website")  

## 📂 Site Structure
- 🛠️ **[Work Portfolio](https://anahill.github.io/work.html)** 
- 👨‍🔬 **[Academic Portfolio](https://anahill.github.io/academic.html)** 
- 📝 Check out my blog posts **[here](https://anahill.github.io/blog/)**  
```

The pic below demostrates how `index.md` is converted to your main page.
![index.md to page](/pics/posts/How_indexmd_shows_as_page.png "how index.md is converted to page")

## Step2: Set-up `_config.yml` file
Create `_config.yml` file in your main folder. In my case, it includes following information.

```
title: A-J Mäki, PhD
description: Data Engineer & Passionate Data Guy 
logo: /pics/headshot_circle_ajm.png
repository: AnaHill/AnaHill.github.io
url: "https://anahill.github.io"
baseurl: ""  # Empty baseurl is okay for GitHub Pages
show_downloads: true
remote_theme: pages-themes/merlot@v0.2.0
plugins:
- jekyll-remote-theme
```
Last three lines above are used to apply merlot theme for the pages; pic below demonstrates how e.g. _title_ and _description_ are shown on your page.
![title and description](/pics/posts/how_title_and_description_is_showed.png "how title and description are shown on page using merlot theme")

## Blogging
To start blogging with GitHub Pages,  I recommend to check out my previous post on [_How to start blogging using GitHub Pages_]({% post_url 2025-03-01-learn-write-posts %}).

📝 Have a great time with GitHub Pages! 😊

## <span id="ref"> Find out more </span>
- GitHub Pages [documentation](https://pages.github.com/)
- Chijioke Joseph Okorji: [_From Meh to Marvelous: The Ultimate Guide to Crafting a Killer GitHub Profile_](https://medium.com/@chijiokeokorji/from-meh-to-marvelous-the-ultimate-guide-to-crafting-a-killer-github-profile-8dd3f6c6d602) and [repo](https://github.com/ChijiokeOkorji/ChijiokeOkorji)
- Shaw Talebi: [_How to Make a (Free) Data Science Portfolio Website With GitHub Pages_](https://medium.com/the-data-entrepreneurs/how-to-make-a-free-data-science-portfolio-website-with-github-pages-aa1e4965e155)
- Alexandre Sanlim's [repo](https://github.com/alexandresanlim/) as well as [Daria Stanilevici's](https://github.com/daria-stanilevici/daria-stanilevici) have some nice features worth of checking

--- 
