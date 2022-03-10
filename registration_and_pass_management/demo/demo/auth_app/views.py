from django import forms
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from demo.auth_app.models import Profile

UserModel = get_user_model()


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=25, )

    # class Meta:
    #     model = UserModel
    #     fields = ('username', 'first_name')
    #
    # def clean_first_name(self):
    #     return self.cleaned_data['first_name']

    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            **self.cleaned_data,
            user=user,
        )

        if commit:
            profile.save()

        return user


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(LogoutView):
    pass
