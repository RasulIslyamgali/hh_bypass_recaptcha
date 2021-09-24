from pyPythonRPA._webtools import byWeb
import speech_recognition as sr
from pydub import AudioSegment
import requests
import os
from time import sleep
import schedule
import time


def bypass_recaptcha():
    filename = r"C:\Users\Admin\Downloads" + "\\audio.mp3"
    print("filename: ", filename)

    sound = AudioSegment.from_mp3(filename)

    sound.export(os.getcwd() + "\\audio.wav", format="wav")

    audio_file = os.getcwd() + "\\audio.wav"

    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as mp3:
        audio_data = r.record(mp3)
        text = r.recognize_google(audio_data)
        print("extract text: ", text)
    return text


path = r"C:\Users\Admin\Desktop\Programming\Python\PROJECTS\hh_RPA\Resources\chrome-win\chrome.exe"
if __name__ == "__main__":
    def hh_update_summary_in_search():
        driver = byWeb()
        driver.get("https://hh.kz/")
        driver.get("https://hh.kz/account/login?backurl=%2F")
        # driver.find_element('//div[@class="supernova-navi-item supernova-navi-item_lvl-2 supernova-navi-item_button supernova-navi-item_no-mobile supernova-navi-item_dashboard "]//a[1][@class="supernova-button "]').click()
        driver.find_element('//span[contains(text(), "Войти с")]').click()
        driver.find_element('//input[@placeholder="Email или телефон"]').send_keys("login")
        driver.find_element('//input[@placeholder="Пароль"]').send_keys("password")
        driver.find_element('//span[text()="Войти"]').click()


        name = driver.find_element('//iframe[@title="reCAPTCHA"]').get_attribute("name")
        print(name)
        driver.webdriver.switch_to.frame(name)
        print("find")
        driver.find_element('//span[@class="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox"]').click()
        driver.webdriver.switch_to.default_content()
        # login button
        try:
            driver.find_element('//button[@data-qa="account-login-submit"]').click()
            el = driver.find_elements(('//iframe[@title="проверка recaptcha"]')[2])
            n = 0
            while not el:
                el = driver.find_elements(('//iframe[@title="проверка recaptcha"]')[2])
                print("search frame. attempt ", n)
                sleep(1)
                if n == 15 or el == True:
                    break
            if el:
                raise Exception
        except Exception as e:
            print(e)
            # в последний раз ничего распознавать не требовалось. тут надо будет скачать mp3 файл
            # func for extract text from mp3 already exist
            name = driver.find_element('//iframe[@title="проверка recaptcha"]').get_attribute("name")
            driver.webdriver.switch_to.frame(name)
            print("find frame for check recaptcha")
            driver.find_element('//button[@class="rc-button goog-inline-block rc-button-audio"]').click()
            # arrow
            # https://stackoverflow.com/questions/65813792/recaptcha-download-audio-file
            driver.find_element('//a[@class="rc-audiochallenge-tdownload-link"]').click()

            # download mp3
            driver.switch_to.window(driver.webdriver.window_handles[-1])
            link = driver.current_url()
            print("current url: ", link)

            # close window
            # try:
            # driver.switch_to.window("Вход в личный кабинет")
            driver.switch_to.window(driver.webdriver.window_handles[0])
            # except Exception as e:
            #     print('window err: ', e)


            r = requests.get(link)
            content = r.content
            with open("audio1.mp3", "wb") as audio:
                audio.write(content)

            # extract text from mp3
            import speech_recognition as sr
            import os
            from pydub import AudioSegment
            # filename = r"C:\Users\Admin\Downloads" + "\\audio1.mp3"
            # print("filename: ", filename)

            from pydub import AudioSegment
            # AudioSegment.ffmpeg = os.getcwd()
            sleep(2)
            sound = AudioSegment.from_mp3("audio1.mp3")

            sound.export(os.getcwd() + "\\audio.wav", format="wav")

            audio_file = os.getcwd() + "\\audio.wav"

            r = sr.Recognizer()

            with sr.AudioFile(audio_file) as mp3:
                audio_data = r.record(mp3)
                # use the text for recaptcha
                text = r.recognize_google(audio_data)
                print("extract text: ", text)

            # send text
            # driver.find_element('//input[@id="audio-response"]').click()
            name = driver.find_element('//iframe[@title="проверка recaptcha"]').get_attribute("name")
            driver.switch_to.frame(name)

            driver.find_element('//input[@id="audio-response"]').send_keys(text)
            # driver.find_elements('(//button[@class="rc-button-default goog-inline-block"])[2]').click()
            driver.find_element('//button[@id="recaptcha-verify-button"]').click()
            driver.webdriver.switch_to.default_content()
            # login
            driver.find_element('//button[@data-qa="account-login-submit"]').click()
            os.remove(os.path.join(os.getcwd(), "audio1.mp3"))
            os.remove(os.path.join(os.getcwd(), "audio.wav"))

        # my resumes
        driver.find_element('//a[@data-qa="mainmenu_myResumes"]').click()

        # up in search
        driver.find_element('//button[text()="Поднять в поиске"]').click()
        # input('e')
        driver.quit()
        print("end")


    schedule.every(250).minutes.do(hh_update_summary_in_search())

    while True:
        schedule.run_pending()
        time.sleep(1)

    # hh_update_summary_in_search()
