# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class IlpostscaraperPipeline:
    # def __init__(self):
    #     self.con = sqlite3.connect("ilpost_italy.db")
    #     self.cur = self.conn.cursor()

    # def create_table(self):
    #     self.cur.execute("""CREATE TABLE IF NOT EXISTS italy (

    #     )""")

    def process_item(self, item, spider):
        return item
