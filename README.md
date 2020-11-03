djangocms-youtube
=================

Speed up your pageloads with this YouTube embed plugin for your Django CMS 
powered site. It requires a (free) YouTube Data API Key and also has options 
for custom video thumbnails and publishing stats to Google Analytics.

Quickstart
----------

1.  Install `djangocms-youtube`:
    ```
        pip install djangocms-youtube-lazyload
    ```
2.  Add `djangocms_youtube_lazyload` to `INSTALLED_APPS`:
    ```
        INSTALLED_APPS = (
            ...
            'djangocms_youtube_lazyload',
            ...
        )
    ```
3.  Sync database :
    ```
        python manage.py migrate
    ```
4.  Plugin requires Server API key to be able to use the YouTube Data
    API:
    ```
        DJANGOCMS_YOUTUBE_LAZYLOAD_API_KEY = '<youtube_data_api_server_key>'
    ```
    Instructions on how to obtain an API key are located here:
    https://developers.google.com/youtube/registering_an_application

Features
--------

Reduce Page Load Time
---------------------

When you embed any YouTube video on your website using standard IFRAME
tags, you’ll be surprised to know how much extra weight that YouTube
video will add to your page. The resources (CSS, images and JavaScript)
will download even if the visitor on your website has chosen not to
watch the embedded YouTube video.

djangocms-youtube uses a clever workaround to reduce the time it takes
to initially load the YouTube video player. Instead of embedding the
full Youtube video player, it displays just the thumbnail images of the
video and a “play” icon is placed over the video so that it looks like a
video player.

When the user hits the play button, the video thumbnail is replaced with
the standard YouTube video player. The extra resources are thus loaded
only when the user has decided to play the embedded video and not
otherwise.

Note: Mobile devices require two taps to play the video. Tap the image
once to remove it and display the video player. Then, tap the play
button to begin the video.

High Resolution Thumbnail
-------------------------

Fetches the highest resolution thumbnail available from YouTube for a
given video with options for custom video thumbnails using
`django-filer`.

```
{
  "default": {
    "url": "https://i.ytimg.com/vi/9bZkp7q19f0/default.jpg",
    "width": 120,
    "height": 90
  },
  "high": {
    "url": "https://i.ytimg.com/vi/9bZkp7q19f0/hqdefault.jpg",
    "width": 480,
    "height": 360
  },
  "medium": {
    "url": "https://i.ytimg.com/vi/9bZkp7q19f0/mqdefault.jpg",
    "width": 320,
    "height": 180
  },
  "maxres": {
    "url": "https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg",
    "width": 1280,
    "height": 720
  },
  "standard": {
    "url": "https://i.ytimg.com/vi/9bZkp7q19f0/sddefault.jpg",
    "width": 640,
    "height": 480
  }
}
```

Schema.org Integration
----------------------

Full support for schema.org `videoObject` markup.

```
<div class="video-wrapper" itemprop="video" itemscope="" itemtype="http://schema.org/VideoObject">
    <meta itemprop="name" content="PSY - GANGNAM STYLE (강남스타일) M/V">
    <meta itemprop="duration" content="PT4M13S">
    <meta itemprop="thumbnailUrl" content="https://i.ytimg.com/vi/9bZkp7q19f0/maxresdefault.jpg">
    <meta itemprop="embedURL" content="https://www.youtube.com/embed/9bZkp7q19f0">
    <meta itemprop="uploadDate" content="2012-07-15T07:46:32.000Z">
    <meta itemprop="height" content="480">
    <meta itemprop="width" content="853">
    <meta itemprop="description" content="...">
</div>
```

See https://developers.google.com/webmasters/videosearch/schema

Video Endscreen
---------------

Plugin can have child plugins (i.e other plugins placed inside this
plugin), rendered as an overlay, when the video finishes. You can
disable this functionality by overriding
`DJANGOCMS_YOUTUBE_LAZYLOAD_ALLOW_CHILDREN` in your `settings.py` file


Google Analytics
----------------

Automatically publishes the metrics listed below to your Google
Analytics account.

```
+ Play
+ 10% watched
+ 25% watched
+ 50% watched
+ 75% watched
+ 90% watched
+ Watch to end
```

Make sure you have installed the Google Analytics tracking scripts.

See https://developers.google.com/analytics/devguides/collection/analyticsjs/
