import math

class Bnode(object):
	def __init__(self,price,e_value,style):
		self.price = price
		self.e_value = e_value
		self.c_value = 0
		self.style = style

	def setcvalue(self,c_value):
		#continue value
		#also the value of the options in European option
		self.c_value = c_value
		if self.style == 'A':
			#American
			self.o_value = max(self.c_value, self.e_value)
		else:
			#European
			self.o_value = c_value
	def __repr__(self):
		return '(' + str(self.price) +','+ str(self.e_value) + ',' + str(self.c_value) + ',' + str(self.o_value) + ')'
		#return '(' + str(self.price) + ',' + str(self.o_value) + ')'

def binTree(S,K,r,v,T,n,otype,style='E'):
	#S is the initial price
	#K is the strike price at the maturity
	#r is the risk-free interest rate
	#v is the volatility
	#T is the length of period
	#n is the number of steps
	#otype is the call/put. input 'call'means call option, others means put
	#style='A' means American options while 'E' means European option

	delta_t = T/n
	
	a = math.exp(r*delta_t)
	u = math.exp(r*delta_t + v*math.sqrt(delta_t))
	d = math.exp(r*delta_t - v*math.sqrt(delta_t))
	
	p = (a-d)/(u-d)
	q = 1-p
	print('a=',a)
	print('u=',u)
	print('d=',d)
	print('p=',p)
	print('q=',q)
	root = Bnode(S,0,style)
	price_list = [[root]]
	
	for l in range(1,n+1):
		new_layer = []
		for i in range(l+1):
			price = S*(u**(l-i))*(d**i)
			if otype == 'call':
				node = Bnode(price,max(price-K,0),style)#for call option
			else:
				node = Bnode(price,max(K-price,0),style)#for put option
			new_layer.append(node)
		price_list.append(new_layer)

	#the value of end node is the same as the difference with strike price
	for each in price_list[-1]:
		each.setcvalue(each.e_value)
	
	for index, line in enumerate(price_list[-2::-1]):
		children = price_list[-index-1]
		for i,each in enumerate(line):
			each.setcvalue((p*children[i].o_value + q*children[i+1].o_value)/a)
	#map(lambda x:x.setcvalue(x.e_value),price_list[-1])
	print(price_list[0][0].o_value)


S = 100
K = 95
r = 0.08
v = 0.3
T = 1
n = 3
otype = 'put'
binTree(S,K,r,v,T,n,otype,style='E')