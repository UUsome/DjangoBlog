from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = "chatai"
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.query_view, name='query'),

]