library(ggplot2)

dat1 <- data.frame(
  sex = factor(c("Female","Female","Female","Male","Male","Male")),
  time = factor(c("Breakfast","Lunch","Dinner","Breakfast","Lunch","Dinner"), levels=c("Breakfast","Lunch","Dinner")),
  total_bill = c(3, 4, 5, 6, 7, 8))
head(dat1)
ggplot(data=dat1, aes(x=time, y=total_bill, fill=sex)) +
  geom_bar(stat="identity", position=position_dodge())


rain<-read.table("D:\\mycode\\emer-testbed\\data\\graph1.csv", header = TRUE,
                 sep = ",")
head(rain)
p<-ggplot(data=rain, aes(x=areaSize, y=taskAmount, fill=solvedPlace)) +
  geom_bar(stat="identity", position = position_dodge()) +
  theme(legend.position = c(.2,.9)) +
  theme(legend.title = element_blank())
p<-p+theme(legend.text = element_text(size=22, family = "serif"))
p<-p+scale_x_continuous("Area size", breaks = c(500, 1000, 1500, 2000, 2500, 3000, 3500))
p<-p+theme(axis.text = element_text(size = 22, family = "serif"), axis.title=element_text(size=24, family = "serif"))
p<-p+scale_y_continuous("Task amount")
p
