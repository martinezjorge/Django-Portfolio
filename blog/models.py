from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    post = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')

    # this function posts the title in the admin page
    def __str__(self):
        return self.title

    # this limits the number of characters that show from a post
    def summary(self):
        return self.post[:100]

    # show the date but not the time
    def date_pretty(self):
        return self.date.strftime('%b %e %Y')