from django.db import models

# Create your models here.

class UserRank(models.Model):
    """Model definition for UserRank."""

    # TODO: Define fields here
    rank = models.PositiveIntegerField(default=1)
    name = models.CharField(max_length=255, null=True, blank=True)
    user_url = models.CharField(max_length=255, null=True, blank=True)
    network = models.CharField(max_length=255, null=True, blank=True)
    last = models.CharField(max_length=255, null=True, blank=True)
    trades = models.CharField(max_length=255, null=True, blank=True)
    total_return = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        """Meta definition for UserRank."""

        verbose_name = 'UserRank'
        verbose_name_plural = 'UserRanks'

    def __str__(self):
        """Unicode representation of UserRank."""
        return self.name
