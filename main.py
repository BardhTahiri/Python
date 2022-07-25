#Miniaventure
emri=input('Shenoni emrin tuaj: ')
print('Miresevini',emri,'ne kete aventur')

pergjigjja=input('Gjendeni ne nje udhekryq a doni te shkoni majtas apo djathtas?:')

if pergjigjja == 'majtas':
    pergjigjja=input('Keni hasur ne nje perbindesh.Doni te luftoni apo ta shmangni perbindshin.Pergjigju luftim apo shmangje:')

if pergjigjja =='luftim':
    print('Ju luftuat furishem por vdiqet nga plaget qe morret nga perbindeshi!!!')
elif pergjigjja =='shmangje':
   pergjigjja=input('Ju u larguat me sukses nga perbindeshi.Tani keni hasur ne njeri te panjohur ai ju ka ofruar ushqim deshironi te pranoni apo jo?(Pergjigju po ose jo):')
if pergjigjja == 'po':
    print('Ju jeni helmuar nga ushqimi i ti dhe keni pasur nje vdekje tragjike.!!!')
elif pergjigjja == 'jo':
    print('Ti pe kurthin e njeriut dhe u largove.Pastaj u ktheve ne shtepi dhe jetove i lumtur jasht rreziqeve.')
elif pergjigjja =='djathtas':
    print('Eshte e bllokuar,kthehu mbrapa')
else:
    print('Pergjigjje jovalide')