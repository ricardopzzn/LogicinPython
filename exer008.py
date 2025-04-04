print('           Conversor de medidas')
print(20 * '=-')
med = float(input('Uma distância em metros: '))
km = med / 1000
hm = med / 100
dam = med / 10
dm = med * 10
cm = med * 100
mm = med * 1000
print(f'{km}KM \n{hm}HM \n{dam}DAM \n{dm:.0f}DM \n{cm:.0f}CM \n{mm:.0f}MM')