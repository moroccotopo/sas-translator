default_data <- read.csv('default_of_credit_card_clients.csv')

filtrar_deuda <- function(umbral) {
  deuda_alta <- subset(default_data, BILL_AMT1 > umbral)
  write.csv(deuda_alta, file = 'output.csv')
}

filtrar_deuda(20000)