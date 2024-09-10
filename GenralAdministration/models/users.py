from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Mannegare(AbstractUser):
    """

    Note:
    This model is responsible for creating and managing 'Managers'.
    Please be cautious when making changes to this model to avoid affecting manager functionality.

    """

    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=250, unique=True, null=False, blank=False)

    groups = models.ManyToManyField(
        Group,
        related_name="mannegare_set",
        blank=True,
        related_query_name="mannegare",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="mannegare_permissions",
        blank=True,
        related_query_name="mannegare",
    )

    class Meta:
        verbose_name = "Mannegare"
        verbose_name_plural = "Mannegares"

    def __str__(self):
        return self.username


class ActivityLog(models.Model):
    """
    This model tracks changes made by managers, including:
    - manager: ForeignKey to the 'Mannegare' model, representing the manager who performed the action.
    - action: Type of action performed (e.g., 'Created', 'Updated').
    - model_name: Name of the model on which the action was performed.
    - object_id: ID of the object that was affected by the action.
    - timestamp: Date and time when the action was performed.

    """

    manager = models.ForeignKey(Mannegare, on_delete=models.PROTECT)
    action = models.CharField(max_length=20)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Activity Log"
        verbose_name_plural = "Activity Logs"

    def __str__(self):
        return f"{self.manager.username} - {self.action} on {self.model_name}"


@receiver(post_save, sender=Mannegare)
def log_activity_on_save(sender, instance, created, **kwargs):
    """
    Signal receiver function to log activity when a 'Mannegare' instance is saved.

    This function is triggered after a 'Mannegare' instance is created or updated. It logs the action performed
    (either 'Created' or 'Updated') along with the relevant details to the 'ActivityLog' model.

    """

    if created:
        action = "Created"
    else:
        action = "Updated"

    ActivityLog.objects.create(
        manager=instance,
        action=action,
        model_name=sender.__name__,
        object_id=instance.pk,
    )


@receiver(post_delete, sender=Mannegare)
def log_activity_on_delete(sender, instance, **kwargs):
    """
    Signal receiver function to log activity when a 'Mannegare' instance is deleted.

    This function is triggered after a 'Mannegare' instance is deleted. It logs the deletion action
    along with relevant details to the 'ActivityLog' model.

    """

    ActivityLog.objects.create(
        manager=instance,
        action="Deleted",
        model_name=sender.__name__,
        object_id=instance.pk,
    )
