from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class MenuList(models.Model):
    module_name=models.CharField(max_length=100, db_index=True)
    menu_name=models.CharField(max_length=100, db_index=True)
    menu_url=models.CharField(max_length=200, unique=True)
    menu_icon=models.CharField(max_length=200, null=True, blank=True)
    parent_id=models.IntegerField(default=0)
    is_main_menu=models.BooleanField(default=False)
    is_sub_menu=models.BooleanField(default=False)
    is_child_sub_menu=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    deleted_at=models.DateTimeField(blank=True, null=True)
    created_by=models.CharField(max_length=100, blank=True, null=True)
    is_active=models.BooleanField(default=True)
    deleted=models.BooleanField(default=False)

    class Meta:
        db_table='menu_list'
    def __str__(self):
        return self.menu_name
    
class UserPermission(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissions')
    menu=models.ForeignKey(MenuList, on_delete=models.CASCADE, related_name='user_permissions')
    can_view=models.BooleanField(default=False)
    can_add=models.BooleanField(default=False)
    can_edit=models.BooleanField(default=False)
    can_delete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    updated_by=models.CharField(max_length=100, blank=True, null=True)
    deleted=models.BooleanField(default=False)
    deleted_at=models.DateTimeField(blank=True, null=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        db_table='user_permission'
    def __str__(self):
        return self.menu.menu_name
    
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True)
    is_active=models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self): 
        return f"{self.name}"

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=100, unique=True)
    content=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    post_image=models.ImageField(upload_to='blog_image/', blank=True, null=True)
    description=RichTextUploadingField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self): 
        return f"{self.title}"