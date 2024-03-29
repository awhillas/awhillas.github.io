AUTHOR = "Alexander Whillas"
SITENAME = "Alexander Whillas"
# SITEURL = 'http://alexander.whillas.com'

# THEME = "/home/alex/dev/opp/pelican-themes/flex"
THEME = "themes/Pelican-Cid"  # best!

LANDING_PAGE_ABOUT = "Something about me"

PATH = "content"

TIMEZONE = "Pacific/Auckland"

DEFAULT_LANG = "en"

OUTPUT_PATH = "docs/"
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ["CNAME"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight", "linenums": True},
        "markdown.extensions.meta": {},
        "smarty": {"smart_angled_quotes": "true"},
        "pymdownx.tilde": {
            "smart_delete": "true",
            "delete": "true",
            "subscript": "true",
        },
        "pymdownx.tasklist": {},
        # "markdown.extensions.toc": {
        #     "permalink": "true",
        # },
    }
}

CONTACTS = (
    ("twitter", "https://twitter.com/awhillas"),
    ("github", "https://github.com/awhillas"),
    ("linkedin", "https://www.linkedin.com/in/whillas/"),
)

DEFAULT_PAGINATION = False
ARTICLE_ORDER_BY = "reversed-date"
PAGE_ORDER_BY = "reversed-date"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
