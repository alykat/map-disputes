# This script uses capturejs - install: npm install -g capturejs
# Execute: python grab_images.py
import subprocess
import os

#TODO (jos) read this data from somewhere
locations = {
  'crimea_ru': 'https://www.google.ru/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda',
  'crimea_us': 'https://www.google.com/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda',
  'crimea_es': 'https://www.google.es/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda'
}

def grab_all_images():
    directory = "./generated_images/"
    if not os.path.exists(directory):
          os.makedirs(directory)

    for loc in locations.keys():
        to_run = "capturejs --uri " + locations[loc] + " --viewportsize 1500x1500 --output '" + directory + loc + ".png'"
        print to_run
        subprocess.call(to_run, shell=True)
        print "end"

    print "Done!"

try:
    subprocess.check_call(['capturejs']);
except subprocess.CalledProcessError:
    # the call to capturejs should fail cause no arguments are passed, but we are
    # good to go (the tool is installed).
    grab_all_images()
except OSError:
    print 'Please install capturejs: npm install -g capturejs'

