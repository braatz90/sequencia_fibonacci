#calculando se um número pertence a sequência fibonacci 
def calcula_fibonacci(n):
  sequencia = [0, 1]
  
  while sequencia[-1] < n:
    sequencia.append(sequencia[-1] + sequencia[-2])

  if n in sequencia:
      return f"O número {n} pertence à sequência de Fibonacci."
  else:
      return f"O número {n} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = calcula_fibonacci(numero)
print(resultado)