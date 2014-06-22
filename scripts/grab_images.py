# This script uses capturejs - install: npm install -g capturejs
# It also uses PIL to crop images - install: pip install PIL
# Execute: python grab_images.py
import subprocess
import os
import Image
import datetime

#TODO (jos) read this data from somewhere
locations = {
  'crimea_ru': 'https://www.google.ru/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda',
  'crimea_us': 'https://www.google.com/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda',
  'crimea_es': 'https://www.google.es/maps/place/Crimea/@45.2935855,34.5598251,8z/data=!3m1!4b1!4m2!3m1!1s0x40ea518fe28653bd:0xa94eced30b92ffda'
}

directory = "./generated_images/"
timestamp_day = str(datetime.datetime.now()).split(' ')[0] + '_'

def grab_all_images():
    if not os.path.exists(directory):
          os.makedirs(directory)

    for loc in locations.keys():
        to_run = "capturejs --uri " + locations[loc] + " --viewportsize 1500x1500 --output '" + directory + timestamp_day + loc + ".png'"
        print to_run
        subprocess.call(to_run, shell=True)

def crop_images():
    for loc in locations.keys():
        im = Image.open(directory + timestamp_day + loc + '.png')
        # Magic numbers - trial and error to remove map interface widgets
        im.crop((500, 200, 1400, 1400)).save(directory + timestamp_day + loc + '.cropped.png', 'PNG')

try:
    subprocess.check_call(['capturejs']);
except subprocess.CalledProcessError:
    # the call to capturejs should fail cause no arguments are passed, but we are
    # good to go (the tool is installed).
    grab_all_images()
    crop_images()
    print 'Done!'
except OSError:
    print 'Please install capturejs: npm install -g capturejs'

