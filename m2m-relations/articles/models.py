from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scope = models.ManyToManyField(Tag, through="Scope")


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='тег')
    is_main = models.BooleanField(default=False)


    def __str__(self):
        return self.article.title+' '+self.tag.name
    
    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
        ordering = ['-is_main', 'tag__name']
    
