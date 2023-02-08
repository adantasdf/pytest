from bytebank import Funcionario

# lucas = Funcionario('Lucas Carvalho', '13/01/1986', 1000)

# print (lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '07/01/1986', 1111)
    print(f'Teste = {funcionario_teste.idade()}')
    
teste_idade()