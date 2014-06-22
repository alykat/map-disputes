# This script uses capturejs - install: npm install -g capturejs
# It also uses PIL to crop images - install: pip install PIL
# Execute: python grab_images.py
import subprocess
import os
import Image
import datetime

#TODO (jos) read this data from somewhere

locations = {
    'Arunachal_Pradesh_us': 'https://www.google.com/maps/@27.06,93.37,9z',
    'Arunachal_Pradesh_co.in': 'https://www.google.co.in/maps/@27.06,93.37,9z',
    'Arunachal_Pradesh_cn': 'http://ditu.google.cn/maps?ll=27.06,93.37&z=9',
    'Tirpani_and_Bara_Hotii_valleys_us': 'https://www.google.com/maps/@31.2763226,79.1074097,9z',
    'Tirpani_and_Bara_Hotii_valleys_co.in': 'https://www.google.co.in/maps/@31.2763226,79.1074097,9z',
    'Tirpani_and_Bara_Hotii_valleys_cn': 'http://ditu.google.cn/maps?ll=31.2763226,79.1074097&z=9',
    'Demchok_us': 'https://www.google.com/maps/@32.7,79.14,9z',
    'Demchok_co.in': 'https://www.google.co.in/maps/@32.7,79.14,9z',
    'Demchok_cn': 'http://ditu.google.cn/maps?ll=32.7,79.14&z=9',
    'Jammu_and_Kashmir_us': 'https://www.google.com/maps/@33.45,76.24,7z',
    'Jammu_and_Kashmir_co.in': 'https://www.google.co.in/maps/@33.45,76.24,7z',
    'Shaksam_Valley_us': 'https://www.google.com/maps/@36.109167,76.646667,9z',
    'Shaksam_Valley_co.in': 'https://www.google.co.in/maps/@36.109167,76.646667,9z',
    'Shaksam_Valley_cn': 'http://ditu.google.cn/maps?ll=36.109167,76.646667&z=9',
    'Aksai_Chin_us': 'https://www.google.com/maps/@35.117,79.133,8z',
    'Aksai_Chin_co.in': 'https://www.google.co.in/maps/@35.117,79.133,8z',
    'Aksai_Chin_cn': 'http://ditu.google.cn/maps?ll=35.117,79.133&z=8',
    'Azad_Kashmir_and_Gilgit_Baltistan_us': 'https://www.google.com/maps/@35.2133333,75.6530469,7z',
    'Azad_Kashmir_and_Gilgit_Baltistan_co.in': 'https://www.google.co.in/maps/@35.2133333,75.6530469,7z',
    'Pinnacle_Islands_us': 'https://www.google.com/maps/@25.8155818,124.0006896,7z',
    'Pinnacle_Islands_co.jp': 'https://www.google.co.jp/maps/@25.8155818,124.0006896,7z',
    'Pinnacle_Islands_com.tw': 'https://www.google.com.tw/maps/@25.8155818,124.0006896,7z',
    'Pinnacle_Islands_cn': 'http://ditu.google.cn/maps?ll=25.8155818,124.0006896&z=7',
    'Siachen_Glacier_us': 'https://www.google.com/maps/@35.421226,77.10954,8z',
    'Siachen_Glacier_us': 'https://www.google.co.in/maps/@35.421226,77.10954,8z',
    'Crimea_us': 'https://www.google.com/maps/@45.3,34.4,8z',
    'Crimea_ru': 'https://www.google.ru/maps/@45.3,34.4,8z',
    'Crimea_com.ua': 'https://www.google.com.ua/maps/@45.3,34.4,8z',
    'Spratly_Islands_us': 'https://www.google.com/maps/@14.349548,116.630859,5z',
    'Spratly_Islands_com.tw': 'https://www.google.com.tw/maps/@14.349548,116.630859,5z',
    'Spratly_Islands_cn': 'http://ditu.google.cn/maps?ll=14.349548,116.630859&z=5',
    'Spratly_Islands_com.my': 'https://www.google.com.my/maps/@14.349548,116.630859,5z',
    'Spratly_Islands_com.ph': 'https://www.google.com.ph/maps/@14.349548,116.630859,5z',
    'Spratly_Islands_com.bn': 'https://www.google.com.bn/maps/@14.349548,116.630859,5z',
    'Bhutan_us': 'https://www.google.com/maps/@27.4705148,90.4578254,8z',
    'Bhutan_cn': 'http://ditu.google.cn/maps?ll=27.4705148,90.4578254&z=8',
    'Bhutan_bt': 'https://www.google.bt/maps/@27.4705148,90.4578254,8z'
}

directory = "./generated_images/"
timestamp_day = str(datetime.datetime.now()).split(' ')[0] + '_'

def grab_all_images():
    if not os.path.exists(directory):
          os.makedirs(directory)

    for loc in locations.keys():
        to_run = "capturejs --uri '" + locations[loc] + "' --viewportsize 1500x1500 --output '" + directory + timestamp_day + loc.lower() + ".png'"
        print to_run
        subprocess.call(to_run, shell=True)

def crop_images():
    for loc in locations.keys():
        im = Image.open(directory + timestamp_day + loc + '.png')
        # Magic numbers - trial and error to remove map interface widgets
        im.crop((500, 200, 1400, 1100)).save(directory + timestamp_day + loc.lower() + '.cropped.png', 'PNG')

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

