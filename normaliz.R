colnames(MSFT)<-c("date","open","high","low","close",
                  "adj","vol")

#Shapiro-Wilk Test
MSFT<-rnorm(100)
shapiro.test(MSFT)

#Kolmogorov Test
MSFT<-rnorm(100)
ks.test(MSFT,"pnorm")

#Mood Ortanca Testi 

