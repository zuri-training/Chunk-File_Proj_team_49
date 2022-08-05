from django.apps import AppConfig
from django.db.models.signals import post_delete
from . signals import delete_zip_file

class ChunkappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chunkapp'
    def ready(self):
        from .models import ChunkOrder
        post_delete.connect(delete_zip_file, sender=ChunkOrder)
        
    
