# Generated by Django 4.1.2 on 2022-10-27 18:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailsvg.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_homepage_logo"),
    ]

    operations = [
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
                                ("icon", wagtail.blocks.CharBlock()),
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