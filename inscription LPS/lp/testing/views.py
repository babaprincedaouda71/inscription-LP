from django.shortcuts import render, redirect
from .models import Cars, Models, Sell
from .forms import SellForm
from django.http import JsonResponse

def add(request):
    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('testing:add')
    else:
        form = SellForm()
    return render(request, 'testing/add.html', {'form' : form})



def get_json_car_data(request):
    qs_val = list(Cars.objects.values())
    return JsonResponse({'data' : qs_val})

