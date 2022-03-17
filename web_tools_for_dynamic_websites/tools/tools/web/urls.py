from django.urls import path

from tools.web.views import index

urlpatterns = (
    path('', index, name='index'),
)