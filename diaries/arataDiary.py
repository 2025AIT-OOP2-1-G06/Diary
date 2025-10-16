from diaries.AbstractDiary import AbstractDiary
from diaries.arataDiary import AbstractDiary

class DiarySample(AbstractDiary):
	def get_date(self):
		return "2021-12-02"
	def get_summary(self):
		return "なんてことない一日だった"
	def get_author(self):
		return "Sample"
