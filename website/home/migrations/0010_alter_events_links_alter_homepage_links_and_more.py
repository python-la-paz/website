# Generated by Django 4.1.2 on 2022-10-28 02:08

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_events_externalraws_events_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="events",
            name="links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "network",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("icon", wagtail.blocks.CharBlock(default="link")),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "imageSVG",
                                    wagtailsvg.blocks.SvgChooserBlock(required=False),
                                ),
                                ("link", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=None,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "network",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("icon", wagtail.blocks.CharBlock(default="link")),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "imageSVG",
                                    wagtailsvg.blocks.SvgChooserBlock(required=False),
                                ),
                                ("link", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=None,
            ),
        ),
        migrations.AlterField(
            model_name="organizers",
            name="links",
            field=wagtail.fields.StreamField(
                [
                    (
                        "network",
                        wagtail.blocks.StructBlock(
                            [
                                ("name", wagtail.blocks.CharBlock()),
                                ("icon", wagtail.blocks.CharBlock(default="link")),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "imageSVG",
                                    wagtailsvg.blocks.SvgChooserBlock(required=False),
                                ),
                                ("link", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=None,
            ),
        ),
    ]
