from rest_framework_gis.serializers import GeoFeatureModelSerializer
from models import multiple_areas
class MultipleAreasSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = multiple_areas
        geo_field = "boundary"
        fields = ('id', 'feature_properties', 'content_type', 'object_id')
