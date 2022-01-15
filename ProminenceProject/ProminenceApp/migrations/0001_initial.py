# Generated by Django 3.2.10 on 2022-01-15 07:23

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name="Enter Member's Name")),
                ('designation', models.CharField(max_length=250, verbose_name='Member Designation')),
                ('email', models.CharField(max_length=250, verbose_name="Member's Email")),
                ('facebook_link', models.CharField(max_length=250, verbose_name="Enter Member's facebook link")),
                ('whatsapp_link', models.CharField(max_length=250, verbose_name='Enter Whatsapp link')),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=300, verbose_name='Main Title')),
                ('advertise_title', models.CharField(max_length=300, verbose_name='Advertisement Title')),
                ('short_about', models.TextField(help_text='Not more than 300 character', max_length=300, verbose_name='Site Short About')),
                ('long_about', ckeditor.fields.RichTextField(verbose_name='Site Long About')),
                ('terms', ckeditor.fields.RichTextField(verbose_name='Enter terms and conditions')),
                ('policy', ckeditor.fields.RichTextField(verbose_name='Enter policy')),
                ('image_field', models.FileField(help_text='Only PNG, JPG, JPEG format supported', upload_to='services_images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])], verbose_name='Home Background hero image')),
                ('phone', models.CharField(max_length=20, verbose_name='Company official Mobile/ Phone number')),
                ('email', models.EmailField(max_length=254, verbose_name='Company official email')),
                ('address', models.CharField(max_length=300, verbose_name='Full Address ')),
                ('facebook_link', models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Facebook Link ')),
                ('whatsapp_link', models.CharField(max_length=300, verbose_name='Whatsapp Link/Mobile number')),
                ('instagram_link', models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Instagram Link')),
                ('linkedin_link', models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Linkedin Link')),
                ('skype_link', models.CharField(help_text="remove 'http://' before your web address, Example: example.com", max_length=300, verbose_name='Skype Link')),
                ('mode', models.CharField(choices=[('1', 'production'), ('2', 'development')], max_length=100, verbose_name='Select Mode')),
                ('last_author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]