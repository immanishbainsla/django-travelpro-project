from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class UserProfile(models.Model):
    # Extending default User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional fields to the default User model
    # using pillow module for images
    profile_pic = models.ImageField(upload_to='accounts/profile_pics', blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    current_address = models.TextField(blank=False, help_text='Enter your Home Address Here.')
    parmanent_address = models.TextField(blank=True, null=True, help_text='Enter Where are you travelling?')
    travel_reason = models.CharField(blank=True, null=True, help_text='eg. Solo Trip!', max_length=100)
    age = models.PositiveIntegerField(default=20, blank=False)
    portfolio_site = models.URLField(blank=True, default='https://www.example.com')

    # def get_absolute_url(self):
    #     return reverse('home', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-slug']


# Contact Model
class ContactModel(models.Model):
    name = models.CharField(max_length=255, blank=False, help_text='Enter your Name here.')
    email = models.EmailField(blank=False, help_text='Enter your Email here.')
    query = models.TextField(blank=False, help_text='Describe your Query here.')

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('index')
