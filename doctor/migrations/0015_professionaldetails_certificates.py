# Generated by Django 4.2.7 on 2023-12-13 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_rename_certificates_pdf_certificatespdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionaldetails',
            name='certificates',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.certificatespdf'),
        ),
    ]
