from django.contrib import admin
from .models import (
    Banner,
    Channel,
    Category,
    Video,
    Show
)

admin.site.register(Banner)
admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Show)