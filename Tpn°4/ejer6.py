

from lista import Lista 

class Superheroes():
    def __init__(self, nombre, anio, casa, bio):
        self.nombre = nombre
        self.anio = anio
        self.casa = casa
        self.bio = bio
        
    def __str__(self):
        return f'{self.nombre} - {self.anio} - {self.casa} - {self.bio}'

Lista_Super = Lista()
heroe = Superheroes('batman', '1965', 'DC', 'armadura')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('linterna verde', '1982', 'marvel', 'se llama hall jordan')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('wolverine', '1942', 'marvel', 'es inmortal')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('dr strange', '1998', 'marvel', 'traje')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('star lord', '1985', 'marvel', 'traje')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('mujer maravilla', '1970', 'DC', 'armadura')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('capitana marvel', '1975', 'marvel', 'traje')
Lista_Super.insert(heroe,'nombre')
heroe = Superheroes('flash', '1955', 'DC', 'es rapido')
Lista_Super.insert(heroe,'nombre')

Lista_Super.barrido()
  

Lista_Super.delete('linterna verde','nombre')


print('   ')
pos = Lista_Super.search('wolverine', 'nombre')
if pos:
    print('Anio de de aparicion de wolverine', Lista_Super.get_element_by_index(pos).anio)


print('   ')
pos = Lista_Super.search('dr strange', 'nombre')
if pos:
    Lista_Super.get_element_by_index(pos).casa = 'DC'
    print('Dr strange se cambio de casa a DC')


print('   ')
cont=0
cont2=0
lista_aux= Lista_Super.obtener_ele()
for super in lista_aux:
    if 'traje' in super.bio:
        cont+=1
    elif 'armadura' in super.bio:
        cont2+=1

print('los heroes con traje son:',cont,'y con armadura:',cont2)


print('   ')
print('Nacidos antes de 1963')
for super in lista_aux:
    if int(super.anio) < 1963:
        print('Nombre:',super.nombre,'Casa:', super.casa)


print('   ')
pos = Lista_Super.search('capitana marvel', 'nombre')
if pos:
    print('casa de capitana marvel', Lista_Super.get_element_by_index(pos).casa)
    
pos2 = Lista_Super.search('mujer maravilla', 'nombre')
if pos2:
    print('casa de mujer maravilla', Lista_Super.get_element_by_index(pos2).casa)


print('   ')
pos = Lista_Super.search('star lord', 'nombre')
if pos:
    print('Informacion de star lord:', Lista_Super.get_element_by_index(pos).bio)
    
pos2 = Lista_Super.search('flash', 'nombre')
if pos2:
    print('Informacion de flash:', Lista_Super.get_element_by_index(pos2).bio)
    

ini=['b','m','s']

print('  ')
print('Los heroes que empizan con B, M y S son:')
for super in lista_aux:
    if super.nombre[0] in ini:
        print(super.nombre)


print('  ')
cont=0
cont2=0
for super in lista_aux:
    if 'marvel' in super.casa:
        cont+=1
    elif 'DC' in super.casa:
        cont2+=1

print('En marvel hay',cont,'superheroes y en DC hay',cont2,'superheroes')


Lista_Super.barrido()

