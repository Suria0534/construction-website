from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to='projects/', blank=True, null=True)  # keep main image optional
    description = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)  # status of project

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"Image for {self.project.name}"

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About content"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero_images/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption or "Hero Image"
