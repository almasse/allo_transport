from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from django.conf import settings


class HomePage(Page):
    api_fields = ['partners']

    content_panels = Page.content_panels + [
        InlinePanel('partners', label="Partenaires"),
    ]
    
class Partner(Orderable):
    page = ParentalKey(HomePage, related_name='partners')
    url = models.CharField(max_length=255)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['url', 'photo', 'photo_url']

    panels = [
        FieldPanel('url'),
        FieldPanel('photo'),
    ]

    @property
    def photo_url(self):
        if self.photo:
            return settings.MEDIA_URL + 'original_images/' + self.photo.filename
