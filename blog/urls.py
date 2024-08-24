from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('blog/<int:id>',detail,name='detail'),
    path('reg/',registration,name='reg'),
    path('login/',sign_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('create/',create_post,name='create'),
    path('update/<int:id>',update_post,name='update')
]