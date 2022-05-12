from config.wsgi import *
from django.test import TestCase
from core.erp.models import Category, Type, Employee

# Listar

''' llamar todos los objetos '''
query = Type.objects.all
print(query)

''' insercion '''

t = Type()
t.name = 'prueba'
t.save()
print(t)

''' Edición '''
# buscar el id
t = Type.objects.get(pk=1)
t.name = 'Accionista'
print(t.name)

''' Eliminar '''
t.delete()

''' Filtros '''
obj = Type.objects.filter(name_contains='prueba')
# buscar por mayusculas y minusculas
obj = Type.objects.filter(name_icontains='prueba')
# empiecen con una letra
obj = Type.objects.filter(name_startswith='p')
# terminen con una letra
obj = Type.objects.filter(name_endswith='p')
# buscar varias palabras
obj = Type.objects.filter(name_in=['prueba','carro'])
# contar los registros
obj = Type.objects.filter(name_in=['prueba','carro']).count()
# el codigo de busqueda
obj = Type.objects.filter(name_contains='prueba').query
# excluir palabras
obj = Type.objects.filter(name_contains='prueba').exclude(id=1)
# iterar para que se muestre
for i in Type.objects.filter(name_startswith='p'):
    print(i.name)
# Sub consultas
obj = Employee.objects.filter(type_id=1)
print(obj)


data = ['leche y derivados', 'Carnes, pescado y huevos','Patatas, legumbres, frutos secos']

for i in data:
    cat = Category(name=i)
    cat.save()
    print(f'registroguardado {cat.i}')




