from django.db import models

class Livebroadcast(models.Model):
    country=models.CharField(max_length=20)
    streamer=models.CharField(max_length=15)
    area=models.CharField(max_length=50,blank=True)

    def __unicode__(self):
        return self.country

class Trip(models.Model):
    country=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=10,decimal_places=0)
    comment = models.CharField(max_length=50,blank=True)
    hotel=models.BooleanField(default=False)
    livebroadcast=models.ForeignKey('Livebroadcast',on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.country

    class Meta:
        ordering=['price']

# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=255)
    user=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    date_time=models.DateTimeField()
    livebroadcast=models.ForeignKey('Livebroadcast',on_delete=models.CASCADE,)
    class Meta:
        ordering=['date_time']
        permissions=(
            ("can_comment","Can comments"),
            # 只有一權限時,千萬不要忘了逗號!
                    )