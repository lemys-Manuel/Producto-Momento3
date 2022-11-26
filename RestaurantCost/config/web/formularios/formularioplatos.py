from django import forms


class FormularioPlatos(forms.Form):
    
    PLATOS=(
        (1,'Entrada'),
        (2,'plato Fuerte'),
        (3,'postre')
    )
    
    nombre=forms.CharField(
        required=True,
        label='Nombre del Plato',
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=PLATOS
        
    )
    
    descripción=forms.CharField(
        required=True,
        label='Descripción del Plato',
        max_length=200,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )