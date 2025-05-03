import json
import os
import django
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'm.settings')
django.setup()

from django.contrib.contenttypes.models import ContentType
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def load_state_map(path):
    """
    To load both state and their map details. If state is unavailable, it will create and add map to it
    """
    from area_pop.models import State
    from maps.models import multiple_areas 
    state_data = read_json(path)
    features = state_data['features']
    import pdb;pdb.set_trace()
    multiple_areas.objects.all().delete()
    State.objects.all().delete()
    for feature in features :
        state_name = feature['properties']['NAME_1']
        if state_name == "Telangana" :
            status = "State"
        else :
            continue 
        '''status = feature['properties']['ENGTYPE_1']
        if status == "Union Territory":
            status = "UT" 
        print(state_name+"---"+status) '''
        state_obj = State.objects.get_or_create(
            State_name=state_name,
            Status=status
        )
        # Get ContentType for the State model

        feature_properties = feature["properties"]
        geometry = GEOSGeometry(str(feature["geometry"]))  # accepts GeoJSON string
        # ensure geometry is MultiPolygon
        if geometry.geom_type == "Polygon":
            geometry = MultiPolygon(geometry)
        content_type = ContentType.objects.get_for_model(state_obj[0])

        # Get object_id
        object_id = state_obj[0].id
        multiple_areas_obj = multiple_areas.objects.get_or_create(
            feature_properties = feature_properties,
            boundary = geometry,
            content_type = content_type,
            object_id = object_id
        )


if __name__ == "__main__":
    #load_state_map("../../maps_jsons/state/india_state.geojson")
    load_state_map("../../maps_jsons/state/india_telengana.geojson")
    #load_district_map()
    

    