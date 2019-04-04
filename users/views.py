from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignUpValidation, LoginValidation
from django.contrib.auth import login, authenticate

class HomeView(TemplateView):
    """
    home view
    """
    template_name = "base.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)


class LoginView(TemplateView):
    """
    login view
    """
    template_name = "user/login.html"
    login_form = LoginValidation()

    def get(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        return render(
            self.request, self.template_name,
            {'forms': self.login_form})

    def post(self, *args, **kwargs):
        forms = LoginValidation(self.request.POST)

        if forms.is_valid():
            user = authenticate(
                username=forms.cleaned_data.get('email'),
                password=forms.cleaned_data.get('password'))
            login(self.request, user)

            return render(self.request, 'main/home.html')
        
        return render(self.request, self.template_name, 
            {'forms': forms})


class SignUpView(TemplateView):
    """
    signup view
    """
    template_name = "user/signup.html"
    signup_form = SignUpValidation()

    def get(self, *args, **kwargs):
        signup_form = SignUpValidation()
        return render(self.request, self.template_name,
            {'forms': self.signup_form})

    def post(self, *args, **kwargs):
        forms = SignUpValidation(self.request.POST)

        if forms.is_valid():
            user = forms.save()
            user.set_password(forms.cleaned_data.get('password'))
            user.save()

            user = authenticate(
                username=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'))
            login(request, user)

            return render(self.request, "base.html")

        return render(self.request, self.template_name, 
            {'forms': forms})





