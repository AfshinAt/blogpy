from django.db import models


class Contact(models.Model):
    full_name = models.CharField('نام و نام خانوادگی', max_length=128)
    phone = models.CharField('شماره تماس', max_length=11, null=True, blank=True)
    email = models.EmailField('ایمیل', null=True, blank=True)
    description = models.TextField('توضیحات')
    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'

    def __str__(self):
        return self.full_name