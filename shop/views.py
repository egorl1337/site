
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import UpdateView
from .models import Comment
from .forms import CommentForm
from .models import Items
# Create your views here.


class New_detail_view(DetailView):
    model = Items
    template_name = 'shop/detail_view.html'
    context_object_name = 'Items'



class edit_comment(UpdateView):
    model = Comment
    template_name = 'shop/comments_edit.html'
    fields = ['text']
    


def index_shop(request):
    items_dict = Items.objects.all()
    return render(request, 'shop\shop_home.html', {'items_dict':items_dict})

def comments(request):
    comment_dict = Comment.objects.order_by('-comment_date')[:2]
    form = CommentForm()
    error = ''
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'форма не правильная'
    return render(request, 'shop\comments_home.html', {'comment_dict':comment_dict, 'form':form, 'error':error})
