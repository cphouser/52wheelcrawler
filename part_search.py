from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()
print('display started')

driver = webdriver.Chrome()
#driver.set_page_load_timeout(120)
print('driver loaded')

driver.get('https://row52.com/Search/Index?Page=1&MakeId=0&ModelId=0&Year=&Distance=50&Sort=dateadded&SortDirection=desc&ZipCode=95403&HasImage=&HasComment=&LocationId=&V1=&V2=&V3=&V4=&V5=&V6=&V7=&V8=&V9=&V10=&V11=&V12=&V13=&V14=&V15=&V16=&V17=&IsVin=false')
result_list = driver.find_elements_by_class_name('list-row')
print('page retrieved')

for result in result_list:
    print(result.find_element_by_tag_name('a').get_attribute('href'))
    print(result.find_elements_by_tag_name('strong')[3].text)
    print('\n')
#results = [tmp.text for tmp in result_list]

driver.quit()
