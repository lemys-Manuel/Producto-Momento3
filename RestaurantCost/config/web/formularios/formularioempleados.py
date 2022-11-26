from django import forms

CARGOS=(
        (1,'chef'),
        (2,'mesero'),
        (3,'tesorero')
    )

class FormularioEmpleados(forms.Form):
    
    nombre=forms.CharField(
        required=True,
        label='Nombre del Empleado',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    documentoidentidad=forms.CharField(
        required=True,
        label='Documento de Identidad',
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
        
    )
    foto=forms.CharField(
        required=True,
        label='Fotografia del Empleado',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    
    tipo=forms.ChoiceField(
        required=True,
        label='Tipo de Cargo',
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=CARGOS
        
    )
    
    