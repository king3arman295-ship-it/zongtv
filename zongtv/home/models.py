from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Channel(models.Model):

    CHANNEL_TYPES = (
        ('news', 'News'),
        ('entertainment', 'Entertainment'),
    )

    name = models.CharField(max_length=100)

    logo = models.ImageField(
        upload_to='channels/'
    )

    stream_url = models.URLField(blank=True, null=True)

    live_video = models.FileField(
        upload_to='channel_videos/',
        blank=True,
        null=True
    )

    channel_type = models.CharField(
        max_length=20,
        choices=CHANNEL_TYPES
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Show(models.Model):

    title = models.CharField(
        max_length=200
    )

    poster = models.ImageField(
        upload_to='shows/'
    )

    banner = models.ImageField(
        upload_to='show_banners/'
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Video(models.Model):

    title = models.CharField(
        max_length=200
    )

    thumbnail = models.ImageField(
        upload_to='thumbnails/'
    )

    video_file = models.FileField(
        upload_to='videos/'
    )

    description = models.TextField(
        blank=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='videos',
        null=True,
        blank=True
    )

    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
        related_name='episodes',
        null=True,
        blank=True
    )

    episode_number = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Banner(models.Model):

    title = models.CharField(
        max_length=200
    )

    image = models.ImageField(
        upload_to='banners/'
    )

    show = models.ForeignKey(
        Show,
        on_delete=models.CASCADE,
        related_name='homepage_banners',
        null=True,
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title