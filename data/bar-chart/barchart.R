df <- data.frame(dose=c("D0.5", "D1", "D2"),
                 len=c(4.2, 10, 29.5))
head(df)
a
library(ggplot2)
p<-ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity")
p
p + coord_flip()

# Change the width of bars
p <- ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity", width=0.5)
p
# Change colors
ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity", color="blue", fill="white")
# Minimal theme + blue fill color
p<-ggplot(data=df, aes(x=dose, y=len)) +
  geom_bar(stat="identity", fill="steelblue")+
  theme_minimal()
p