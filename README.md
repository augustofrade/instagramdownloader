# Instagram Downloader  
\
Instagram image downloading made easy

## Setup
Setting up your downloader is simple:
```
downloader = InstaDownloader()
```

## Usage

It has two functionalities (methods):

1. **.getUserRecentPics('username')**\
   Downloads all images from the **recent** posts within the amount specified
   * Obligatory parameters:
     - **username** = username of the Instagram account; string
   * Optional paremeters:
     - **amount** = amount of recent posts that will be analyzed and downloaded if they are images (the maximum amount being 20). The default value is _12_; int
     - **directory** = directory that the images will be saved in. Ex: an absolute dir _'C:/Users/Coder/Documents/InstagramDownloads'_ or a relative one: *InstagramDownloads/user_x*. The default is _InstagramDownloader_ and will be created in the same folder of the project; string
   * File downloaded name will look like:
     - *username_PostNo_index* (index is the index of the image on the post)

2. **.getPic('instagram.com/p/xxxxxx')**\
   Downloads all images from the **specified** post URL
   * Obligatory paremeters:
     - **url**: url of the Instagram post that will have its images downloaded.
   * Optional paremets:
   	 - **directory**: same as the other method
   * File downloaded name will look like:
     - *pic_date_time_index* (index is the index of the image on the post)

### Example of usage
```
downloader = InstaDownloader()
downloader.getUserRecentPics('instagram', amount=3)
downloader.getUserRecentPics('https://instagram.com/p/xxxxxxx', directory='insta/user_x')
```

## Important
The webdriver used in this application is Chromedriver.
To use the application make sure to have one in the same directory of this code named as "chromedriver.exe"
To use others, specifiy in the line 17 the webdriver and it's path.  
You can download chromedriver [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Known Bugs
- Cannot analyze and download more than 20 posts
- If the user has less posts than the specified in the 'amount' paremeter it won't download the images

## About
Made for practicing puporses. Someday I'll fix the issues.