from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password/reset/done/'}),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^unselect/(\d+)/', 'skcrm.views.unselect'),
    url(r'^reset/', 'skcrm.views.reset'),
    url(r'^export/', 'skcrm.views.export'),
    url(r'^contacts/', 'skcrm.views.contacts', name='contactes'),
    url(r'^sectors/(\d+)?', 'skcrm.views.sectors', name='sectors'),
    url(r'^medias/(\d+)?', 'skcrm.views.medias', name='mitjans'),
    url(r'^companies/(\d+)?', 'skcrm.views.companies', name='empreses'),
    url(r'^sections/(\d+)?', 'skcrm.views.sections', name='seccions'),

    # Examples:
    # url(r'^$', 'skcrm.views.home', name='home'),
    # url(r'^skcrm/', include('skcrm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^.*', 'skcrm.views.index')
)
