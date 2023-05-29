from django.urls import path,include
from . import views

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    path("", login_required(index_view), name="index"),
    path('', include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('activate/<uidb64>/<token>/', views.ActivateView.as_view(), name='activate'),
]