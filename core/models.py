from django.db import models


class District(models.Model):
    slug = models.SlugField(unique=True)
    name_qq = models.CharField(max_length=80)
    name_uz = models.CharField(max_length=80)
    name_ru = models.CharField(max_length=80)
    name_en = models.CharField(max_length=80)
    lat = models.FloatField()
    lon = models.FloatField()
    population = models.PositiveIntegerField(default=0)
    distance_to_aralkum_km = models.PositiveIntegerField(default=0)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "slug"]

    def __str__(self):
        return self.name_en

    def name(self, lang):
        return getattr(self, f"name_{lang}", self.name_en) or self.name_en


class CitizenReport(models.Model):
    KIND_CHOICES = [
        ("dust", "dust"),
        ("salt", "salt"),
        ("visibility", "visibility"),
        ("health", "health"),
    ]
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="reports")
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default="dust")
    severity = models.PositiveSmallIntegerField(default=3)  # 1..5
    comment = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.district.slug} {self.kind} {self.severity}"


class Snapshot(models.Model):
    """Last successful fetch of atmospheric data, so pages work even if the API is slow."""
    created_at = models.DateTimeField(auto_now_add=True)
    payload = models.JSONField()
    simulated = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]


class AdviceLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(max_length=20)  # advice / chat
    lang = models.CharField(max_length=5)
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)
    model_used = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ["-created_at"]
