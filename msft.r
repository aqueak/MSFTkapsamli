getwd()
setwd("C:/Users/FURKAN/Desktop/R-PYTHON")
msft<-read.csv(file.choose())

colnames(MSFT)<-c("date","open","high","low","close",
                  "adj","vol")
install.packages("randomForest")
library(caret)
library(randomForest)

set.seed(123)
index<-createDataPartition(MSFT$open,p=0.7,list = FALSE)

train_data<-MSFT[index, ]
test_data<-MSFT[index, ]
head(MSFT)




model<-randomForest(open ~ .,data=train_data)
predictions<-predict(model,newdata=test_data)
confusionMatrix(predictions,test_data$open)



str(MSFT)
library(Amelia)
missmap(MSFT)
