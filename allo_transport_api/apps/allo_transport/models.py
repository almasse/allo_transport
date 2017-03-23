from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.rich_text import expand_db_html
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from django.conf import settings
from wagtailmenus.models import MenuPage



class HomePage(MenuPage):
    blue_body = RichTextField(blank=True)
    blue_body_title = models.CharField(max_length=150,blank=True)
    body = RichTextField(blank=True)
    body_title = RichTextField(blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['partners', 'subpage_types','body','photo','photo_url','body_title','blue_body_title','blue_body','body1','blue_body1','body_title1']

    content_panels = Page.content_panels + [
        FieldPanel('blue_body_title'),
        FieldPanel('blue_body'),
        FieldPanel('body_title'),
        FieldPanel('photo'),
        FieldPanel('body'),
        InlinePanel('partners', label="Partenaires"),


    ]
    subpage_types = ['allo_transport.NewsPage']
    @property
    def photo_url(self):
        if self.photo:
            return settings.MEDIA_URL + 'original_images/' + self.photo.filename

    def body1(self):
        return expand_db_html(self.body)

    def blue_body1(self):
        return expand_db_html(self.blue_body)

    def body_title1(self):
        return expand_db_html(self.body_title)


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


class AboutPage(MenuPage):
    body = RichTextField(blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['body','photo','photo_url','body1']

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('photo'),
    ]

    @property
    def photo_url(self):
        if self.photo:
            return settings.MEDIA_URL + 'original_images/' + self.photo.filename

    def body1(self):
        return expand_db_html(self.body)


class NewsPage(MenuPage):
    body = RichTextField(blank=True)
    apercu = models.CharField(max_length=150,blank=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    api_fields = ['body','photo','photo_url','apercu','body1']
    


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

    def body1(self):
        return expand_db_html(self.body)


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