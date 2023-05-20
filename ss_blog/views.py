from django.shortcuts import render, get_object_or_404,redirect
from .models import Topics,Article,Comment
from .forms import Article_form,CommentForm
# Create your views here.

def add_article(request):
    if request.method == 'POST':
        form = Article_form(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            article = form.save(commit=False)
            article.save()
            return redirect('ss_blog:home')
        else:
            # Display the form with validation errors
            print(form.errors)
            return render(request, 'ss_blog/add_article.html', {'form': form})
    else:
        # Display a blank form for adding a new article
        form = Article_form()
        return render(request, 'ss_blog/add_article.html', {'form': form})

def home_view(request):
    topic_na=Article.objects.all()
    return render(request,'ss_blog/home.html',{'topic_na':topic_na,})

def contentpage_view(request, Topics_id):
    post = get_object_or_404(Article, id=Topics_id)
    comments = Comment.objects.filter(post=post)
    form = CommentForm(initial={'post': post})
    return render(request, 'ss_blog/display_content_page.html', {'post': post, 'comments': comments, 'form': form})

def post_comment(request,Topics_id):
    post=get_object_or_404(Article,id=Topics_id)
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('ss_blog:contentpage_view',Topics_id=post.id)
    else:
        form =CommentForm(initial={'post':post})
    return render(request,'ss_blog/display_content_page.html',{'post':post,'form':form,})


    

def loging(request):
    post = Article.objects.all()
    return render(request,'ss_blog/login.html',{' post':post})

def edit_my_model(request,Article_id):
    post = get_object_or_404(Article, id=Article_id)
    if request.method == 'POST':
        form =Article_form(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('ss_blog:contentpage_view', Topics_id=post.id)
    else:
        form = Article_form(instance=post)
    return render(request, 'ss_blog/edit.html', {'form': form, 'post': post})


def delete_post(request, Article_id):
    post = get_object_or_404(Article, id=Article_id)
    if request.method == 'POST':
        post.delete()
        return redirect('ss_blog:home')  # Redirect to the home view after deletion
    return render(request, 'ss_blog/delete.html', {'post': post})
