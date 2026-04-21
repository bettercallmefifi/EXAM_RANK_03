class Solution:
	def mergeList(self, list1: list[int], list2: list[int]) -> list[int]:
			if list1 is None:
				return sorted(list2)
			if list2 is None:
				return sorted(list1)
			
			final_list = []
			for i in list1:
				final_list.append(i)
			for j in list2:
				final_list.append(j)
			return sorted(final_list)

def main():
	answer = Solution()

	# Basic cases
	print(answer.mergeList([1, 3, 5, -1], [0, 8, 2, 1]))
	# [-1, 0, 1, 1, 2, 3, 5, 8]

	print(answer.mergeList([99, -22, 10, 9], []))
	# [-22, 9, 10, 99]

	# Both lists non-empty
	print(answer.mergeList([4, 2], [1, 3]))
	# [1, 2, 3, 4]

	# One list is None
	print(answer.mergeList(None, [5, 3, 1]))
	# [1, 3, 5]

	print(answer.mergeList([7, 6, 8], None))
	# [6, 7, 8]

	# Edge cases
	print(answer.mergeList([], []))
	# []

	print(answer.mergeList([1, 1, 1], [1, 1]))
	# [1, 1, 1, 1, 1]

	print(answer.mergeList([-5, -2], [-3, -1]))
	# [-5, -3, -2, -1]

main()