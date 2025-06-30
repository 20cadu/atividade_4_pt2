from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
        labels = {
            'name': 'Nome',
            'age': 'Idade',
        }
        
    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        if len(name.strip()) < 3:
            raise forms.ValidationError('O nome deve ter pelo menos 3 caracteres.')
        return name

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is None:
            raise forms.ValidationError('Informe a idade.')
        if not isinstance(age, int):
            raise forms.ValidationError('A idade deve ser um número inteiro.')
        if age > 150:
            raise forms.ValidationError('A idade máxima permitida é 150.')
        if age < 0:
            raise forms.ValidationError('A idade não pode ser negativa.')
        return age