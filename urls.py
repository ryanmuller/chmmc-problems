from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^chmmc/', include('chmmc.problems.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', 'chmmc.problems.views.home'),
    (r'^create/$', 'chmmc.problems.views.create_problem'),
    (r'^create/submit/$', 'chmmc.problems.views.submit_problem'),
    (r'^problem/$', 'chmmc.problems.views.do_random_problem'),
    (r'^problem/(?P<problem_id>\d+)/$', 'chmmc.problems.views.do_problem'),
    (r'^problem/submit/$', 'chmmc.problems.views.submit_eval'),
    (r'^problems/$', 'chmmc.problems.views.list_problems'),
    (r'^feedback/(?P<problem_id>\d+)/$', 'chmmc.problems.views.list_feedbacks'),
    (r'^test/$', 'chmmc.problems.views.request_test'),
    (r'^gentex/$', 'chmmc.problems.views.generate_tex'),
    

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
