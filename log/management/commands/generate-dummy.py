from django.core.management.base import BaseCommand, CommandError
from log.models import Activity, Log
from django.contrib.auth.models import User

from datetime import datetime, timedelta

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        Activity.objects.all().delete()
        Log.objects.all().delete()
        
        for activity in ["Formula", "Diaper Change", "Medicine"]:
            Activity.objects.create(name=activity)
        
        logs = [
            ("Formula", "30ml", "mom"),
            ("Diaper Change", "Poop", "mom"),
            ("Formula", "40ml", "dad"),
            ("Medicine", "Flacol 0.3ml", "mom"),
        ]
        

        now = datetime.now()
        diff = timedelta(minutes=90)
        
        for activity, remark, author in logs:
            Log.objects.create(
                timestamp=now,
                activity=Activity.objects.get(name=activity),
                remark=remark,
                author=User.objects.get(username=author)
                )
            
            now = now-diff
