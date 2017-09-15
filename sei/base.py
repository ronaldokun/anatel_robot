#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:44:15 2017

@author: ronaldo
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from contextlib import contextmanager

from locators import LoginLocators



class Page(object):
    # assumes self.driver is a selenium webdriver
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30        
         
        
    def close(self):
        self.driver.close()
        
    @contextmanager
    # Only used when navigating between different types of Pages == != titles
    def wait_for_page_load(self):
        old_page = self.driver.find_element_by_tag_name('title')
        yield
        WebDriverWait(self.driver, self.timeout).until(
            EC.staleness_of(old_page)
        )    
        
    def find_element(self, *locator):
        return self.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def check_element_exists(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
    
    def wait_for_element(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(*locator))
        
    def wait_for_element_to_click(self, *locator):
        return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(*locator))
