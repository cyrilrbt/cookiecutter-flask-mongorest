import datetime
import mongoengine as db


class {{ cookiecutter.project_name|title }}Document(db.Document):
    meta = {
        'allow_inheritance': True,
        'abstract': True,
        'strict': False,
        'indexes': ['created_at'],
    }
    created_at = db.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = db.DateTimeField(default=datetime.datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow()
        super().save(*args, **kwargs)
