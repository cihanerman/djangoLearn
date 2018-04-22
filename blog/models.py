# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.translation import uggetext_lazy as _


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name=_('author'),
    ))
    title = models.CharField(_('title'), max_length=200)
    text = models.TextField(_('text'),)
    created_date = models.DateTimeField(_('Created Date'),
            default=timezone.now)
    published_date = models.DateTimeField(_('Published Date'),
            blank=True, auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
