from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(verbose_name="promotion name", 
                                   max_length=255)
    discount = models.FloatField()
        
class Collection(models.Model):
    title = models.CharField(verbose_name="collection name", 
                             max_length=255, 
                             null=False)
    
class Product(models.Model): 
    title = models.CharField(verbose_name="product title",
                             max_length=255,)
    
    description = models.TextField()
    
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    
    inventory = models.IntegerField()
    
    last_update = models.DateTimeField(auto_now=True)
    
    # If we delete the collection, then all of the products within 
    # that collection are also deleted    
    collection = models.ForeignKey(Collection,
                                   on_delete=models.CASCADE)
    promotions = models.ManyToManyField(Promotion)
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'b'
    MEMBERSHIP_SILVER = 's'
    MEMBERSHIP_GOLD = 'g'
    
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'bronze'),
        (MEMBERSHIP_SILVER,'silver'),
        (MEMBERSHIP_GOLD,'gold'),
    ]
    first_name = models.CharField(verbose_name="first name",
                                  max_length=255,)
    
    family_name = models.CharField(verbose_name="family name",
                                   max_length=255,)
    
    email = models.EmailField(verbose_name="email",
                              max_length=254,
                              unique=True)
    
    phone = models.CharField(verbose_name="Phone Number",
                             max_length=20)
    
    birth_date = models.DateField(verbose_name="date of birth",
                                  null=True)
    
    membership = models.CharField(verbose_name="membership level",
                                  max_length=1,
                                  choices=MEMBERSHIP_CHOICES,
                                  default=MEMBERSHIP_BRONZE)
    
class Order(models.Model):
    PAYMENT_PENDING = "p"
    PAYMENT_COMPLETE = "c"
    PAYMENT_FAILED = "f"
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_FAILED,"failed"),
        (PAYMENT_COMPLETE,"complete"),
        (PAYMENT_PENDING,"pending"),
        
    ]
    placed_at = models.DateTimeField(verbose_name="Time of order placement",
                                     auto_now_add=True,)
    
    payment_status = models.CharField(verbose_name="payment status",
                                      max_length=1,
                                      choices=PAYMENT_STATUS_CHOICES,
                                      default=PAYMENT_PENDING)
    
    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE)
    
class Address(models.Model):
    street = models.CharField(verbose_name="street address",
                              max_length=255)
    
    
    city = models.CharField(verbose_name="city",
                              max_length=255)
    
    # When we delete the customer, we delete the address also.
    customer = models.ForeignKey(Customer, 
                                 on_delete=models.CASCADE)

class Cart(models.Model):
    created = models.DateTimeField(verbose_name="cart creation date", 
                                   auto_now_add=True )
    
class Item(models.Model):
    cart = models.ForeignKey(Cart, 
                             on_delete=models.CASCADE)
    
    order = models.ForeignKey(Order,
                              on_delete=models.PROTECT)


