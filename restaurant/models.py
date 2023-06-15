from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField(db_index=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
