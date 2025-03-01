from django.db import models



class PopularDestination(models.Model):
    point_code = models.CharField(max_length=50, verbose_name="Код пункта", help_text="Пример: FRU(Manas)")
    point_name = models.CharField(max_length=100, verbose_name="Название пункта")
    point_name_ru = models.CharField(max_length=100, verbose_name="Название пункта(RU)")
    city_code = models.CharField(max_length=50, verbose_name="Код города", help_text="Пример: FRU")
    city_name = models.CharField(max_length=100, verbose_name="Название города", help_text="Пример: Bishkek")
    city_name_ru = models.CharField(max_length=100, verbose_name="Название города(RU)", help_text="Пример: Бишкек")
    airport = models.BooleanField(default=False, verbose_name="Пункт является аэропортом")
    own_route = models.BooleanField(default=False, verbose_name="Oбслуживает пункт собственные маршруты")
    interline_route = models.BooleanField(default=False, verbose_name="Часть межлинейных маршрутов")
    popular = models.BooleanField(default=False, verbose_name="Популярный пункт")
    country_code = models.CharField(max_length=10, verbose_name="Код страны")
    place_image = models.ImageField(upload_to='flight/popular/destination/%Y/%m/%d/')

    def __str__(self):
        return f"Пункт: {self.point_name_ru} ➤➤➤➤ Г: {self.city_name_ru}"
    
    class Meta:
        verbose_name = "Популярное направление"
        verbose_name_plural = "Популярные направления"
        ordering = ['id']