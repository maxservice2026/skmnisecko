from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_economyexpense_expense_type_economyexpense_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsettings',
            name='registration_confirmation_subject',
            field=models.CharField(
                default='Potvrzujeme přijetí registrace',
                max_length=200,
                verbose_name='Potvrzení přijetí registrace - předmět',
            ),
        ),
        migrations.AddField(
            model_name='appsettings',
            name='registration_confirmation_body',
            field=models.TextField(
                default='Dobrý den, děkujeme za zaslání registrace. Tým SK Mníšecko.',
                verbose_name='Potvrzení přijetí registrace - text',
            ),
        ),
    ]
