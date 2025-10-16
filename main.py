from diaries.DiarySample import DiarySample
from diaries.ganbaruruDiary import ganbaruruDiary
from diaries.WapponDiary import WapponDiary
from diaries.JinmaDiary import JinmaDiary
from diaries.arataDiary import arataDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
	DiarySample(), 
	ganbaruruDiary(),
	WapponDiary(),
    JinmaDiary(),
    arataDiary(),
]

for d in diaries:
	print("---------------------------------")
	print(d.get_date())
	print(d.get_summary())
	print(d.get_author())
	print()