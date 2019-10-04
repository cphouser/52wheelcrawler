# Python script for finding wheels on row52.com

## Requirements:
* Selenium (tested with v2.53.2)
  * compatible browser and driver for browser (tested with Chromium v27.0.3626.121 and ChromeDriver v72.0.3626.121)
* Python3 (tested with v3.5.3)
compatibility note: script is configured to run on a headless raspberry pi using a virtual display and attempts to use pyvirtualdisplay with xvfb. [Install Instructions](http://www.knight-of-pi.org/python3-browser-tests-on-a-raspberry-pi-with-firefox-virtualdisplay-selenium-and-pytest/)

## Setup:
### Set Search URL
1. Go to row52.com and click "Search Vehicles". Enter any location data for the search (yard or zip) and click "Search". *No need to fill in vehicle specification fields.*
