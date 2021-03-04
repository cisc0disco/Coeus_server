from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import HomeDataForm
from .models import HomeData

class HomeView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated == True:
            try:
                data = HomeData.objects.get(username=request.user.username)
                form = HomeDataForm(initial={'azure_key': data.azure_key, 'azure_end': data.azure_end, "wit_key": data.wit_key, "weather_key": data.weather_key, "bridge_ip": data.bridge_ip, "voice": data.voice})
            except:
                form = HomeDataForm()
                form1 = form.save(commit=False)
                form1.username = request.user.username
                form1.save()
            return render(request, 'home.html', {'form': form })
        else:
            return render(request, 'home.html')


    def post(self, request):
        form = HomeDataForm(request.POST)
        if form.is_valid():
            form1 = form.save(commit=False)
            form1.username = request.user.username
            form1.save()
            
        return render(request, 'home.html', {'form': form })