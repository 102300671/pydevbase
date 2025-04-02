---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
码途钥匙  
[源代码](https://github.com/102300671/102300671pydevbase.github.io/tree/main/code)

{% for post in site.posts %}
{% assign file_components = post.path | split: '/' | last | split: '.' | first | split: '-' %}
{% assign year = file_components[0] %}
{% assign month = file_components[1] %}
{% assign day = file_components[2] %}
<p>{{ year }}-{{ month }}-{{ day }}</p>
<p><a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></p>
{% endfor %}