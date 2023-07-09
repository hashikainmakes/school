from.import views
from django.urls import path

app_name='schoolapp'

urlpatterns = [
    path('', views.demo,name='demo'),
    path('register/',views.register,name="register"),
    path('login/', views.login, name='login'),
    path('accept/', views.accept, name='accept'),
    path('form/',views.index,name='form'),
    path('load-courses/', views.load_courses, name="ajax_load_courses"),
    path('success/', views.submit, name='submit'),
    path('logout', views.logout, name='logout')

]
