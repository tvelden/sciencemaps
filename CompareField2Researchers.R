top <- read.csv(file.choose())
node <- read.csv(file.choose())

#x<-top1$year
#y<-top1$value

# Define colors to be used for cars, trucks, suvs
plot_colors <- c("red","orange","yellow", "green", "blue","blueviolet", "brown", "cyan","darkgreen", "darkorchid")


y1<-top$author1
y2<-top$author2
y3<-top$author3
y4<-top$author4
y5<-top$author5
y6<-top$author6
y7<-top$author7
y8<-top$author8
y9<-top$author9
y10<-top$author10

plot(years,y10, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode10*100, col=plot_colors[10],ylim = c(0.00,0.30))
legend("topright", "author10", col = plot_colors[10], pch=15, lty = 1:3)
plot(years,y9, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode9*100, col=plot_colors[9],ylim = c(0.00,0.30))
legend("topright", "author9", col = plot_colors[9], pch=15, lty = 1:3)
plot(years,y8, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode8*100, col=plot_colors[8],ylim = c(0.00,0.30))
legend("topright", "author8", col = plot_colors[8], pch=15, lty = 1:3)
plot(years,y7, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode7*100, col=plot_colors[7],ylim = c(0.00,0.30))
legend("topright", "author7", col = plot_colors[7], pch=15, lty = 1:3)
plot(years,y6, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode6*100, col=plot_colors[6],ylim = c(0.00,0.30))
legend("topright", "author6", col = plot_colors[6], pch=15, lty = 1:3)
plot(years,y5, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode5*100, col=plot_colors[5],ylim = c(0.00,0.30))
legend("topright", "author5", col = plot_colors[5], pch=15, lty = 1:3)
plot(years,y4, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode4*100, col=plot_colors[4],ylim = c(0.00,0.30))
legend("topright", "author4", col = plot_colors[4], pch=15, lty = 1:3)
plot(years,y3, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode3*100, col=plot_colors[3],ylim = c(0.00,0.30))
legend("topright", "author3", col = plot_colors[3], pch=15, lty = 1:3)
plot(years,y2, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode2*100, col=plot_colors[2],ylim = c(0.00,0.30))
legend("topright", "author2", col = plot_colors[2], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode1*100, col=plot_colors[1],ylim = c(0.00,0.30))
legend("topright", "author1", col = plot_colors[1], pch=15, lty = 1:3)

plot(years,y1, xlab="Year", ylab="Rao-Stirling Diversity", main="Compare Field2 Highly Productive Researchers", type="o", pch=15, cex = node$authornode1*100, col=plot_colors[1],ylim = c(0.00,0.30))
points(x,y2,type="o", pch=15, cex = node$authornode2*100,col=plot_colors[2])
points(x,y3,type="o", pch=15, cex = node$authornode3*100,col=plot_colors[3])
points(x,y4,type="o", pch=15, cex = node$authornode4*100,col=plot_colors[4])
points(x,y5,type="o", pch=15, cex = node$authornode5*100,col=plot_colors[5])
points(x,y6,type="o", pch=15, cex = node$authornode6*100,col=plot_colors[6])
points(x,y7,type="o", pch=15, cex = node$authornode7*100,col=plot_colors[7])
points(x,y8,type="o", pch=15, cex = node$authornode8*100,col=plot_colors[8])
points(x,y9,type="o", pch=15, cex = node$authornode9*100,col=plot_colors[9])
points(x,y10,type="o", pch=15, cex = node$authornode10*100,col=plot_colors[10])

legend("topright", names(top), col = plot_colors, pch=15, lty = 1:3)




