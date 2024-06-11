if (!require('readxl')) install.packages('readxl')
if (!require('gmodels')) install.packages('gmodels')
if (!require('arules')) install.packages('arules')
if (!require('arulesViz')) install.packages('arulesViz')
if (!require('vcd')) install.packages('vcd')
if (!require('readr')) install.packages('readr')
install.packages("sparklyr")
if (!require('dplyr')) install.packages('dplyr')
library(dplyr)
library(sparklyr)
library(cluster)
library(factoextra)
library(dendextend)
library(readxl)
library(arules)
library(readr)
library(reshape2)

instakart <- read_csv("C:\\Users\\danyg\\OneDrive\\Documents\\Javeriana Maestria\\Primer Semestre\\Metodo Analítica 1\\Taller 2\\apriori.csv")

# Convertir el DataFrame a una lista de transacciones
transacciones <- split(instakart$product_name, instakart$order_id)

# Convertir la lista de transacciones a un objeto de clase 'transactions'
transacciones <- as(transacciones, "transactions")

# Muestrear el 20% de las transacciones
set.seed(123) # Esto es para reproducibilidad del muestreo
indices_muestra <- sample(length(transacciones), 1 * length(transacciones))
transacciones_muestreadas <- transacciones[indices_muestra]

itemFrequencyPlot(transacciones_muestreadas, topN=10,  cex.names=.5)

rules<-apriori(transacciones_muestreadas,parameter=list(support=0.005,confidence=0.2,maxlen=3))

summary(rules)

inspect(head(sort(rules,by="lift"),20))
inspect(head(sort(rules,by="support"),20))

plot(rules, measure=c("support","lift"), shading="confidence")

subrules<-subset(rules,quality(rules)$confidence>0.2)A
plot (subrules, method="matrix", measure="lift", control=list(reorder='support/confidence'))
