top <- read.csv("MajorTopicField1.csv")
node <- read.csv("MajorTopicFieldNodeSize1.csv")

years <- 1991:2010
plot_colors <- c("red","orange","yellow", "green", "blue","blueviolet", "brown", "cyan")

y1<-top$top1
y2<-top$top2
y3<-top$top3
y4<-top$top4
y5<-top$top5
y6<-top$top6
y7<-top$top7
y8<-top$top8

plot(years,y8, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node8/100.0, col=plot_colors[8],ylim = c(0.00,0.30))
legend("topleft", "top8", col = plot_colors[8], pch=15, lty = 1:3)
plot(years,y7, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node7/100.0, col=plot_colors[7],ylim = c(0.00,0.30))
legend("topleft", "top7", col = plot_colors[7], pch=15, lty = 1:3)
plot(years,y6, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node6/100.0, col=plot_colors[6],ylim = c(0.00,0.30))
legend("topleft", "top6", col = plot_colors[6], pch=15, lty = 1:3)
plot(years,y5, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node5/100.0, col=plot_colors[5],ylim = c(0.00,0.30))
legend("topleft", "top5", col = plot_colors[5], pch=15, lty = 1:3)
plot(years,y4, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node4/100.0, col=plot_colors[4],ylim = c(0.00,0.30))
legend("topleft", "top4", col = plot_colors[4], pch=15, lty = 1:3)
plot(years,y3, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node3/100.0, col=plot_colors[3],ylim = c(0.00,0.30))
legend("topleft", "top3", col = plot_colors[3], pch=15, lty = 1:3)
plot(years,y2, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node2/100.0, col=plot_colors[2],ylim = c(0.00,0.30))
legend("topleft", "top2", col = plot_colors[2], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node1/100.0, col=plot_colors[1],ylim = c(0.00,0.30))
legend("topleft", "top1", col = plot_colors[1], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field1 Major Topic Areas", type="o", pch=15, cex = node$node1/100.0, col=plot_colors[1],ylim = c(0.00,0.30))
points(years, y2,type="o", pch=15, cex = node$node2/100.0, col=plot_colors[2])
points(years, y3,type="o", pch=15, cex = node$node3/100.0,col=plot_colors[3])
points(years, y4,type="o", pch=15, cex = node$node4/100.0,col=plot_colors[4])
points(years, y5,type="o", pch=15, cex = node$node5/100.0,col=plot_colors[5])
points(years, y6,type="o", pch=15, cex = node$node6/100.0,col=plot_colors[6])
points(years, y7,type="o", pch=15, cex = node$node7/100.0,col=plot_colors[7])
points(years, y8,type="o", pch=15, cex = node$node8/100.0,col=plot_colors[8])

legend("topleft", names(top), col = plot_colors, pch=15, lty = 1:3)

