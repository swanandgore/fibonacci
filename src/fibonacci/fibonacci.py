import logging, unittest


class Fibonacci :
	def __init__(s) :
		s.fibo = {0:0, 1:1, 2:1}
	def find(s, range_start, range_end) :
		fibo_series = []
		for num in range(range_start, range_end) :
			fibo_series.append( s.getNthFibonacci(num) )
		return fibo_series
	def getNthFibonacci(s, num) :
		assert num >= 0, "Fibonacci of negative numbers is undefined..."
		if s.fibo.has_key(num) :
			return s.fibo[num]
		else :
			s.fibo[num] = s.getNthFibonacci(num-1) + s.getNthFibonacci(num-2)
			return s.fibo[num]


class PrimeTester(unittest.TestCase) :
	def test_primes(s) :
		fibo = Fibonacci()
		s.assertEqual ( fibo.find(1,10) , [1, 1, 2, 3, 5, 8, 13, 21, 34, 12342345235] )


if __name__=="__main__" :
	unittest.main()
