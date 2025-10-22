from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_user, name='signup_user'),
    path('login/', views.login_user, name='login_user'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-resource/', views.add_resource_view, name='add_resource'),
    path('resource-detail/<int:resource_id>/', views.resource_detail_view, name='resource_detail'),
    path('logout/', views.logout_user, name='logout_user'),
]