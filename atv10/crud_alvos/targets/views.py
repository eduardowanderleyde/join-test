from django.shortcuts import render
from .models import Target
from django.core.serializers import serialize
import json

def map_view(request):
    # Busca todos os alvos do banco de dados
    targets = Target.objects.all()
    # Serializa os alvos para JSON
    targets_json = json.loads(serialize('json', targets))
    # Formats data for simplicity on the frontend
    formatted_targets = [
        {
            'id': target['pk'],
            'identifier': target['fields']['identifier'],
            'name': target['fields']['name'],
            'latitude': target['fields']['latitude'],
            'longitude': target['fields']['longitude'],
            'expiration_date': target['fields']['expiration_date'],
        }
        for target in targets_json
    ]
    # Render the template passing the formatted targets
    return render(request, 'targets/index.html', {'targets': json.dumps(formatted_targets)})
