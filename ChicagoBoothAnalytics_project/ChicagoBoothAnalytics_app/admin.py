from autocomplete_light import modelform_factory
from django.contrib.admin import ModelAdmin, site, TabularInline

from models import BusinessSector, RoleLevel, Role, GeogRegion, Org, CareerOpportunity, CareerOpportunityURL,\
    UserInterestedInOrgs, UserCareerOpportunityStatus, Person, PersonOrgRole, FactType, PersonFact, OrgFact


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


class BusinessSectorAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',

site.register(BusinessSector, BusinessSectorAdmin)


class GeogRegionAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('name',))),
    list_view = 'name',
    search_fields = 'name',

site.register(GeogRegion, GeogRegionAdmin)


class RoleLevelAdmin(ModelAdmin):
    fieldsets = ('Level', dict(fields=('level', 'level_number_from_high_to_low'))),
    list_view = 'level',
    search_fields = 'level',

site.register(RoleLevel, RoleLevelAdmin)


class RoleAdmin(ModelAdmin):
    fieldsets =\
        ('Title', dict(fields=('title',))),\
        ('Level', dict(fields=('level',)))
    list_view = 'title', 'level'
    search_fields = 'title',

site.register(Role, RoleAdmin)


class OrgAdmin(ModelAdmin):
    form = modelform_factory(Org, fields='__all__')
    list_view = 'name',
    search_fields = 'name',
    inlines = OrgFactInline, PersonOrgRoleInline

site.register(Org, OrgAdmin)


class CareerOpportunityAdmin(ModelAdmin):
    form = modelform_factory(CareerOpportunity, fields='__all__')
    list_view = 'org', 'role', 'url', 'open', 'posting_date', 'notes'
    list_filer = 'org', 'role', 'active'
    search_fields = 'org', 'role', 'url', 'notes'

site.register(CareerOpportunity, CareerOpportunityAdmin)


class CareerOpportunityURLAdmin(ModelAdmin):
    form = modelform_factory(CareerOpportunityURL, fields='__all__')
    list_view = 'url',
    search_fields = 'url',

site.register(CareerOpportunityURL, CareerOpportunityURLAdmin)


class UserCareerOpportunityStatusAdmin(ModelAdmin):
    form = modelform_factory(UserCareerOpportunityStatus, fields='__all__')

site.register(UserCareerOpportunityStatus, UserCareerOpportunityStatusAdmin)


class UserInterestedInOrgsAdmin(ModelAdmin):
    form = modelform_factory(UserInterestedInOrgs, fields='__all__')
    list_view = 'user',
    search_fields = 'user',

site.register(UserInterestedInOrgs, UserInterestedInOrgsAdmin)


class PersonAdmin(ModelAdmin):
    fieldsets = \
        ('Name', dict(fields=('first_name', 'first_name_alias', 'last_name'))), \
        ('Gender', dict(fields=('gender',)))
    list_view = 'last_name', 'first_name', 'first_name_alias', 'gender'
    search_fields = 'last_name', 'first_name', 'first_name_alias',
    inlines = PersonFactInline, PersonOrgRoleInline

site.register(Person, PersonAdmin)


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
