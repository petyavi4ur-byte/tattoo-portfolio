from django.db import models
from django.contrib.auth.models import User

class ArtistProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    base_rate = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def update_base_rate(self):
        calibrations = self.calibrations.all()
        if not calibrations:
            return 0
        rates = [work.calculate_wprk_rate() for work in calibrations]
        self.base_rate = round(sum(rates)/len(rates),2)
        self.save()
        return self.base_rate

    def __str__(self):
        return self.user.username


class TattooStyle(models.Model):
    name = models.CharField(max_length=100)
    complexity_factor = models.FloatField(default=1.0)

    def __str__(self):
        return self.name


class CalibrationWork(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE,
related_name='calibrations')
    style = models.ForeignKey(TattooStyle,on_delete=models.CASCADE,)
    width = models.FloatField(verbose_name="Ширина (см)")
    height = models.FloatField(verbose_name="Высота(см)")
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Цена за работу")

    def calculate_wprk_rate(self):
        area = self.width * self.height
        if area > 0:
            return float(self.price) / (area * self.style.complexity_factor)
        return 0


class Sketch(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE,related_name='sketches')
    style = models.ForeignKey(TattooStyle,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Название эскиза")
    image = models.ImageField(upload_to='sketches/',verbose_name="Изображение")
    detail_modifier = models.FloatField(default=1.0,verbose_name="Множитель детализации")

    def calculate_price(self,width,height):
        area = width* height
        artist_rate = float(self.artist.base_rate)
        total = area * artist_rate * self.style.complexity_factor * self.detail_modifier
        return round(total,2)
    def __str__(self):
        return f"{self.title} ({self.artist.user.username})"