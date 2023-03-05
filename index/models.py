from django.db import models
from django.utils.safestring import mark_safe


class Users(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    name = models.CharField(verbose_name="用户名", max_length=120)
    password = models.CharField(verbose_name="用户名", max_length=120)
    phone = models.CharField(verbose_name="手机号", max_length=120, default='')
    photo = models.ImageField(verbose_name="头像", upload_to='media/users/photo')
    email = models.EmailField(verbose_name="邮箱")
    is_active = models.IntegerField(verbose_name="状态", default=1)  # 1 普通用户 3禁用
    time = models.TimeField(verbose_name="时间", auto_now=True)

    def admin_sample(self):
        return mark_safe('<img src="/media/%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '  图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Users'
        verbose_name = '用户'
        verbose_name_plural = '用户'
        # 后台管理名
        managed = True


class Start(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user = models.ForeignKey(verbose_name="用户名", to="Users", on_delete=models.CASCADE, default=1)
    name = models.ForeignKey(verbose_name="电影", to="Films", on_delete=models.CASCADE)
    time = models.TimeField(verbose_name="创建时间", auto_now=True)

    def admin_sample(self):
        return mark_safe('<img src="%s" height="60" width="60" />' % (self.name.photo,))

    admin_sample.short_description = '  图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name.name

    class Meta:
        # 数据库列表名
        db_table = 'Star'
        # 后台管理名
        verbose_name_plural = '收藏'
        verbose_name = '收藏'


class Films(models.Model):
    """('排名', '名称', '链接', '星级', '评分', '评价人数', '封面图片', '导演', '年份')"""
    id = models.AutoField(verbose_name='id', primary_key=True)
    rank = models.IntegerField(verbose_name='排名')
    name = models.CharField(verbose_name='名称', max_length=200, default='')
    link = models.CharField(verbose_name='链接', max_length=200, default='')
    star = models.CharField(verbose_name='星级', max_length=200, default='')
    grade = models.CharField(verbose_name='评分', max_length=200, default='')
    numOfGrade = models.CharField(verbose_name='评价人数', max_length=200, default='')
    photo = models.CharField(verbose_name='封面图', max_length=200, default='')
    person = models.CharField(verbose_name='导演', max_length=200, default='')
    year = models.CharField(verbose_name='年份', max_length=200, default='')

    def admin_sample(self):
        return mark_safe('<img src="%s" height="60" width="60" />' % (self.photo,))

    admin_sample.short_description = '  图片'
    admin_sample.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        # 数据库列表名
        db_table = 'Films'
        # 后台管理名
        verbose_name_plural = '电影列表'
