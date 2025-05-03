from django.db import models
from person.models import person
class president(person):
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False,null=True, blank=True)

