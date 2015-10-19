from django.db.models import Model, BooleanField, CharField, DateField, ForeignKey, ManyToManyField, NullBooleanField,\
    PositiveSmallIntegerField, TextField, URLField
from django.utils.timezone import now


class BusinessSector(Model):
    name = CharField(max_length=255)

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class RoleLevel(Model):
    level = CharField(max_length=255)
    level_number_from_high_to_low = PositiveSmallIntegerField()

    class Meta:
        ordering = 'level_number_from_high_to_low',

    def __unicode__(self):
        return self.level


class Role(Model):
    title = CharField(max_length=255)
    level = ForeignKey(RoleLevel, related_name='role_level', blank=True, null=True)

    class Meta:
        ordering = 'level', 'title'

    def __unicode__(self):
        role = self.title
        if self.level:
            role += ' [%s level]' % str(self.level)
        return role


class GeogRegion(Model):
    name = CharField(max_length=255)

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class Org(Model):
    name = CharField(max_length=255)
    business_sectors = ManyToManyField(BusinessSector, related_name='org_business_sectors', blank=True)
    geog_regions = ManyToManyField(GeogRegion, related_name='org_geog_regions', blank=True)
    roles = ManyToManyField(Role, related_name='org_roles', blank=True)

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class CareerOpportunity(Model):
    org = ForeignKey(Org, related_name='careeropportunity_org')
    role = ForeignKey(Role, related_name='careeropportunity_role')
    geog_regions = ManyToManyField(GeogRegion, related_name='careeropportunity_geog_regions', blank=True)
    url = URLField(max_length=255, blank=True, null=True)
    active = BooleanField(default=True)
    posting_date = DateField(default=now, blank=True, null=True)
    notes = TextField(blank=True, null=True)

    class Meta:
        ordering = 'org', 'role', '-active', '-posting_date'

    def __unicode__(self):
        opp = '%s: %s' % (str(self.org), str(self.role))
        if self.geog_regions.all():
            opp += ' in %s' % ', '.join(str(g) for g in self.geog_regions.all())
        if self.active:
            if self.posting_date:
                return '%s [posted on %s]' % (opp, str(self.posting_date))
            else:
                return opp
        else:
            return '%s [INACTIVE]' % opp


class Person(Model):
    first_name = CharField(max_length=255)
    first_name_alias = CharField(max_length=255, blank=True, null=True)
    last_name = CharField(max_length=255)
    gender = NullBooleanField(choices=((False, 'female'), (True, 'male')))
    current_geog_regions = ManyToManyField(GeogRegion, related_name='person_current_geog_region', blank=True)

    class Meta:
        ordering = 'last_name', 'first_name', 'first_name_alias'

    def __unicode__(self):
        if self.first_name_alias:
            first_name = self.first_name_alias
        else:
            first_name = self.first_name
        return '%s %s' % (first_name, self.last_name.upper())


class MutualPersonalRelationship(Model):
    persons = ManyToManyField(Person, related_name='mutualpersonalrelationship_persons', blank=True)
    description = CharField(max_length=255)

    def __unicode__(self):
        return ', '.join(str(p) for p in self.persons.all()) + ' know one another: ' + self.description


class PersonOrgRole(Model):
    person = ForeignKey(Person, related_name='personorgrole_person')
    org = ForeignKey(Org, related_name='personorgrole_org')
    roles = ManyToManyField(Role, related_name='personorgrole_roles')
    geog_regions = ManyToManyField(GeogRegion, related_name='personorgrole_geog_regions')
    from_when = DateField(DateField, blank=True, null=True)
    to_when = DateField(DateField, blank=True, null=True)

    class Meta:
        ordering = 'person', 'org', 'to_when'

    def __unicode__(self):
        roles = str(self.person) + ' @ ' + str(self.org)
        if self.roles.all():
            roles += ' as ' + ', '.join(str(r) for r in self.roles.all())
        if self.from_when:
            roles += ' from ' + str(self.from_when)
        if self.to_when:
            roles += ' to ' + str(self.to_when)
        return roles


class FactType(Model):
    label = CharField(max_length=255)

    class Meta:
        ordering = 'label',

    def __unicode__(self):
        return self.label


class PersonFact(Model):
    person = ForeignKey(Person, related_name='personfact_person')
    fact_type = ForeignKey(FactType, related_name='personfact_type')
    fact = CharField(max_length=255)

    class Meta:
        ordering = 'person', 'fact_type', 'fact'

    def __unicode__(self):
        return str(self.person) + ': ' + str(self.fact_type) + ': ' + self.fact


class OrgFact(Model):
    org = ForeignKey(Org, related_name='orgfact_org')
    fact_type = ForeignKey(FactType, related_name='orgfact_type')
    fact = CharField(max_length=255)

    class Meta:
        ordering = 'org', 'fact_type', 'fact'

    def __unicode__(self):
        return str(self.org) + ': ' + str(self.fact_type) + ': ' + self.fact







