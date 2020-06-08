#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
	def subtractProductAndSum(self, n: int) -> int:

	    # break the original number into chars
	    n_list = list(str(n))
	    n_len = len(n_list)
	    
	    sum_digits = 0
	    prod_digits = 1
	    
	    for i in range(n_len):
	        sum_digits = sum_digits + int(n_list[i])
	        prod_digits = prod_digits * int(n_list[i])
	    
	    return(prod_digits - sum_digits)