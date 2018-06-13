"""RaySharoz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls.static import static
from polls import views
from sharoz_v1 import views as vs
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  # ex: /polls/
                  url(r'^$', vs.home, name='home'),
                  url(r'^about/$', vs.about, name='about'),
                  url(r'^suggest/$', vs.suggest, name='suggest'),
                  url(r'^products/$', vs.products, name='products'),
                  url(r'^submit/suggestion/$', vs.submit_suggestion, name='suggestion'),
                  url(r'^product_id/(?P<product_id>[0-9]+)/$', vs.single_product, name='single_product'),

                  # ex: /polls/5/
                  url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
                  # ex: /polls/5/results/
                  url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
                  # ex: /polls/5/vote/
                  url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:
    urlpatterns += staticfiles_urlpatterns()
