from selenium import webdriver
import time
import warnings

warnings.filterwarnings("ignore")
driver = webdriver.Chrome("F:\\Interview\\FirstSeleniumTest\\drivers\\chromedriver.exe")
time.sleep(3)
driver.get("https://www.gsmarena.com/")
print("Title is:" + driver.title)
driver.maximize_window()
# by searching apple
# driver.find_element_by_xpath("//input[@id='topsearch-text']").click()
# driver.find_element_by_xpath("//input[@id='topsearch-text']").send_keys("apple")
# driver.find_element_by_xpath("//header/div[1]/div[1]/div[2]/form[1]/div[2]/a[1]").click()

# by clicking on apple
driver.find_element_by_xpath("//*[@id='body']/aside/div[1]/ul/li[2]/a").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/6)")
time.sleep(2)

test_path = "F:\\Interview\\FirstSeleniumTest\\Test\\PngFile\\"
test_path2 = "F:\\Interview\\FirstSeleniumTest\\Test\\Text File\\"
for p in range(3):
    for product in range(40):
        phoneName = driver.find_element_by_xpath(f"//*[@id='review-body']/div[1]/ul/li[{product+1}]/a/strong/span").text
        driver.find_element_by_xpath(f"//*[@id='review-body']/div[1]/ul/li[{product+1}]/a/strong/span").click()
        fileName = phoneName + '.png'
        with open(test_path + fileName, 'wb') as file:    #creating png file  using file name
            file.write(driver.find_element_by_xpath("//*[@id='body']/div/div[1]/div/div[2]/div/a/img").screenshot_as_png)
        fileName2 = phoneName + '.txt'
        with open(test_path2 + fileName2, 'w', encoding="utf-8") as f:  #creating text file  using file name
            for i in range(15):
                value = driver.find_elements_by_xpath("//*[@id='specs-list']/table[{}]".format(i))
                for j in value:
                    f.write(j.text)
            driver.back()
    driver.find_element_by_xpath(f"//*[@id='body']/div/div[3]/div[1]/a[{p+1}]").click()

driver.quit()
