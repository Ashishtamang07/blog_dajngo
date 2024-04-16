from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
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
    paginate_by=5
    
class UserPostListView(ListView):
    model = Post
    template_name= 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order by latest post 
    paginate_by=5
    
    """
    get user from url with usename 
    if user exist filter post by author= user
    """
    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        
    
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
    "only the author of post can update post"
    def test_func(self):
        post= self.get_object()
        return self.request.user == post.author
    
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