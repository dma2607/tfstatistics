#!/usr/bin/python3
import pandas as pd
import numpy as np
import tensorflow as tf
from leastsquares import leastSquaresSolver, byNormalEquation, byQRFactorization, bySVD

# response variabl (Y): SalePrice
# predictors: LotArea (Numerical) LotFrontage (Numerical) Street(Categorical)
# example data to develop the linear regression method
#
def getXYData(fin='~/tfstatistics/house_pricing_train.csv'):
    df = pd.read_csv(fin)
    xydata = df['SalePrice LotArea LotFrontage'.split()]
    xydata = xydata.dropna(axis=0)
    #xydata.Street = xydata.Street.factorize()[0]
    # xydata.Street.cat.codes.values
    return xydata
#
# class for linear regression model
class lm:
    def __init__(self, data, response_id):
        self.y = data[[response_id]].values
        self.x = data.drop([response_id], axis=1).values
        self.x = np.column_stack((self.x, np.ones(shape=(self.x.shape[0]))))
    # .
    def fit(self, lss):
        return lss.solve(self.x, self.y)

#
# example
df = getXYData()
qr = byQRFactorization()
nr = byNormalEquation()
svd = bySVD()
#
lreg = lm(df, 'SalePrice')
print('Coefficients: \n{}'.format(lreg.fit(qr)))
print('Coefficients: \n{}'.format(lreg.fit(nr)))
print('Coefficients: \n{}'.format(lreg.fit(svd)))



