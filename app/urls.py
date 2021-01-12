from django.urls import path
from . import views
from . import auth

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('table/', views.table, name='table'),
    path('data/', views.data, name='data'),
    path('predict/form/', views.predict, name='predict'),
    path('predict/', views.predict_form, name='submit_prediction'),
    path('user/signup/', auth.user_register, name='signup'),
    path('user/signin/', auth.user_login, name='signin'),
    path('user/profile/<username>/', auth.user_profile, name='profile'),
    path('user/logout/', auth.logout_user, name='logout')
]
