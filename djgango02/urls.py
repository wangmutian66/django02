"""djgango02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
import os
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^wangmutian/add$',learn_views.add),
    url(r'^wangmutian/home$',learn_views.home),
    url(r'^wangmutian$',learn_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^wangmutian/new/$', learn_views.new,name="new"),
]
if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR,'learn/static')
    urlpatterns += static('/learn/static/', document_root=media_root)