from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import book
# Create your views here.

class bookListView(ListView):#to see full database only, extend ListView.
    model=book#here django searches for a default template named book_list.html,so we have to create it.
    template_name='testapp/books.html'#if we want to create our own template externally i.e. changing default name of template file.
    context_object_name="CustomizedBooks"


class bookdetailView(DetailView):
    model=book#here django searches for a default template named book_detail.html,so we have to create it.
