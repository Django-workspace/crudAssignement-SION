from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from firstBlog.forms import BlogForm
from firstBlog.models import Blog
# Create your views here.
def list_blog(request):
    blogs=Blog.objects.all()
    context={"blogs":blogs}
    return render(request, 'viewBlog.html', context)

def add_blog(request):
    form=BlogForm()
    context={"form":form}
    if request.method == 'POST':
        blog_form=BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('view')
    return render(request,'createBlog.html',context)
        
def update_blog(request, id):
    blog=Blog.objects.get(id=id)
    form=BlogForm
    context={'form':form}
    if form.is_valid:
        form.save()
        return redirect('view')
    return render(request, "viewBlog.html", context)
    
    # queryset= Blog.objects.get(id=id)
    # form = BlogForm(instance=queryset)
    # if request.method == 'POST':
    #     form = BlogForm(request.POST, instance=queryset)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('view')
    # context = {
    #     'form': form
    # }
    # return render(request, "viewBlog.html", context)


# views for deleting a trainee
# def delete_blog(request, id):
#     queryset = Blog.objects.get(id=id)
#     if request.method == 'POST':
#         queryset.delete()
#         messages.success(request, 'successful deleted')
#         return redirect('/')

    #return render(request, "viewBlog.html")
def delete_blog(request, id):
        blog = Blog.objects.get(id=id)
        blog.delete()
        return redirect('view')
        