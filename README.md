# Python script for finding wheels on row52.com

## Requirements:
* Selenium (tested with v2.53.2)
  * compatible browser and driver for browser (tested with Chromium v27.0.3626.121 and ChromeDriver v72.0.3626.121)
* Python3 (tested with v3.5.3)

*compatibility note: script is configured to run on a headless raspberry pi using a virtual display and attempts to use pyvirtualdisplay with xvfb. [Install Instructions](http://www.knight-of-pi.org/python3-browser-tests-on-a-raspberry-pi-with-firefox-virtualdisplay-selenium-and-pytest/)*

## Setup:
### Set Search URL
1. Go to row52.com and click "Search Vehicles". Enter any location data for the search (yard or zip) and click "Search". *No need to fill in vehicle specification fields.*
2. Copy this url into an otherwise empty file and save as **search_url** (no file extension) in the same directoy as **part_search.py**
 
### Set Up Table of Vehicles
Create a CSV file named cars.csv (or modify the one included in the repository) with a list of all vehicles to search for and save it in same directory as **search_url** and **part_search.py** other files.

#### Format:
"MAKE MODEL_KEYWORDS",min_year,max_year,[notes] (last field unchecked but is returned with any matched listing)
*note: make and model keywords must be capitalized*
```
"DODGE RAIDER",1986,1989,"15 X 6,12 X 1.5,108"
"FORD COURIER PICKUP",1977,1984,"14 X 6,12 X 1.5,108.0"
"HONDA PASSPORT",1994,2003,"15 X 6,12 X 1.5,108"
"HUMMER H3, H3X, H3 ALPHA, BASE, LUXURY",2006,2008,"12 X 1.5,100.0"
"HYUNDAI ENTOURAGE",2007,2008,"12 X 1.5,95.3"
```
It is important that the make is a single word and separated from the model keywords by a space. The only make this should effect is "ALFA ROMEO". The included table was generated using [this list](http://www.wheelsupport.com/bolt-pattern-stud-pattern-6-x-139-7/), Sublime Text 3, and the Python 3 shell. A similar file can be written manually in excel or a similar program (export as csv).

## Running:
on Debian: *python3 part_search.py mm/dd/yy* where mm/dd/yy is the earliest date to return results from. This argument must be specified.
