from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Notas
import json

# Create your views here.

class NotaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            notas=list(Notas.objects.filter(id=id).values())
            if len(notas)>0:
                nota=notas[0]
                datos={'message':"Exito!", 'notas':nota}
            else:
                datos={'message':"Nota no encontrada..."}
            return JsonResponse(datos)
        else:
            notas=list(Notas.objects.values())
            if len(notas)>0:
                datos={'message':"Exito!", 'notas':notas}
            else:
                datos={'message':"Notas no encontradas..."}
            return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        Notas.objects.create(titulo=jd['titulo'], descripcion=jd['descripcion'], estado=jd['estado'], fecha_creacion=jd['fecha_creacion'], fecha_cierre=jd['fecha_cierre'])
        datos={'message':"Exito!"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        notas=list(Notas.objects.filter(id=id).values())
        if len(notas)>0:
            nota=Notas.objects.get(id=id)
            nota.titulo=jd['titulo']
            nota.descripcion=jd['descripcion']
            nota.estado=jd['estado']
            nota.fecha_cierre=jd['fecha_cierre']
            nota.save()
            datos={'message':"Exito!"}
        else:
            datos={'message':"Nota no encontrada..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        notas=list(Notas.objects.filter(id=id).values())
        if len(notas)>0:
            Notas.objects.filter(id=id).delete()
            datos={'message':"Exito!"}
        else:
            datos={'message':"Nota no encontrada..."}
        return JsonResponse(datos)