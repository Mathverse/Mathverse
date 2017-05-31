# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from dal import autocomplete
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Ref, Topic, Problem, Solution


class RefInline(TabularInline):
     model = Ref
     can_delete = True
     extra = 0


class RefAdmin(ModelAdmin):
    fieldsets = \
        ('URL', dict(fields=('url',))),

    list_view = 'url',
    search_fields = 'url',

site.register(Ref, RefAdmin)


class TopicAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',
    inlines = RefInline,

site.register(Topic, TopicAdmin)


class ProblemAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',
    inlines = RefInline,

site.register(Problem, ProblemAdmin)


class SolutionAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',
    inlines = RefInline,

site.register(Solution, SolutionAdmin)
