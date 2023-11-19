from django.db import models
from django.contrib.auth.models import User

class Sentiment(models.Model):
    sentiment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sentiment}"


class Dweet(models.Model):
    user = models.ForeignKey(User,
                             related_name="dweets",
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    sentiment = models.ForeignKey(Sentiment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username
