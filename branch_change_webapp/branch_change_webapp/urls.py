from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin



#admin.site.index_template = 'admin/branch_chnge/change_form.html'
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'branch_change_webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$' , 'branch_change.views.login' , name = 'login'),

    url(r'^branch_change_form/', 'branch_change.views.branch_change_form', name='branch_change_form'),

    url(r'^login/$' , 'branch_change.views.login' , name = 'branch_change_form' ),

    url(r'^logout/$' , 'branch_change.views.logout' , name = 'branch_change_form' ),

    url(r'^authorized/' , 'branch_change.views.authorized_view' , name = 'authorized_view'),

    url(r'^register/' , 'branch_change.views.register' , name = 'register'),

    url(r'^naveen/' , 'branch_change.views.naveen' , name = 'user'),

    url(r'^download_csv/' , 'branch_change.views.download_csv' , name= 'branch_change_view'),

    url(r'^import_csv/' , 'branch_change.views.save_csv' , name = 'save' ),

    url(r'^get_allocation/' , 'branch_change.views.get_allocation' , name = 'output' ),

    url(r'^see_allocation/' , 'branch_change.views.see_allocation' , name='allo'),

    url(r'^see_stats/' , 'branch_change.views.see_stats' , name = 'stats'),
    
)



if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Branch Change \'15 Administration'
