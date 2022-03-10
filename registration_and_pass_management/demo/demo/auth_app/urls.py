from django.urls import path, include

from demo.auth_app.views import UserRegistrationView, UserLoginView, UserLogoutView, RestrictedView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('restricted/', RestrictedView.as_view(), name='restricted')
    # path('accounts/', include('django.contrib.auth.urls')),
]