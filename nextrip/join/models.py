from django.db import models

class Join(models.Model):
	email = models.EmailField(max_length=250)
	full_name = models.CharField(max_length=250, null=True, blank=True)
	zip_code = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.email
