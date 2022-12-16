from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import FieldPanel
from wagtail.models import Page
from wagtailsvg.blocks import SvgChooserBlock


class HomePage(Page):
    header = RichTextField(blank=True)
    small_header = RichTextField(blank=True)
    about_title = models.CharField(max_length=250, blank=True)
    about_content = RichTextField(blank=True)
    banner = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    logo = models.ForeignKey(
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
                        ("icon", blocks.CharBlock(default="link")),
                        ("image", ImageChooserBlock(required=False)),
                        ("imageSVG", SvgChooserBlock(required=False)),
                        ("link", blocks.URLBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
    )
    externalStyles = StreamField(
        [
            (
                "external",
                blocks.StructBlock(
                    [
                        ("rawStyles", RawHTMLBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
    )
    externalScripts = StreamField(
        [
            (
                "external",
                blocks.StructBlock(
                    [
                        ("rawScripts", RawHTMLBlock(required=False)),
                    ]
                ),
            ),
        ],
        blank=True,
    )
    externalContentMiddle = StreamField(
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
    externalContentFooter = StreamField(
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
        FieldPanel("logo"),
        FieldPanel("banner"),
        FieldPanel("header"),
        FieldPanel("small_header"),
        FieldPanel("about_title"),
        FieldPanel("about_content"),
        FieldPanel("links"),
        FieldPanel("externalStyles"),
        FieldPanel("externalScripts"),
        FieldPanel("externalContentMiddle"),
        FieldPanel("externalContentFooter"), 
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        organizers = self.get_children().live().type(Organizers)  # type: ignore
        events = self.get_children().live().type(Events).order_by("-slug")  # type: ignore
        photos = self.get_children().live().type(Photos)  # type: ignore
        # organizers = self.get_children().live().order_by('-first_published_at')
        context["organizers"] = organizers
        context["events"] = events
        context["photos"] = photos
        return context


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
    content_panels = Page.content_panels + [  # type: ignore
        FieldPanel("name"),
        FieldPanel("images"),
    ]


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
    image = models.ForeignKey(
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
                        ("icon", blocks.CharBlock(default="link")),
                        ("image", ImageChooserBlock(required=False)),
                        ("imageSVG", SvgChooserBlock(required=False)),
                        ("link", blocks.URLBlock()),
                    ]
                ),
            ),
        ],
        blank=True,
    )
    STATE_CHOICES = [
        ("past", "Evento Pasado"),
        ("current", "Evento Actual"),
        ("upcoming", "Próximo Evento"),
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="past")
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

    content_panels = Page.content_panels + [  # type: ignore
        FieldPanel("name"),
        FieldPanel("about"),
        FieldPanel("detail"),
        FieldPanel("city"),
        FieldPanel("date"),
        FieldPanel("banner"),
        FieldPanel("links"),
        FieldPanel("state"),
        FieldPanel("image"),
        FieldPanel("externalRaws"),
    ]


class Organizers(Page):
    name = models.CharField(max_length=250)
    about = RichTextField(blank=True)
    detail = RichTextField(blank=True)
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
                        ("icon", blocks.CharBlock(default="link")),
                        ("image", ImageChooserBlock(required=False)),
                        ("imageSVG", SvgChooserBlock(required=False)),
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
        FieldPanel("about"),
        FieldPanel("detail"),
        FieldPanel("banner"),
        FieldPanel("image"),
        FieldPanel("city"),
        FieldPanel("roles"),
        FieldPanel("links"),
        FieldPanel("externalRaws"),
    ]
