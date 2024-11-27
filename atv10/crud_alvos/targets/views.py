from django.shortcuts import render
from .models import Target
from django.core.serializers import serialize
from rest_framework.viewsets import ModelViewSet
from .serializers import TargetSerializer
import json

# View para renderizar o mapa
def map_view(request):
    # Busca todos os alvos do banco de dados
    targets = Target.objects.all()
    # Serializa os alvos para JSON
    targets_json = json.loads(serialize('json', targets))
    # Formata os dados para simplificação no frontend
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
    # Renderiza o template passando os alvos formatados
    return render(request, 'targets/index.html', {'targets': json.dumps(formatted_targets)})

# API para CRUD de alvos
class TargetViewSet(ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
