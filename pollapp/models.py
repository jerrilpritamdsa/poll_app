from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=20)
    option_two = models.CharField(max_length=20)
    option_three = models.CharField(max_length=20)
    count_one = models.IntegerField(default=0)
    count_two = models.IntegerField(default=0)
    count_three = models.IntegerField(default=0)
    
    def total(self):
        return self.count_one + self.count_two + self.count_three