from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ManyToManyField(Seller)

    def __str__(self):
        return self.name




# from django.db import connection
# connection.queries
# Product.objects.filter(price__gte=100).values('name')
# Product.objects.filter(price__gte=100).exists()
# Product.objects.filter(name__contains='be').exists()
# Product.objects.first()
# Product.objects.prefetch_related('seller').all() Таким образом мы получаем все объекты Product, связанные с Seller
from django.db.models import Q
# Product.objects.filter(~Q(price=150)&Q(name__contains='sony'))
# Product.objects.filter(~Q(price=150)|Q(name__contains='sony'))
from django.db.models import Sum, Avg, Min
# Product.objects.all().aggregate(Sum('price'))
# Product.objects.all().agregate(total=Sum('price'))
# Product.objects.all().count()
# Product.objects.order_by('-price')
# Product.objects.all().reverse()
# beef = Product.objects.get(pr=1)
# beef.category_id