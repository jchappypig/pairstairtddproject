from django.conf.urls.defaults import patterns, include, url
from pair_stair.views import add_programmer_index, pair_stair_index, remove_programmers_index, mark_pair

urlpatterns = patterns('',
    # Examples:
    url(r'^addProgrammer/$', add_programmer_index),
    url(r'^pairStair/$', pair_stair_index),
    url(r'^removeAllProgrammers/$', remove_programmers_index),
    url(r'^pairStair/(?P<programmer1_id>.+?)/(?P<programmer2_id>.+?)$', mark_pair)
    # url(r'^pairstairtddproject/', include('pairstairtddproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
