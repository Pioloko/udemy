# Considere a expressão a seguir.

# x³+x²+10x-x+4

# Use uma função integrada para encontrar o resultado desta expressão, quando o valor de x é 10. Resultado esperado: 1264.

# Dica: use a função eval().


x =2

expressao="(x**3)+(x**2)+(x*10)-x+4"
resultado=eval(expressao)
print(resultado)