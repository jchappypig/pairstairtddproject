from django.conf.urls.defaults import patterns, include, url
from pair_stair.views import add_programmer_index

urlpatterns = patterns('',
    # Examples:
    url(r'^addProgrammer/', add_programmer_index),
    # url(r'^pairstairtddproject/', include('pairstairtddproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
