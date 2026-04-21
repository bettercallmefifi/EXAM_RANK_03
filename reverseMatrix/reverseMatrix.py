def reverseMatrix(lst : list[list[int]]) -> list[list[int]]:
    return [e[::-1] for e in lst]

def main():
    # Basic cases
	print(reverseMatrix([[1, 2], [3, 4]]))        
	# [[2, 1], [4, 3]]

	print(reverseMatrix([[1, 2, 3], [4, 5, 6]]))  
	# [3, 2, 1], [6, 5, 4]]

	# Single row
	print(reverseMatrix([[1, 2, 3, 4]]))          
	# [[4, 3, 2, 1]]

	# Single column
	print(reverseMatrix([[1], [2], [3]]))         
	# [[1], [2], [3]]

	# Edge cases
	print(reverseMatrix([[1]]))                   
	# [[1]]

	print(reverseMatrix([]))                      
	# []

	# Larger matrix
	print(reverseMatrix([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]))
	# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

main()