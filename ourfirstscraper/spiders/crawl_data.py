import scrapy
from selenium import webdriver
import json
import re
import time


class Crawl_Data(scrapy.Spider):
    name = "hello_world"
    start_urls = ['https://www.w3schools.com']

    def parse(self, response):
        pass