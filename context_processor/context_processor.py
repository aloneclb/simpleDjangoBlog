from post.models import Category, SiteConfig


def site_context(request):
    """
        Site İçerisinde Kullanılan Navbar, Footer Alanlarına
        - Category Name, Url Link
        - Site Confugirasyon Object
            - Social URL (Facebook, İnstagram etc.)
            - Footer Description
            - About Us 
    """
    context = dict()
    context['categories'] = Category.objects.all().order_by('-update_time')
    context['site_config'] = SiteConfig.objects.get(id =1)
    return context