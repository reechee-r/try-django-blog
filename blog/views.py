from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost

#
# def blog_post_detail_page(request, slug):
#     print(request.method, request.user, request.path)
#     print(type(request))
#     obj = get_object_or_404(BlogPost, slug=slug)
#     # try:
#     #     obj = BlogPost.objects.get(id=post_id)
#     # except ValueError:
#     #     raise Http404
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     template_name = 'blog_pos_detail.html'
#     context = {"object": obj}
#     return render(request, template_name, context)


# CRuD ++> Create Retrieve Update Delete
def blog_post_list_view(request):
    # qs = BlogPost.objects.filter(title__icontains='hello')
    # list out a Items using .all
    # could be searched using filter
    qs = BlogPost.objects.all()
    template_name = "blog/list.html"
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # obj = get_object_or_404(BlogPost, slug=slug)
    # create forms
    # use forms
    template_name = 'blog/blog_post_create.html'
    context = {"form": None}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_update.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/blog_post_delete.html'
    context = {"object": obj}
    return render(request, template_name, context)