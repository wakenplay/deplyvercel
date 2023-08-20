from django.urls import path
from . import views



urlpatterns=[
  path('',views.home,name='home'),
  path('singup',views.SignUp,name='signup'),
  path('login',views.user_login,name='login'),
  path('mytodos/<str:user_todo>',views.mytodos,name='mytodos'),
  path('add_todo',views.add_todo,name='add_todo'),
  path('remove',views.remove_todo,name='remove')

]
