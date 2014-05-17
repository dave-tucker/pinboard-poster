#!/usr/bin/env python

import datetime
import os

from jinja2 import Environment, FileSystemLoader
import pinboard

import config


def is_autoblog_tag(s):
    return s == config.PINBOARD_TAG

p = pinboard.connect(token=config.PINBOARD_API_TOKEN)
to_date = datetime.datetime.utcnow()
days = datetime.timedelta(days=config.DAYS)
from_date = to_date - days
posts = p.posts(tag=config.PINBOARD_TAG, fromdt=from_date, todt=to_date)

env = Environment(loader=FileSystemLoader('templates'))
env.tests['autoblog_tag'] = is_autoblog_tag

template = env.get_template('pelican.md')

title = config.POST_TITLE_PREFIX + " " + to_date.strftime("%d %b %Y")
slug = title.lower().replace(" ", "-")

output = template.render(title=title,
                         date=to_date.strftime("%Y-%m-%d"),
                         author=config.POST_AUTHOR,
                         category=config.POST_CATEGORY,
                         tags=config.POST_TAGS,
                         slug=slug,
                         summary=config.POST_SUMMARY,
                         posts=posts)

filename = slug + ".md"
abspath = os.path.abspath(config.POST_PATH + filename)
with open(abspath, "wb") as fh:
    fh.write(output)
