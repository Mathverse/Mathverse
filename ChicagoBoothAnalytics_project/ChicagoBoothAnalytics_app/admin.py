from django.contrib.admin import ModelAdmin, site, TabularInline

from models import Person


class PersonAdmin(ModelAdmin):
    fieldsets = ('Name', dict(fields=('first_name', 'last_name', 'gender'))),
    list_display = 'last_name', 'first_name', 'gender'
    search_fields = 'first_name', 'last_name'

site.register(Person, PersonAdmin)
