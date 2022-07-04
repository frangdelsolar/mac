# Generated by Django 4.0.5 on 2022-07-03 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0004_person_id_alter_person_metadata'),
        ('users', '0002_profile_person'),
        ('metadata', '0002_metadata_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('metadata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='metadata.metadata')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person', verbose_name='Persona')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professional_profile', to='users.profile')),
            ],
            options={
                'verbose_name': 'Profesional',
                'verbose_name_plural': 'Profesionales',
            },
            bases=('metadata.metadata',),
        ),
    ]
