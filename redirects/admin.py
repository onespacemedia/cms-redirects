from django.contrib import admin
from django.utils.html import escape
from .models import Redirect


@admin.register(Redirect)
class RedirectAdmin(admin.ModelAdmin):
    list_display = ('old_path', 'new_path', 'test_redirect')
    search_fields = ('old_path', 'new_path')

    def test_redirect(self, obj):
        return '<a target="_blank" href="{}">Test</a>'.format(
            escape(obj.old_path)
        )

    test_redirect.allow_tags = True
