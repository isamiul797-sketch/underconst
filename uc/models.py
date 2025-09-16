from django.db import models

# Create your models here.
class UnderConstruction(models.Model):
    is_under_construction = models.BooleanField(default=False)
    uc_note = models.TextField(
        blank=True, null=True, help_text="Note for under construction mode" 
    )
    uc_duration = models.DateTimeField(
        blank=True, null=True, help_text="End date and time for under construction mode" 
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Under Construction:{self.is_under_construction}"
