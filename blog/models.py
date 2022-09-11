from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 1000:
            return '"' + self.body[:100] + '..."'
        else:
            return '"' + self.body + '"'

    def pub_date_format(self):  # might not use but it's good to have options
        return self.pub_date.strftime('%b %e %Y')
