from .models import Category

def category(request):
    return {
        'category':Category.objects.filter(parent__isnull=True),
    }


