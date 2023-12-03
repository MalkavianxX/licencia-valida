from django.shortcuts import render
import requests
# Create your views here.
def view_start(request):
    return render(request, 'valida/valida.html')

def get_licencia(request,XWOPSLT,FFTWRPTO):
    #get_licencia/3/SHHHA
    url = 'http://localhost:8000/licenciasvalidar_licencia/' + str(XWOPSLT) +'/'+str("CUALQUIERCOSA") # La URL de tu API
    response = requests.get(url)  # Hacer la petición GET
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta a JSON
        print(data)
        return render(request, 'valida/ok.html',{'data':data})

    else:
        return render(request, 'valida/no.html')
