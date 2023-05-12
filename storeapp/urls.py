"""storeapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from oauth2_provider.views import TokenView, AuthorizationView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('o/token/', TokenView.as_view(), name='token'),
    # path('o/authorize/', AuthorizationView.as_view(), name='authorize'),
    path('', include('applications.tasks.urls')),
    path('', include('applications.store.urls')),
    path('', include('applications.register.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
