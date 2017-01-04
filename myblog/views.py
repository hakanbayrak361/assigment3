from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import Blog
from .forms import BlogForm

def show_blog(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            myblog = form.save(commit=False)
            myblog.owner = request.user
            myblog.save()
            #myblog.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "my_entry.html", {"blogs": Blog.objects.filter(owner=request.user.id),
                                             "tags": Tag.objects.all(),
                                             "form": form})

def get_blog(request, todo_id):
    try:
        myblog = Blog.objects.get(id=todo_id)
        if request.user.id != myblog.owner.id:
            raise PermissionDenied
        return render(request, "exstra.html", {"myblog": myblog})
    except Blog.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def show_all_blog(request):
    return render(request, "my_entry.html", {"blogs": Blog.objects.all()})

@permission_required('is_superuser')
def show_all_blog_from_user(request, userId):
    return render(request, "my_entry.html", {"blogs": Blog.objects.filter(owner=userId)})
