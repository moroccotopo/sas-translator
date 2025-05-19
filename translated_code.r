class_data <- read.csv("default_of_credit_card_clients.csv", header = TRUE)
adultos <- subset(class_data, AGE >= 18)
write.csv(adultos, file = "output.csv")