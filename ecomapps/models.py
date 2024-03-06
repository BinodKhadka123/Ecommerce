from django.db import models 

class ProductManager(models.Manager):
    def filter_by_category_name(self, category_name):
        return self.get_queryset().filter(category__name=category_name)

    def get_queryset(self):
        return super().get_queryset().filter(price__gt=2000)


class Category(models.Model):
    name=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='static/img')
    model_name=models.CharField(max_length=100,default='Mobile is a new Technology')
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    description=models.TextField()
    stock=models.IntegerField()
    qty=models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    custom_objects = ProductManager()
    def __str__(self):
        return self.name

    




class Address(models.Model):
    city=models.CharField(max_length=20)
    street=models.CharField(max_length=20)
    nearest_landmark=models.TextField()


class Cart(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)

    order_ref=models.IntegerField()
    quantity=models.IntegerField()
    subtotal=models.IntegerField()
    created_at=models.DateField()

class Finorder(models.Model):
    address_id=models.ForeignKey(Address, on_delete=models.CASCADE)
    order_item=models.ForeignKey(Cart, on_delete=models.CASCADE)
    
    

class Payment(models.Model):
    payment_method=models.IntegerField()
    Amount=models.IntegerField()
class Shipment(models.Model):
    shipment_date=models.DateTimeField()
    address_id=models.ForeignKey(Address, on_delete=models.CASCADE)

class Customer (models.Model):
   
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    address=models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Review(models.Model):
    user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
    prodct_id=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
class Discount(models.Model):
    name=models.CharField(max_length=20)
    d_percentage=models.IntegerField()
    status=models.CharField(max_length=20)

    
    


    
   

    

    

