from plyer import notification
import time

if __name__ == '__main--':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is necessary for our health and for being at our best when we are working",
            app_icon="C:/Users/91628/Downloads/clock.ico",
            timeout=5
        )
        time.sleep(10)