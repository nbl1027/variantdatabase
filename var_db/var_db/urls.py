"""var_db URL Configuration

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
from snps import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload_file/', views.upload_file, name='upload_file'),
    url(r'^admin/', admin.site.urls),
    url(r'^variants/', views.variants, name = 'variants'),
    url(r'^success/', views.success, name = 'success'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient_search/', views.patient_search, name='patient_search'),
    url(r'^patientresult/', views.patient_search, name='patientresult'),
    url(r'^sample_search/', views.sample_search, name='sample_search'),
    url(r'^ins_search/', views.ins_search, name='ins_search'),
    #url(r'^sampleresult/', views.sampleresult, name='sampleresult'),
]

