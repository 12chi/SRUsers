from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return " id: " + str(self.id) + " name: " + self.name + " city: " + self.city  + " state: " + self.state + " desc: " + self.desc


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")

    def __unicode__(self):
        return " id: " + str(self.id) + " name: " + self.first_name + " " + self.last_name

# Create your models here.
