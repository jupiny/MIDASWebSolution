"""midas_web_solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from users.views import UserCreateView, UserCreateDoneTV
from .views import home, UserAnalysisView, AdminAnalysisView


urlpatterns = [
                  url(r'^admin/', admin.site.urls),

                  # --- Registration Url
                  url(r'^account/', include('django.contrib.auth.urls')),
                  url(r'^account/register/$', UserCreateView.as_view(), name='register'),
                  url(r'^account/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

                  url(r'^$', home, name='home'),
                  url(r'^user/analysis/$', UserAnalysisView.as_view(), name='user-analysis'),
                  url(r'^admin/analysis/$', AdminAnalysisView.as_view(), name='admin-analysis'),
                  url(r'^foods/', include('food.urls', namespace='food')),
                  url(r'^date/', include('date.urls', namespace='date')),
                  url(r'^api/', include('api.urls', namespace='api')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
