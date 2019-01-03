"""nasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from nasagram.views import NasaCommentListView, NasaCommentCreateView, NasaCommentDetailView, NasaCommentDeleteView, NasaCommentUpdateView, DatePickerTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nasa/datepicker', DatePickerTemplateView.as_view()),
    path('nasa/createcomment', NasaCommentCreateView.as_view(), name="nasa_comment_create"),
    path('nasa/list', NasaCommentListView.as_view(), name="nasa_comment_list"),
    path('nasa/detail/<int:pk>', NasaCommentDetailView.as_view(), name="nasa_comment_detail"),
    path('nasa/delete/<int:pk>', NasaCommentDeleteView.as_view()),
    path('nasa/update/<int:pk>', NasaCommentUpdateView.as_view()),
]
