# Generated by Django 4.0.3 on 2022-03-21 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0003_delete_category_delete_pptmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.CharField(max_length=200)),
                ('outputs', models.CharField(max_length=200)),
                ('u', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.registermodel')),
            ],
        ),
    ]