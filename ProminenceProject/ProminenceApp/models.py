import datetime

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from djongo import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey


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


team_category = (
    ('1', 'lead'),
    ('2', 'current'),
    ('3', 'former')
)


class Team(models.Model):
    team_category = models.CharField(max_length=250, choices=team_category, verbose_name="Select Team Category")
    name = models.CharField(max_length=250, verbose_name="Enter Member's Name")
    designation = models.CharField(max_length=250, verbose_name="Member Designation")
    email = models.CharField(max_length=250, verbose_name="Member's Email", null=True, blank=True)
    facebook_link = models.CharField(max_length=250, verbose_name="Enter Member's facebook link", null=True, blank=True,
                                     help_text='You must input "http://" before insert your link')
    whatsapp_link = models.CharField(max_length=250, verbose_name="Enter Whatsapp number", null=True, blank=True)
    instagram_link = models.CharField(max_length=250, verbose_name="Enter instagram link", null=True, blank=True,
                                      help_text='You must input "http://" before insert your link')
    image = models.FileField(verbose_name="Team member image", upload_to='Team_image',
                             help_text="Only PNG, JPG, JPEG format supported",
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.name


class PackagesCategory(models.Model):
    category_name = models.CharField(max_length=250, verbose_name="Enter Category Name")
    category_photo = models.FileField(verbose_name="Home Background hero image", upload_to='Category_Image',
                                      help_text="Only PNG, JPG, JPEG format supported",
                                      validators=[FileExtensionValidator(
                                          allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = datetime.datetime.now()

    def __str__(self):
        return self.category_name


class SubPackagesCategory(models.Model):
    main_category = models.ForeignKey(PackagesCategory, verbose_name='Select Main Category',
                                      on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=250, verbose_name="Enter Category Name")
    sub_category_photo = models.FileField(verbose_name="Sub Category Image", upload_to='Sub_Category_Image',
                                          help_text="Only PNG, JPG, JPEG format supported",
                                          validators=[FileExtensionValidator(
                                              allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = datetime.datetime.now()

    def __str__(self):
        return self.sub_category_name


class Packages(models.Model):
    main_category = models.ForeignKey(PackagesCategory, on_delete=models.CASCADE,
                                      verbose_name="Select Packages Category")
    sub_category = ChainedForeignKey(SubPackagesCategory, verbose_name='Select Sub-Packages Category',
                                     chained_field="main_category", chained_model_field="main_category",
                                     auto_choose=True,
                                     show_all=False, null=True, blank=True)
    package_name = models.CharField(max_length=250, verbose_name="Enter package name")
    package_price = models.IntegerField(verbose_name="Package Price")
    package_details = RichTextField(verbose_name="Package Details")
    package_photo = models.FileField(verbose_name="Package Image", upload_to='Package_Image',
                                     help_text="Only PNG, JPG, JPEG format supported",
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = datetime.datetime.now()

    def __str__(self):
        return self.package_name


class Gallery(models.Model):
    _id = models.ObjectIdField()
    gallery_category = models.ForeignKey(PackagesCategory, verbose_name="Select Gallery Category",
                                         on_delete=models.DO_NOTHING)
    photo = models.FileField(verbose_name="Gallery Image", upload_to='Gallery_image',
                             help_text="Only PNG, JPG, JPEG format supported",
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.gallery_category.category_name
