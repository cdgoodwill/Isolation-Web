from django.http import JsonResponse
from django.db.models import Count
import uuid

from webmanager.models import Place, User, UserConnection

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
def placesToNodes(place):
    return {
        'id': place.id,
        'label': place.house_name,
        'size': place.user_count,
        'color': '#009',
        'x': place.lng,
        'y': place.lat * -1,
    }


def userConnectionsToEdges(userConnection):
  return {
    'id': uuid.uuid4(),
    'source': userConnection.user.place.id,
    'target': userConnection.connected_place,
  }


def render_data(request):
    places = Place.objects.annotate(user_count=Count('user')).filter()
    userConnections = UserConnection.objects.filter()
    data = {
        'nodes': list(map(placesToNodes, places)),
        'edges': list(map(userConnectionsToEdges, userConnections))
    }

    return JsonResponse(data)
