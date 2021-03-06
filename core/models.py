# -*- coding: utf 8 -*-
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField

class Post(models.Model):
	titulo = models.CharField(max_length=200)
	apresentacao = models.TextField()
	imagem = CloudinaryField('imagem', null=False, blank=False)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(null=False, blank=False)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		#return reverse("detalhe", kwargs={"pk": self.pk})
		return "/post/%s" %(self.pk)