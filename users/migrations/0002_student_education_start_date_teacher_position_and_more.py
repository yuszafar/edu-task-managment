# Generated by Django 4.0.6 on 2022-07-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='education_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(default=1, max_length=222),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='student_list', to='users.student'),
        ),
    ]