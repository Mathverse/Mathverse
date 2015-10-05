from autocomplete_light import modelform_factory
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Person, Org, PersonOrgRole, FactType, PersonFact, OrgFact


class PersonOrgRoleInline(TabularInline):
    model = PersonOrgRole
    can_delete = True
    extra = 3


class PersonFactInline(TabularInline):
    model = PersonFact
    can_delete = True
    extra = 3


class OrgFactInline(TabularInline):
    model = OrgFact
    can_delete = True
    extra = 3


class PersonAdmin(ModelAdmin):
    form = modelform_factory(Person, fields='__all__')
    inlines = PersonFactInline, PersonOrgRoleInline

site.register(Person, PersonAdmin)


class OrgAdmin(ModelAdmin):
    form = modelform_factory(Org, fields='__all__')
    inlines = OrgFactInline, PersonOrgRoleInline

site.register(Org, OrgAdmin)


class PersonOrgRoleAdmin(ModelAdmin):
    fieldsets =\
        ('Person', dict(fields=('person',))),\
        ('At Org', dict(fields=('org',))),\
        ('As Role', dict(fields=('role',))),\
        ('When', dict(fields=('from_when', 'to_when')))
    list_display = 'person', 'org', 'role'
    list_filter = 'org',
    search_fields = 'person', 'org', 'role'

site.register(PersonOrgRole, PersonOrgRoleAdmin)


class FactTypeAdmin(ModelAdmin):
    form = modelform_factory(FactType, fields='__all__')

site.register(FactType, FactTypeAdmin)


class PersonFactAdmin(ModelAdmin):
    fieldsets = \
        ('Person', dict(fields=('person',))), \
        ('Fact', dict(fields=('fact_type', 'fact')))
    list_display = 'person', 'fact_type', 'fact'
    list_filter = 'fact_type',
    search_fields = 'person', 'fact_type', 'fact'

site.register(PersonFact, PersonFactAdmin)


class OrgFactAdmin(ModelAdmin):
    fieldsets = \
        ('Org', dict(fields=('org',))), \
        ('Fact', dict(fields=('fact_type', 'fact')))
    list_display = 'org', 'fact_type', 'fact'
    list_filter = 'fact_type',
    search_fields = 'org', 'fact_type', 'fact'

site.register(OrgFact, OrgFactAdmin)
