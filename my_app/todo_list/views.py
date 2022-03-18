from django.shortcuts import render
from .models import List
from .forms import ListForm
# Create your views here.

# The python dictionary which is the last parameter in the render can be used to pass data
# to our html pages.

def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all 
            return render(request, 'home.html', {'all_items':all_items})
    else:
        all_items = List.objects.all 
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    # Call using full name
    # my_name = 'Terry Dutcher'
    # return render(request, 'about.html', {'name': my_name})
   
    # Call using multiple variables
    # my_name = 'Terry'
    # return render(request, 'about.html', {'first_name': my_name, 'last_name': 'Dutcher'})
   
    # Create the dictionary seperately - good for readability. 
    context = {'first_name': 'Terry', 'last_name': 'Dutcher'}
    return render(request, 'about.html', context)