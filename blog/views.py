from django.shortcuts import render
from datetime import  datetime
from django.shortcuts import render_to_response,render
from blog.models import BlogPost
from django.http import HttpResponseRedirect
from django.template import RequestContext
from  django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def archive(request):
    # post = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
    posts = BlogPost.objects.all()[:10]
    # return render_to_response('blog/archive.html', {'posts': posts, }, RequestContext(request))
    return render(request, 'blog/archive.html', {'posts': posts})


def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now(),
        ).save()
    return HttpResponseRedirect('/blog/')