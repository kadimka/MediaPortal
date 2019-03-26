from django.views.generic.list import MultipleObjectMixin
from mediaportalapp.models import Category, Article

class CategoryAndArticleListMixin(MultipleObjectMixin):

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all().order_by('-id')
        context['tab_articles'] = Article.objects.all()
        return context