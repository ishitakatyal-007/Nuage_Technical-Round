# Generated by Django 3.0 on 2020-09-20 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionIOU',
            fields=[
                ('iou_id', models.AutoField(primary_key=True, serialize=False)),
                ('iou_amount', models.FloatField()),
                ('iou_record', models.DateTimeField(auto_now=True)),
                ('iou_type', models.CharField(choices=[('L', 'Lending'), ('B', 'Borrowing')], max_length=1)),
                ('friends_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='friends.Friends')),
                ('transactor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactor', to='friends.Friends')),
            ],
            options={
                'db_table': 'transaction_iou',
                'managed': True,
            },
        ),
    ]
