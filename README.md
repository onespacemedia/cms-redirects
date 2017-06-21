# onespacemedia-cms-redirects

Allow admin users to add redirects from one path to another.

## Installation

Add `'redirects'` to your `INSTALLED_APPS`.

Set `REDIRECTS_ENABLE_REGEX` to `True` if you wish to enable regular expressions. (This could be slow with a large enough number of redirects.)

Add `'redirects.middleware.RedirectFallbackMiddleware'` to your `MIDDLEWARE_CLASSES`.

Run `./manage.py migrate`.
