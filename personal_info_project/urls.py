from django.contrib import admin
from django.urls import path
from info_app.views import WelcomeView, GoodbyeView, TimeView, GreetView, AgeCategoryView, SumView1, AboutTemplateView, PersonListView, PersonCreateView, PersonUpdateView, feedback_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('goodbye', GoodbyeView.as_view(), name='goodbye'),
    path('current-time', TimeView.as_view(), name='current-time'),
    path('greet', GreetView.as_view(), name='greet'),
    path('age-category', AgeCategoryView.as_view(), name='age-category'),
    path('sum/<num1>/<num2>/', SumView1.sum_numbers, name='sum'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('people/', PersonListView.as_view(), name='people'),
    path('people-new/', PersonCreateView.as_view(), name='people-new'),
    path('people-edit/<int:pk>', PersonUpdateView.as_view(), name='people-edit'),
    path('feedback/', feedback_view, name='feedback'),
]