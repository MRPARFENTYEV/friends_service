from django.urls import path
from django.contrib.auth import views as auth_views
from sweet_friends_app import views
from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
app_name = 'sweet_friends_app'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
    path('', views.home_page, name='home_page'),
    path('potential_friends/', views.potential_friends, name='potential_friends'),
    path('<int:user_id>', views.friend_detail, name='friend_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),]
    # path('add_friend/<int:friend_id>/', views.add_friend, name='add_friend')]


