from django.urls import path
from . import views

app_name = 'paginas'


urlpatterns = [
    #path('admin/', admin.site.urls),
    path ('', views.home, name='home'),
]
