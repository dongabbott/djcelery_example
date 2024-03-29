"""tsmsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token

from auth_admin.views import add_handler

schema_view = get_swagger_view(title='tsmsa接口文档')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path(r'account/api-token-auth/', obtain_jwt_token),
    path('account/api-token-refresh/', refresh_jwt_token),
    path('add/', add_handler),
]
