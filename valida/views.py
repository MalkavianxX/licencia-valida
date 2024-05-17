from django.shortcuts import render
import requests
# Create your views here.
def view_start(request):
    return render(request, 'valida/valida.html')

def get_licencia(request,XWOPSLT,FFTWRPTO):
    url = 'https://monkfish-app-5i4nb.ondigitalocean.app/licenciasvalidar_licencia/' + str(XWOPSLT) +'/'+str("CUALQUIERCOSA")
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

