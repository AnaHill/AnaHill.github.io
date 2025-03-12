---
layout: post
title: "Create a website from your repo using GitHub Pages"
date: 2025-03-12
# last_modified_at: 2025-03-20
categories: [portfolio]
tags: [GitHub Pages, Jekyll, portfolio]
---

In this post, I will explain how you can start with GitHub Pages.
As an example, I'll show how I set-up my [main page](https://anahill.github.io/) and created a FREE 🤑 [work portfolio](https://anahill.github.io/work.html).


<strong><big> I don't try to invent the wheel again </big></strong>  
👉 So, check the [links I provide in the end](#ref), first three links will guide you to set up your portfolio.  
...except one thing I recommend you to do🚨  
<strong><big>  Use `index.md` for main page of GitHub Pages and `readme.md`</big></strong>  
... trust me, you will thank me for this! Next, I will explain why.

## How to set-up your main page
### Step1: Create a repo (`username.github.io`) and set-up `index.md` and `readme.md` files
First, create a **public** repo named as `username.github.io`.

After you have created a repo (be sure that your **repo is public**, otherwise this wont't work!)
- add `index.md` file to your main folder 
- keep your `readme.md` minimal, I recommend to add link your main page when it is ready.

As an example, see `readme.md` and `index.md` in my repo
- my [repo page](https://github.com/AnaHill/AnaHill.github.io "https://github.com/AnaHill/AnaHill.github.io") shows what is written in `readme.md`
- whereas, my `index.md` is the code that will be deployed to Github Pages using Github actions
  - my`index.md` raw code can be check [here](https://github.com/AnaHill/AnaHill.github.io/blob/main/index.md?plain=1 "https://github.com/AnaHill/AnaHill.github.io/blob/main/index.md?plain=1") 
  - my `readme.md` mainly provides links to web pages, see below shortened example what `readme.md` could contain.

```markdown
🌐 **Visit the live site**: [anahill.github.io](https://anahill.github.io/ "my personal website")  

## 📂 Site Structure
- 🛠️ **[Work Portfolio](https://anahill.github.io/work.html)** 
- 👨‍🔬 **[Academic Portfolio](https://anahill.github.io/academic.html)** 
- 📝 Check out my blog posts **[here](https://anahill.github.io/blog/)**  
```
![alt text](..\pics\posts\How_indexmd_shows_as_page.png "how index.md is converted to page")

### Step2: set-up config 
create `_config.yml` in your main folder.
```yml
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
Using merlot theme, _title_ and _description_ are shown like following in your main page 
![title and description](..\pics\posts\how_title_and_description_is_showed.png "how title and description are shown on  page using merlot theme")

## <span id="ref"> Find out more </span>
- GitHub Pages [documentation](https://pages.github.com/)
- Chijioke Joseph Okorji: [_From Meh to Marvelous: The Ultimate Guide to Crafting a Killer GitHub Profile_](https://medium.com/@chijiokeokorji/from-meh-to-marvelous-the-ultimate-guide-to-crafting-a-killer-github-profile-8dd3f6c6d602) and [repo](https://github.com/ChijiokeOkorji/ChijiokeOkorji)
- Shaw Talebi: [_How to Make a (Free) Data Science Portfolio Website With GitHub Pages_](https://medium.com/the-data-entrepreneurs/how-to-make-a-free-data-science-portfolio-website-with-github-pages-aa1e4965e155)
- Alexandre Sanlim: his [repo](https://github.com/alexandresanlim/) has some nice features worth of checking
- Daria Stanilevici: her [repo](https://github.com/daria-stanilevici/daria-stanilevici)  has some nice features worth of checking
- https://pages.github.com/

