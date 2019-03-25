from django.db import models

class Brexit(models.Model):
	brexit_endTimeEU = models.CharField(max_length=300)
	brexit_timeTillEnd = models.CharField(max_length=300)

	def _str_(self):
		return self.brexit_endTimeEU

	def _str_(self):
		return self.brexit_timeTillEnd