from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserSignUpForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class SignUpView(FormView):
    template_name ='signup.html'
    form_class = UserSignUpForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        print(form.cleaned_data)
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
        
class UserLogin(LoginView):
    template_name='user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogout(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

class UserAccountUpdate(View):
    template_name = 'profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})    