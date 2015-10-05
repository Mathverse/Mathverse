from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Person, Org, PersonOrgRole


class PersonAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('first_name', 'last_name', 'gender'))),
    list_display = 'last_name', 'first_name', 'gender'
    search_fields = 'first_name', 'last_name'

site.register(Person, PersonAdmin)


class OrgAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_display = 'name',
    search_fields = 'name',

site.register(Org, OrgAdmin)


class PersonOrgRoleAdmin(ModelAdmin):
    fieldsets =\
        ('Person', dict(fields=('person',))),\
        ('At Org', dict(fields=('org',))),\
        ('As Role', dict(fields=('role',)))
    list_display = 'person', 'org', 'role'
    list_filter = 'org',
    search_fields = 'person', 'org', 'role'

site.register(PersonOrgRole, PersonOrgRoleAdmin)