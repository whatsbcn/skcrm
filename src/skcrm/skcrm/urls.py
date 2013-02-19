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
    
    url(r'^contact/list/$', 'skcrm.view.contact.ls', name='contact_list'),
    url(r'^contact/select_list/$', 'skcrm.view.contact.ls', {'select': True}, name='contact_select_list'),
    #url(r'^contact/edit/(?P<id>\d+)?$', 'skcrm.view.contact.edit', name='contact_edit'),
    #url(r'^contact/del/(?P<id>\d+)/$', 'skcrm.view.contact.delete', name='contact_del'),
    url(r'^contact/unselect/(?P<id>\d+)/$', 'skcrm.view.contact.unselect', name='contact_unselect'),
    url(r'^contact/reset/', 'skcrm.view.contact.reset', name='contact_reset'),
    url(r'^contact/export/', 'skcrm.view.contact.export', name='contact_export'),


    url(r'^person/list/$', 'skcrm.view.person.ls', name='person_list'),
    url(r'^person/edit/(?P<id>\d+)?$', 'skcrm.view.person.edit', name='person_edit'),
    url(r'^person/del/(?P<id>\d+)/$', 'skcrm.view.person.delete', name='person_del'),
    url(r'^person/(?P<id>\d+)/edit_cd/(?P<cd_id>\d+)?$', 'skcrm.view.person.edit_cd', name='person_edit_cd'),
    url(r'^person/(?P<id>\d+)/del_cd/(?P<cd_id>\d+)$', 'skcrm.view.person.del_cd', name='person_del_cd'),
    
    url(r'^sector/list/$', 'skcrm.view.sector.ls', name='sector_list'),
    url(r'^sector/edit/(?P<id>\d+)?$', 'skcrm.view.sector.edit', name='sector_edit'),
    url(r'^sector/del/(?P<id>\d+)/$', 'skcrm.view.sector.delete', name='sector_del'),
    
    url(r'^section/list/$', 'skcrm.view.section.ls', name='section_list'),
    url(r'^section/edit/(?P<id>\d+)?$', 'skcrm.view.section.edit', name='section_edit'),
    url(r'^section/del/(?P<id>\d+)/$', 'skcrm.view.section.delete', name='section_del'),

    url(r'^concept_type/list/$', 'skcrm.view.concept_type.ls', name='concept_type_list'),
    url(r'^concept_type/edit/(?P<id>\d+)?$', 'skcrm.view.concept_type.edit', name='concept_type_edit'),
    url(r'^concept_type/del/(?P<id>\d+)/$', 'skcrm.view.concept_type.delete', name='concept_type_del'),

    url(r'^sub_concept_type/list/$', 'skcrm.view.sub_concept_type.ls', name='sub_concept_type_list'),
    url(r'^sub_concept_type/edit/(?P<id>\d+)?$', 'skcrm.view.sub_concept_type.edit', name='sub_concept_type_edit'),
    url(r'^sub_concept_type/del/(?P<id>\d+)/$', 'skcrm.view.sub_concept_type.delete', name='sub_concept_type_del'),
    
    url(r'^media/list/$', 'skcrm.view.media.ls', name='media_list'),
    url(r'^media/edit/(?P<id>\d+)?$', 'skcrm.view.media.edit', name='media_edit'),
    url(r'^media/del/(?P<id>\d+)/$', 'skcrm.view.media.delete', name='media_del'),
    url(r'^media/(?P<id>\d+)/edit_cd/(?P<cd_id>\d+)?$', 'skcrm.view.media.edit_cd', name='media_edit_cd'),
    url(r'^media/(?P<id>\d+)/del_cd/(?P<cd_id>\d+)$', 'skcrm.view.media.del_cd', name='media_del_cd'),
    
    url(r'^company/list/$', 'skcrm.view.company.ls', name='company_list'),
    url(r'^company/edit/(?P<id>\d+)?$', 'skcrm.view.company.edit', name='company_edit'),
    url(r'^company/(?P<id>\d+)/add_ot$', 'skcrm.view.company.add_ot', name='company_add_ot'),
    url(r'^company/(?P<id>\d+)/del_ot/(?P<ot_id>\d+)$', 'skcrm.view.company.del_ot', name='company_del_ot'),
    url(r'^company/del/(?P<id>\d+)/$', 'skcrm.view.company.delete', name='company_del'),
    url(r'^company/(?P<id>\d+)/edit_cd/(?P<cd_id>\d+)?$', 'skcrm.view.company.edit_cd', name='company_edit_cd'),
    url(r'^company/(?P<id>\d+)/del_cd/(?P<cd_id>\d+)$', 'skcrm.view.company.del_cd', name='company_del_cd'),

    url(r'^expense/list/$', 'skcrm.view.expense.ls', name='expense_list'),
    url(r'^expense/edit/(?P<id>\d+)?$', 'skcrm.view.expense.edit', name='expense_edit'),
    url(r'^expense/(?P<id>\d+)/add_item$', 'skcrm.view.expense.add_item', name='expense_add_item'),
    url(r'^expense/(?P<id>\d+)/del_item/(?P<item_id>\d+)$', 'skcrm.view.expense.del_item', name='expense_del_item'),    
    url(r'^expense/del/(?P<id>\d+)/$', 'skcrm.view.expense.delete', name='expense_del'),
    
    url(r'^report/gastos_por_ot/(?P<id>\d+)?$', 'skcrm.views.report', {'report': 'gastos_por_ot'}, name='r_gastos_por_ot'),
    url(r'^report/gastos_por_proveedor/(?P<id>\d+)?$', 'skcrm.views.report', {'report': 'gastos_por_proveedor'}, name='r_gastos_por_proveedor'),
    
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    # Examples:
    # url(r'^$', 'skcrm.views.home', name='home'),
    # url(r'^skcrm/', include('skcrm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^chaining/', include('smart_selects.urls')),
    url(r'^$', 'skcrm.views.index'),

    
)

