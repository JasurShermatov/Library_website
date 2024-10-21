from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    count = models.IntegerField()
    pages = models.IntegerField(default=500)
    book_file = models.FileField(upload_to='books/', blank=True, null=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"{self.title} by {self.author} count: {self.count} pages: {self.pages}"






class Forma(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=512)
    age = models.IntegerField()
    phone = models.CharField(max_length=512)
    address = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.full_name}"


class User(models.Model):
    STUDENT = 'student'
    TEACHER = 'teacher'
    ROLES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default=ROLES[0][0])  # student or teacher
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.first_name} {self.last_name} role: {self.role}"



