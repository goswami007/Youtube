from django.db import models

class Youtube(models.Model):
	def __str__(self):
		return self.video_name
	
	video_url = models.URLField()
	video_id = models.CharField(max_length=15, default=None)
	video_name = models.CharField(max_length=80)
	original_file = models.FileField(upload_to='audio/')
	transposed_file = models.FileField(upload_to='shifted_audio/')