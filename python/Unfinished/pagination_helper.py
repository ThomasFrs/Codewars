from math import *

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.collection = collection
      self.items_per_page = items_per_page
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
  
  # returns the number of pages
  def page_count(self):
      return ceil(self.item_count()/self.items_per_page)
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      split_collection = []
      for i in range(self.page_count()):
        page[i] = {}
        for j in range(self.items_per_page):
          if len(split_collection) < self.item_count():
            split_collection.append(j)
          
      print(split_collection)
  
  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
    return floor()

page = PaginationHelper(['a','b','c','d','e','f'], 4)
print(page.item_count(), page.page_count())