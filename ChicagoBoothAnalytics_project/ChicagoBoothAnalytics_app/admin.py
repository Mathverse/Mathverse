from autocomplete_light import modelform_factory
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Person, MutualPersonalRelationship, Org, PersonOrgRole, FactType, PersonFact, OrgFact


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
    fieldsets = \
        ('Name', dict(fields=('first_name', 'first_name_alias', 'last_name'))), \
        ('Gender', dict(fields=('gender',)))
    list_view = 'last_name', 'first_name', 'first_name_alias', 'gender'
    search_fields = 'last_name', 'first_name', 'first_name_alias',
    inlines = PersonFactInline, PersonOrgRoleInline

site.register(Person, PersonAdmin)


class MutualPersonalRelationshipAdmin(ModelAdmin):
    form = modelform_factory(MutualPersonalRelationship, fields='__all__')

site.register(MutualPersonalRelationship, MutualPersonalRelationshipAdmin)


class OrgAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',
    inlines = OrgFactInline, PersonOrgRoleInline

site.register(Org, OrgAdmin)


class PersonOrgRoleAdmin(ModelAdmin):
    form = modelform_factory(PersonOrgRole, fields='__all__')
    list_filter = 'org',
    search_fields = 'person', 'org', 'role'

site.register(PersonOrgRole, PersonOrgRoleAdmin)


class FactTypeAdmin(ModelAdmin):
    fieldsets = ('Label', dict(fields=('label',))),
    list_view = 'label',
    search_fields = 'label',

site.register(FactType, FactTypeAdmin)


class PersonFactAdmin(ModelAdmin):
    form = modelform_factory(PersonFact, fields='__all__')
    list_view = 'person', 'fact_type', 'fact'
    search_fields = 'person', 'fact_type', 'fact'

site.register(PersonFact, PersonFactAdmin)


class OrgFactAdmin(ModelAdmin):
    form = modelform_factory(OrgFact, fields='__all__')
    list_view = 'org', 'fact_type', 'fact'
    search_fields = 'org', 'fact_type', 'fact'

site.register(OrgFact, OrgFactAdmin)
