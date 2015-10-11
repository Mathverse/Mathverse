from autocomplete_light import register
from models import Role, GeogRegion, Person, Org, FactType

register(Role, search_fields=('title',))
register(GeogRegion, search_fields=('name',))
register(Org, search_fields=('name',))
register(Person, search_fields=('first_name', 'first_name_alias', 'last_name'))
register(FactType, search_fields=('label',))
