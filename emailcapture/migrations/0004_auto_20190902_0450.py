# Generated by Django 2.2.4 on 2019-09-02 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emailcapture', '0003_leadcaptureemail_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadcaptureemail',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='emailcapture.RequestIpInfo'),
        ),
    ]
