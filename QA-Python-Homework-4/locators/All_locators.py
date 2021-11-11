from appium.webdriver.common.mobileby import MobileBy

class BasicLocators():
    #BUSTTON_ALLOW_PERMISSIOM = (MobileBy.ID, 'com.android.packageinstaller:id/permission_allow_button')
    BLOCK_OF_RUSSIA = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_content_block')
    CAROUSEL_FACT = (MobileBy.ID, 'ru.mail.search.electroscope:id/suggests_list')
    BUTTON_POPULATION_RUSSIAN = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"население россии")]')
    RESPONSE_POPULATION_RUSSIAN = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_title')
    RESPONSE_CALCULATE = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"{}")]')
    BLOCK_NEWS = (MobileBy.XPATH, '//android.widget.FrameLayout/android.view.ViewGroup')
    PLAYER_TRACK_NAME = (MobileBy.ID, 'ru.mail.search.electroscope:id/player_track_name')

class MainpageLocators(BasicLocators):
    BUTTON_VOICE_MAIN = (MobileBy.XPATH, '//android.view.ViewGroup/android.view.View')
    BUTTON_KEYBOARD = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    BUTTON_SETINGS = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')

class MainPagewithkeyboardLocators(BasicLocators):
    FIELD_SEARCH = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    BUTTON_SEND_TEXT = (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_send')
    BUTTON_INPUT_ACTION= (MobileBy.ID, 'ru.mail.search.electroscope:id/text_input_action')

class SettingsPageLocators():
    BUTTON_SOURCE_NEWS = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    BUTTON_ABOUT_APP = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')
    EXIT_SETTINGS = (MobileBy.XPATH, '//android.widget.LinearLayout[contains(@resource-id, "ru.mail.search.electroscope:id/user_settings_toolbar")]/android.widget.ImageButton')

class SourceNewsPageLocators():
    BUTTON_CHOICE_VESTE_FM = (MobileBy.XPATH,'//android.widget.FrameLayout[android.widget.TextView[contains(@text,"Вести FM")]]')
    CONFIRM_CHOICE = (MobileBy.ID, 'ru.mail.search.electroscope:id/news_sources_item_selected')
    RETURN_SETTINGS = (MobileBy.XPATH, '//android.widget.LinearLayout[contains(@resource-id, "ru.mail.search.electroscope:id/news_sources_toolbar")]/android.widget.ImageButton')

class AboutPageLocators():
    VERSION_APP = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    COPYRIGHT_APP = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_copyright')
    RETURN_SETTINGS = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_toolbar_back')


