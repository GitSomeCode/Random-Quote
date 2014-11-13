from django.db import models

# Create your models here.
class SingleQuote(models.Model):
  quote_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField(auto_now_add = True)
  
  def __str__(self):
    return self.quote_text