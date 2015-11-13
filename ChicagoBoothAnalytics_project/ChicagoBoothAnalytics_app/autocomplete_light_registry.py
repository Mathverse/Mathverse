from autocomplete_light import register
from django.contrib.auth.models import User
from models import BusinessSector, Role, GeogRegion, Person, Org, FactType


register(User, search_fields=('username', 'first_name', 'last_name', 'email'))
register(BusinessSector, search_fields=('name',))
register(Role, search_fields=('title',))
register(GeogRegion, search_fields=('name',))
register(Org, search_fields=('name',))
register(Person, search_fields=('first_name', 'first_name_alias', 'last_name'))
register(FactType, search_fields=('label',))
