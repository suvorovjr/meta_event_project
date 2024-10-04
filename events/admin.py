from django.contrib import admin
from .models import FacebookPages, InstagramPages


@admin.register(FacebookPages)
class FacebookPagesAdmin(admin.ModelAdmin):
    pass


@admin.register(InstagramPages)
class InstagramPagesAdmin(admin.ModelAdmin):
    pass
