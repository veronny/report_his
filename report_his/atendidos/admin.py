from django.contrib import admin
from .models import Mes,Tipo_reporte,Disa,Red,Microred,Establecimiento,Provincia,Distrito

# Register your models here.
admin.site.register(Tipo_reporte)
admin.site.register(Disa)
admin.site.register(Red)
admin.site.register(Microred)
admin.site.register(Establecimiento)
admin.site.register(Mes)
admin.site.register(Provincia)
admin.site.register(Distrito)