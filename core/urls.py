from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

urlpatterns = [
    path(_('admin/'), admin.site.urls),
    path(_('rosetta'), include('rosetta.urls')),
    path('', include('blog.urls')),
]

urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path(_('rosetta'), include('rosetta.urls')),
    path('', include('blog.urls'))
)
