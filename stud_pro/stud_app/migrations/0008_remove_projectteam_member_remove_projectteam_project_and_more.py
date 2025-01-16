# Generated by Django 5.1.4 on 2024-12-23 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0007_project_teammember_projectteam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectteam',
            name='member',
        ),
        migrations.RemoveField(
            model_name='projectteam',
            name='project',
        ),
        migrations.AddField(
            model_name='projectteam',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='team_projects', to='stud_app.teammember'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectteam',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='project_teams', to='stud_app.project'),
            preserve_default=False,
        ),
    ]
