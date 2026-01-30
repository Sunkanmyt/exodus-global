from django.db import models

class Sermon(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=100)
    date_preached = models.DateField()
    description = models.TextField(blank=True, null=True) 
    video_url = models.URLField(blank=True, null=True) 
    transcript = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField() 
    location = models.CharField(max_length=255, default="Online")
    registration_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} on {self.start_time}"


class Milestone(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='milestones/')
    description = models.TextField(blank=True)
    date_achieved = models.DateField()

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Partnertier(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    minimum_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Partner(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    tier = models.ForeignKey(Partnertier, on_delete = models.SET_NULL, null=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
    