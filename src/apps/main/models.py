from django.db import models
from django.utils.translation import gettext_lazy as _


class FAQ(models.Model):

    question = models.CharField(_("Вопрос"), max_length=255)
    answer = models.TextField(_("Ответ"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Часто задаваемый вопрос")
        verbose_name_plural = _("Часто задаваемые вопросы")

    def __str__(self):
        return self.question[::20]


class TechSupportFeedback(models.Model):

    email = models.EmailField(_("E-mail"))
    phone = models.CharField(_("Номер телефона"))
    ReasonDesc = models.TextField(_("Причина"))
    img = models.ImageField(upload_to='feedback/reason/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _("Запрос в техническую поддержку")
        verbose_name_plural = _("Запросы в техническую поддержку")
    
    # def __str__(self):


class Notification(models.Model):
    title = models.CharField(_('Уведомление'), max_length=1000)
    description = models.TextField(_("Описание"), blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    
    # sendtoall = models.BooleanField(default=True, verbose_name=_("Отправить всем"))
    # user_id = models.ManyToManyField(
    #     "DeviceToken",
    #     blank=True,
    #     verbose_name=_("Кому отправить?"),
    #     help_text="**Если хотите уведомить всех, оставьте это поле пустым**"
    # )
    # big_img = models.ImageField(
    #     _("Оболожка"),
    #     upload_to='notifications/%Y_%m',
    #     null=True, 
    #     blank=True,
    #     help_text="Большое фото товара для магазина, обложка новости, рекламный баннер или иллюстрация к событию."
    # )
    # large_img = models.ImageField(
    #     _("Значок акции"),
    #     upload_to='notifications/%Y_%m',
    #     null=True, 
    #     blank=True,
    #     help_text="Тематическая иконка, связанная с содержимым уведомления (например, значок акции или события)."
    # )

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Уведомление')
        verbose_name_plural = ('Уведомления')