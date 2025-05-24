def aumentar(num):
    """
    param: num: recebe um alor digitado pelo usuario
    porc: recebe o valor * porcentagem no caso por padrão 10%
    return: retorna o aumento da porcentagem + valor (num)
    """
    
    porc = (num * 0.10) + num
    return f'{porc:.2f}' 
    

def dobro(num):
    """
    :param: num: rece um valor digitado pelo usuario
    :res: recebe um valor e multiplica por 2
    :return: returna o resultado convertido com duas casas decimais 
    """
    res = num * 2
    return f'{res:.2f}'


def metade(num):
    """
    :param: num: recebe o valor digitado pelo usuario
    res: dividi o valor digitado pelo usuario por 2
    :return: retorna o valor já convertido  com duas casas decimais 
    """
    
    res =  num / 2
    return f'{res:.2f}'


def diminuir(num):
    """
    :param: num: recebe um valor digitado pelo usuario
    :porc: recebe o valor num * 10% e diminui esse valor de num
    return: retorna o valor já convertido para duas casas decimais 
    """
    
    porc = num - (num * 0.10) 
    return f'{porc:.2f}'
   

