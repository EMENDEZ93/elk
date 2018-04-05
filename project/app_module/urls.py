from django.conf.urls import url

from .views import error_view

urlpatterns = [

    url(
        regex=r'^elk$',
        view=error_view,
        name='elk'
    ),
]