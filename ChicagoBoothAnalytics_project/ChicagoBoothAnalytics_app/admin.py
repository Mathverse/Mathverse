from autocomplete_light import modelform_factory
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Person, Org, PersonOrgRole, FactType, PersonFact, OrgFact


class PersonAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('first_name', 'last_name', 'gender'))),
    list_display = 'last_name', 'first_name', 'gender'
    search_fields = 'first_name', 'last_name'
    #form = modelform_factory(Person)

site.register(Person)


class OrgAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_display = 'name',
    search_fields = 'name',
    #form = modelform_factory(Org)

site.register(Org)


class PersonOrgRoleAdmin(ModelAdmin):
    fieldsets =\
        ('Person', dict(fields=('person',))),\
        ('At Org', dict(fields=('org',))),\
        ('As Role', dict(fields=('role',)))
    list_display = 'person', 'org', 'role'
    list_filter = 'org',
    search_fields = 'person', 'org', 'role'

site.register(PersonOrgRole)


class FactTypeAdmin(ModelAdmin):
    fieldsets = ('Label', dict(fields=('label',))),
    list_display = 'label',
    search_fields = 'label',
    #form = modelform_factory(FactType)

site.register(FactType)


class PersonFactAdmin(ModelAdmin):
    fieldsets = \
        ('Person', dict(fields=('person',))), \
        ('Fact', dict(fields=('fact_type', 'fact')))
    list_display = 'person', 'fact_type', 'fact'
    list_filter = 'fact_type',
    search_fields = 'person', 'fact_type', 'fact'

site.register(PersonFact)


class OrgFactAdmin(ModelAdmin):
    fieldsets = \
        ('Org', dict(fields=('org',))), \
        ('Fact', dict(fields=('fact_type', 'fact')))
    list_display = 'org', 'fact_type', 'fact'
    list_filter = 'fact_type',
    search_fields = 'org', 'fact_type', 'fact'

site.register(OrgFact)
