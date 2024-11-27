import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "company.settings")
django.setup()

from queries.models import Position, Employee


def populate():

    position1 = Position.objects.get_or_create(title="Gerente de Projetos")[0]
    position2 = Position.objects.get_or_create(title="Tecnologia da Informacao")[0]
    position3 = Position.objects.get_or_create(title="Serviços Gerais")[0]
    position4 = Position.objects.get_or_create(title="Departamento Pessoal")[0]

    Employee.objects.get_or_create(name="Antonio Carlos", position=position1, hire_date="1999-05-10")
    Employee.objects.get_or_create(name="Marcos Paulo", position=position2, hire_date="1998-04-05")
    Employee.objects.get_or_create(name="Samanta Oliveira", position=position3, hire_date="2005-06-20")
    Employee.objects.get_or_create(name="Beatriz Pires", position=position1, hire_date="2003-12-10")
    Employee.objects.get_or_create(name="José dos Santos", position=position1, hire_date="1999-01-17")
    Employee.objects.get_or_create(name="Maria das Graças", position=position4, hire_date="2007-06-07")

    print("Dados populados com sucesso!")


if __name__ == "__main__":
    populate()
