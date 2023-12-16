library(ggplot2)

colnames(MSFT)<-c("date","open","high","low","close",
                  "adj","vol")

View(MSFT)

ggplot(MSFT,aes(x=high,y=low))+
  geom_smooth()

ggplot(MSFT,aes(x=high,y=low))+
  geom_line(colour="red",)


model<-lm(open~adj , data=MSFT)
summary(model)
summary(model)$coef
new_data<-data.frame(open=(0.1000))
predict(model,newdata=MSFT)
abline(lm(open~adj,data = MSFT),col='red')
bar=ggplot(MSFT,aes(x=open,y=adj))
bar+geom_point() 

pie(model)









install.packages("Rcpp")
library(Rcpp)
sourceCpp("cpp.cpp")