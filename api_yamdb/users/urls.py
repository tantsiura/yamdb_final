from api import views
from django.urls import path

urlpatterns = [
    path("signup/", views.SignUpViewSet.as_view(), name="signup"),
    path('token/', views.CreateTokenViewSet.as_view(), name='auth_token')
]
