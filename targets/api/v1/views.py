from django.shortcuts import render
from ...models import Target
from django.core.serializers import serialize
from rest_framework.viewsets import ModelViewSet
from .serializers import TargetSerializer
import json

# View to render map
def map_view(request):
    # Fetches all targets from the database
    targets = Target.objects.all()
    # Serializes targets to JSON
    targets_json = json.loads(serialize('json', targets))
    # Formats data for simplification on the frontend
    formatted_targets = [
        {
            'id': target['pk'],
            'name': target['fields']['name'],
            'latitude': target['fields']['latitude'],
            'longitude': target['fields']['longitude'],
            'expiration_date': target['fields']['expiration_date'],
        }
        for target in targets_json
    ]
    # Render the template passing the formatted targets
    return render(request, 'targets/index.html', {'targets': json.dumps(formatted_targets)})

# API for target CRUD
class TargetViewSet(ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
