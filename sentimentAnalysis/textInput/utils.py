from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Dweet, Sentiment

@receiver(post_save, sender=Dweet)
def analyze_sentiment(sender, instance, created, **kwargs):
    if created:
        # Perform sentiment analysis here and update instance.sentiment
        # sentiment = perform_sentiment_analysis(instance.body)
        sentiment = 'Not Analyzed'

        # Create or update Sentiment object
        sentiment_obj, created = Sentiment.objects.get_or_create(sentiment=sentiment)
        sentiment_obj.analyzed_at = timezone.now()
        sentiment_obj.save()

        # Link the sentiment to the Dweet
        instance.sentiment = sentiment_obj
        instance.save()