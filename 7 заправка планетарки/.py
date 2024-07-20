def f(x):
	return 703.7*(1-x), 804.2*(1-(x+0.1))

for i in range(0,90+1):
	t2, t1 = f(i/100)
	print(f"{i}-{i+10}%	{round(t1)}	{round(t2)}	{round(t1-t2)}")