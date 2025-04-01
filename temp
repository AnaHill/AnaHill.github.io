# 1) _includes/blog-meta.html
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



# 2 layouts/post.html
{% comment %}
Custom layout that wraps the Merlot theme's layout,
but adds blog-only metadata like tags and dates.
{% endcomment %}
{% include head.html %}

<main>
  {% include blog-meta.html %}
  {{ content }}
</main>
