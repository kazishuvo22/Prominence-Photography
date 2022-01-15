import datetime

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

class General(models.Model):
    main_title = models.CharField(max_length=300, verbose_name="Main Title")
    advertise_title = models.CharField(max_length=300, verbose_name="Advertisement Title")
    short_about = models.TextField(max_length=300, verbose_name="Site Short About",
                                   help_text="Not more than 300 character")
    long_about = RichTextField(verbose_name="Site Long About")
    last_edited = datetime.datetime.now()
    terms = RichTextField(verbose_name="Enter terms and conditions")
    policy = RichTextField(verbose_name="Enter policy")
    image_field = models.FileField(verbose_name="Home Background hero image", upload_to='services_images',
                                   help_text="Only PNG, JPG, JPEG format supported",
                                   validators=[FileExtensionValidator(
                                       allowed_extensions=['png', 'jpg', 'jpeg'])])
    last_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=20, verbose_name="Company official Mobile/ Phone number")
    email = models.EmailField(verbose_name="Company official email")
    address = models.CharField(max_length=300, verbose_name="Full Address ")
    facebook_link = models.CharField(max_length=300, verbose_name="Facebook Link ",
                                     help_text="remove 'http://' before your web address, Example: example.com")
    whatsapp_link = models.CharField(max_length=300, verbose_name="Whatsapp Link/Mobile number")
    instagram_link = models.CharField(max_length=300, verbose_name="Instagram Link",
                                      help_text="remove 'http://' before your web address, Example: example.com")
    linkedin_link = models.CharField(max_length=300, verbose_name="Linkedin Link",
                                     help_text="remove 'http://' before your web address, Example: example.com")
    skype_link = models.CharField(max_length=300, verbose_name="Skype Link",
                                  help_text="remove 'http://' before your web address, Example: example.com")

    mode = models.CharField(max_length=100, verbose_name="Select Mode",
                            choices=(('1', 'production'), ('2', 'development')))

    def save(self, **kwargs):
        self.pk = self.id = 1
        if ('request') in kwargs and self.last_author is None:
            request = kwargs.pop('request')
            self.last_author = request.user
        super(General, self).save(**kwargs)

    def __str__(self):
        return self.main_title


class Team(models.Model):
    name = models.CharField(max_length=250, verbose_name="Enter Member's Name")
    designation = models.CharField(max_length=250, verbose_name="Member Designation")
    email = models.CharField(max_length=250, verbose_name="Member's Email")
    facebook_link = models.CharField(max_length=250, verbose_name="Enter Member's facebook link")
    whatsapp_link = models.CharField(max_length=250, verbose_name="Enter Whatsapp link")

    def __str__(self):
        return self.name


