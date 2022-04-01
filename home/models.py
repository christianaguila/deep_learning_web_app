from django.db import models

# Create your models here.
class Plantsgallery(models.Model):
    class Meta:
        verbose_name_plural = "Plant Galleries"

    title = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200, default='')
    slug = models.SlugField(unique=True)
    plant_image = models.ImageField(upload_to='gallery image', default=None)
    pronounciation = models.TextField(default='-')

    botany = models.TextField(default='-')

    common_philippine_name1 = models.CharField(max_length=200, default='', blank=True)
    common_philippine_name2 = models.CharField(max_length=200, default='', blank=True)
    common_philippine_name3 = models.CharField(max_length=200, default='', blank=True)

    common_foreign_name1 = models.CharField(max_length=200, default='', blank=True)
    common_foreign_name2 = models.CharField(max_length=200, default='', blank=True)
    common_foreign_name3 = models.CharField(max_length=200, default='', blank=True)

    sci_philippine_name1 = models.CharField(max_length=200, default='', blank=True)
    sci_philippine_name2 = models.CharField(max_length=200, default='', blank=True)
    sci_philippine_name3 = models.CharField(max_length=200, default='', blank=True)
    
    sci_foreign_name1 = models.CharField(max_length=200, default='', blank=True)
    sci_foreign_name2 = models.CharField(max_length=200, default='', blank=True)
    sci_foreign_name3 = models.CharField(max_length=200, default='', blank=True)

    distribution = models.CharField(max_length=200, default='', blank=True)

    conservation_status = models.TextField(default='-')

    use_1 = models.TextField(default='-')
    use_2 = models.TextField(default='', blank=True)
    use_3 = models.TextField(default='', blank=True)

    scientific_studies1 = models.TextField(default='-')
    scientific_study_link1 = models.TextField(default='', blank=True)

    scientific_studies2 = models.TextField(default='', blank=True)
    scientific_study_link2 = models.TextField(default='', blank=True)

    scientific_studies3 = models.TextField(default='', blank=True)
    scientific_study_link3 = models.TextField(default='', blank=True)

    light_preference = models.TextField(default='', blank=True)
    water_preference = models.TextField(default='', blank=True)
    propagation_method = models.TextField(default='', blank=True)
    references = models.TextField(default='', blank=True)

    gallery_slider_1_image1 = models.ImageField(upload_to='gallery image', default='-')
    gallery_slider_1_image2 = models.ImageField(upload_to='gallery image', default='-')
    gallery_slider_1_image3 = models.ImageField(upload_to='gallery image', default='-')

    gallery_slider_2_image1 = models.ImageField(upload_to='gallery image', default='-')
    gallery_slider_2_image2 = models.ImageField(upload_to='gallery image', default='-')
    gallery_slider_2_image3 = models.ImageField(upload_to='gallery image', default='-')

    ar_link = models.TextField(default='', blank=True)

    def __str__(self):
            return f'{self.title}, {self.slug}'



