# Generated by Django 2.2.4 on 2019-10-15 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pretixbase', '0136_auto_20190918_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_backend',
            field=models.CharField(default='native', max_length=255),
        ),
    ]