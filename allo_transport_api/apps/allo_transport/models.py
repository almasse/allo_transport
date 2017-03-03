from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from django.conf import settings


class HomePage(Page):
    api_fields = ['partners', 'subpage_types']

    content_panels = Page.content_panels + [
        InlinePanel('partners', label="Partenaires"),
    ]
    subpage_types = ['allo_transport.NewsPage']


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


class NewsPage(Page):
    body = RichTextField(blank=True)
    apercu = models.CharField(max_length=150,blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['body','photo','photo_url','apercu']
    


    parent_page_types = ['allo_transport.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('photo'),
        FieldPanel('apercu'),
    ]

    @property
    def photo_url(self):
        if self.photo:
            return settings.MEDIA_URL + 'original_images/' + self.photo.filename

"""
class Photo(Orderable):
    page = ParentalKey(NewsPage, related_name='photo')
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


class Content(Orderable):
    page = ParentalKey(NewsPage, related_name='content')
    title = models.CharField(max_length=255,null=True,blank=True)
    description = RichTextField(null=True,blank=True)

    api_fields = ['title', 'description']

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
    ]
"""