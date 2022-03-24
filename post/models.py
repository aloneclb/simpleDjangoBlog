from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools
from ckeditor.fields import RichTextField



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

    @property
    def total_post(self):
        return self.post_set.all().count()

    class Meta:
        ordering = ('-created_time',)


    def save(self, *args, **kwargs):
        """
            models.Model.save() metodu çalışırken yani kaydederken eşsiz bir slug yaratma
        """
        if not self.id: # Eğer Veritabanında daha önceden atanmış bir pk'sı yoksa
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not Category.objects.filter(slug = self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)
        super(Category, self).save()



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    stand = models.BooleanField(verbose_name='Öne çıkarılsın mı?', default=True)
    category = models.ManyToManyField(Category, blank=True) 
    # İlişkisel Olmayan Alanlar
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, editable=False)
    body = RichTextField()
    snippet = models.TextField(max_length=200, default='Linke Tıkla ve Okumaya Başla') # Home Sayfasında Açıklayıcı Yazı
    image = models.ImageField(upload_to = 'post/%Y/%m/%d/', default='post-image/default.jpg') # 800 x 560
    created_time = models.DateTimeField(auto_now_add=True) 
    update_time = models.DateTimeField(auto_now=True) 
    
    class Meta:
        ordering = ('-created_time',)
    
    def __str__(self):
        return self.title
    
    
    
    def save(self, *args, **kwargs):
        """
            Model.save() metodu çalışırken yani kaydederken eşsiz bir slug yaratma
        """
        if not self.id: # Eğer Veritabanında daha önceden atanmış bir pk'sı yoksa
            self.slug = slugify(self.title)

            for slug_id in itertools.count(1):
                if not Post.objects.filter(slug = self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)
        super(Post, self).save()

    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='Kullanıcı E-maili:')
    body = models.TextField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True, help_text='Yorum Görüntülensin mi?')
    
    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return 'Comment by {} - {} '.format(self.post.title, self.body)



class SiteConfig(models.Model):
    STATUS = (
        ('embed', 'Yayınla'),
        ('development', 'Yayından Kaldır'),
    )
    title =             models.CharField(max_length=50, verbose_name='Ayar İsmi')
    keywords =          models.CharField(blank=True, null=True, max_length=255) # TODO SEO 
    description =       models.CharField(blank=True, null=True, max_length=255)
    address =           models.TextField(blank=True, null=True, max_length=150)
    phone =             models.CharField(blank=True, null=True, max_length=150)
    fax =               models.CharField(blank=True, null=True, max_length=50)
    email =             models.CharField(blank=True, null=True, max_length=60)
    smtpserver =        models.CharField(blank=True, null=True, max_length=50)
    smtpemail =         models.CharField(blank=True, null=True, max_length=50)
    smtppassword =      models.CharField(blank=True, null=True, max_length=50)
    smtpport =          models.CharField(blank=True, null=True, max_length=9)
    logo =              models.ImageField(upload_to ='SiteIcon/%Y/%m/%d/', blank=True)
    facebook =          models.CharField(blank=True, null=True, max_length=255)
    instagram =         models.CharField(blank=True, null=True, max_length=255)
    twitter =           models.CharField(blank=True, null=True, max_length=255)
    aboutus =           RichTextField()
    status =            models.CharField(max_length=15, choices=STATUS) 
    created_time =      models.DateTimeField(auto_now_add=True) 
    update_time =       models.DateTimeField(auto_now=True) 


    def __str__(self):
        return self.title