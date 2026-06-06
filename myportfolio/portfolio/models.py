from django.db import models


class Skill(models.Model):
    """Model for skills"""
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=[
            ('Programming Languages', 'Programming Languages'),
            ('AI & Machine Learning', 'AI & Machine Learning'),
            ('Libraries & Frameworks', 'Libraries & Frameworks'),
            ('Web & Tools', 'Web & Tools'),
            ('Data Skills', 'Data Skills'),
            ('Other Skills', 'Other Skills'),
        ]
    )
    proficiency = models.IntegerField(help_text="Rate 1-5", default=3)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return self.name


class Project(models.Model):
    """Model for projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, help_text="Comma-separated list")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-featured', 'order', '-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    """Model for work experience"""
    EMPLOYMENT_TYPE = [
        ('Full-time', 'Full-time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
    ]

    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-is_current', '-start_date', 'order']

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    """Model for education"""
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date', 'order']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    """Model for certifications"""
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    certificate_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date', 'order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Model for contact messages"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
