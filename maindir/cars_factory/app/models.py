from django.db import models
from django.db.models import Sum, F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class DetailType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды запчастей"
        ordering = ['name']

    def __str__(self):
        return self.name


class Detail(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('DetailType', null=True, on_delete=models.PROTECT)
    price = models.IntegerField(default=0)

    def get_properties_and_values(self):
        return DetailTypePropertyValue.objects.filter(detail=self).select_related('property')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Деталь"
        verbose_name_plural = "Детали"
        ordering = ['type']


class CarDetail(models.Model):
    detail = models.ForeignKey('Detail', on_delete=models.CASCADE, null=False)
    count = models.IntegerField(default=1)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.car.name + " " + self.detail.name

    class Meta:
        verbose_name = "Запчасть"
        verbose_name_plural = "Автозапчасти"
        ordering = ['car']


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    manufacturer_margin = models.IntegerField(default=0)  # Наценка производителя

    def __str__(self):
        return self.name

    @receiver(post_save, sender=Detail)
    def update_car_price_if_detail_created_or_edited(sender, instance, created, **kwargs):
        """Update car price if factory detail was created/changed"""
        Car.bulk_price_update()

    @receiver(post_delete, sender=Detail)
    def update_car_price_if_detail_deleted(sender, instance, **kwargs):
        """Update car price if factory detail was deleted"""
        Car.bulk_price_update()

    @staticmethod
    def bulk_price_update():
        """Update price of all cars"""
        cars = Car.objects.all()
        for car in cars:
            car.price = CarDetail.objects.filter(car=car).aggregate(s=Sum(F('detail__price')*F('count') ) )['s']
        Car.objects.bulk_update(cars, ['price'])

    def get_details(self):
        """Return all car's details"""
        return CarDetail.objects.filter(car=self).select_related('detail', 'detail__type', 'detail__type')

    def update_instance_price(self):
        """Updates car price"""
        self.price = CarDetail.objects.filter(car=self).aggregate(s=Sum(F('detail__price')*F('count') ) )['s']
        self.save()

    @receiver(post_save, sender=CarDetail)
    def update_car_price_if_car_detail_created(sender, instance, created, **kwargs):
        """Update car price if factory detail was added to car's details """
        instance.car.update_instance_price()

    @receiver(post_delete, sender=CarDetail)
    def update_car_price_if_car_detail_deleted(sender, instance, **kwargs):
        """Update car price if factory detail was deleted from car's details """
        instance.car.update_instance_price()

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ['price']


class DetailTypeProperty(models.Model):
    type = models.ForeignKey('DetailType', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name + " " + self.type.name

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики деталей"
        ordering = ['type']


class DetailTypePropertyValue(models.Model):
    value = models.CharField(max_length=255)
    property = models.ForeignKey('DetailTypeProperty', on_delete=models.CASCADE, null=True)
    detail = models.ForeignKey('Detail', on_delete=models.CASCADE)

    def __str__(self):
        return self.property.name + " " + self.value

    class Meta:
        verbose_name = "Значение"
        verbose_name_plural = "Значение характеристик деталей"
        ordering = ['detail']