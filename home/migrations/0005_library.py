# Generated by Django 2.2.2 on 2019-07-02 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_marks_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sut', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Student')),
            ],
        ),
    ]