from django.contrib import admin
from .models import TestRecord, Specimen, Principle, Container

admin.site.register(TestRecord)
admin.site.register(Specimen)
admin.site.register(Principle)
admin.site.register(Container)
