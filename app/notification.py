"""
Must be run with Python2
"""

import sys, os
#import objc
#from Foundation import NSUserNotification
#from Foundation import NSUserNotificationDefaultSoundName
#from argparse import ArgumentParser

#NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')


#command = "osascript -e 'display notification \"{0}\" with title \"3SH3 New Announcement\"'".format(sys.argv[1])
command = "terminal-notifier -title '3SH3 New Announcement' -message '{0}' -open 'http://www.cas.mcmaster.ca/~pophlin/teaching/cs3sh3/announcements.html'".format(sys.argv[1])
os.system("echo '{0}' >> log.out".format(sys.argv[1]))
os.system("echo 'Showing notification' >> log.out".format())
os.system(command)

"""parser = ArgumentParser(usage="-t TITLE -m MESSAGE")
parser.add_argument('-t', '--title', action="store", default="3SH3 New Announcement")
parser.add_argument('-m', '--message', action='store', default="\"{0}\"".format(sys.argv[1]))
parser.add_argument('--no-sound', action='store_false', default=False, dest='sound')

options, args = parser.parse_args()

notification = NSUserNotification.alloc().init()
notification.setTitle_("3SH3 New Announcement")
notification.setInformativeText_(sys.argv[1])
notification.setSoundName_(NSUserNotificationDefaultSoundName)

center = NSUserNotification.defaultUserNotificationCenter()
center.deliverNotification_(notification)"""
