
from django.shortcuts import render
from http.client import responses
from platform import python_version
import datetime
from django.http import JsonResponse
from django.template.context_processors import request
from django.template.defaultfilters import title
from django.views import View
from django.views.generic import TemplateView
from info_app.models import Person
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from .models import Person
from .forms import PersonForm, FeedbackForm

class WelcomeView(View):
    def get(self, request):
        return JsonResponse({
            "message": "Welcome to the Personal Info API!"
        })

class GoodbyeView(View):
    def get(self, request):
        return JsonResponse({
            "message": "Goodbye, see you next time!"
        })

class TimeView(View):
    def get(self, request):
        current_time = datetime.datetime.now().strftime('%H.%M.%S')
        return JsonResponse({
            "current time": current_time
        })

class GreetView(View):
    def get(self, request):
        name = request.GET.get('name' ,'Stranger')
        return JsonResponse({

            "message": f"Hello, {name}!",

        })

class AgeCategoryView(View):
    def get(self, request):
        age = int(request.GET.get('age'))
        try:  
            if 0 < age <= 12:
                return JsonResponse({'age category': 'Child'})
            if 12 < age <= 17:
                return JsonResponse({'age category': 'Teenager'})
            if 17 < age <= 59:
                return JsonResponse({'age category': 'Adult'})
            if 59 < age :
                return JsonResponse({'age category': 'Senior'})
        except ValueError:
            return JsonResponse({ 'error': "Missing 'age' parameter."})

class SumView1(View):
    def sum_numbers(self, num1, num2):
        try:
            n1 = int(num1)
            n2 = int(num2)
            result = n1 + n2
            return JsonResponse({"sum": result})
        except ValueError:
            return JsonResponse({"error": "Invalid input, please provide two integers."}, status=400)

class AboutTemplateView(TemplateView):
    template_name = 'info_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_nome'] = 'Sobre'
        context['site_desc'] = 'Site em processo de desenvolvimento.'
        context['site_ano'] = '2025'
        return context


class PersonListView(ListView):
    model = Person
    template_name = 'info_app/person_list.html'
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'info_app/person_form.html'
    success_url = reverse_lazy('people')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'info_app/person_form.html'
    success_url = reverse_lazy('people')


def feedback_view(request):
    mensagem = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            satisfacao = form.cleaned_data['satisfacao']
            mensagem = f'Obrigado pelo feedback, {nome}! Sua satisfação: {satisfacao}.'
            return render(request, 'feedback/feedback.html', {'mensagem': mensagem})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form, 'mensagem': mensagem})


