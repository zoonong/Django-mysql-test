"""insta URL Configuration

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
# from os import sta
from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.home, name="home"),
    path('<int:id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('<int:id>/create_comment', views.create_comment, name="create_comment"),
    path('update_comment/<int:post_id>/<int:comment_id>', views.update_comment, name="update_comment"),
    path('edit_comment/<int:post_id>/<int:comment_id>', views.edit_comment, name="edit_comment"),
    path('delete/<int:post_id>/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('like_toggle/<int:post_id>', views.like_toggle, name="like_toggle"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
