# Generated by Django 4.1.2 on 2022-10-27 04:21

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("wagtailcore", "0077_alter_revision_user"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photos",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                (
                    "images",
                    wagtail.fields.StreamField(
                        [
                            (
                                "event",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        ("description", wagtail.blocks.CharBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=None,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AddField(
            model_name="homepage",
            name="about_content",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="about_title",
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name="homepage",
            name="header",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
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
                                ("link", wagtail.blocks.URLBlock()),
                            ]
                        ),
                    )
                ],
                blank=True,
                use_json_field=None,
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="small_header",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.CreateModel(
            name="Organizers",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("city", models.CharField(max_length=250)),
                ("roles", models.CharField(max_length=250)),
                (
                    "links",
                    wagtail.fields.StreamField(
                        [
                            (
                                "network",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("name", wagtail.blocks.CharBlock()),
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("link", wagtail.blocks.URLBlock()),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=None,
                    ),
                ),
                (
                    "externalRaws",
                    wagtail.fields.StreamField(
                        [
                            (
                                "external",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "rawHTML",
                                            wagtail.blocks.RawHTMLBlock(required=False),
                                        )
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=None,
                    ),
                ),
                (
                    "banner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("about", wagtail.fields.RichTextField(blank=True)),
                ("detail", wagtail.fields.RichTextField(blank=True)),
                ("city", models.CharField(max_length=250)),
                ("date", models.CharField(max_length=250)),
                (
                    "links",
                    wagtail.fields.StreamField(
                        [
                            (
                                "network",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("name", wagtail.blocks.CharBlock()),
                                        ("icon", wagtail.blocks.CharBlock()),
                                        ("link", wagtail.blocks.URLBlock()),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        use_json_field=None,
                    ),
                ),
                (
                    "banner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
    ]