from selenium import webdriver
from selenium.webdriver.support.ui import Select
import json
from automation_constants import *
import os

script_dir = os.path.dirname(__file__)
rel_path = "./automation_data.json"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as f:
  data = json.load(f)

working_status_choice = int(input('''What is the working status ?
        1 >> Work From Home
        2 >> Work From Office
        3 >> On Leave
        4 >> Business Trip
        5 >> Weekend or Holiday
Enter your choice : ''').strip())

driver = ""
driver = webdriver.Firefox(executable_path=data['firefox_driver_path'])
driver.get(data['website'])

# Page 1
user_name = data['user_name']
user_name_xpath_action = driver.find_element_by_xpath('//*[@id="userName"]').send_keys(user_name)
print('Entering username :', user_name)

password = data['password']
password_xpath_action = driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
print('Entering password...')
print('Signing in...')
page1_submit_button_xpath = driver.find_element_by_xpath('//*[@id="da_verified"]').click()

# Page 2
current_city = data['user_details']['current_city']
current_city_xpath_action = driver.find_element_by_xpath('//*[@id="tx_currentCity"]').send_keys(current_city)
print('Entering city :', current_city)
current_state = data['user_details']['current_state']
current_state_xpath = Select(driver.find_element_by_xpath('//*[@id="tx_currentState"]'))
current_state_xpath.select_by_visible_text(current_state)
print('Selecting State :', current_state)

aarogya_setu_status = AarogyaSetuStatus.Safe
if data['user_details']['aarogya_setu_status'].lower() == "unsafe":
    aarogya_setu_status = AarogyaSetuStatus.Unsafe

aarogya_setu_app_xpath = Select(driver.find_element_by_xpath('//*[@id="aarogyaStatusid"]'))
aarogya_setu_app_xpath.select_by_visible_text(aarogya_setu_status.name)
print('Selecting AarogyaSetu Status :', aarogya_setu_status.name)

working_status = data['user_details']['working_status']
working_status_xpath = Select(driver.find_element_by_xpath('//*[@id="workStatus"]'))
working_status_xpath.select_by_visible_text(working_status)
print('Selecting Working status : ', working_status)

if working_status == "WFH":
    able_to_connect_vpn = True
    if able_to_connect_vpn == True:
        driver.find_element_by_xpath('//*[@id="isVpnIssue1"]').click()
    else:
        driver.find_element_by_xpath('//*[@id="isVpnIssue2"]').click()

    network_connection_type = NetworkConnectionType.Broadband
    if network_connection_type == NetworkConnectionType.Broadband:
        network_connection_xpath = Select(driver.find_element_by_xpath('//*[@id="tx_inetCon"]'))
        network_connection_xpath.select_by_visible_text(network_connection_type.name)
    # elif network_connection_type == NetworkConnectionType.DialUp:
    #     driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/form/div/table[1]/tbody/tr[5]/td[2]/select/option[2]').click()
    # else:
    #     driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/form/div/table[1]/tbody/tr[5]/td[2]/select/option[3]').click()
    
    able_to_connect_MobisON = True
    if able_to_connect_MobisON == True:
        driver.find_element_by_xpath('//*[@id="isConnectMobison1"]').click() # Yes
    else:
        driver.find_element_by_xpath('//*[@id="isConnectMobison2"]').click() # No

is_tested_covid_positive = False
if is_tested_covid_positive == True:
    driver.find_element_by_xpath('//*[@id="isTestedCovid1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isTestedCovid2"]').click() # No


is_body_temperature_abnormal = False
if is_body_temperature_abnormal == True:
    driver.find_element_by_xpath('//*[@id="isValidBodyTemp1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isValidBodyTemp2"]').click() # No

has_symptoms = False
if has_symptoms == True:
    driver.find_element_by_xpath('//*[@id="haveSymptoms1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="haveSymptoms2"]').click() # No

has_other_symptoms = False
if has_other_symptoms == True:
    driver.find_element_by_xpath('//*[@id="haveOtherSymptoms1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="haveOtherSymptoms2"]').click() # No

has_14day_travel_history = False
if has_14day_travel_history == True:
    driver.find_element_by_xpath('//*[@id="travelhistory_yes"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="travelhistory_no"]').click() # No

has_attended_public_gathering_or_function = False
if has_attended_public_gathering_or_function == True:
    driver.find_element_by_xpath('//*[@id="is_attended_yes"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="is_attended_no"]').click() # No

has_family_attended_public_gathering_or_function = False
if has_family_attended_public_gathering_or_function == True:
    driver.find_element_by_xpath('//*[@id="is_family_attended_yes"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="is_family_attended_no"]').click() # No

is_family_tested_covid_positive = False
if is_family_tested_covid_positive == True:
    driver.find_element_by_xpath('//*[@id="isFamilyTestedCovid1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isFamilyTestedCovid2"]').click() # No

is_family_health_issue = False
if is_family_health_issue == True:
    driver.find_element_by_xpath('//*[@id="isfamilyillIssue1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isfamilyillIssue2"]').click() # No

is_building_in_containtment_zone = False
if is_building_in_containtment_zone == True:
    driver.find_element_by_xpath('//*[@id="isContainmentZone1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isContainmentZone2"]').click() # No

is_neighbours_tested_covid_positive = False
if is_neighbours_tested_covid_positive == True:
    driver.find_element_by_xpath('//*[@id="isNeighbourTestedCovid1"]').click() # Yes
else:
    driver.find_element_by_xpath('//*[@id="isNeighbourTestedCovid2"]').click() # No

validate_form = True
if validate_form == True:
    driver.find_element_by_xpath('//*[@id="isFormValidCheck"]').click() # Accept
print('Validating form...')

page2_submit_button_xpath_action = driver.find_element_by_xpath('//*[@id="saveCovidDetails"]').click()

signout_xpath_action = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/table/tbody/tr[2]/td/a').click() # signing out

driver.quit() # closing browser
