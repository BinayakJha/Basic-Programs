import time
from plyer.facades import notification
import pyttsx3
from plyer import notification


if __name__ == "__main__":
    while True:
        notification.notify(
            title="**Please Drink Water Now !!**",
            message="The U.S. National Academies Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon=".\water-drop.ico",
            timeout=2
        )

        engine = pyttsx3.init()

        engine.say("Please Drink Water Now")
        engine.runAndWait()

        time.sleep(60*60)