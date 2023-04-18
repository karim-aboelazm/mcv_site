from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView
from django.contrib.auth import authenticate , login ,logout
from .models import *
from .forms import *


class MCVRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and MCVUser.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect('/dashboard/?carname=1')
        return super().dispatch(request, *args, **kwargs)
    

class HomePageView(MCVRequiredMixin,TemplateView):
    template_name = "home.html"


class DashBoardPageView(MCVRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print("Connected...")
        kw = self.request.GET.get("carname")
        context["all_cars"] = Car.objects.all().order_by("-id")
        context["car_detail"] = Car.objects.get(car_id=kw) if kw else None
        context["driver"] = Driver.objects.get(drive_car=context["car_detail"].id) if context["car_detail"] != None else None
        context["last_cars"] = Car.objects.all().exclude(car_id=kw) if kw else None
        return context

class McvUserLogin(FormView):
    template_name = "mcv_user_login.html"
    form_class = McvUserLoginForm
    success_url = '/dashboard/?carname=1'
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and MCVUser.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)
    


