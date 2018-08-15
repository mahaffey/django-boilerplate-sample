from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    name = models.CharField(_('name'), max_length=255, blank=False)
    content = models.TextField(_('content'), blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               blank=False)
    created_date = models.DateTimeField(default=timezone.now, blank=False)

    class Meta():
        app_label = "blog"
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return "{}: {}...".format(self.name, self.content[:20])
