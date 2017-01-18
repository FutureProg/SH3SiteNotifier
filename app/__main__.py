"""
This application checks the COMPSCI3SH3 website and checks for changes.
Then shows an OSX notification linking to the change.
Requires terminal-notifier to run
"""
NOTIFIER_VERSION = "1.7.1"

import os
import time

if __name__ == "__main__":
    # Check if system connected to internet
    import http.client as httpclient
    CONNECTION = httpclient.HTTPConnection("www.google.com", timeout=5)
    RESULT = False
    try:
        CONNECTION.request("HEAD", "/")
        CONNECTION.close()
        RESULT = True
    except:
        CONNECTION.close()

    if RESULT:
        # RUN PROGRAM
        numlines = 0
        try:
            with open("announcements.csv") as f:
                for line in f:
                    numlines += 1
                os.system("rm announcements.csv")
        except FileNotFoundError:
            numlines = -1

        os.system("scrapy runspider app/announce.py -o announcements.csv") # Run the spider        

        # Check the number of lines in the newly downloaded announcements
        newlines = 0
        lines = []
        with open("announcements.csv") as f:
            lines = f.readlines()
            newlines = len(lines)

        if newlines > numlines:
            # if there are new announcements, show a notification
            print("Showing notification: {0}".format(lines[1]))
            command = "/usr/local/Cellar/terminal-notifier/{0}/bin/terminal-notifier -title '3SH3 New Announcement' -message '{1}' -open 'http://www.cas.mcmaster.ca/~pophlin/teaching/cs3sh3/announcements.html' -sender com.nick.sh3siteparser -timeout 10".format(NOTIFIER_VERSION, lines[1])
            os.system("echo '{0}' >> log.out".format(lines[1]))
            os.system("echo 'Showing notification' >> log.out")
            os.system(command)
            #os.system("python2 app/notification.py \"{0}\"".format(lines[1]))
        time.sleep(10)

