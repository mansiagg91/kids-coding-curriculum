# PyGame Pet AI - Ages 10-12 Python Programming Game
# Intermediate game with Python code and simple AI concepts

import pygame
import random
import math
import json
from datetime import datetime

# Initialize Pygame
pygame.init()

class PetAI:
    """Simple AI system for pet behavior"""
    
    def __init__(self, pet_name, personality_weights):
        self.name = pet_name
        self.personality = personality_weights
        self.memory = []
        self.current_goal = None
        
    def think(self, game_state):
        """AI decision making based on needs and personality"""
        
        # Analyze current situation
        my_pet = game_state['pets'][self.name]
        other_pets = [p for name, p in game_state['pets'].items() if name != self.name]
        
        # Calculate urgency for different needs
        needs = {
            'hunger': max(0, my_pet['hunger'] - 30) / 70.0,  # 0-1 scale
            'energy': max(0, 100 - my_pet['energy']) / 70.0,
            'social': max(0, 50 - my_pet['happiness']) / 50.0,
            'help_others': sum(1 for p in other_pets if p['hunger'] > 70 or p['happiness'] < 30)
        }
        
        # Weight needs by personality
        weighted_needs = {}
        for need, urgency in needs.items():
            weight = self.personality.get(need, 0.5)
            weighted_needs[need] = urgency * weight
        
        # Choose action based on highest weighted need
        if weighted_needs['hunger'] > 0.7:
            self.current_goal = 'find_food'
        elif weighted_needs['energy'] > 0.8:
            self.current_goal = 'rest'
        elif weighted_needs['help_others'] > 0.5 and self.personality.get('helpful', 0) > 0.6:
            self.current_goal = 'help_friend'
        elif weighted_needs['social'] > 0.4:
            self.current_goal = 'socialize'
        else:
            self.current_goal = 'explore'
            
        return self.current_goal
    
    def execute_action(self, action, game_state):
        """Execute the chosen action"""
        
        my_pet = game_state['pets'][self.name]
        
        if action == 'find_food':
            # Move toward food
            if game_state['food_items']:
                closest_food = min(game_state['food_items'], 
                                 key=lambda f: self.distance_to(my_pet, f))
                return self.move_toward(my_pet, closest_food)
        
        elif action == 'help_friend':
            # Find pet that needs help
            other_pets = [p for name, p in game_state['pets'].items() if name != self.name]
            needy_pets = [p for p in other_pets if p['hunger'] > 70 or p['happiness'] < 30]
            
            if needy_pets:
                friend = needy_pets[0]
                return self.move_toward(my_pet, friend)
        
        elif action == 'socialize':
            # Move toward other happy pets
            other_pets = [p for name, p in game_state['pets'].items() 
                         if name != self.name and p['happiness'] > 50]
            if other_pets:
                friend = random.choice(other_pets)
                return self.move_toward(my_pet, friend)
        
        elif action == 'rest':
            # Find quiet corner
            corner = {'x': random.choice([50, 750]), 'y': random.choice([50, 550])}
            return self.move_toward(my_pet, corner)
        
        else:  # explore
            # Random movement
            return {
                'dx': random.randint(-2, 2),
                'dy': random.randint(-2, 2)
            }
    
    def distance_to(self, pet, target):
        """Calculate distance between pet and target"""
        return math.sqrt((pet['x'] - target['x'])**2 + (pet['y'] - target['y'])**2)
    
    def move_toward(self, pet, target):
        """Calculate movement vector toward target"""
        dx = target['x'] - pet['x']
        dy = target['y'] - pet['y']
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 0:
            # Normalize and scale movement
            speed = 2
            return {
                'dx': int((dx / distance) * speed),
                'dy': int((dy / distance) * speed)
            }
        return {'dx': 0, 'dy': 0}

class PyGamePetAI:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("🐍 Python Pet AI - Ages 10-12")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Colors
        self.colors = {
            'background': (135, 206, 235),  # Sky blue
            'pet1': (255, 105, 180),        # Hot pink
            'pet2': (60, 179, 113),         # Sea green  
            'pet3': (255, 165, 0),          # Orange
            'food': (255, 215, 0),          # Gold
            'text': (25, 25, 112),          # Dark blue
            'ui': (240, 248, 255)           # Alice blue
        }
        
        # Game state
        self.pets = {
            'Buddy': {
                'x': 200, 'y': 200,
                'hunger': 30,
                'energy': 80,
                'happiness': 70,
                'color': self.colors['pet1'],
                'ai': PetAI('Buddy', {'helpful': 0.8, 'social': 0.7, 'hunger': 0.6})
            },
            'Luna': {
                'x': 400, 'y': 300,
                'hunger': 50,
                'energy': 60,
                'happiness': 40,
                'color': self.colors['pet2'],
                'ai': PetAI('Luna', {'helpful': 0.4, 'social': 0.3, 'hunger': 0.8})
            },
            'Dash': {
                'x': 600, 'y': 150,
                'hunger': 20,
                'energy': 90,
                'happiness': 80,
                'color': self.colors['pet3'],
                'ai': PetAI('Dash', {'helpful': 0.6, 'social': 0.9, 'hunger': 0.4})
            }
        }
        
        self.food_items = []
        self.messages = []
        
        # Fonts
        self.font_large = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 18)
        self.font_small = pygame.font.Font(None, 14)
        
        # Code display
        self.show_code = False
        self.current_code = ""
        
    def spawn_food(self):
        """Randomly spawn food items"""
        if len(self.food_items) < 3 and random.random() < 0.02:  # 2% chance per frame
            food = {
                'x': random.randint(50, self.width - 50),
                'y': random.randint(50, self.height - 150),
                'timer': 300  # Food disappears after 5 seconds
            }
            self.food_items.append(food)
    
    def update_pets(self):
        """Update pet AI and states"""
        
        game_state = {
            'pets': self.pets,
            'food_items': self.food_items
        }
        
        for pet_name, pet in self.pets.items():
            # AI thinking
            action = pet['ai'].think(game_state)
            movement = pet['ai'].execute_action(action, game_state)
            
            # Apply movement
            if movement:
                pet['x'] = max(25, min(self.width - 25, pet['x'] + movement['dx']))
                pet['y'] = max(25, min(self.height - 150, pet['y'] + movement['dy']))
            
            # Update pet stats over time
            pet['hunger'] = min(100, pet['hunger'] + 0.1)  # Gradually get hungry
            
            if action == 'rest':
                pet['energy'] = min(100, pet['energy'] + 1)
            else:
                pet['energy'] = max(0, pet['energy'] - 0.05)
            
            # Check food collision
            for food in self.food_items[:]:  # Copy list to avoid modification during iteration
                distance = math.sqrt((pet['x'] - food['x'])**2 + (pet['y'] - food['y'])**2)
                if distance < 30:
                    pet['hunger'] = max(0, pet['hunger'] - 30)
                    pet['happiness'] = min(100, pet['happiness'] + 10)
                    self.food_items.remove(food)
                    self.add_message(f"{pet_name} found food! 🍎")
            
            # Social interactions
            for other_name, other_pet in self.pets.items():
                if other_name != pet_name:
                    distance = math.sqrt((pet['x'] - other_pet['x'])**2 + (pet['y'] - other_pet['y'])**2)
                    if distance < 40:
                        # Pets interact when close
                        pet['happiness'] = min(100, pet['happiness'] + 0.5)
                        other_pet['happiness'] = min(100, other_pet['happiness'] + 0.5)
            
            # Generate code display based on AI actions
            if random.random() < 0.1:  # Show code occasionally
                self.generate_code_display(pet_name, action)
    
    def generate_code_display(self, pet_name, action):
        """Show Python code representation of AI thinking"""
        
        code_templates = {
            'find_food': f"""# {pet_name}'s AI Decision
if my_hunger > 70:
    goal = 'find_food'
    move_toward(closest_food)
    print('{pet_name}: I need food!')""",
            
            'help_friend': f"""# {pet_name}'s AI Decision  
if friend.happiness < 30:
    goal = 'help_friend'
    move_toward(friend)
    print('{pet_name}: My friend needs help!')""",
            
            'socialize': f"""# {pet_name}'s AI Decision
if my_happiness < 50:
    goal = 'socialize'
    find_happy_friend()
    print('{pet_name}: Time to make friends!')""",
            
            'rest': f"""# {pet_name}'s AI Decision
if my_energy < 20:
    goal = 'rest'
    find_quiet_spot()
    print('{pet_name}: I need to rest...')"""""
        }
        
        self.current_code = code_templates.get(action, "# AI thinking...")
        self.show_code = True
    
    def update_food(self):
        """Update food items"""
        for food in self.food_items[:]:
            food['timer'] -= 1
            if food['timer'] <= 0:
                self.food_items.remove(food)
    
    def add_message(self, message):
        """Add message to game log"""
        self.messages.append({
            'text': message,
            'timer': 180  # 3 seconds at 60 FPS
        })
        if len(self.messages) > 5:
            self.messages = self.messages[-5:]  # Keep last 5 messages
    
    def update_messages(self):
        """Update message timers"""
        for message in self.messages[:]:
            message['timer'] -= 1
            if message['timer'] <= 0:
                self.messages.remove(message)
    
    def draw_pet(self, pet, name):
        """Draw a pet with visual indicators"""
        
        x, y = int(pet['x']), int(pet['y'])
        
        # Pet body (circle)
        pygame.draw.circle(self.screen, pet['color'], (x, y), 20)
        pygame.draw.circle(self.screen, (0, 0, 0), (x, y), 20, 2)
        
        # Eyes
        pygame.draw.circle(self.screen, (255, 255, 255), (x-8, y-5), 4)
        pygame.draw.circle(self.screen, (255, 255, 255), (x+8, y-5), 4)
        pygame.draw.circle(self.screen, (0, 0, 0), (x-8, y-5), 2)
        pygame.draw.circle(self.screen, (0, 0, 0), (x+8, y-5), 2)
        
        # Mouth (happy/sad based on happiness)
        if pet['happiness'] > 60:
            # Happy mouth
            pygame.draw.arc(self.screen, (0, 0, 0), (x-8, y, 16, 10), 0, math.pi, 2)
        elif pet['happiness'] < 30:
            # Sad mouth
            pygame.draw.arc(self.screen, (0, 0, 0), (x-8, y+5, 16, 10), math.pi, 2*math.pi, 2)
        
        # Name label
        name_surface = self.font_small.render(name, True, self.colors['text'])
        name_rect = name_surface.get_rect(center=(x, y+35))
        self.screen.blit(name_surface, name_rect)
        
        # Status indicators
        if pet['hunger'] > 70:
            # Hungry indicator
            hunger_surface = self.font_medium.render("🍽️", True, self.colors['text'])
            self.screen.blit(hunger_surface, (x+25, y-25))
        
        if pet['energy'] < 30:
            # Tired indicator  
            tired_surface = self.font_medium.render("😴", True, self.colors['text'])
            self.screen.blit(tired_surface, (x-35, y-25))
        
        if pet['happiness'] > 80:
            # Happy indicator
            happy_surface = self.font_medium.render("😊", True, self.colors['text'])
            self.screen.blit(happy_surface, (x, y-35))
    
    def draw_food(self, food):
        """Draw food item"""
        x, y = int(food['x']), int(food['y'])
        pygame.draw.circle(self.screen, self.colors['food'], (x, y), 8)
        pygame.draw.circle(self.screen, (255, 140, 0), (x, y), 8, 2)
        
        # Food emoji
        food_surface = self.font_small.render("🍎", True, self.colors['text'])
        food_rect = food_surface.get_rect(center=(x, y))
        self.screen.blit(food_surface, food_rect)
    
    def draw_ui(self):
        """Draw user interface"""
        
        # UI background
        ui_rect = pygame.Rect(0, self.height - 140, self.width, 140)
        pygame.draw.rect(self.screen, self.colors['ui'], ui_rect)
        pygame.draw.rect(self.screen, self.colors['text'], ui_rect, 2)
        
        # Pet status bars
        y_start = self.height - 130
        for i, (pet_name, pet) in enumerate(self.pets.items()):
            x_start = 20 + i * 250
            
            # Pet name
            name_surface = self.font_medium.render(f"{pet_name}", True, self.colors['text'])
            self.screen.blit(name_surface, (x_start, y_start))
            
            # Status bars
            stats = [('Hunger', pet['hunger']), ('Energy', pet['energy']), ('Happy', pet['happiness'])]
            
            for j, (stat_name, value) in enumerate(stats):
                bar_y = y_start + 20 + j * 15
                
                # Stat label
                stat_surface = self.font_small.render(f"{stat_name}:", True, self.colors['text'])
                self.screen.blit(stat_surface, (x_start, bar_y))
                
                # Progress bar
                bar_rect = pygame.Rect(x_start + 60, bar_y, 100, 10)
                pygame.draw.rect(self.screen, (200, 200, 200), bar_rect)
                
                # Fill based on value
                fill_width = int((value / 100.0) * 100)
                if fill_width > 0:
                    fill_rect = pygame.Rect(x_start + 60, bar_y, fill_width, 10)
                    
                    # Color based on value
                    if value > 70:
                        color = (0, 255, 0)  # Green
                    elif value > 30:
                        color = (255, 255, 0)  # Yellow
                    else:
                        color = (255, 0, 0)  # Red
                    
                    pygame.draw.rect(self.screen, color, fill_rect)
                
                pygame.draw.rect(self.screen, self.colors['text'], bar_rect, 1)
        
        # Messages
        message_y = self.height - 35
        for message in self.messages:
            message_surface = self.font_small.render(message['text'], True, self.colors['text'])
            self.screen.blit(message_surface, (20, message_y))
            message_y -= 15
    
    def draw_code_display(self):
        """Draw Python code representation"""
        
        if self.show_code and self.current_code:
            # Code background
            code_rect = pygame.Rect(self.width - 300, 20, 280, 120)
            pygame.draw.rect(self.screen, (240, 240, 240), code_rect)
            pygame.draw.rect(self.screen, self.colors['text'], code_rect, 2)
            
            # Code title
            title_surface = self.font_medium.render("🐍 Python AI Code:", True, self.colors['text'])
            self.screen.blit(title_surface, (code_rect.x + 5, code_rect.y + 5))
            
            # Code lines
            code_lines = self.current_code.split('\n')
            for i, line in enumerate(code_lines[:5]):  # Show first 5 lines
                line_surface = self.font_small.render(line, True, self.colors['text'])
                self.screen.blit(line_surface, (code_rect.x + 5, code_rect.y + 25 + i * 15))
    
    def handle_events(self):
        """Handle pygame events"""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Spawn food manually
                    food = {
                        'x': random.randint(50, self.width - 50),
                        'y': random.randint(50, self.height - 150),
                        'timer': 300
                    }
                    self.food_items.append(food)
                    self.add_message("Food spawned! 🍎")
                
                elif event.key == pygame.K_c:
                    # Toggle code display
                    self.show_code = not self.show_code
                
                elif event.key == pygame.K_h:
                    # Show help
                    self.add_message("SPACE: Spawn food, C: Toggle code, H: Help")
    
    def run(self):
        """Main game loop"""
        
        print("🐍 PyGame Pet AI Started!")
        print("🎮 Watch the AI pets think and act autonomously!")
        print("⌨️  Controls: SPACE = Spawn Food, C = Toggle Code Display, H = Help")
        print()
        
        while self.running:
            # Handle events
            self.handle_events()
            
            # Update game logic
            self.spawn_food()
            self.update_pets()
            self.update_food()
            self.update_messages()
            
            # Hide code display after a while
            if self.show_code:
                if random.random() < 0.005:  # 0.5% chance to hide
                    self.show_code = False
            
            # Draw everything
            self.screen.fill(self.colors['background'])
            
            # Draw game objects
            for food in self.food_items:
                self.draw_food(food)
            
            for pet_name, pet in self.pets.items():
                self.draw_pet(pet, pet_name)
            
            # Draw UI
            self.draw_ui()
            
            if self.show_code:
                self.draw_code_display()
            
            # Title
            title_surface = self.font_large.render("🐍 Python Pet AI - Watch AI Pets Think!", True, self.colors['text'])
            title_rect = title_surface.get_rect(center=(self.width // 2, 20))
            self.screen.blit(title_surface, title_rect)
            
            # Instructions
            instruction_surface = self.font_small.render("SPACE: Spawn Food | C: Toggle Code | H: Help", True, self.colors['text'])
            instruction_rect = instruction_surface.get_rect(center=(self.width // 2, 45))
            self.screen.blit(instruction_surface, instruction_rect)
            
            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()

# Run the intermediate game
if __name__ == "__main__":
    try:
        game = PyGamePetAI()
        game.run()
    except ImportError:
        print("❌ PyGame not installed!")
        print("💡 Install with: pip install pygame")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have Python with PyGame installed")