from django.db import models

# Create your models here.


COMMANDS_CHOICES = [
    ("ON", "Включить"),
    ("OFF", "Выключить")
] 

class LedCommand(models.Model):
    command_esp = models.CharField(verbose_name="Команда", max_length=10, choices=COMMANDS_CHOICES)
    date =  models.DateTimeField(verbose_name="время/дата", auto_now_add=True)


    class Meta:
        verbose_name = "Команда LED"
        verbose_name_plural = "Команды LED"

    def __str__(self):
        return f"{self.command_esp} — {self.date}"