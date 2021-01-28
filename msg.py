from iLoveYou import greeting, ily, lelly, emj1, emj2, emj3, emj4, emj5
from tempGreenfield import temp, description

desc = ''

if temp <= 0:
      desc = 'its super frigid outside please wear a biggg jacket and a hat!!'
if 1 < temp <= 30 :
      desc = 'its really cold outside so wear a jacket and a hat'
if 31 < temp < 50 :
      desc = 'its cool outside so wear a small sweater!!'
if 51 < temp < 80 :
      desc = 'yay its warm outside! enjoy the weather!!'
if temp > 80 :
      desc = 'OMG its really hot outside, make sure you drink lots of water!! '

msg = greeting + ' ' + lelly + ' ' + ily + ' ' + emj1 + emj2 + emj3 + emj4 + '\nThe weather is ' + \
      str(temp) + '° ' + 'right now ' + desc + emj5