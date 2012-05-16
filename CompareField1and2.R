diversity <- read.csv(file = file.choose(), head =TRUE, sep=",")
diversity2 <- read.csv(file = file.choose(), head =TRUE, sep=",")


x<-diversity2$year
y<-diversity2$value
z<-diversity2$total

#x2<-diversity2$year
y2<-diversity$value
z2<-diversity$total

plot(x,y, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1(blue) and Field2(green)", type="o", pch=15, col="blue", cex = z/1000.0, ylim = c(0.0,0.30))

points(x, y2,type="o", pch=15, col="green", cex = z2/1000.0)
#line1.fit<-lm(y~x)
#summary(line1.fit)
#abline(line1.fit)
#line2.fit<-lm(y2~x2)
#summary(line2.fit)
#abline(line2.fit)


