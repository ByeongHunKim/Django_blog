"""config URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from webpage.views import Main

from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # url 뒤에 아무도 없다 -> url만 접속했을 떄 Main class 실행
    path('', Main.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_route=settings.STATIC_URL)
