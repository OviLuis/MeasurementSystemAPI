from django.db import models


class Measure(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="UUID")
    device_id = models.IntegerField(verbose_name='ID Dispositivo')
    measure_value = models.DecimalField(verbose_name='Medida', decimal_places=2, max_digits=5)
    measure_unit = models.CharField(verbose_name='Unidad de medida', max_length=10)
    measure_date = models.DateTimeField(verbose_name='Fecha de la medida', editable=False, auto_now_add=True)

    def __str__(self):
        return '%d' % self.id

    class Meta:
        managed = True
        db_table = 'measure'
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'
