import pandas as pd
import numpy as np
import statsmodels.api as sm

def vital_stats(player_file):
    df_adv = pd.read_csv(player_file, index_col=0)
    df_adv = df_adv.dropna()
    currentv = []
    globalv = ['1V','2V','3V','4V','5V','6V','7V','8V','9V','10V','11V','12V','13V','14V','15V','16V','17V','18V','19V','20V','21V','22V']

    while True:

        pval = []
        for i in range(1,23):
            pval.append(1)

        for i in range(1,23):
            curr_col = str(str(i)+'V')
            currentuse = []
            if curr_col not in currentv and curr_col != '3V':
                for k in range(0,len(currentv)):
                    currentuse.append(currentv[k])

                currentuse.append(curr_col)
                X = df_adv[currentuse]
                Y = df_adv['3V']
                X = sm.add_constant(X)
                est = sm.OLS(Y, X,intercept=True).fit(method='pinv')
                pval[i-1] = est.pvalues[len(currentuse)-1]

        minv=1;
        minpos=0;
        for i in range(1,23):
            if pval[i-1]<minv:
                minv = pval[i-1]
                minpos = i

        if minv>0.05:
            break
        else:
            currentv.append(str(minpos+1)+'V')

    Yf = df_adv['3V']
    Xf = df_adv[currentv]
    Xf = sm.add_constant(Xf)
    est = sm.OLS(Yf, Xf,intercept=True).fit(method='pinv')
    print(est.summary())

    df_adv.head()
    print(currentv)


vital_stats('advanced1.csv')
