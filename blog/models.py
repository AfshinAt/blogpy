from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('نام', max_length=24)
    image = models.ImageField('عکس', upload_to='media/category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'دسته بندی'
        verbose_name_plural= 'دسته بندی ها'


class Post(models.Model):
    STATUS_CHOICE = (
        ('0','در انتظار'),
        ('1','منتشر شده')
    )
    title = models.CharField('عنوان',max_length=256)
    cover = models.ImageField('کاور',upload_to='media/post/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    description = models.TextField('متن')
    visit = models.PositiveIntegerField('بازدید ها',default=0)
    created_at = models.DateTimeField(auto_now=True)
    status = models.CharField('وضعیت',choices=STATUS_CHOICE, default='0', max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= 'پست'
        verbose_name_plural= 'پست ها'