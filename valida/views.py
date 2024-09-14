from django.shortcuts import render
import requests
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def view_start(request):
    return render(request, 'valida/form.html')

def get_licencia(request,id,FFTWRPTO):
    url = 'https://whale-app-jwrqn.ondigitalocean.app/licenciasvalidar_licencia_id/'+str(id)+'/'
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

@csrf_exempt
def verificar_licencia(request):
    data = json.loads(request.body)

    # Extraer los datos en variables individuales
    numero_licencia = data.get('numLicencia')

    url = 'https://whale-app-jwrqn.ondigitalocean.app/licenciasvalidar_licencia/' + str(numero_licencia) +'/'+str("CUALQUIERCOSA")
    response = requests.get(url)
    print("respondio la api")
    if response.status_code == 200:
        data = response.json()
        print(data)
        return JsonResponse({'id': data['id']})  # Retorna solo el ID

    else:
        try:
            data = response.json()
        except ValueError:
            return JsonResponse({'id': "0"},status = 500)  # Retorna solo el ID

        return render(request, 'valida/no.html',{'data':data})

