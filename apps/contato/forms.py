from django import forms

class ContatoForms (forms.Form):

    nome = forms.CharField(
        label= 'Nome',
        max_length=100,
        required=True
    )

    fone = forms.CharField(
        label='Fone:',
        max_length=15,
        required=True
    )