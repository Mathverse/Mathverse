from django.db.models import Model, CharField, ForeignKey, NullBooleanField


class Person(Model):
    first_name = CharField(max_length=255)
    first_name_alias = CharField(max_length=255, blank=True, null=True)
    last_name = CharField(max_length=255)
    gender = NullBooleanField(choices=((False, 'female'), (True, 'male')))

    class Meta:
        ordering = 'last_name', 'first_name', 'first_name_alias'

    def __unicode__(self):
        if self.first_name_alias:
            first_name = self.first_name_alias
        else:
            first_name = self.first_name
        return first_name + ' ' + self.last_name.upper()


class Org(Model):
    name = CharField(max_length=255)

    class Meta:
        ordering = 'name',

    def __unicode__(self):
        return self.name


class PersonOrgRole(Model):
    person = ForeignKey(Person, related_name='PersonOrgRole')
    org = ForeignKey(Org, related_name='PersonOrgRole')
    role = CharField(max_length=255)

    class Meta:
        ordering = 'person', 'org', 'role'

    def __unicode__(self):
        return str(self.person) + ' as ' + self.role + ' @ ' + str(self.org)


class FactType(Model):
    label = CharField(max_length=255)

    class Meta:
        ordering = 'label',

    def __unicode__(self):
        return self.label


class PersonFact(Model):
    person = ForeignKey(Person, related_name='PersonFact')
    fact_type = ForeignKey(FactType, related_name='PersonFact')
    fact = CharField(max_length=255)

    class Meta:
        ordering = 'person', 'fact_type', 'fact'

    def __unicode__(self):
        return str(self.person) + ': ' + str(self.fact_type) + ': ' + self.fact


class OrgFact(Model):
    org = ForeignKey(Org, related_name='OrgFact')
    fact_type = ForeignKey(FactType, related_name='OrgFact')
    fact = CharField(max_length=255)

    class Meta:
        ordering = 'org', 'fact_type', 'fact'

    def __unicode__(self):
        return str(self.org) + ': ' + str(self.fact_type) + ': ' + self.fact
