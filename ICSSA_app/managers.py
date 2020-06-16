from django.db import models

class StudentManager(models.Manager):

    def _create_student(self, email, matric_number, password, is_president=False):
        if not email:
            raise ValueError('The given email must be set')
        if not matric_number:
            raise ValueError('Matric number must be set')
        email = self.normalize_email(email)
        student = self.model(email=email, matric_number=matric_number, is_president=is_president)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_student(self, email, matric_number, password=None,):
        return self._create_student(email, password, matric_number)

    def create_president(self, email, matric_number, password=None, is_president=True):
        return self._create_student(email, password, matric_number, is_president)

class LevelManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
