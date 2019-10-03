from selenium import webdriver
from pyvirtualdisplay import Display
import csv

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
    result_list = fetch_page(driver)
    result_tups = [clean_result(result) for result in result_list]
    reference_dict = load_car_table('cars.csv')
    #for make in reference_dict:
    #    print(make)
    #    for model in reference_dict[make]:
    #        print('--', *model, sep='\t')
    #    print('...')
    for result in result_tups:
        print(result)
    driver.quit()

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

def fetch_page(driver):
    driver.get('https://row52.com/Search/Index?Page=1&MakeId=0&ModelId=0&Year=&Distance=50&Sort=dateadded&SortDirection=desc&ZipCode=95403&HasImage=&HasComment=&LocationId=&V1=&V2=&V3=&V4=&V5=&V6=&V7=&V8=&V9=&V10=&V11=&V12=&V13=&V14=&V15=&V16=&V17=&IsVin=false')
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
