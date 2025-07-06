from django import forms
from .models import Person
from django import forms

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'gender','email']

        labels = {
            'name': 'Nome',
            'age': 'Idade',
            'gender': 'Gênero',
            'email': 'E-mail'
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
    

class FeedbackForm(forms.Form):
    feedback = [
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    ]

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail')
    comentario = forms.CharField(label='Comentário', widget=forms.Textarea)
    satisfacao = forms.ChoiceField(label='Satisfação', choices=feedback)