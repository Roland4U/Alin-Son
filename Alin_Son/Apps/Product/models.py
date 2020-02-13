from django.db import models
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + str(int(time()))

class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    img = models.ImageField(upload_to='media', null=False)
    banner = models.ImageField(upload_to='media', null=False)
    description = models.TextField()
    header = models.CharField(max_length=150, blank=True, null=True)
    sub_header = models.CharField(max_length=150, blank=True, null=True)
    available = models.BooleanField(default=True)
    available_qty = models.IntegerField()
    size = models.ForeignKey('FKNAME', on_delete=models.CASCADE)
    sold_qty = models.PositiveIntegerField()
    tags = models.ManyToManyField('Tag', related_name='product', blank=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model = models.ForeignKey("app.Model", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    mods = models.OneToOneField("app.Model", on_delete=models.SET_NULL)
    # parameters = models.OneToOneField("app.Model", on_delete=models.SET_NULL)
    seller = models.ForeignKey(
                                'User',
                                on_delete=models.CASCADE,
                                related_name='Seller',
                                limit_choices_to={'is_staff': True}
                              )
    pub_date = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse("product_det", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse("product_edit", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name)
        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Comment(models.Model):
    product = models.ForeignKey("Product.Product", on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    comment_text = models.TextField(db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    banner = models.ImageField(upload_to='media')

    def get_absolute_url(self):
        return reverse('product:category_det', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse("product:category_edit", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoryes'


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    country = models.CharField(max_length=50)
