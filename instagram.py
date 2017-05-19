from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import org.openqa.selenium.Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium

listoftags = ["algorithm","array","csharp","compiler",'css']

tags = "#programming"
baseurl = "http://instagram.com"
username = "instacoded"#"computerlaughs"#
password = "Gatswag1996"
loaded = 0

driver = webdriver.Chrome("/Users/chigoanyaso/PycharmProjects/afterawhile/chromedriver")
wait = WebDriverWait(driver, 10)
def inits():

    driver.get(baseurl)
    driver.maximize_window()

def go_to_loginPage():
    loginbutton = driver.find_element_by_class_name("_fcn8k")
    loginbutton.click()

def logincredentials():
    usernamebox = driver.find_element_by_name("username")
    passwordbox = driver.find_element_by_name("password")
    loginbutton = driver.find_element_by_class_name("_ah57t")
    usernamebox.clear()
    usernamebox.send_keys(username)
    passwordbox.clear()
    passwordbox.send_keys(password)
    loginbutton.click()

def search_tags(tag):
    searchbox = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_9x5sw")))
    searchbox.send_keys(tag)
    firstink = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_orhxc")))
    searchbox.send_keys(Keys.RETURN)
    firstink.click()

def performactionof_Follow():
    try:
        count = 0
        box = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_8mlbc")))
        # eachbox = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_8mlbc")))
        print("total num of links is ", len(box))
        for x in range(0, len(box)):
            try:
                if box[x].is_displayed():
                    # box[x].click()
                    # eachbox.click()
                    box[x].send_keys(Keys.RETURN)
                    box[x].send_keys(Keys.ENTER)


                #check for following
                    followbtn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_ah57t")))
                    boxcancel = driver.find_element_by_class_name("_3eajp")
                    if followbtn.text == "Follow":
                        count += 1
                        print("trueeee")
                        try:
                            print("trying to follow once")
                            followbtn.click()
                        except:
                            try:
                                print("trying to follow second time")
                                followbtn.send_keys(Keys.ENTER)
                            except:

                                print("trying to follow third time")
                                followbtn.send_keys(Keys.RETURN)


                    # boxcancel = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_3eajp")))

                        boxcancel.click()
                        # time.sleep(2)


                    else:
                        count += 1
                        # boxcancel = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_3eajp")))
                        boxcancel.click()
                        # time.sleep(2)

            except selenium.common.exceptions.WebDriverException as e:
                pass
                print(e)
        print(count)
        done()
    except selenium.common.exceptions.TimeoutException as e:
        print(e)
        re_request()
def done():
    try:
        global loaded
        print("Loading more!!!")
        loaded += 1
        print(loaded)
        if "" == "":
            loadmore = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_8imhp")))
            try:
                print("trying to follow once")
                loadmore.click()
            except:
                try:
                    print("trying to follow second time")
                    loadmore.send_keys(Keys.ENTER)
                except:
                    print("trying to follow third time")
                    loadmore.send_keys(Keys.RETURN)

            performactionof_Follow()
    except selenium.common.exceptions.TimeoutException as e:
        print(e)
        re_request()


def re_request():
    driver.get("http://instagram.com")
    newtag = input("new Tag? \n")
    if newtag != "done":
        tags = "#"+newtag
        search_tags(tags)
        performactionof_Follow()
    else:
        print("unfollowing now...")
        unfollow()


def unfollow():
    # inits()
    # go_to_loginPage()
    # logincredentials()
    """_soakw _vbtk2 """
    profilebtn = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "coreSpriteDesktopNavProfile")))
    profilebtn.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_218yx")))
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if elem.get_attribute("href") == "https://www.instagram.com/instacoded/followers/":
            followers = elem
            followers.click()
            print("Done")

    followerslinks = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "_ah57t")))
    for followbtn in followerslinks:
        if followbtn.text == "Following":
            try:
                print("trying to unfollow once")
                followbtn.click()
                time.sleep(2)
            except:
                try:
                    print("trying to unfollow second time")
                    followbtn.send_keys(Keys.ENTER)
                    time.sleep(2)
                except:

                    print("trying to unfollow third time")
                    followbtn.send_keys(Keys.RETURN)
                    time.sleep(2)




        else:
            print('passing...')
    print("doneee unfollowinh")
    # driver.get("https://www.instagram.com/"+username)
def follow():
    inits()
    go_to_loginPage()
    logincredentials()
    search_tags(tags)
    performactionof_Follow()
follow()
