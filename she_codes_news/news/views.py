from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        author=self.request.GET.get('author')
        qs = NewsStory.objects.all().order_by('-pub_date')
        if author:
            qs = qs.filter(author__username=author)
        context['all_stories'] = qs
        return context
        # context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

        # 'pub_date': forms.DateInput(format=('%m/%d/%Y'),
        # attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),

