from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    header = RichTextField(blank=True)
    small_header = RichTextField(blank=True)
    about_title = models.CharField(max_length=250, blank=True)
    about_content = RichTextField(blank=True)

    links = StreamField(
        [
            (
                "network",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("icon", blocks.CharBlock()),
                        ("image", ImageChooserBlock(required=False)),
                        ("link", blocks.URLBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("header"),
        FieldPanel("small_header"),
        FieldPanel("about_title"),
        FieldPanel("about_content"),
        FieldPanel("links"),
    ]


class Photos(Page):
    name = models.CharField(max_length=500)
    images = StreamField(
        [
            (
                "event",
                blocks.StructBlock(
                    [
                        ("title", blocks.CharBlock()),
                        ("description", blocks.CharBlock()),
                        ("image", ImageChooserBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
    )

class Events(Page):
    name = models.CharField(max_length=500)
    about = RichTextField(blank=True)
    detail = RichTextField(blank=True)
    city = models.CharField(max_length=250)
    date = models.CharField(max_length=250)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    links = StreamField(
        [
            (
                "network",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("icon", blocks.CharBlock()),
                        ("link", blocks.URLBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
    )


    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("about"),
        FieldPanel("detail"),
        FieldPanel("city"),
        FieldPanel("date"),
        FieldPanel("banner"),
        FieldPanel("links"),
    ]


class Organizers(Page):
    name = models.CharField(max_length=250)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    city = models.CharField(max_length=250)
    roles = models.CharField(max_length=250)
    links = StreamField(
        [
            (
                "network",
                blocks.StructBlock(
                    [
                        ("name", blocks.CharBlock()),
                        ("icon", blocks.CharBlock()),
                        ("link", blocks.URLBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
    )

    externalRaws = StreamField(
        [
            (
                "external",
                blocks.StructBlock(
                    [
                        ("rawHTML", RawHTMLBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel("banner"),
        FieldPanel("image"),
        FieldPanel("city"),
        FieldPanel("roles"),
        FieldPanel("links"),
        FieldPanel("externalRaws"),
    ]
