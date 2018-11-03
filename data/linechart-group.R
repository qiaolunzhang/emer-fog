library(ggplot2)

df2 <- data.frame(supp=rep(c("VC", "OJ"), each=3),
                  dose=rep(c("D0.5", "D1", "D2"), 2),
                  len=c(6.8, 15, 33, 4.2, 10, 29.5))
head(df2)

ggplot(data=df2, aes(x=dose, y=len, group=supp)) +
  geom_line(aes(color=supp))+
  geom_point(aes(color=supp))

library(ggplot2)

rain<-read.table("D:\\mycode\\emer-testbed\\data\\graph-size1.csv", header = TRUE,
                 sep = ",")
head(rain)
p<-ggplot(data=rain, aes(x=areaSize, y=longestExecutionTime, group=scheme)) +
  geom_line(aes(color=scheme))+
  geom_point(aes(color=scheme))+
  theme(legend.position = c(.24,.9)) +
  theme(legend.title = element_blank())
p<-p+theme(legend.text = element_text(size=22, family = "serif"))
p<-p+scale_x_continuous("Number of areas owns per emergency center", breaks = c(50, 100, 150, 200, 250, 300, 350, 400))
p<-p+theme(axis.text = element_text(size = 22, family = "serif"), axis.title=element_text(size=24, family = "serif"))
p<-p+scale_y_continuous("Longest global execution time(s)", breaks = c(100, 200, 300, 400, 500, 600))
p
