from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    #vistas render
    path('',views.view_start, name='view_start'),
    path('form/<int:id>/<str:token>/', views.form, name="form"),
    path('view_licencia/<int:id>/<str:token>/', views.view_licencia, name= "view_licencia" )
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)