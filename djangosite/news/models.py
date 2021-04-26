from django.db import models
from django.urls import reverse

# Create your models here.



class News(models.Model):
    # id automatic
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name='Content')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null= True, verbose_name='Photo')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')
    views = models.IntegerField(default=0)
    # related_name='get_news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('view_news', kwargs={"news_id": self.pk})
        return reverse('view_news', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Category')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Category'
        ordering = ['title']
