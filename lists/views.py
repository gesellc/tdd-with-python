from django.shortcuts import render
from lists.models import Item

# TODO: Don't save blank items for every request

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text) # create and save a new Item
    else:
      new_item_text = ''

    return render(request, 'home.html', {
        'new_item_text': new_item_text
    })
