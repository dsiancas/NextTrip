from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'static/(?P<path>,*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
	(r'media/(?P<path>,*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # Examples:
    url(r'^$', 'join.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
) # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

