from django.urls import path
from .views.session_views import Sessions, SessionDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from . import views
urlpatterns = [
  	# Restful routing
    path('sessions/', Sessions.as_view(), name='sessions'),
    path('sessions/<int:pk>/', SessionDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
