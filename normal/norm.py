#! /usr/bin/env python3

# Autor: Nicolas Alan
import scipy.stats as stats
import math

def norm(average: float, sigma: float, n: int, var1: float, var2: float, tip: int) -> float:
     """
     Example Case 1: P(𝑥̅ ≤ 894)
     """
     if tip == 0:
          sigma =  math.sqrt(sigma)
          # calculando o erro padrão
          print("Passo 1 - Calcule o erro padrão da média:")
          std_error = sigma / math.sqrt(n)
          print("Standard error =", round(std_error, 4))
          
          # calculando o valor z-score para x̅ = var
          print("\nEtapa 2 - Calcule os escores z para os limites inferior e superior:")
          z = (var1 - average) / std_error
          print("lower =", round(z, 4))
          
          # encontrando a probabilidade usando a função de distribuição acumulada padrão
          print("\nPasso 3 - Use a função de distribuição cumulativa (cdf) para calcular a probabilidade:")
          prob = stats.norm.cdf(z)
          
          # imprimindo a resposta
          print("P(x̅ ≤ %.4f) = %.4f" % (var1, prob))

          return prob
     
     """
     Example Case 2: P(700 ≤ 𝑥̅ ≤ 894)
     """
     elif tip == 1: 
          # calcula o erro padrão da média
          std_error = sigma / math.sqrt(n)
          print("Passo 1 - Calcule o erro padrão da média:")
          print("Standard error = ", round(std_error, 4))

          # calculando o valor z-score para x̅ = var
          z_lower = (var1 - average) / std_error
          z_upper = (var2 - average) / std_error
          print("\nEtapa 2 - Calcule os escores z para os limites inferior e superior:")
          print("z_lower =", round(z_lower, 4))
          print("z_upper =", round(z_upper, 4))

          # encontrando a probabilidade usando a função de distribuição acumulada padrão
          prob = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)  
          print("\nPasso 3 - Use a função de distribuição cumulativa (cdf) para calcular a probabilidade:")
          print("P(%.4f < x̅ < %.4f) = %.4f" % (var1, var2, round(prob, 4)))

          return prob

if __name__ == '__main__':
     
     average = 900
     sigma = 642
     n = 30
     var1 = 894
     var2 = 0
     tip = 0

     norm(average, sigma, n, var1, var2, tip)