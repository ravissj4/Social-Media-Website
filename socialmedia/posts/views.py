from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from django.views import generic

from django.http import Http404

from . import models

from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

from braces.views import SelectRelatedMixin

# views.py posts
# Create your views here.
class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user", "group")

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(
                username__iexact=self.kwargs.get('username')
            )

        except User.DoesNotExist:
            raise Http404
        
        else:
            return self.post_user.posts.all()
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
    
class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "group")

    def get_queryset(self, **kwargs):
        query_set = super().get_queryset()
        return query_set.filter(user__username__iexact=self.kwargs.get("username"))


class CreatePost(SelectRelatedMixin, generic.CreateView, LoginRequiredMixin):
    model = models.Post
    fields = ('message', 'group')

    def form_valid(self):
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        self.object.save()

        return super().form_valid(form)

class DeletePost(SelectRelatedMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('post_detail')

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(userid=self.request.user.id)
    
    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

    

        

