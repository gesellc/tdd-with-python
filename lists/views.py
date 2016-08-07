from django.shortcuts import render
from lists.models import Item

# TODO: Don't save blank items for every request

def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()

    return render(request, 'home.html', {
        'new_item_text': item.text
    })
