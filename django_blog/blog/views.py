from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name= 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order by latest post 
    paginate_by=2
    
class PostDetailView(DetailView):
    model = Post
 
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields =["title", "content"]
    
    """
    form_valid() is overridden to set the user associated
    with the form instance to the currently logged-in user (self.request.user).
    it successfully processes a form submission but cannot determine where to redirect the user afterward.
    
    """
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields =["title", "content"]

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    "only the author of post can ipdate post"
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url= '/'
    
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})