from django.conf.urls import url

from .views import show_tag, get_tag

urlpatterns = [
    url(r'^$', show_tag),
    url(r'^(?P<entry_id>[0-9])', get_tag)
]
