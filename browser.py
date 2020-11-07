from selenium import webdriver
import time
import userınfo as ui
import control as c

PATH ="/home/ilkayus/path/chromedriver"


class Browser:
    def __init__(self,link):
        self.link=link
        self.browser=webdriver.Chrome(PATH)
        Browser.loginInstagram(self)
        # Browser.followersList(self) -------> Followers lıst
        # Browser.followingList(self) -------> Following List
        # Browser.followingList(self)
        # Browser.userPostLike(self)  #-------> User FulPage Like
        Browser.userPostCommand(self)





    def loginInstagram(self):
        self.browser.get(self.link)
        time.sleep(3)
        username = self.browser.find_element_by_name("username")                           #---------> Instagram User Name
        password =self.browser.find_element_by_name("password")
        loginBtn = self.browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')   #---------> Instagram Password
        username.send_keys(ui.username)
        password.send_keys(ui.password)
        loginBtn.click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        time.sleep(2)
        

    # def unfollow(self):
    #     self.browser.get(self.link+ui.username+'/')
    #     self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    #     time.sleep(3000)
    #     Browser.scrollDown(self)
        
    #     with open("following.txt", "r", encoding="utf-8") as file:    
    #         nameSet1 = set(file.read().splitlines())

    #     with open("followers.txt", "r", encoding="utf-8") as file:
    #         nameSet2 = set(file.read().splitlines())

                 




    #BASIC COMMANDS
    def userPostCommand(self):
        self.browser.find_element_by_xpath('//input[@type="text"]').send_keys(c.UsertPostLike)
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]').click()
        time.sleep(2)
        PostsClass=self.browser.find_elements_by_class_name('v1Nh3')
        Posts=[]
        TrueorFalse=0

        if TrueorFalse==c.fulpage:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                print(Posts)
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
                
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.CommandList[0])
                time.sleep(2)
                self.browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button").click()      
                time.sleep(3)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()

        elif TrueorFalse!=c.fulpage:
            for i in PostsClass:
                Posts.append(i.find_element_by_tag_name('a'))
                c.fulpage=c.fulpage-1
                if c.fulpage == TrueorFalse:
                    break
            
            for i in Posts:
                i.click()
                time.sleep(2)
                self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                time.sleep(2)
                
                self.browser.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(c.CommandList[0])
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
        for i in PostsClass:
            Posts.append(i.find_element_by_tag_name('a'))
        
        for i in Posts:
            i.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
            time.sleep(2)
            self.browser.find_element_by_xpath('/html/body/div[5]/div[3]/button').click()
            time.sleep(0.5)

        time.sleep(5000)




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
            
            followingTxt=open("following.txt","a")
            followingTxt.write(followings.text+"\n")

    def followersList(self):
        self.browser.get(self.link+ui.username+'/')
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(3)
        Browser.scrollDown(self)
        followers= self.browser.find_elements_by_css_selector('.FPmhX.notranslate._0imsa')

        for follow in followers:
            follwersTxt=open("followers.txt","a")
            follwersTxt.write(follow.text+"\n")

    def unfollowList(self):
        with open("following.txt", "r", encoding="utf-8") as file:    
            nameSet1 = set(file.read().splitlines())

        with open("followers.txt", "r", encoding="utf-8") as file:
            nameSet2 = set(file.read().splitlines())
            
        with open("unfollow.txt", "w", encoding="utf-8") as file:
            for value in nameSet1.difference(nameSet2):   
                file.write(value + "\n")