"""priceIsRight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from authentication.forms import LoginForm #, UserForm
from stocks import views
from authentication import views as custom_auth_views

urlpatterns = [
    url(r'', include('authentication.urls')),
    # url(r'^register/$', custom_auth_views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
    url(r'^place_order/$', views.index, name='place_order'),
    url(r'^order/(?P<id>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^admin/', admin.site.urls),
]
