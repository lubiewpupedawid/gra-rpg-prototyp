
import random
import time

class Player:
   
    def __init__(self, name):
      
        self.name = name
        
        self.hp = 100
        
        self.max_hp = 100
       
        self.attack_min = 8
       
        self.attack_max = 15
      
        self.gold = 20
       
        self.xp = 0
        
        self.level = 1
        
        self.healing_potions = 3
       

    def is_alive(self):
        
        return self.hp > 0

    def attack(self):
       
        return random.randint(self.attack_min, self.attack_max)

    def heal(self):
       
        if self.healing_potions > 0:
          
            amount = random.randint(15, 30)
           
            self.hp = min(self.max_hp, self.hp + amount)
           
            self.healing_potions -= 1
           
            print(f"Użyto mikstury. HP +{amount}")
        else:
            
            print("Brak mikstur!")

    def add_xp(self, amount):
      
        self.xp += amount
     
        print(f"+{amount} XP!")
        
        if self.xp >= self.level * 50:
          
            self.level_up()

    def level_up(self):
        
        self.level += 1
      
        self.max_hp += 20
        
        self.hp = self.max_hp
      
        self.attack_min += 3
        
        self.attack_max += 3
       
        print(f"*** AWANS NA POZIOM {self.level}! ***")

class Enemy:
    
    def __init__(self, name, hp, attack_min, attack_max, gold_reward, xp_reward):
      
        self.name = name
       
        self.hp = hp
    
        self.attack_min = attack_min
    
        self.attack_max = attack_max
      
        self.gold_reward = gold_reward
        
        self.xp_reward = xp_reward

    def is_alive(self):
  
        return self.hp > 0

    def attack(self):
   
        return random.randint(self.attack_min, self.attack_max)


def create_random_enemy(player_level):
   
    enemies = [
        ("Goblin", 40 + player_level * 5, 5, 10, 10, 20),
       
        ("Wilk", 35 + player_level * 4, 6, 12, 8, 18),
    
        ("Szkielet", 45 + player_level * 6, 7, 14, 15, 25),
      
    ]
   
    name, hp, amin, amax, gold, xp = random.choice(enemies)
   
    return Enemy(name, hp, amin, amax, gold, xp)

def fight(player, enemy):
    
    print(f"\n=== WALKA: {enemy.name} ===")
    
    while player.is_alive() and enemy.is_alive():
      
        print(f"\n{player.name} HP: {player.hp}/{player.max_hp}")
       
        print(f"{enemy.name} HP: {enemy.hp}")
       
        print("[1] Atak")
       
        print("[2] Leczenie")
     
        print("[3] Ucieczka")
       
        choice = input("> ")
      
        if choice == "1":
          
            dmg = player.attack()
            
            enemy.hp -= dmg
           
            print(f"Zadajesz {dmg} obrażeń!")
        elif choice == "2":
          
            player.heal()
        elif choice == "3":
           
            if random.random() < 0.5:
               
                print("Uciekłeś!")
              
                return
            else:
               
                print("Nie udało się uciec!")
        else:
           
            print("Zły wybór.")
            continue
     
        if enemy.is_alive():
            
            dmg = enemy.attack()
           
            player.hp -= dmg
           
            print(f"{enemy.name} zadaje ci {dmg} obrażeń!")
          
            if not player.is_alive():
                print("Zginąłeś!")
              
                return
    
    print(f"\nPokonałeś {enemy.name}!")
   
    player.gold += enemy.gold_reward
    
    print(f"Zdobyt złoto: {enemy.gold_reward}")
   
    player.add_xp(enemy.xp_reward)

def shop(player):
  
    while True:
       
        print("\n=== SKLEP ===")
      
        print(f"Twoje złoto: {player.gold}")
      
        print("[1] Mikstura leczenia (10 złota)")
       
        print("[2] Wzmocnienie ataku (50 złota)")
       
        print("[3] Wyjście")
        
        choice = input("> ")
     
        if choice == "1":
          
            if player.gold >= 10:
            
                player.gold -= 10
             
                player.healing_potions += 1
             
                print("Kupiono miksturę.")
            else:
               
                print("Za mało złota.")
        elif choice == "2":
         
            if player.gold >= 50:
                
                player.gold -= 50
              
                player.attack_min += 2
               
                player.attack_max += 2
            
                print("Wzmocniono atak.")
            else:
             
                print("Za mało złota.")
        elif choice == "3":
         
            return
        else:
        
            print("Zły wybór.")

def main_menu():
   
    print("==== RPG ====")
    
    name = input("Podaj imię bohatera: ")
   
    player = Player(name)
   
    while True:
        
        print("\n=== MENU ===")
      
        print("[1] Walcz")
      
        print("[2] Sklep")
        
        print("[3] Statystyki")
        
        print("[4] Zakończ")
        
        choice = input("> ")
     
        if choice == "1":
           
            enemy = create_random_enemy(player.level)
           
            fight(player, enemy)
           
            if not player.is_alive():
               
                print("Koniec gry!")
              
                break
        elif choice == "2":
            
            shop(player)
        elif choice == "3":
        
            print(f"\n{player.name} — Poziom {player.level}")
           
            print(f"HP: {player.hp}/{player.max_hp}")
          
            print(f"Atak: {player.attack_min}-{player.attack_max}")
          
            print(f"XP: {player.xp}")
         
            print(f"Złoto: {player.gold}")
           
            print(f"Mikstury: {player.healing_potions}")
        elif choice == "4":
          
            print("Do zobaczenia!")
        
            break
        else:
           
            print("Zły wybór.")

lore = [
    
    "Dawno temu kraina Eldoria upadła pod naporem mroku.",
  
    "Tylko nieliczni bohaterowie mieli odwagę stawić mu czoła.",
   
    "W ruinach starożytnych miast kryją się sekrety dawnych czasów.",
   
    "Bestie wypełzają z lasów, atakując podróżnych.",
]

def show_lore():
    
    print("\n=== LORE ===")
  
    for line in lore:
      
        print(line)
        
        time.sleep(0.1)

extra_messages = [
   
    "Czujesz dziwną obecność...",
    
    "Wiatr niesie szepty starożytnych.",
   
    "Twoje przeznaczenie jeszcze się nie wypełniło.",
]

def random_message():
    
    if random.random() < 0.2:
       
        print(random.choice(extra_messages))

def exploration_event(player):
    
    print("\nWyruszasz na wyprawę...")
    
    random_message()
    
    event = random.randint(1, 4)
    
    if event == 1:
       
        print("Znalazłeś skrzynkę! +10 złota")
       
        player.gold += 10
    elif event == 2:
   
        print("Napotykasz wroga!")
      
        enemy = create_random_enemy(player.level)
      
        fight(player, enemy)
    elif event == 3:
      
        print("Odnajdujesz starożytny posąg. +20 XP")
        
        player.add_xp(20)
    else:
     
        print("Nic się nie wydarzyło.")

def extended_menu(player):
    
    while True:
       
        print("\n=== DODATKOWE OPCJE ===")
      
        print("[1] Odkrywaj świat")
       
        print("[2] Lore świata")
        
        print("[3] Powrót")
     
        c = input("> ")
       
        if c == "1":
           
            exploration_event(player)
        elif c == "2":
           
            show_lore()
        elif c == "3":
         
            return
        else:
          
            print("Zły wybór.")

def game():
    print("Witaj w rozszerzonej wersji RPG!")
    name = input("Podaj imię bohatera: ")
   
    player = Player(name)
    
    while True:
 
        print("\n=== MENU GŁÓWNE ===")
     
        print("[1] Walcz")
   
        print("[2] Sklep")
      
        print("[3] Statystyki")
     
        print("[4] Dodatkowe opcje")
     
        print("[5] Wyjście")
       
        choice = input("> ")
       
        if choice == "1":
            
            enemy = create_random_enemy(player.level)
       
            fight(player, enemy)
          
            if not player.is_alive():
              
                print("Koniec gry!")
           
                break
        elif choice == "2":
           
            shop(player)
        elif choice == "3":
          
            print(f"\n{player.name} — Poziom {player.level}")
          
            print(f"HP: {player.hp}/{player.max_hp}")
           
            print(f"Atak: {player.attack_min}-{player.attack_max}")
          
            print(f"XP: {player.xp}")
           
            print(f"Złoto: {player.gold}")
     
            print(f"Mikstury: {player.healing_potions}")
        elif choice == "4":
          
            extended_menu(player)
        elif choice == "5":
       
            print("Do zobaczenia!")

            break
        else:

            print("Zły wybór.")

def padding():
  
    pass

game()  
