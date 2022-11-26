from django.shortcuts import render
#importo los formularios de python para las vistas
from web.formularios.formularioplatos import FormularioPlatos
from web.formularios.formularioempleados import FormularioEmpleados
# Create your views here.
#todas las vistas son funciones de python
#el nombre de la funcion debe iniciar en mayuscula
def Home(request):
    return render(request,'home.html')

def Platos(request):
    #Esta vista vá a utilizar un formulario de django
    # debo crear entonces un objeto de la clas formularioplatos
    formulario=FormularioPlatos()
    #Creamos un formulario para poder enviar el formulario al html
    data={
        'formulario': formulario
    }
     
    #recibimos los datos del formulario
    if request.method == 'POST':
        datosformularioplatos=FormularioPlatos(request.POST)
        #Volvemos a preguntar si los datos estan limpios
        if datosformularioplatos.is_valid():
            datoslimpios=datosformularioplatos.cleaned_data
            print(datoslimpios)
        
         
         
     
     
     
    return render(request,'menuplatos.html',data)
 

def Empleados(request):
    fempleados=FormularioEmpleados()
    data={
        'fempleados': fempleados
    }
    if request.method == 'POST':
            datosformularioempleados=FormularioEmpleados(request.POST)
            if datosformularioempleados.is_valid():
                datoslimpiosempleados=datosformularioempleados.cleaned_data
                print(datoslimpiosempleados)
         
            
            
    return render(request,'empleados.html',data)
    

