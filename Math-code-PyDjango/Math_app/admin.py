# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from dal import autocomplete
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Ref, Topic, Problem, Solution


# class PersonOrgRoleInline(TabularInline):
#     model = PersonOrgRole
#     can_delete = True
#     extra = 0


# class PersonFactInline(TabularInline):
#     model = PersonFact
#     can_delete = True
#     extra = 0


# class OrgFactInline(TabularInline):
#    model = OrgFact
#    can_delete = True
#    extra = 0


#class OrgCareerOpportunityInLine(TabularInline):
#    model = CareerOpportunity
#    can_delete = True
#    extra = 0


class RefAdmin(ModelAdmin):
    fieldsets = \
        ('Name', dict(fields=('name',))),

    list_view = 'name',
    search_fields = 'name',

site.register(Ref, RefAdmin)


class TopicAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',

site.register(Topic, TopicAdmin)


class ProblemAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',

site.register(Problem, ProblemAdmin)


class SolutionAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',

site.register(Solution, SolutionAdmin)


#class OrgAdmin(ModelAdmin):
#    form = modelform_factory(Org, fields='__all__')
#    list_view = 'name',
#    search_fields = 'name',
#    inlines = OrgFactInline, OrgCareerOpportunityInLine, PersonOrgRoleInline

#site.register(Org, OrgAdmin)


#class CareerOpportunityAdmin(ModelAdmin):
#    form = modelform_factory(CareerOpportunity, fields='__all__')
#    list_view = 'org', 'role', 'url', 'open', 'posting_date', 'notes'
#    list_filer = 'org', 'role', 'active'
#    search_fields = 'org', 'role', 'url', 'notes'

#site.register(CareerOpportunity, CareerOpportunityAdmin)


#class CareerOpportunityURLAdmin(ModelAdmin):
#    form = modelform_factory(CareerOpportunityURL, fields='__all__')
#    list_view = 'url',
#    search_fields = 'url',

#site.register(CareerOpportunityURL, CareerOpportunityURLAdmin)


#class UserCareerOpportunityStatusAdmin(ModelAdmin):
#    form = modelform_factory(UserCareerOpportunityStatus, fields='__all__')

#site.register(UserCareerOpportunityStatus, UserCareerOpportunityStatusAdmin)


#class UserInterestedInOrgsAdmin(ModelAdmin):
#    form = modelform_factory(UserInterestedInOrgs, fields='__all__')
#    list_view = 'user',
#    search_fields = 'user',

#site.register(UserInterestedInOrgs, UserInterestedInOrgsAdmin)


#class PersonAdmin(ModelAdmin):
#    fieldsets = \
#        ('Name', dict(fields=('first_name', 'first_name_alias', 'last_name'))), \
#        ('Gender', dict(fields=('gender',)))
#    list_view = 'last_name', 'first_name', 'first_name_alias', 'gender'
#    search_fields = 'last_name', 'first_name', 'first_name_alias',
#    inlines = PersonFactInline, PersonOrgRoleInline

#site.register(Person, PersonAdmin)


#class PersonOrgRoleAdmin(ModelAdmin):
#    form = modelform_factory(PersonOrgRole, fields='__all__')
#    list_filter = 'org',
#    search_fields = 'person', 'org', 'role'

#site.register(PersonOrgRole, PersonOrgRoleAdmin)


#class FactTypeAdmin(ModelAdmin):
#    fieldsets = ('Label', dict(fields=('label',))),
#    list_view = 'label',
#    search_fields = 'label',

#site.register(FactType, FactTypeAdmin)


#class PersonFactAdmin(ModelAdmin):
#    form = modelform_factory(PersonFact, fields='__all__')
#    list_view = 'person', 'fact_type', 'fact'
#    search_fields = 'person', 'fact_type', 'fact'

#site.register(PersonFact, PersonFactAdmin)


#class OrgFactAdmin(ModelAdmin):
#    form = modelform_factory(OrgFact, fields='__all__')
#    list_view = 'org', 'fact_type', 'fact'
#    search_fields = 'org', 'fact_type', 'fact'

#site.register(OrgFact, OrgFactAdmin)
