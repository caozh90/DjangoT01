from django.shortcuts import render
from datetime import  datetime
from django.shortcuts import render_to_response
from blog.models import BlogPost

# Create your views here.
def archive(request):
    # post = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
    posts = BlogPost.objects.all()[:10]
    return render_to_response('blog/archive.html', {'posts': posts})
