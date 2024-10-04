from django.db import models
from django.utils.translation import gettext_lazy as _


class FacebookPages(models.Model):
    social_platform_id = models.CharField(_('social platform ID'), max_length=255, unique=True)
    name = models.CharField(max_length=255)
    page_token = models.CharField(_('page token'), max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}-{self.social_platform_id}'

    class Meta:
        verbose_name = _('станица Facebook')
        verbose_name_plural = _('станицы Facebook')


class InstagramPages(models.Model):
    social_platform_id = models.CharField(_('social platform ID'), max_length=255, unique=True)
    page_token = models.CharField(_('page token'), max_length=255, unique=True)
    facebook_page_id = models.ForeignKey(_('facebook page'), FacebookPages, on_delete=models.CASCADE)

    def __str__(self):
        return self.facebook_page_id

    class Meta:
        verbose_name = _('Станица Instagram')
        verbose_name_plural = _('Станицы Instagram')
