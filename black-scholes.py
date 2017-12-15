from scipy import stats
import math

def black_scholes (cp, s, k, t, v, rf, div):
        """ Price an option using the Black-Scholes model.
        s: initial stock price
        k: strike price
        t: expiration time
        v: volatility
        rf: risk-free rate
        div: dividend
        cp: +1/-1 for call/put
        """

        d1 = (math.log(s/k)+(rf-div+0.5*math.pow(v,2))*t)/(v*math.sqrt(t))
        d2 = d1 - v*math.sqrt(t)

        optprice = (cp*s*math.exp(-div*t)*stats.norm.cdf(cp*d1)) - (cp*k*math.exp(-rf*t)*stats.norm.cdf(cp*d2))
        return optprice

price = black_scholes(-1,30,29,1/3,0.25,0.05,0)
print(price)