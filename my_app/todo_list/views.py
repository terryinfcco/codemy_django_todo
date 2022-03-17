from django.shortcuts import render

# Create your views here.

# The python dictionary which is the last parameter in the render can be used to pass data
# to our html pages.

def home(request):
    return render(request, 'home.html', {})

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