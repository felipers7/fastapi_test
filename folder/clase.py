class Waifu:

    def __init__(self, nombre,hair_color,alive, health):
        self.nombre = nombre 
        self.hair_color = hair_color
        self.alive = alive
        self.health = health

    def get_damage(self, damage):
        self.health = self.health - damage
        if(self.health <= 0):
            self.alive = False
            print(self.nombre + " ha moricido")
        else:
            print(self.nombre + " todavía puede pelear, vida restante: "+ str(self.health))
