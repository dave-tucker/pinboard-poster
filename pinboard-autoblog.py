#!/usr/bin/env python

import datetime
import os

from jinja2 import Environment, PackageLoader
import pinboard

import config

p = pinboard.connect(token=config.PINBOARD_API_TOKEN)
from_date = datetime.datetime(2014, 1, 1)
to_date = datetime.datetime.utcnow()

posts = p.posts(fromdt=from_date, todt=to_date)

env = Environment(loader=PackageLoader('pinboard-autoblogger',
                                       'templates'))

template = env.get_template('pelican.md')
output = template.render(posts=posts)

filename = config.POST_FILENAME_PREFIX + from_date.isoformat()[:10]
abspath = os.abspath(config.POST_PATH + filename)
with open(filename, "wb") as fh:
    fh.write(output)
