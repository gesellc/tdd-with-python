from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text']) # create and save a new Item
        return redirect('/')

    return render(request, 'home.html')
