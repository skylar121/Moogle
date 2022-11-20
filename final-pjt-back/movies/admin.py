from django.contrib import admin
from .models import Movie, Genre, Community, Comment, Review, ReviewComment

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(ReviewComment)