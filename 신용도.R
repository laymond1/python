library(readxl)

bank <- read_xls("/Users/Baobab/Downloads/은행신용도.xls",
         col_names = T)

head(bank)

bank <- as.data.frame(bank)

summary(bank)
str(bank)

bank$결혼상태 <- as.factor(bank$결혼상태)
bank$신용카드 <- as.factor(bank$신용카드)
bank$주택소유 <- as.factor(bank$주택소유)
bank$신용도 <- as.factor(bank$신용도)

prcomp(bank)

install.packages("e1071")
install.packages("kernlab")
library(e1071)
library(kernlab)

svm <- svm(신용도~.    , data = bank[,-1] )
summary(svm)









