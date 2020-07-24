from django.shortcuts import render, get_object_or_404, redirect
from .models import Diary
from django.db.models import Count

# Create your views here.

def main(request):
    diary=Diary.objects.all().order_by('-id')
    return render(request, 'main.html', {'diary': diary})

def detail(request, diary_id):
    diary=get_object_or_404 (Diary, pk=diary_id)
    total = Diary.objects.count()
    return render(request, 'detail.html', {'diary_detail':diary, "total":total})

def prev(request, diary_id):
    prev_diary=diary_id-1
    return redirect('/detail/'+str(prev_diary))

def next(request, diary_id):
    next_diary=diary_id+1
    return redirect('/detail/'+str(next_diary))    
