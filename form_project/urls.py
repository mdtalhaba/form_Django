from django.contrib import admin
from django.urls import path, include
from first_app import views as first_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form.urls')),
    path('', include('first_app.urls'))
]
