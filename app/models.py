from django.db import models
 
 
class Category(models.Model):
    """カテゴリ."""
 
    name = models.CharField('カテゴリ名', max_length=255)
 
    def __str__(self):
        return self.name

 
class Tag(models.Model):
    """タグ."""
 
    name = models.CharField('タグ名', max_length=255)
 
    def __str__(self):
        return self.name
 
 
class Post(models.Model):
    """記事."""
 
    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')
    category = models.ForeignKey(
        Category, verbose_name='カテゴリ', on_delete=models.PROTECT,
    )
    tag = models.ManyToManyField(Tag, verbose_name='タグ')
 
    def __str__(self):
        return self.title