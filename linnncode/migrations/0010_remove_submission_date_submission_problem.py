# Generated by Django 4.1.5 on 2023-10-04 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linnncode', '0009_submission_code_submission_date_submission_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='date',
        ),
        migrations.AddField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='linnncode.problem'),
        ),
    ]