top <- read.csv(file.choose())
node <- read.csv(file.choose())
#years <- c("1991", "1992", "1993","1994","1995","1996","1997","1998","1999", "2000", "2001","2002","2003","2004","2005","2006","2007","2008","2009","2010")

years <- 1991:2010
plot_colors <- c("red","orange","yellow", "green", "blue","blueviolet", "brown", "cyan","darkgreen", "darkorchid", "darkred")


y1<-top$top1
y2<-top$top2
y3<-top$top3
y4<-top$top4
y5<-top$top5
y6<-top$top6
y7<-top$top7
y8<-top$top8
y9<-top$top9
y10<-top$top10
y11<-top$top11

plot(years,y11, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node11*10, col=plot_colors[11], ylim = c(0.00,0.30))
legend("topleft", "top11", col = plot_colors[11], pch=15, lty = 1:3)
plot(years,y10, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node10*10, col=plot_colors[10], ylim = c(0.00,0.30))
legend("topleft", "top10", col = plot_colors[10], pch=15, lty = 1:3)
plot(years,y9, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node9*10, col=plot_colors[9], ylim = c(0.00,0.30))
legend("topleft", "top9", col = plot_colors[9], pch=15, lty = 1:3)
plot(years,y8, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node8*10, col=plot_colors[8], ylim = c(0.00,0.30))
legend("topleft", "top8", col = plot_colors[8], pch=15, lty = 1:3)
plot(years,y7, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node7*10, col=plot_colors[7], ylim = c(0.00,0.30))
legend("topleft", "top7", col = plot_colors[7], pch=15, lty = 1:3)
plot(years,y6, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node6*10, col=plot_colors[6], ylim = c(0.00,0.30))
legend("topleft", "top6", col = plot_colors[6], pch=15, lty = 1:3)
plot(years,y5, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node5*10, col=plot_colors[5], ylim = c(0.00,0.30))
legend("topleft", "top5", col = plot_colors[5], pch=15, lty = 1:3)
plot(years,y4, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node4*10, col=plot_colors[4], ylim = c(0.00,0.30))
legend("topleft", "top4", col = plot_colors[4], pch=15, lty = 1:3)
plot(years,y3, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node3*10, col=plot_colors[3], ylim = c(0.00,0.30))
legend("topleft", "top3", col = plot_colors[3], pch=15, lty = 1:3)
plot(years,y2, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node2*10, col=plot_colors[2], ylim = c(0.00,0.30))
legend("topleft", "top2", col = plot_colors[2], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node1*10, col=plot_colors[1], ylim = c(0.00,0.30))
legend("topleft", "top1", col = plot_colors[1], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Major Topic Areas", type="o", pch=15, cex = node$node1*10, col=plot_colors[1], ylim = c(0.00,0.30))
points(x, y2,type="o", pch=15, cex = node$node2*10,col=plot_colors[2])
points(x, y3,type="o", pch=15, cex = node$node3*10, col=plot_colors[3])
points(x, y4,type="o", pch=15, cex = node$node4*10, col=plot_colors[4])
points(x, y5,type="o", pch=15, cex = node$node5*10, col=plot_colors[5])
points(x, y6,type="o", pch=15, cex = node$node6*10, col=plot_colors[6])
points(x, y7,type="o", pch=15, cex = node$node7*10, col=plot_colors[7])
points(x, y8,type="o", pch=15, cex = node$node8*10, col=plot_colors[8])
points(x, y9,type="o", pch=15, cex = node$node9*10, col=plot_colors[9])
points(x, y10,type="o", pch=15, cex = node$node10*10, col=plot_colors[10])
points(x, y11,type="o", pch=15, cex = node$node11*10, col=plot_colors[11])

legend("topleft", names(top), col = plot_colors, pch=15, lty = 1:3)


