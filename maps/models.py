from django.contrib.gis.db import models as geomodels
from django.db.models import JSONField
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from loksabha.models import LoksabhaConstituency

class multiple_areas(geomodels.Model):
    """
    Used for representing states, districts and taluks
    """
    feature_properties = JSONField(blank=True, null=True)
    boundary = geomodels.MultiPolygonField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) 
    object_id = models.PositiveIntegerField()
    entity = GenericForeignKey('content_type', 'object_id')
    ## To avoid multiple maps per entity
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['content_type', 'object_id'],
                name='unique_map_per_entity'
            )
        ]

class LoksabhaConstituencyMap(geomodels.Model):
    """
    Used for representing loksabha constituencies
    """    
    boundary = geomodels.MultiPolygonField()
    LoksabhaConstituency = models.ForeignKey(LoksabhaConstituency, on_delete=models.SET_NULL, null=True)
    ## To avoid multiple maps per LoksabhaConstituency
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['LoksabhaConstituency'],
                name='unique_boundary_per_constituency'
            )
        ]