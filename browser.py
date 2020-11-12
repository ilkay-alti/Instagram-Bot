from selenium import webdriver
import time
import userınfo as ui
import control as c
import random
import os
import urllib.request

PATH ="/home/ilkayus/path/chromedriver"


class Browser:
    def __init__(self,link):
        self.link=link
        self.browser=webdriver.Chrome(PATH)
        Browser.loginInstagram(self)
        # Browser.followersList(self) -------> Followers lıst
        # Browser.followingList(self) -------> Following List
        
        # Browser.userPostLike(self)  #-------> User FulPage Like
        # Browser.userPostCommand(self)  #--------> User Fulpage Command
        # Browser.HastagPostLike(self)  #Hastag Ful Page Lıke
        # Browser.HastagPostCommand(self)  # Hastag Full page Command
       
        # Browser.DeleteNotFollow(self)   ------>Delete Not Follow
        # Browser.DowonloadHastagsFullPicture(self)  -----> install ful page dowondload
        # Browser.DowondloadUserPicture(self)  --------> install ful page user dowondload
        # Browser.UserFollowDM(self)
        # Browser.followingList
        # Browser.GTuser(self)
        # Browser.DmDelete(self)
        # Browser.userUnFollowDM(self)
        Browser.DmDelete(self)





    def loginInstagram(self):
        self.browser.get(self.link)
        time.sleep(3)
        username = self.browser.find_element_by_name("username")                           #---------> Instagram User Name
        password =self.browser.find_element_by_name("password")
        loginBtn = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')   #---------> Instagram Password
        username.send_keys(ui.username)
        password.send_keys(ui.password)
        loginBtn.click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
     
        




    #BASIC COMMANDS
    def userPostCommand(self):
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.UsertCommand)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        time.sleep(2)
        PostsClass=self.browser.find_elements_by_class_name('v1Nh3')
        Posts=[]
        TrueorFalse=0

        if TrueorFalse==c.fulpageCommand:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                print(Posts)
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
              
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.userPostCommand[random.randint(0,len(c.userPostCommand)-1)])
                time.sleep(2)
                
                self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()      
                time.sleep(3)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()

        elif TrueorFalse!=c.fulpageCommand:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                c.fulpageCommand=c.fulpageCommand-1
                if c.fulpageCommand == TrueorFalse:
                    break
            
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
              
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.userPostCommand[random.randint(0,len(c.userPostCommand)-1)])
                time.sleep(2)
              
                self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()      
                time.sleep(3)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()                                                               

    def userPostLike(self):
       
        
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.UsertPostLike)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        time.sleep(2)
        
        PostsClass=self.browser.find_elements_by_class_name('v1Nh3')
        Posts=[]
        TrueorFalse=0
        if TrueorFalse==c.fulpageLike:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
            
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                time.sleep(0.5)

        elif TrueorFalse!=c.fulpageLike:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))  
                c.fulpageLike=c.fulpageLike-1
                if c.fulpageLike == TrueorFalse:
                    break  
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                time.sleep(0.5)
    
    def HastagPostLike(self):
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys('#'+c.HastagLike)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        time.sleep(2)
        PostsClass=self.browser.find_elements_by_class_name('v1Nh3')
        Posts=[]
        TrueorFalse=0
        if TrueorFalse==c.hastagfulpageLike:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
            
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                time.sleep(0.5)

        elif TrueorFalse!=c.hastagfulpageLike:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))  
                c.hastagfulpageLike=c.hastagfulpageLike-1
                if c.hastagfulpageLike == TrueorFalse:
                    break  
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
                time.sleep(0.5)
        
    def HastagPostCommand(self):
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.HastagCommand)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        time.sleep(2)
        PostsClass=self.browser.find_elements_by_class_name('v1Nh3')
        Posts=[]
        TrueorFalse=0

        if TrueorFalse==c.hastagfulpagecommand:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                print(Posts)
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.HastagPageCommads[random.randint(0,len(c.HastagPageCommads)-1)])
                time.sleep(2)
                self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()      
                time.sleep(3)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()

        elif TrueorFalse!=c.hastagfulpagecommand:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                c.hastagfulpagecommand=c.hastagfulpagecommand-1
                if c.hastagfulpagecommand == TrueorFalse:
                    break
            
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.HastagPageCommads[random.randint(0,len(c.HastagPageCommads)-1)])
                time.sleep(2)
                self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()      
                time.sleep(3)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()               

    def DeleteNotFollow(self):
        Browser.followingList(self)
        time.sleep(2)
        Browser.followersList(self)
        time.sleep(2)
        Browser.unfollowList(self)
        time.sleep(2)
        os.remove("Users/following.txt")
        os.remove("Users/followers.txt")
        self.browser.get(self.link+ui.username)
        with open("Users/unfollow.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())
            for user in nameSet1:
                print(user)
                time.sleep(2)
                self.browser.get(self.link+user)
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                time.sleep(2)

            os.remove('Users/unfollow.txt')



    def DowonloadHastagsFullPicture(self):
        
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.DowondloadHastagsPicture)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        time.sleep(2)

        images=self.browser.find_elements_by_tag_name('img')
        images=[image.get_attribute('src') for image in images] 

        for image in images:
            imageJpg=open("image.txt","a")
            imageJpg.write(image+"\n")

        with open("image.txt","r",encoding="utf-8") as file:
            nameset1=set(file.read().splitlines())
            for img_url in nameset1:
                name=random.randrange(1,1000000)
                fulname="picture/"+str(name)+".jpg"
                urllib.request.urlretrieve(img_url,fulname)

        os.remove("images.txt")

    def DowondloadUserPicture(self):
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.DowondloadUserPicture)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        time.sleep(2)

        images=self.browser.find_elements_by_tag_name('img')
        images=[image.get_attribute('src') for image in images] 

        for image in images:
            imageJpg=open("image.txt","a")
            imageJpg.write(image+"\n")

        with open("image.txt","r",encoding="utf-8") as file:
            nameset1=set(file.read().splitlines())
            for img_url in nameset1:
                name=random.randrange(1,1000000)
                fulname="picture/"+str(name)+".jpg"
                urllib.request.urlretrieve(img_url,fulname)
              
            
                
        os.remove("image.txt")

    def UserNewFollowDM(self):
        Browser.followersList(self)
        Browser.followingList(self)
        Browser.messageList(self)
        os.remove('Users/followers.txt')
        os.remove('Users/following.txt')
        self.browser.get('https://www.instagram.com/direct/inbox/')
        with open("Users/newFollower.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())
            for user in nameSet1:
                self.browser.get('https://www.instagram.com/direct/inbox/')
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
                print(user)
                self.browser.find_element_by_xpath('//input[@name="queryBox"]').send_keys(user)
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[2]/div/div[3]/button/span').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(c.newUserMessage)
                time.sleep(10)
                print(user)
                time.sleep(2)
                self.browser.get(self.link+user)
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button').click()
                time.sleep(2)                      
            os.remove('Users/newFollower.txt')       
     

    def userUnFollowDM(self):
        Browser.followersList(self)
        Browser.followingList(self)
        Browser.unfollowList(self)
        os.remove('Users/followers.txt')
        os.remove('Users/following.txt')
        
        self.browser.get('https://www.instagram.com/direct/inbox/')
        with open("Users/unfollow.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())
            for user in nameSet1:
                self.browser.get('https://www.instagram.com/direct/inbox/')
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
                print(user)
                time.sleep(2)
                self.browser.find_element_by_xpath('//input[@name="queryBox"]').send_keys(user)
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[2]/div/div[3]/button').click()
                time.sleep(2)                      
                self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(c.lostUserMessage)
                time.sleep(2)
                self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                time.sleep(2)
        os.remove('Users/unfollow.txt')

    def DmDelete(self):
        self.browser.get('https://www.instagram.com/direct/inbox/')
        Browser.scrollDown2(self)
    
        followers= self.browser.find_elements_by_css_selector('.-qQT3.rOtsg')
      
        for follow in followers:
            self.browser.find_element_by_class_name('-qQT3').click()
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button').click()
            time.sleep(3)
            self.browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button').click()
            time.sleep(3)
            self.browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/button[1]').click()
            time.sleep(3)
            self.browser.get('https://www.instagram.com/direct/inbox/')
            time.sleep(3)
            print(follow)

    #GENERAL COMMANDS
    def scrollDown(self):
        jsCommand="""
        page = document.querySelector(".isgrP");
        page.scrollTo(0,page.scrollHeight);
        var pageAnd= page.scrollHeight;
        return pageAnd;
        """
        pageAnd=self.browser.execute_script(jsCommand)
        while True:
            finish=pageAnd
            time.sleep(1)
            pageAnd=self.browser.execute_script(jsCommand)
            if finish == pageAnd:
                break

    def followingList(self):
        self.browser.get(self.link+ui.username)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(2)
        Browser.scrollDown(self)
        following=self.browser.find_elements_by_css_selector('.FPmhX.notranslate._0imsa')
        for followings in following:
            
            followingTxt=open("Users/following.txt","a")
            followingTxt.write(followings.text+"\n")

    def followersList(self):
        self.browser.get(self.link+ui.username+'/')
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        Browser.scrollDown(self)
        followers= self.browser.find_elements_by_css_selector('.FPmhX.notranslate._0imsa')

        for follow in followers:
            follwersTxt=open("Users/followers.txt","a")
            follwersTxt.write(follow.text+"\n")

    def unfollowList(self):
        with open("Users/following.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())

        with open("Users/followers.txt", "r", encoding="utf-8") as file:
            nameSet2 = set(file.read().splitlines())
            
        with open("Users/unfollow.txt", "w", encoding="utf-8") as file:
            for value in nameSet1.difference(nameSet2):   
                file.write(value + "\n")

    def messageList(self):
        with open("Users/following.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())

        with open("Users/followers.txt", "r", encoding="utf-8") as file:
            nameSet2 = set(file.read().splitlines())
            
        with open("Users/newFollower.txt", "w", encoding="utf-8") as file:
            for value in nameSet2.difference(nameSet1):   
                file.write(value + "\n")

    
                

    def scrollDown2(self): #Dm Scroll
        jsCommand="""
        page = document.querySelector(".N9abW");
        page.scrollTo(0,page.scrollHeight);
        var pageAnd= page.scrollHeight;
        return pageAnd;
        """
        pageAnd=self.browser.execute_script(jsCommand)
        while True:
            finish=pageAnd
            time.sleep(1)
            pageAnd=self.browser.execute_script(jsCommand)
            if finish == pageAnd:
                break