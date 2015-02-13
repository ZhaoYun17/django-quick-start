from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hello_world_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('hello_world.urls')),
    )
	# These literally means, import all the hello_world apps url into after http:.../
	# and import all the url in admin app into http:/.../admin/