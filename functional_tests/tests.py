from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time  
from selenium.webdriver.common.by import By
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10 #(1)


class NewVisitorTest(LiveServerTestCase): 

	def setUp(self): 
		self.browser = webdriver.Chrome()            

	def tearDown(self): 
		self.browser.quit()

	def wait_for_row_in_list_table(self, row_text):
		start_time = time.time()
		while True: #(2)
			try:
				table = self.browser.find_element(By.ID,'id_list_table') #(3)
				rows = table.find_elements(By.TAG_NAME,'tr') 
				self.assertIn(row_text, [row.text for row in rows])
				return #(4)
			except (AssertionError, WebDriverException) as e: #(5)
				if time.time() - start_time > MAX_WAIT: #(6)
					raise e #(6)
				time.sleep(0.5) #(5)


	def test_can_start_a_list_and_retrieve_it_later(self): 

		# 张三听说有一个在线待办事项的应用
		# 他去看了这个应用的首页                  
		self.browser.get(self.live_server_url) 

		# 他注意到网页的标题和头部都包含“To-Do"这个词          
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element(By.TAG_NAME,'h1').text  
		self.assertIn('To-Do', header_text)
		
		# 应用有一个输入待办事项的文本输入框
		inputbox = self.browser.find_element(By.ID,'id_new_item') 
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)

		# 他在文本输入框中输入了“Buy flowers"
		inputbox.send_keys('Buy flowers') 

		# 他按了回车键键后，页面更新了
		# 待办事项表格中显示了“1：Buy flowers" 
		inputbox.send_keys(Keys.ENTER) 
		self.wait_for_row_in_list_table('1: Buy flowers')

		

		# 页面中又显示了一个文本输入框，可以输入其他待办事项
		# 他输入了“Give a gift to Lisi" 
		inputbox = self.browser.find_element(By.ID,'id_new_item')
		inputbox.send_keys('Give a gift to Lisi')
		inputbox.send_keys(Keys.ENTER)
		
		# 页面再次更新，她的清单中显示了这两个待办事项
		self.wait_for_row_in_list_table('1: Buy flowers')
		self.wait_for_row_in_list_table('2: Give a gift to Lisi')

		# 张三想知道这个网站是否会记住她的清单
		# 他看到网站为他生成了一个唯一的URL
		self.fail('Finish the test!') 

		# 他访问那个URL，发现他的待办事项列表还在
		# 他满意的离开了

if __name__ == '__main__': 
	unittest.main()
