import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink Water Now",
            message="Average of 3.7 liters a day for men and 2.7 liters for women, depending on climate, activity, pregnancy status, and health",
            app_icon= r"C:\Users\Isha Gupta\Desktop\imp\pylearn\waterrem\Iconsmind-Outline-Glass-Water.ico",
            timeout=10
        )
        time.sleep(60*60)
