from django.db.models import Model, NullBooleanField, CharField


class Person(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    gender = NullBooleanField(choices=((False, 'female'), (True, 'male')))

    class Meta:
        ordering = 'last_name', 'first_name'

    def __unicode__(self):
        return self.first_name + self.last_name.upper()
