library(ggplot2)
library(ggiraph)

cars = read.csv("cars-sample.csv", header=TRUE, row.names=1)

cars$Make.Model = paste(cars$Manufacturer, cars$Car, sep=" ")
head(cars)

print(cars$Car)

plot = ggplot(cars, aes(x=Weight, y=MPG, color=Manufacturer)) + geom_point_interactive(alpha=0.5, aes(size=Weight, tooltip = Make.Model, data_id = Make.Model))

plot2 = girafe(ggobj = plot)
plot2

htmlwidgets::saveWidget(file = "ggplot_plot.html", plot2)
