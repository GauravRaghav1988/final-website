from django.contrib import admin
from .models import QuesModel
from .forms import SignUpForm, addQuestionform
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import BlogPost
# Custom admin class for the User model using SignUpForm
class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = SignUpForm
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name']

# Register the custom User admin class
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Custom admin class for QuesModel using addQuestionform
class QuesModelAdmin(admin.ModelAdmin):
    form = addQuestionform

# Register the custom QuesModel admin class
admin.site.register(QuesModel, QuesModelAdmin)





class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('post_number', 'heading', 'user_name')
    search_fields = ('heading', 'user_name')
    list_filter = ('user_name',)

admin.site.register(BlogPost, BlogPostAdmin)