from django.db import models  # 导入Django的模型模块
from django.utils import timezone  # 导入Django的时区相关工具
from userapp.models import CustomUser  # 从userapp应用的models中导入CustomUser模型
# Create your models here.


class Post(models.Model):  # 定义一个名为Post的模型，继承自models.Model
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 定义一个外键字段，关联到CustomUser，当用户被删除时，相关的帖子也会被删除
    title = models.CharField(max_length=200)  # 定义一个字符字段，用于存储帖子的标题，最大长度为200
    text = models.TextField()  # 定义一个文本字段，用于存储帖子的内容
    created_date = models.DateTimeField(default=timezone.now)  # 定义一个日期时间字段，用于存储帖子的创建时间，默认值为当前时间
    published_date = models.DateTimeField(blank=True, null=True)  # 定义一个日期时间字段，用于存储帖子的发布时间，可以为空

    def publish(self):  # 定义一个方法，用于设置帖子的发布时间
        self.published_date = timezone.now()  # 将发布时间设置为当前时间
        self.save()  # 保存改动

    def __str__(self):  # 定义对象的字符串表示方法
        return self.title  # 返回帖子的标题

    def approved_comments(self):  # 定义一个方法，用于获取所有已批准的评论
        return self.comments.filter(approved_comment=True)  # 返回与这个帖子相关联且已批准的评论


class Comment(models.Model):  # 定义一个名为Comment的模型，继承自models.Model
    post = models.ForeignKey('forum.Post', on_delete=models.CASCADE, related_name='comments')  # 定义一个外键字段，关联到Post模型，并指定关联名称为comments
    author = models.CharField(max_length=200)  # 定义一个字符字段，用于存储评论作者的名称，最大长度为200
    text = models.TextField()  # 定义一个文本字段，用于存储评论的内容
    created_date = models.DateTimeField(default=timezone.now)  # 定义一个日期时间字段，用于存储评论的创建时间，默认值为当前时间
    approved_comment = models.BooleanField(default=False)  # 定义一个布尔字段，用于标记评论是否已被批准，默认为False

    def approve(self):  # 定义一个方法，用于批准评论
        self.approved_comment = True  # 将approved_comment字段设为True
        self.save()  # 保存改动

    def __str__(self):  # 定义对象的字符串表示方法
        return self.text  # 返回评论的内容
