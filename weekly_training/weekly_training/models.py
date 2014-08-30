# coding: utf-8
__author__ = 'buyvich'

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Training(models.Model):

    name = models.CharField(max_length=50)
    goal = models.IntegerField()
    tng_type = models.CharField(max_length=15,
                                choices=((u'hours', u'Часы'),
                                         (u'bool', u'да/нет'),
                                         (u'number', u'Число')))
    user = models.ForeignKey(User)

    class Meta:
        db_table = u't_training'
        verbose_name = u'Тренировка'
        verbose_name_plural = u'Тренировки'

    def __unicode__(self):
        return self.name


class TrainingForm(ModelForm):

    class Meta:
        model = Training
