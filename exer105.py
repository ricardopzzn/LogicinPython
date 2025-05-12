def notas(*nums, sit=False):
   dic = {}
   
   if len(nums) == 0:
       dic['erro'] = 'Nenhuma nota foi fornecida'
   else:
        total = len(nums)
        maior = max(nums)
        menor = min(nums)
        media = sum(nums) / total
        
        dic['Total'] = total
        dic['maior'] = maior
        dic['menor'] = menor
        dic['media'] = media
        
        if sit is True:
            if media >= 7:
                dic['situação'] = 'Boa'
                
            elif media >= 5:
                dic['situação'] = 'Razoàvel'
                
            else:
                dic['situação'] = 'Ruim'
                
        return dic


print(notas(7, 8, 3, sit=True))