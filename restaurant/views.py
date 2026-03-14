from django.shortcuts import render
from restaurant.forms import BookingForm
from restaurant.models import Menu

def home(request):
    return render(request, 'index.html')

def menu(request):
    menu_data = Menu.objects.all()
    print(menu_data)
    main_data = {
        'menu': menu_data
    }
    print(main_data)
    return render(request, 'menu.html', main_data)

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book.html', {'form': form})
    
def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request, 'menu_item.html', {'menu_item': menu_item})
