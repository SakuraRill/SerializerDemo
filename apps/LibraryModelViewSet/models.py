from django.db import models


class PublisherModel(models.Model):
    """出版社"""
    name = models.CharField(max_length=30, verbose_name='出版社名称')
    address = models.CharField(max_length=50, blank=True, null=True, verbose_name='地址')
    city = models.CharField(max_length=60, verbose_name='城市')

    class Meta:
        db_table = "Library_Publisher"


class AuthorModel(models.Model):
    """作者"""
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )

    name = models.CharField(max_length=30, verbose_name='作者名称')
    sex = models.PositiveSmallIntegerField(choices=sex_choices, default=1)
    email = models.EmailField(verbose_name='电子邮箱')

    class Meta:
        db_table = "Library_Author"


class BookModel(models.Model):
    title = models.CharField(max_length=100, verbose_name="书名")
    authors = models.ManyToManyField(AuthorModel)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    publication_date = models.DateField()

    class Meta:
        db_table = "Library_Book"
