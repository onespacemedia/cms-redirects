# onespacemedia-cms-redirects

Allow admin users to add redirects from one path to another.

## Installation

Add `'redirects'` to your `INSTALLED_APPS`.

Add `'redirects.middleware.RedirectFallbackMiddleware'` to your `MIDDLEWARE_CLASSES`.

Run `./manage.py migrate` (if you're using South).
