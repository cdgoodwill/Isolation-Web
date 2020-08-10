from django.http import JsonResponse
from django.db.models import Count
import uuid

from webmanager.models import Place, Person, ConnectedPlace

# {
#   "nodes": [
#     {
#       "id": "f531b79b-02aa-48a6-8b08-e8b4fb8ee24d",
#       "label": "Bohemia",
#       "x": -73.9828,
#       "y": -40.6669,
#       "size": 1,
#       "color": "#009"
#     },
#   ],
#   "edges": [
#     {
#       "id": "bc2bec12-31de-4a22-90f3-e21185aa3a26",
#       "source": "f531b79b-02aa-48a6-8b08-e8b4fb8ee24d",
#       "target": "60e5be64-021b-4197-b35d-9e555bfa02c5"
#     },
#   ]
# }
def _places_to_nodes(place):
    return {
        'id': place.id,
        'label': place.house_name,
        'size': place.user_count,
        'color': '#009',
        'x': place.lng,
        'y': place.lat * -1,
    }


def _user_connections_to_edges(connected_places):
  return {
    'id': uuid.uuid4(),
    'source': connected_places.place.id,
    'target': connected_places.connected_place,
  }


def render_data(request):
    places = Place.objects.filter()
    connected_places = ConnectedPlace.objects.filter()
    data = {
        'nodes': list(map(_places_to_nodes, places)),
        'edges': list(map(_user_connections_to_edges, connected_places))
    }

    return JsonResponse(data)
