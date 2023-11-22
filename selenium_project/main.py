from selenium import webdriver
from selenium.webdriver.common.by import By

# To keep the Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.in/Lifelong-Dumbbells-Equipment-Exercise-Warranty/dp/B09W5PSTBP/?_encoding=UTF8"
           "&pd_rd_w=MdW2D&content-id=amzn1.sym.211684f4-ebe1-443f-8a4a-0773471e979f&pf_rd_p=211684f4-ebe1-443f-8a4a"
           "-0773471e979f&pf_rd_r=HM94XRZJN50HTNKVAT9R&pd_rd_wg=eapu8&pd_rd_r=d25eed39-ffa6-414f-93f6-30c7256c0edb"
           "&ref_=pd_gw_crs_zg_bs_1984443031&th=1")
price_rupees=driver.find_element(By.CLASS_NAME,value="a-price-whole")

print(f"The price is {price_rupees.text}")

# driver.close()
driver.quit()
