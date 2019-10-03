from selenium import webdriver
from pyvirtualdisplay import Display
import csv
import sys
import datetime

def init():
    display = Display(visible=0, size=(800, 600))
    display.start()
    print('display started')

    driver = webdriver.Chrome()
    #driver.set_page_load_timeout(120)
    print('driver loaded')
    return driver

def main():
    driver = init()
    reference_dict = load_car_table('cars.csv')
    driver.get('https://row52.com/Search/Index?Page=1&MakeId=0&ModelId=0&Year=&Distance=50&Sort=dateadded&SortDirection=desc&ZipCode=95403&HasImage=&HasComment=&LocationId=&V1=&V2=&V3=&V4=&V5=&V6=&V7=&V8=&V9=&V10=&V11=&V12=&V13=&V14=&V15=&V16=&V17=&IsVin=false')
    end_date = datetime.datetime.strptime(sys.argv[1],'%m/%d/%y')
    while True:
        result_tups, more = results_from_page(driver, reference_dict, end_date)
        if more is False:
            break
        next_page(driver)
    driver.quit()

def results_from_page(driver, reference_dict, end_date):
    result_list = fetch_page(driver)
    result_tups = [clean_result(result) for result in result_list]
    #for make in reference_dict:
    #    print(make)
    #    for model in reference_dict[make]:
    #        print('--', *model, sep='\t')
    #    print('...')
    matching_results = []
    for result in result_tups:
        list_date = datetime.datetime.strptime(result[1], '%b %d, %Y')
        if list_date < end_date:
            return (matching_results, False)
        #result = result_tups[i]
        matches = check_matches(result, reference_dict)
        for match in matches:
            print(match)
        else: print("no matches for", result)
        if len(matches) > 0:
            result.append(matching_results)
    return (matching_results, True)
        
def check_matches(listing, ref_dict):
    year, make, model = listing[0]
    make = make.upper()
    model = model.upper()
    if ref_dict.get(make) is None: return []
    else:
        ref_makes = ref_dict[make]
        matches = []
        for ref_make in ref_makes:
            make_words = make.split()
            if all([ref_make[0].find(word) > 0 for word in make_words]) \
                    and in_year_range(year, ref_make[1], ref_make[2]):
                matches.append(ref_make)
                print(ref_make)
        return matches

def in_year_range(year, min_y, max_y):
    if int(year) >= min_y and int(year) <= max_y: return True
    else: return False


def load_car_table(filen):
    car_dict = {}
    with open(filen, 'r') as f:
        car_table = csv.reader(f)
        for row in car_table:
            name = row[0].split(maxsplit=1)
            if car_dict.get(name[0]) is None:
                car_dict.update({name[0]:[(name[1], *row[1:])]})
            else:
                current_item = car_dict[name[0]]
                current_item.append((name[1], *row[1:]))
                car_dict.update({name[0]: current_item})
    return car_dict

def next_page(driver):
    next_btn = driver.find_element_by_xpath("//input[@value='NEXT']")
    next_btn.click()

def fetch_page(driver):
    result_list = driver.find_elements_by_class_name('list-row')
    print('page retrieved')
    return(result_list)

def clean_result(result):
    link_elem = result.find_elements_by_tag_name('a')[1]
    l_url = link_elem.get_attribute('href')
    title = link_elem.text
    date = result.find_elements_by_tag_name('strong')[3].text
    return(title.split('\n'), date, l_url)
        
if __name__ == '__main__':
    main()
