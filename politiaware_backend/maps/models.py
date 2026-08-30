from django.contrib.gis.db import models as geomodels
from django.db.models import JSONField
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from area_pop.models import State, Districts, Taluk
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

class StateMap(geomodels.Model):
    """
    Used for representing State boundary maps
    """
    feature_properties = JSONField(blank=True, null=True)
    boundary = geomodels.MultiPolygonField()
    State = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['State'],
                name='unique_boundary_per_state'
            )
        ]

class DistrictMap(geomodels.Model):
    """
    Used for representing District boundary maps
    """
    feature_properties = JSONField(blank=True, null=True)
    boundary = geomodels.MultiPolygonField()
    District = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['District'],
                name='unique_boundary_per_district'
            )
        ]

class TalukMap(geomodels.Model):
    """
    Used for representing Taluk boundary maps
    """
    feature_properties = JSONField(blank=True, null=True)
    boundary = geomodels.MultiPolygonField()
    Taluk = models.ForeignKey(Taluk, on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Taluk'],
                name='unique_boundary_per_taluk'
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