from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

# Create your models here.
def upload_location(instance, filename):
	return "%s%s"%(instance.id, filename)

class Movie(models.Model):
	title = models.CharField(max_length=50)
	preview = models.ImageField(
		upload_to = upload_location, 
		null=True, 
		blank=True,
		width_field="width_field",
		height_field="height_field"
		)

	height_field = models.PositiveIntegerField(default=0)
	width_field = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		time= timezone.now().date()
		return reverse("movie", kwargs={'id': self.id})

class MoviePricing(models.Model):
	movie = models.ManyToManyField(Movie)
	starting_time = models.TimeField()
	student_fee = models.PositiveIntegerField(null=True, blank=True)
	regular_fee = models.PositiveIntegerField()
	def __unicode__(self):
		fee =  " Student fee: " + str(self.student_fee) if self.student_fee != None else ""
		return str(self.starting_time)  + fee + " Regular fee: " + str(self.regular_fee)

class MovieViewing(models.Model):
	movie = models.OneToOneField(
		'Movie',
		on_delete=models.CASCADE,
		)
	movie_preview_video = models.URLField()
	movie_preview_poster = models.FileField(upload_to=upload_location)

	def __unicode__(self):
		return str(self.movie)
		
class CinemaSeat(models.Model):
	seat = models.CharField(max_length=3)
	
	def __unicode__(self):
		return str(self.seat)
	
		
class Ticket(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		null=True
		)
	movie = models.ForeignKey(
		'Movie',
		on_delete=models.CASCADE,
		null=True
		)
	date = models.DateField(default=timezone.now())
	seat = models.ManyToManyField(CinemaSeat)
	number_of_regular_tickets = models.PositiveIntegerField(default=0)
	number_of_student_tickets = models.PositiveIntegerField(default=0)
	pricing = models.ForeignKey(
		'MoviePricing',
		on_delete=models.CASCADE,
		null=True
		)
	total_payment = models.PositiveIntegerField(default=0)
	def __unicode__(self):
		return str(self.user) + ': ' + str(self.movie) 
		