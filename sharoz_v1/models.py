from __future__ import unicode_literals
import math
from PIL import Image
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField('Description', null=True, blank=True)
    size = models.CharField(max_length=10)
    sex = models.CharField(max_length=10, default='F')
    price = models.FloatField('Price', default=0.0)
    link_to_buy = models.TextField('Link to buy', null=True, blank=True)
    created_at = models.DateTimeField('Created At')

    def __unicode__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField('Photo')
    photo_thumbnail = models.ImageField('Photo Thumbnail', blank=True, null=True)
    product = models.ForeignKey(Product, related_name='photos')
    color = models.ForeignKey(Color, related_name='photos')

    def __unicode__(self):
        return 'photo of product ' + str(self.product.name) + ' in color ' + str(self.color.name)

    def save(self):
        if not self.photo:
            return

        self.photo.name = self.photo.name[:-4] + ".jpg"
        self.photo_thumbnail = self.photo.name[:-4] + "_thumbnail.jpg"
        super(Photo, self).save()
        img = Image.open(self.photo)
        img = img.convert("RGB")
        width, height = img.size[0], img.size[1]
        aspect = 1.0 * height / width
        self.ratio = aspect
        "Max width and height 800"
        if (width < height):
            factor = 760.0 / width
            factor_t = 300.0 / width
        else:
            factor = 760.0 / height
            factor_t = 300.0 / height

        quality_val = 95
        if factor != 1.0:
            img1 = img.resize((int(math.ceil(width * factor)), int(math.ceil(height * factor))), Image.ANTIALIAS)
            img1.save(self.photo.path[:-4] + ".jpg", "JPEG", quality=90, optimize=True)
        # if self.photo.name.endswith(".png"):
        #   bg = Image.new("RGBA", img.size, (255, 255, 255))
        #  bg.paste(img)
        # img = bg

        img2 = img.resize((int(math.ceil(width * factor_t)), int(math.ceil(height * factor_t))), Image.ANTIALIAS)
        img2.save(self.photo.path[:-4] + "_thumbnail.jpg", "JPEG", quality=quality_val, optimize=True)
        self.photo_thumbnail = self.photo.name[:-4] + "_thumbnail.jpg"
        super(Photo, self).save()


class Suggestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __unicode__(self):
        return str(self.name) + ' ' + str(self.email)
