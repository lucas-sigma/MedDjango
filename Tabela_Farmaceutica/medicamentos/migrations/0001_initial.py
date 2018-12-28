# Generated by Django 2.1.4 on 2018-12-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicamento', models.CharField(max_length=50)),
                ('para_que_serve', models.TextField()),
                ('contraindicacao', models.TextField()),
                ('como_usar', models.TextField()),
                ('precaucoes', models.TextField()),
                ('reacoes_adversas', models.TextField()),
                ('riscos', models.TextField()),
                ('interacao_med', models.TextField()),
                ('interacao_alimenticia', models.TextField()),
                ('acao_da_substancia', models.TextField()),
            ],
        ),
    ]
