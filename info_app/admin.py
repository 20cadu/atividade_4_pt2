from django.contrib import admin

from info_app.models import Person, ContactLog

# Register your models here.
admin.site.register(Person)
admin.site.register(ContactLog)
