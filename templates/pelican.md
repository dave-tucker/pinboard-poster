Title: {{ title}}
Date: {{ date }}
Author: {{ author }}
Category: {{ category }}
Tags: {{ tags }}
Slug: {{} slug }}

{ summary }

<!--more -->

{% for p in posts %}

# {{ p.title }}

{{ p.descripton }}

*{{ p.tags }}*
