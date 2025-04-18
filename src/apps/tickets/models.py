from django.db import models



class PopularDestination(models.Model):
    # airport = models.BooleanField(default=False, verbose_name="Пункт является аэропортом")
    # own_route = models.BooleanField(default=False, verbose_name="Oбслуживает пункт собственные маршруты")
    # interline_route = models.BooleanField(default=False, verbose_name="Часть межлинейных маршрутов")
    # popular = models.BooleanField(default=False, verbose_name="Популярный пункт")
    # country_code = models.CharField(max_length=10, verbose_name="Код страны")
    place_image = models.ImageField(upload_to='flight/popular/destination/%Y/%m/%d/')
    point_code = models.CharField(max_length=50, verbose_name="Код пункта", help_text="Пример: FRU(Manas)")
    point_name = models.CharField(max_length=100, verbose_name="Название пункта")
    country_name = models.CharField(max_length=100, verbose_name="Название страны", help_text="Пример: Кыргызстан")

    def __str__(self):
        return f"Страна: {self.country_name} ➤➤➤➤ Г: {self.point_name}"
    
    class Meta:
        verbose_name = "Популярное направление"
        verbose_name_plural = "Популярные направления"
        ordering = ['id']
