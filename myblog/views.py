from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import blog

def show_blog(request):

    if request.method == "POST":
        myblog = blog.objects.create(name=request.POST.get("todo_name"),
                            description=request.POST.get("description_name"),
                            owner=request.user)

        myblog.tags.add(*request.POST.getlist("tag_names"))


    return render(request, "my_todos.html", {"todos": blog.objects.filter(owner=request.user.id),
                                             "tags":Tag.objects.all()})


def get_blog(request, todo_id):
    try:
        myblog = blog.objects.get(id=todo_id)
        if request.user.id != myblog.owner.id:
            raise PermissionDenied
        return render(request, "detailed_todo.html", {"todo": myblog})
    except blog.DoesNotExist:
        raise Http404("We don't have any.")