from django.conf.urls import patterns, include, url
from WePlay import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'Pessoas.views.index'),
	url(r'^Pessoa/Cadastro/$', 'Pessoas.views.cadastro_pessoa'),
	url(r'^Jogo/Cadastro/$', 'Pessoas.views.cadastro_jogo'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.STATIC_ROOT, 
        }),
    )