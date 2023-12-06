
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def lista(request):
    itens = Item.objects.all()
    context = {'itens': itens }
    return render(request, "index.html", context)


def add_item(request):
    if request.method == 'GET':
        form = ItemForm()
        context = {'form':form}
        return render(request, "add_item.html", context)
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            context = {'form' : form}
            form.save()
            form = ItemForm()
            return redirect('/')
        else:
          return render(request, 'index.html', context)
        
        
def updateitem(resquest, id):
    item = get_object_or_404(Item, pk=id)
    form = ItemForm(instance=item)

    if(resquest.method == 'POST'):
        form = ItemForm(resquest.POST, instance=item)

        if(form.is_valid()):
            form.save()

            form = ItemForm()
            return redirect('/')
        else:
            return render (resquest, 'updateitem.html', {'form': form, 'item': item})

    else:
        return render (resquest, 'updateitem.html', {'form': form, 'item': item})
    


def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('/')


def itens(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'itens.html', {'item' : item})