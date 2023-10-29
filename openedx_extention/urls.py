"""
URLs for openedx_extention.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import UserGreetings

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # re_path(r'', TemplateView.as_view(template_name="openedx_extention/base.html")),
    re_path(r'/greeting',UserGreetings.as_view(), name='greeting'),
]
