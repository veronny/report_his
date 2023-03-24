"""report_his URL Configuration """
from django.contrib import admin
from django.urls import path

from atendidos import views as atendidos_views
from atendidos.views import *

from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # filer arendido
    
    
    path('atendidos_submenu_diresa/', atendidos_views.submenu_diresa, name='atendidos_submenu_diresa'),
    path('atendidos_submenu_red/', atendidos_views.submenu_red, name='atendidos_submenu_red'),  
    path('atendidos_submenu_microred/', atendidos_views.submenu_microred, name='atendidos_submenu_microred'),   
    path('atendidos_submenu_establecimiento/', atendidos_views.submenu_establecimiento, name='atendidos_submenu_establecimiento'),   
    path('atendidos_submenu_provincia/', atendidos_views.submenu_diresa, name='atendidos_submenu_provincia'),   
    path('atendidos_submenu_distrito/', atendidos_views.submenu_diresa, name='atendidos_submenu_distrito'),      
    # filer atendidos
    path('atendidos_establecimientos/', atendidos_views.establecimientos, name='atendidos_establecimientos'), 
    path('atendidos_microredes/', atendidos_views.microredes, name='atendidos_microredes'), 
    path('atendidos_redes/', atendidos_views.redes, name='atendidos_redes'),    
    path('atendidos/', atendidos_views.diresa, name='atendidos'),    
    path('rpt_atendidos/', atendidos_views.rpt_atendidos, name='rpt_atendidos'),
    # login
    path('', users_views.login_view, name='login'),
    path('user/logout/', users_views.logout_view, name='logout'),
    
    #principal  
    path('home/', users_views.home, name='home'),     
]
