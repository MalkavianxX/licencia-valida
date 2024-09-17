from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def view_start(request):
    return render(request, 'valida/form.html')


def form(request,id,token):
    """_summary_

    Args:
        
        id (int): Id de la licencia original

    Returns:
        view: form para buscar la licencia
    """
    return render(request,'valida/form.html',{'id':id})

@csrf_exempt
def view_licencia(request,id,token):
    url = 'http://127.0.0.1:8080/licenciasvalidar_licencia_id/'+str(id)+'/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request, 'valida/ok.html',{'data':data})
    else:
        try:
            data = response.json()
        except ValueError:
            data = {'error': 'Error desconocido'}
        return render(request, 'valida/no.html',{'data':data})