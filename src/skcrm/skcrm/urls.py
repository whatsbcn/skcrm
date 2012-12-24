from django.conf.urls.defaults import patterns, include, url

import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
                           
    url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/accounts/password/reset/done/'}),
    url(r'^accounts/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),       
    url(r'^accounts/profile/$',  redirect_to, {'url': '/'}),                    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^unselect/(\d+)/', 'skcrm.views.unselect'),
    url(r'^reset/', 'skcrm.views.reset'),
    url(r'^export/', 'skcrm.views.export'),
    url(r'^contacts/', 'skcrm.views.contacts', name='contactes'),
    url(r'^sectors/(\d+)?', 'skcrm.views.sectors', name='sectors'),
    url(r'^medias/(\d+)?', 'skcrm.views.medias', name='mitjans'),
    
    
    url(r'^company/list/$', 'skcrm.views.company', {'action': 'list'}, name='company_list'),
    url(r'^company/edit/(?P<id>\d+)?$', 'skcrm.views.company', {'action': 'edit'}, name='company_edit'),
    url(r'^company/(?P<id>\d+)/add_ot$', 'skcrm.views.company', {'action': 'add_ot'}, name='company_add_ot'),
    url(r'^company/(?P<id>\d+)/del_ot/(?P<ot_id>\d+)$', 'skcrm.views.company', {'action': 'del_ot'}, name='company_del_ot'),
    url(r'^company/del/(?P<id>\d+)/$', 'skcrm.views.company', {'action': 'del'}, name='company_del'),

    url(r'^expense/list/$', 'skcrm.views.expense', {'action': 'list'}, name='expense_list'),
    url(r'^expense/edit/(?P<id>\d+)?$', 'skcrm.views.expense', {'action': 'edit'}, name='expense_edit'),
    url(r'^expense/(?P<id>\d+)/add_item$', 'skcrm.views.expense', {'action': 'add_item'}, name='expense_add_item'),
    url(r'^expense/(?P<id>\d+)/del_item/(?P<item_id>\d+)$', 'skcrm.views.expense', {'action': 'del_item'}, name='expense_del_item'),    
    url(r'^expense/del/(?P<id>\d+)/$', 'skcrm.views.expense', {'action': 'del'}, name='expense_del'),
    
    url(r'^report/gastos_por_ot/(?P<id>\d+)?$', 'skcrm.views.report', {'report': 'gastos_por_ot'}, name='r_gastos_por_ot'),
    url(r'^report/gastos_por_proveedor/(?P<id>\d+)?$', 'skcrm.views.report', {'report': 'gastos_por_proveedor'}, name='r_gastos_por_proveedor'),
    
    url(r'^sections/(\d+)?', 'skcrm.views.sections', name='seccions'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    # Examples:
    # url(r'^$', 'skcrm.views.home', name='home'),
    # url(r'^skcrm/', include('skcrm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'skcrm.views.index'),

    
)

