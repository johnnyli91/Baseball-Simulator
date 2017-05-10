from django.conf.urls import include, url
from django.contrib import admin
from Baseball.views import index, signup, roster
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include('Baseball.api.urls')),
    url(r'^login/$', auth_views.login, {'template_name': '../static/app/views/registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^roster/$', roster, name='roster'),
]
