from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import GchatSpace, GchatUser, GroupGchatSpace
from .models import Group, Role, Permission, GroupMember
from .models import Post, Comment, Reaction, LastSeenOnPost
from .models import Favourite
from .models import User, Tag

class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'parent', 'ext_id', 'attributes')
    list_display = ('name', 'parent', 'ext_id', 'is_visible', 'attributes')

class LastSeenOnPostAdmin(admin.ModelAdmin):
    fields = ('post', 'user', 'seen')
    list_display = ('post', 'user', 'seen')
    readonly_fields = ('seen', )

class GchatSpaceAdmin(admin.ModelAdmin):
    fields = ('name', 'space')

class PermissionAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)
    
class RolePermissionInline(admin.TabularInline):
    fields = ('permission',)
    model = Role.permissions.through

class RoleAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', 'permissons_csv', )
    inlines = (RolePermissionInline,)

class GroupMemberInline(admin.TabularInline):
    fields = ('user', 'role',)
    model = Group.members.through

class GroupGchatSpaceInline(admin.StackedInline):
    max_num = 3
    extra = 1
    description = "Associate google chat rooms to this group. Only rooms that have added the charcha chatbot will show up"
    fields = ('gchat_space', 'sync_members', 'notify')
    model = Group.gchat_spaces.through

class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'group_type', 'purpose', 'description', 'emails', 'is_deleted', )
    list_display = ('name', 'group_type', 'purpose',)
    inlines = (GroupGchatSpaceInline, GroupMemberInline,)
    
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'gchat_space', 'score', 'email', 'is_active', 'is_staff')
    readonly_fields = ('username', )

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'parent_post', 'author', 'submission_time', 'slug',)
    fields = ('group', 'parent_post', 'title', 'slug', 'html', 'author',)
    readonly_fields = ('num_comments', 'score')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('submission_time', 'post', 'author', 'html')
    fields = ('post', 'author', 'html', )
    #readonly_fields = ('submission_time', 'post', 'author')

class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'reaction', 'submission_time')

class FavouriteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(LastSeenOnPost, LastSeenOnPostAdmin)
admin.site.register(GchatSpace, GchatSpaceAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reaction, ReactionAdmin)
admin.site.register(Favourite, FavouriteAdmin)
