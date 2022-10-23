from django.urls import path, include
from django.contrib import admin
from blog1.views import home_view

urlpatterns = [
   path('', home_view),
   path('admin/', admin.site.urls),
   path('polls/', include('ankieta.urls', namespace='polls')),
]
