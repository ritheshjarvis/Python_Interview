driver = Login().login_with_url("10.9.192.67",'bdadmin','Passw0rd12345#')
time.sleep(10)
shadow_driver = driver.find_element(By.CSS_SELECTOR, "div[id^='container-'][id*='-targetE'] > gz-header").shadow_root
shadow_driver = shadow_driver.find_element(By.CSS_SELECTOR,'gz-header-ui').shadow_root
shadow_driver = shadow_driver.find_element(By.CSS_SELECTOR,"gz-tooltip[tooltiptext='Notifications']>button").click()
# shadow_driver.find_element(By.CSS_SELECTOR,'button').click()
time.sleep(10)
notification_page = Notifications(driver)
# notification_page.click_icon_notification_bell()
print('Bell icon clicked')
notification_page.click_link_notification_all()
print('Notification clicked')
notification_page.click_antimalware_event()
print("----- Fetching Start ------------->")
notification_details = notification_page.fetch_antimalware_event_details()
print(notification_details)

