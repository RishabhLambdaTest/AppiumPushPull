from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

from parallel12 import driver_init_1
desired_caps = {
    "deviceName": "Galaxy S20",
    "platformName": "Android",
    "platformVersion": "10",
    "app": "lt://APP10160591891684932168238931",  # Enter app_url here
    "isRealMobile": True,
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}
def startingTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "rishabhsinghlambdatest"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "7f4Xoi2I7A1H7f4Y84emKmZKhE0Cn440Obyy1WGIcud425cWei"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")
    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub") # type: ignore
        driver.push_file("/sdcard/Download/images/file.png","C:\\Users\\rishabhsingh\\Pictures\\Screenshots\\Screenshot 2023-05-12 125946.png")
        print("File Uploaded")
        driver.find_element("id","com.handycloset.android.jpegpng:id/loadButton").click()
        driver.find_element("id","com.android.permissioncontroller:id/permission_allow_button").click()
        driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.drawerlayout.widget.DrawerLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ImageView").click()
        file_content_base64 = driver.pull_file("/sdcard/Download/images/file.png")
        print("File Pulled")
        driver.quit()
    except:
        driver_init_1.quit()
startingTest()