# A list of additional installed applications.

INSTALLED_APPS = (
    # Put this at the bottom of your apps list.
    "PROJECT_NAME.apps.redirects",
)

# Dispatch settings.

MIDDLEWARE_CLASSES = (
    # Put this line after all of the Django middlewares and before the others.
    "PROJECT_NAME.apps.redirects.middleware.RedirectFallbackMiddleware",
)
