from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import urllib.request
from os import makedirs
from os.path import isdir


class InstaDownloader:
    def __init__(self):
        self.directory = self.pic_class = ''
        self.options = Options()
        self.options.add_argument('--headless')
        # To be able to view the proccess, remove the options parameter
        self.driver = webdriver.Chrome('chromedriver.exe')#, options=self.options)

    def DirCorrection(self, directory):
        """
        Makes sure that the directory exists. If none is passed, it will be the default (InstaDownloader)
        """
        if not directory:
            directory = 'InstaDownloader/'
        elif not directory.endswith('/'):
            directory = directory + '/'
        if not isdir(directory):
            makedirs(directory)
        return directory
        
    def getUserRecentPics(self, userID, save_to='', amount=12):
        """
        If the target Instagram profile has less than 20 posts, make sure to set 'amount' to the specific
        amount you desire. Ex: profile with 13 posts -> amount=13. Otherwise (ex.: amount=22) it won't work.

        Optional parameters:
        save_to: directory in which the images will be saved
        amount: default is 12, maximum is 20. 
        """
        self.directory = self.DirCorrection(save_to)
        amount = int(amount) if int(amount) < 21 else 20
        self.driver.get(f'https://instagram.com/{userID}')
        sleep(1)
        #debugging
        print(f'User ID: {userID}\nSaving to directory: {self.directory}\nDownloading images from {amount} posts\n\n')
        while True:
            posts = self.driver.find_elements_by_class_name('v1Nh3')
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(1)
            if len(posts) >= amount:
                posts = posts[:amount]
                break
        for x in posts:
            print(x)
        posts = list(map(self.getURL, posts))
        # download images and then finishes the program
        for i, post_url in enumerate(posts):
            self.downloadIMGs(post_url, self.directory, userID, i+1)
            sleep(1)
        self.driver.quit()
        print('\n\n-----| Process finished |-----')

    def getURL(self, post):
        try:
            url = post.find_element_by_tag_name('a').get_attribute('href')
        except:
            url = ''
        print(url)
        return url

    def getPic(self, url, directory=''):
        directory = self.DirCorrection(directory)
        self.downloadIMGs(url, directory, 'pic', datetime.now().strftime("%H.%M.%S_%d-%m-%y"))
        self.driver.quit()
        print('\n\n-----| Process finished |-----')

    def downloadIMGs(self, url, directory, prefix, info):
        """
        Used when downloading single posts (by passing the URL) or multiple (user id)
        Downloads all images from an instagram post url (ex.: 2 images on the same /p/ address.
        If encounters an error (the last picture) it stops.
        
        :param url: post url containing 1 or more media
        :param directory: directory to be saved the images
        :param prefix: file identifier method
        :param info: count of the number of posts from most recent to least

        index: (located in the last for loop) identifier method to specify which image of the post the archive is
        """
        self.driver.get(url)
        sleep(1)
        imgs = []
        while True:
            try:
                img_src = self.driver.find_element_by_class_name('FFVAD').get_attribute('src')
                print(img_src, '\n')
                imgs.append(img_src)
            except:
                print("Video found and won't be downloaded\n")
            try:
                button = self.driver.find_element_by_class_name('_6CZji')
                button.click()
                sleep(0.5)
            except:
                print('Last image found\n')
                break
        for index, img_url in enumerate(imgs):
            urllib.request.urlretrieve(img_url, f'{directory}{prefix}_{info}_img{index+1}.png')


# -------------------------------------
downloader = InstaDownloader()
downloader.getUserRecentPics('USERID')
downloader.getPic('post URL')
