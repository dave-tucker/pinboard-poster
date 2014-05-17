Title: {{ title}}
Date: {{ date }}
Author: {{ author }}
Category: {{ category }}
Tags: {{ tags }}
Slug: {{ slug }}

{{ summary }}

<!--more-->
{% for p in posts %}
## [{{ p.description }}]({{ p.href }})

> {{ p.extended }}

*{{ p.tags|reject("autoblog_tag")|join(", ")}}*

{% endfor %}
