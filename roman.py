class Solution:
	def romanToInt(self, s: str)-> int:
		roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
		num = 0
		for i in range(len(s)):
			num = num + roman[s[i]]
			print(roman[s[i]])
		return num


solution = Solution()

print(solution.romanToInt("XXI"))
