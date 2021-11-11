import os

URL_ANDROID = 'http://127.0.0.1:4723/wd/hub'
CAPABILITY = {
    "platformName": "Android",
    "platformVersion": "8.1",
    "automationName": "Appium",
    "appPackage": "ru.mail.search.electroscope",
    "appActivity": "ru.mail.search.electroscope.ui.activity.AssistantActivity",
    "app": os.path.abspath(os.path.join(os.path.dirname(__file__),'stuff','Marussia_v1.50.2.apk')),
    "orientation": "PORTRAIT",
    "autoGrantPermissions": True
}