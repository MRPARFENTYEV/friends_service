from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.urls import reverse

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password, ):
        if not email:
            raise ValueError('Email is required!')
        if not full_name:
            raise ValueError('full name is required!')

        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, verbose_name='Электронная почта')
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    image = models.ImageField(upload_to='users')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    search_fields =['full_name']
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def return_friends(self):
        friends = Friends.objects.filter(user_id=self.id)
        friends_id = []
        for friend in friends:
            friends_id.append(friend.friend_id)
        return friends_id

    def get_absolute_url(self):
        return reverse('sweet_friends_app:friend_detail', kwargs={'user_id': self.id})
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Friends(models.Model):

    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    friend_id = models.CharField(max_length=50)
    is_hidden = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'
    def return_friend_info(self,friends_id:list):
        info =[]
        for friend_id in friends_id:
            friend_info = User.objects.filter(id = friend_id)
            for friend in friend_info:
                for obj in friend:

                    info.append({'friend_info':obj})
        return info
    def get_absolute_url(self):
        return reverse('sweet_friends:friend_detail', kwargs={'user_id': self.friend_id})