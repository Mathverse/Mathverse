from autocomplete_light import register
from models import Person, Org, FactType


register(Person, search_fields=('first_name', 'first_name_alias', 'last_name'))
register(Org, search_fields=('name',))
register(FactType, search_fields=('label',))
