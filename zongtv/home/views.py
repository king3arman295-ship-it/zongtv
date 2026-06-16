from django.shortcuts import render, get_object_or_404
from .models import Video
from .models import Banner, Channel, Category
from .models import Show
from .models import Channel
from django.views.decorators.cache import cache_page



def channel_detail(request, id):

    channel = get_object_or_404(
        Channel,
        id=id
    )

    news_channels = Channel.objects.filter(
        channel_type='news'
    )

    entertainment_channels = Channel.objects.filter(
        channel_type='entertainment'
    )

    context = {

        'channel': channel,

        'news_channels': news_channels,

        'entertainment_channels': entertainment_channels,
    }

    return render(
        request,
        'channel_detail.html',
        context
    )
def all_channels(request):

    channels = Channel.objects.all()

    return render(
        request,
        'all_channels.html',
        {
            'channels': channels
        }
    )
def all_shows(request):

    shows = Show.objects.all()

    return render(
        request,
        'all_shows.html',
        {
            'shows': shows
        }
    )
def category_detail(request, id):

    category = Category.objects.get(
        id=id
    )

    videos = category.videos.all()

    return render(
        request,
        'category_detail.html',
        {
            'category': category,
            'videos': videos
        }
    )
def video_detail(request, id):

    video = get_object_or_404(
        Video,
        id=id
    )
    return render(
        request,
        'video_detail.html',
        {
            'video': video
        }
    )
def show_detail(request, id):

    show = get_object_or_404(
        Show,
        id=id
    )

    episodes = show.episodes.all().order_by(
        'episode_number'
    )

    context = {
        'show': show,
        'episodes': episodes,
    }

    return render(
        request,
        'show_detail.html',
        context
    )
@cache_page(60 * 5)
def home(request):
  
    banners = Banner.objects.filter(active=True)

    news_channels = Channel.objects.filter(
        channel_type='news'
    )

    entertainment_channels = Channel.objects.filter(
        channel_type='entertainment'
    )

    categories = Category.objects.prefetch_related('videos')[:4]

    zong_shows = Show.objects.only(
    'id',
    'title',
    'poster'
)
    

    print("HOME VIEW EXECUTED")

    banners = Banner.objects.filter(active=True)

    # ADD THESE
    drama = Category.objects.filter(name="Drama").first()
    action = Category.objects.filter(name="Action").first()
    thriller = Category.objects.filter(name="Thriller").first()
    romance = Category.objects.filter(name="Romance").first()

    context = {
        'banners': banners,
        'news_channels': news_channels,
        'entertainment_channels': entertainment_channels,
        'categories': categories,
        'zong_shows': zong_shows,

        # ADD THESE
      "drama": drama,
      "action": action,
      "thriller": thriller,
}
    

    return render(request,'home.html',context)
from django.shortcuts import render, get_object_or_404

def lazy_category(request, id):

    category = get_object_or_404(
        Category,
        id=id
    )

    return render(
        request,
        "partials/category_section.html",
        {
            "category": category
        }
    )