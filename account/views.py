from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


def custom_logout_view(request):
    # Handle logout logic here (if needed)
    logout(request)
    # Render the logout.html template
    return render(request, 'registration/logout.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('account:dashboard'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})




class CustomPasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')  # replace with your desired success URL
    template_name = 'registration/password_change.html'  # replace with your custom template path

    def get_success_url(self):
        return self.success_url


class CustomPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})
