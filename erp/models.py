from django.db import models
from django.utils.translation import gettext as _


class SoftDeleteQueryset(models.QuerySet):
    """
    Prevents objects from being hard-deleted. Instead, sets the
    ``date_deleted``, effectively soft-deleting the object.
    """

    # def delete(self):
    #     for obj in self:
    #         obj.deleted_at = timezone.now()
    #         obj.deleted = True
    #         obj.save()


class SoftDeleteManager(models.Manager):
    """
    Only exposes objects that have NOT been soft-deleted.
    """

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(deleted=False)


class SoftDeleteModel(models.Model):
    class Meta:
        abstract = True

    deleted = models.BooleanField(db_index=True, default=False, verbose_name=_('Deleted'))
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name=_('Deleted At'))

    objects = SoftDeleteManager()
    original_objects = models.Manager()

    # def delete(self, using=None, keep_parents=False):
    #     self.deleted = True
    #     self.deleted_at = timezone.now()
    #     self.save()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
