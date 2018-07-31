from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
	status = HTMLField()
	profilepicture = models.ImageField(upload_to='images/', blank=True,default="media/jVr43h8.png")

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
				Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Category(models.Model):
	name=models.CharField(max_length=60,default="")


class Project(models.Model):
	title=models.CharField(max_length=20)
	image=models.ImageField(upload_to='projects/', blank=True)
	detailed_description=models.TextField()
	repo_link=models.CharField(max_length=50)
	deployed_link=models.CharField(max_length=40)
	category=models.ForeignKey(Category,related_name='category',null=True, blank=True, on_delete=models.CASCADE)

