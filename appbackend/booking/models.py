from django.db import models
# Create your models here.
class Booking(models.Model):

    username = models.CharField(max_length=256)
    moviename = models.CharField(max_length=25)
    screenname = models.CharField(max_length=25)
    eventname = models.CharField(max_length=25)
    timing = models.CharField(max_length=25)
    seatclass = models.CharField(max_length=5)
    showtime = models.CharField(max_length=25)
    timestamp = models.TimeField(auto_now_add=True)
    seat = models.IntegerField(default=10)
    cost = models.IntegerField(default=10)
    eventtype = models.CharField(max_length=25)

# ("id","username","salad","buns","slices","cutlets","cost","timestamp")

    # class Meta:
    #     ordering = ('timestamp', )

    def __str__(self):
        return str(self.id) + " --- " + self.username




