import numpy as np
import math

class BlackScholes:
    def __init__(self):
        self.s = 100
        self.k = 100
        self.v = 0.01
        self.r = 0.01
        self.t = 1

        self.size = 10
        self.callHeatMap = np.zeros((self.size, self.size))
        self.putHeatMap = np.zeros((self.size, self.size))


    def _cdf(self, x):
        return (1 + math.erf(x / math.sqrt(2))) / 2

    def calculateCallPrice(self):
        d1 = (math.log(self.s / self.k) + self.t * (self.r + (self.v ** 2 / 2))) / (self.v * math.sqrt(self.t))
        d2 = d1 - self.v * math.sqrt(self.t)

        return (self._cdf(d1) * self.s) - (self._cdf(d2) * self.k * math.exp(-self.r * self.t))

    def _calculateCallPrice(self, strikePrice, volatility):
        d1 = (math.log(self.s / strikePrice) + self.t * (self.r + (volatility ** 2 / 2))) / (volatility * math.sqrt(self.t))
        d2 = d1 - volatility * math.sqrt(self.t)

        return (self._cdf(d1) * self.s) - (self._cdf(d2) * strikePrice * math.exp(-self.r * self.t))

    def calculatePutPrice(self):
        d1 = (math.log(self.s / self.k) + self.t * (self.r + (self.v ** 2 / 2))) / (self.v * math.sqrt(self.t))
        d2 = d1 - self.v * math.sqrt(self.t)
    
        return (self.k * math.exp(-self.r * self.t) * self._cdf(-d2)) - (self.s * self._cdf(-d1))

    def _calculatePutPrice(self, strikePrice, volatility):
        d1 = (math.log(self.s / strikePrice) + self.t * (self.r + (volatility ** 2 / 2))) / (volatility * math.sqrt(self.t))
        d2 = d1 - volatility * math.sqrt(self.t)
    
        return (strikePrice * math.exp(-self.r * self.t) * self._cdf(-d2)) - (self.s * self._cdf(-d1))

    def calculateCallHeatMap(self, strikePriceRange, volatilityRange):
        for i in range(strikePriceRange.size):
            for j in range(volatilityRange.size):
                self.callHeatMap[i][j] = self._calculateCallPrice(strikePriceRange[i], volatilityRange[j])
        
    def calculatePutHeatMap(self, strikePriceRange, volatilityRange):
        for i in range(strikePriceRange.size):
            for j in range(volatilityRange.size):
                self.putHeatMap[i][j] = self._calculatePutPrice(strikePriceRange[i], volatilityRange[j])