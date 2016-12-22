from django.conf.urls import url , include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^todos/', include("todo.urls")),
    url('^blog/entries/', include("myblog.urls")),
    url('^users/', include("users.urls")),
    url('^tags/', include("tags.urls"))

]

