from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello_world'),
    path('frontpage/', views.FrontPageView.as_view(), name='frontpage'),
    path('postpage/', views.PostPageView.as_view(), name='postpage'),
]
