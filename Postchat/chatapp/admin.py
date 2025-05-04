from django.contrib import admin
from .models import myUser
from .models import Post

admin.site.register(myUser)
admin.site.register(Post)
