# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # открывает браузер и  ждет в течение 3-х секунд, чтобы страница загрузилась
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()  # метод запускается после каждого теста. Он закрывает браузер

    def test_it_worked(self):
        self.browser.get(
            'http://localhost:8000')  # метод который проверяет, что название веб-страницы Welcome to Django
        self.assertIn('Welcome to Django', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
