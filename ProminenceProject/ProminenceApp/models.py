from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from djongo import models

# Create your models here.
from smart_selects.db_fields import ChainedForeignKey
from tinymce.models import HTMLField
from io import BytesIO  # basic input/output operation
from PIL import Image  # Imported to compress images
from django.core.files import File  # to store files


# image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=50)
    new_image = File(im_io, name=image.name)
    return new_image


class General(models.Model):
    main_title = models.CharField(max_length=300, verbose_name="Main Title")
    advertise_title = models.CharField(max_length=300, verbose_name="Advertisement Title")
    terms = HTMLField(verbose_name="Enter terms and conditions")
    hero_image_field = models.FileField(verbose_name="Home Background hero image", upload_to='Homepage_images',
                                        help_text="Only PNG, JPG, JPEG format supported",
                                        validators=[FileExtensionValidator(
                                            allowed_extensions=['png', 'jpg', 'jpeg'])])
    last_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    policy = HTMLField(verbose_name="Enter policy")
    home_video_link = models.CharField(max_length=250, verbose_name="Enter youtube link for home video",
                                       help_text="Add 'http:// or https://' before your web address if not inserted, "
                                                 "Example:(http://example.com)")
    phone = models.CharField(max_length=20, verbose_name="Company official Mobile/ Phone number")
    email = models.EmailField(verbose_name="Company official email")
    address = models.CharField(max_length=300, verbose_name="Full Address ")
    facebook_link = models.CharField(max_length=300, verbose_name="Facebook Link ",
                                     help_text="Add 'http:// or https://' before your web address if not inserted, "
                                               "Example:(http://example.com)")
    whatsapp_link = models.CharField(max_length=300, verbose_name="Whatsapp Link/Mobile number")
    instagram_link = models.CharField(max_length=300, verbose_name="Instagram Link",
                                      help_text="Add 'http:// or https://' before your web address if not inserted, "
                                                "Example:(http://example.com)")
    linkedin_link = models.CharField(max_length=300, verbose_name="Linkedin Link",
                                     help_text="Add 'http:// or https://' before your web address if not inserted, "
                                               "Example:(http://example.com)")
    youtube_link = models.CharField(max_length=300, verbose_name="Youtube Link",
                                    help_text="Add 'http:// or https://' before your web address if not inserted, "
                                              "Example:(http://example.com)")

    mode = models.CharField(max_length=100, verbose_name="Select Mode",
                            choices=(('1', 'production'), ('2', 'development')))
    last_edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        if ('request') in kwargs and self.last_author is None:
            request = kwargs.pop('request')
            self.last_author = request.user
        new_image = compress(self.hero_image_field)
        self.hero_image_field = new_image
        super(General, self).save(*args, **kwargs)

    def __str__(self):
        return self.main_title


class About(models.Model):
    short_about = models.TextField(max_length=300, verbose_name="Site Short About",
                                   help_text="Not more than 300 character")
    happy_clients = models.IntegerField(verbose_name="Enter Happy clients Count", blank=True, null=True)
    years_of_experience = models.IntegerField(verbose_name="Enter the company work of experiences", blank=True,
                                              null=True)
    about_body_image = models.FileField(verbose_name="About section body image", upload_to='About_image',
                                        help_text="Only PNG, JPG, JPEG format supported",
                                        validators=[FileExtensionValidator(
                                            allowed_extensions=['png', 'jpg', 'jpeg'])])
    last_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    long_about = HTMLField(verbose_name="Site Long About", null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        if ('request') in kwargs and self.last_author is None:
            request = kwargs.pop('request')
            self.last_author = request.user
        new_image = compress(self.about_body_image)
        self.about_body_image = new_image
        super(About, self).save(*args, **kwargs)

    def __str__(self):
        return self.short_about


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
                                     help_text="Add 'http:// or https://' before your web address if not inserted, "
                                               "Example:(http://example.com)")
    whatsapp_link = models.CharField(max_length=250, verbose_name="Enter Whatsapp number", null=True, blank=True)
    instagram_link = models.CharField(max_length=250, verbose_name="Enter instagram link", null=True, blank=True,
                                      help_text="Add 'http:// or https://' before your web address if not inserted, "
                                                "Example:(http://example.com)")
    image = models.FileField(verbose_name="Team member image", upload_to='Team_image',
                             help_text="Only PNG, JPG, JPEG format supported",
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PackagesCategory(models.Model):
    category_name = models.CharField(max_length=250, verbose_name="Enter Category Name")
    category_photo = models.FileField(verbose_name="Home Background hero image", upload_to='Category_Image',
                                      help_text="Only PNG, JPG, JPEG format supported",
                                      validators=[FileExtensionValidator(
                                          allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = models.DateTimeField(auto_now=True)

    # calling image compression function before saving the data
    def save(self, *args, **kwargs):
        new_image = compress(self.category_photo)
        self.category_photo = new_image
        super().save(*args, **kwargs)

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
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.sub_category_photo)
        self.sub_category_photo = new_image
        super().save(*args, **kwargs)

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
    package_details = HTMLField()
    package_photo = models.FileField(verbose_name="Package Image", upload_to='Package_Image',
                                     help_text="Only PNG, JPG, JPEG format supported",
                                     validators=[FileExtensionValidator(
                                         allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.package_photo)
        self.package_photo = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.package_name


class Gallery(models.Model):
    _id = models.ObjectIdField()

    # def number():
    #     no = Gallery.objects.count()
    #     if no is None:
    #         return 1
    #     else:
    #         return no + 1
    #
    # image_no = models.CharField(max_length=250, unique=True, default=number, editable=False,
    #                             verbose_name="")
    gallery_category = models.ForeignKey(PackagesCategory, verbose_name="Select Gallery Category",
                                         on_delete=models.CASCADE)
    photo = models.FileField(verbose_name="Gallery Image", upload_to='Gallery_image',
                             help_text="Only PNG, JPG, JPEG format supported",
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['png', 'jpg', 'jpeg'])])
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.photo)
        self.photo = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.gallery_category.category_name


class Contact(models.Model):
    name = models.CharField(max_length=250, verbose_name="Customer Name")
    phone = models.CharField(max_length=250, verbose_name="Customer Phone")
    subject = models.CharField(max_length=250)
    message = models.TextField()
    message_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250)

    def __str__(self):
        return self.name
