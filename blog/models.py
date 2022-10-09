from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField('نام', max_length=24)
    image = models.ImageField('عکس', upload_to='media/category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Tag(models.Model):
    name = models.CharField('تگ', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Post(models.Model):
    STATUS_CHOICE = (
        ('0', 'در انتظار'),
        ('1', 'منتشر شده')
    )
    title = models.CharField('عنوان', max_length=256)
    cover = models.ImageField('کاور', upload_to='media/post/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    description = models.TextField('متن', blank=True, null=True)
    visit = models.PositiveIntegerField('بازدید ها', default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField()
    status = models.CharField('وضعیت', choices=STATUS_CHOICE, default='0', max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    tag = models.ManyToManyField(Tag, verbose_name='تگ')

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
