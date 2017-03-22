def sqroot(val):
	start,end,ans,mid = 1,val,0,0
	while start <= end:
		if val == 1 or val == 0:
			return 1
		mid = (int)(start + end) / 2
		if(mid*mid == val):
			return mid
		if(mid * mid < val):
			start = mid + 1
			ans = mid
		else:
			end = mid -1;
	return ans
print sqroot(900)