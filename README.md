pinboard-poster
===============

You bookmark in pinboard and think "Hey, it would be a really cool idea if I could put my pinboard bookmarks in to a blog post". You use a static site generator for your blog, so fancy Wordpress or Blogger plugins won't help you. If this is you, then this is the project that will make your pinboard blog posting dreams come true.

# Installation

Clone this repository. Then

    pip -r requirements.txt

# How it works

Simples. First `./init` to generate your config file.
Then you adjust the settings in `config.py` to your liking and run `python pinboard-poster` and away you go.

Run once a week. I'd recommend automating this with a cron job, through launchctl or however else you might want to launch it.

Edit and review your Markdown file and checking it once weekly before you go.
Push to your blog however you normally push new posts.

# Configuration Guide

Your Pinboard API token can be found on the "Passwords" page in Pinboard

    PINBOARD_API_TOKEN = "foo"

Add the tag of items that you want pinboard-poster to post

    PINBOARD_TAG = "blog"

How many days of links do you want to publish?

    DAYS = 7

Adjust the filename of your post by modifying the prefix

    POST_FILENAME_PREFIX = "bookmarks-"

The date of the post will be appended to that prefix to make the full filename

To change the path where you would like to add post to be generated...

    POST_PATH = "../blog/content/notable/"

> Note: Don't use `~`. Use an absolute or relative path

This will be the title of your post...

    POST_TITLE_PREFIX = "My pinboard bookmarks for"

`POST_TITLE_PREFIX` + The Date. As in "17 May"

You can also change the post author:

    POST_AUTHOR = "Dave"

or post category:

    POST_CATEGORY = "Notable"

or tags:

    POST_TAGS = "pinboard, bookmarks, notable"

or the summary:

    POST_SUMMARY = "Things of note that were discovered on the web this week."

# Contributing

1) Fork
2) Hack
3) Pull Request

# License

Author: Dave Tucker

> Copyright 2014 Dave Tucker
>
> Licensed under the Apache License, Version 2.0 (the "License");
> you may not use this file except in compliance with the License.
> You may obtain a copy of the License at
>
>    http://www.apache.org/licenses/LICENSE-2.0
>
> Unless required by applicable law or agreed to in writing, software
> distributed under the License is distributed on an "AS IS" BASIS,
> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
> See the License for the specific language governing permissions and
> limitations under the License.
