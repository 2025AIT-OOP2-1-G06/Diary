from diaries.DiarySample import DiarySample
from diaries.ganbaruruDiary import ganbaruruDiary
from diaries.WapponDiary import WapponDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
	DiarySample(), 
	ganbaruruDiary(),
	WapponDiary()
]

for d in diaries:
	print("---------------------------------")
	print(d.get_date())
	print(d.get_summary())
	print(d.get_author())
	print()