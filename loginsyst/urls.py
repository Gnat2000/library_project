from django.conf.urls import url, include

from loginsyst.views import login, register, logout

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^', include('allauth.urls')),
]
