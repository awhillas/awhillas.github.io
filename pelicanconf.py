AUTHOR = 'Alexander Whillas'
SITENAME = 'Alexander Whillas'
# SITEURL = 'http://alexander.whillas.com'

THEME = "/home/alex/dev/opp/pelican-themes/cid" # best!

LANDING_PAGE_ABOUT = "Something about me"

PATH = 'content'

TIMEZONE = 'Pacific/Auckland'

DEFAULT_LANG = 'en'

OUTPUT_PATH = 'docs/'
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ["CNAME"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'markdown.extensions.meta': {},
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
    }
}

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Sebastian Sequoiah-Grayson, Logic and Philosophy are his game', 'http://logicalrockpools.com/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True