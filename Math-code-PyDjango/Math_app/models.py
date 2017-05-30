# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db.models import Model, \
    BooleanField, CharField, DateField, ForeignKey, ManyToManyField, NullBooleanField, PositiveSmallIntegerField, \
    TextField, URLField, \
    CASCADE, PROTECT, SET, SET_DEFAULT, SET_NULL


class Ref(Model):
    name = CharField(
        max_length=255,   # CharFields must define a 'max_length' attribute
        blank=False,
        null=False
    )

    url = URLField(
        max_length=255,   # CharFields must define a 'max_length' attribute
        blank=True,
        null=True
    )

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class Topic(Model):
    name = CharField(
        max_length=255,   # CharFields must define a 'max_length' attribute
        blank=False,
        null=False
    )

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class Problem(Model):
    name = CharField(
        max_length=255,   # CharFields must define a 'max_length' attribute
        blank=False,
        null=False
    )

    text = TextField(
        blank=True,
        null=True
    )

    topics = ManyToManyField(
        to=Topic,
        related_name='problem_topics',
        blank=True
        # null=True   # null has no effect on ManyToManyField
    )

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class Solution(Model):
    problem = ForeignKey(
        to=Problem,
        on_delete=CASCADE,
        related_name='problem_solutions',
        blank=False,
        null=False
    )

    name = CharField(
        max_length=255,   # CharFields must define a 'max_length' attribute
        blank=True,
        null=True
    )

    text = TextField(
        blank=True,
        null=True
    )

    topics = ManyToManyField(
        to=Topic,
        related_name='solution_topics',
        blank=True
        # null=True   # null has no effect on ManyToManyField
    )

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name
