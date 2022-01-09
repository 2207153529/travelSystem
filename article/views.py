
# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown
from static.spider import quanerCrawl


def getWebArticle():
    # article = ArticlePost.objects.get(id=id)
    article_id = ['7591941', '7591896', '7591810', '7592079',
                  '7591948', '7591946', '7591700', '7591634',
                  '7591546', '7589192', '7588831', '7588449', ]
    for id_1 in article_id:
        html = quanerCrawl.getModule(id_1)
        author = html.getAuthor()
        title = html.getTitle()
        # 判断当前文章是否在数据库中存在
        if ArticlePost.objects.filter(title=title) \
                and ArticlePost.objects.filter(author=author):
            break
        body = html.getContent()
        # now = ArticlePost()  # 当前存储的数据
        new_article = ArticlePost(
            author=author,
            title=title,
            body=body,
        )
        new_article.save()



# 文章列表
def ArticleList(request):
    getWebArticle()
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/article_list.html', context)



# 文章细节
def ArticleDetail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         # 缩写、表格等常用扩展
                                         'markdown.extensions.extra',
                                         # 语法高亮
                                         'markdown.extensions.codehilite',
                                     ])
    context = {'article': article}
    return render(request, 'article/article_detail.html', context)

# 写文章的视图
def ArticleCreate(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:ArticleList")
        else:
            return HttpResponse("Error")
    # 用户请求获取数据
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/article_create.html', context)

# 删除文章
def ArticleDelete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:ArticleList")
    else:
        return HttpResponse("仅允许POST请求")


# 文章更新
def ArticleUpdate(request, id):
    article = ArticlePost.objects.get(id=id)
    if request.method == 'POST':
        # 将数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:ArticleDetail", id=id)
        else:
            return HttpResponse("表单有误，请重新填写")
    # 获得数据
    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form}
        return render(request, 'article/article_update.html', context)


# getWebArticle()
