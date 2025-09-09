# Lesson 6: Game Development with PyGame! 🎮

## 🎯 Today's Mission
Create your first real video game using Python and PyGame with sprites, sounds, and animations!

---

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<img src="https://via.placeholder.com/60x60/4CAF50/FFFFFF?text=👩‍💻" alt="Instructor">
<strong>Dr. Pythonia:</strong><br>
"Welcome to the most exciting part of programming - game development! PyGame is a powerful library that lets us create real video games with graphics, sounds, and animations. I've used similar graphics libraries in professional applications, and the concepts you'll learn apply to all visual programming!"
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<img src="https://via.placeholder.com/60x60/2196F3/FFFFFF?text=👦" alt="Student">
<strong>Jordan:</strong><br>
"We're making REAL games?! With moving characters and sound effects? Can I make a game like the ones on my phone? This is going to be epic!"
</div>

</div>

---

## 🎮 Introduction to PyGame

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia explains:</strong><br>
"PyGame is like a digital art studio combined with a physics engine! It handles graphics, sounds, collision detection, and user input. Many indie games are built with PyGame, and the concepts transfer to professional game engines like Unity."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan discovers:</strong><br>
"So PyGame is like the engine that makes everything work? And sprites are like the characters and objects in my game? Can I draw my own sprites?"
</div>

</div>

### Setting Up Your Game Window

```python
import pygame
import random
import sys

# Initialize PyGame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors (RGB values)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jordan's Awesome Game!")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill(BLACK)
    
    # Draw a welcome message
    font = pygame.font.Font(None, 74)
    text = font.render("Welcome to PyGame!", True, WHITE)
    text_rect = text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
    screen.blit(text, text_rect)
    
    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
```

---

## 🏃‍♂️ Activity 1: Creating Your First Sprite

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's sprite wisdom:</strong><br>
"Sprites are game objects - players, enemies, items, anything that moves or interacts! We'll create a Player class that handles movement, animation, and collision detection. This object-oriented approach is how professional games are structured."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's character idea:</strong><br>
"I want to make a space explorer character that can fly around and collect stars! Can I make it change colors when it moves? And add a trail effect?"
</div>

</div>

### Player Sprite Class

```python
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        # Create player sprite (simple colored rectangle)
        self.width = 40
        self.height = 30
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)
        
        # Add some style - draw a simple spaceship shape
        pygame.draw.polygon(self.image, WHITE, [
            (0, self.height), 
            (self.width//2, 0), 
            (self.width, self.height)
        ])
        
        # Position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement properties
        self.speed = 5
        self.vel_x = 0
        self.vel_y = 0
        
        # Animation properties
        self.trail = []  # Store previous positions for trail effect
        self.color_cycle = 0  # For color changing effect
        
    def update(self):
        # Handle movement
        keys = pygame.key.get_pressed()
        self.vel_x = 0
        self.vel_y = 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel_x = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel_x = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel_y = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel_y = self.speed
        
        # Move the player
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
        
        # Update trail effect
        if self.vel_x != 0 or self.vel_y != 0:  # Only add to trail when moving
            self.trail.append((self.rect.centerx, self.rect.centery))
            if len(self.trail) > 10:  # Keep trail to last 10 positions
                self.trail.pop(0)
        
        # Update color cycle for moving effect
        if self.vel_x != 0 or self.vel_y != 0:
            self.color_cycle += 1
            if self.color_cycle > 60:  # Reset every second at 60 FPS
                self.color_cycle = 0
    
    def draw_trail(self, screen):
        # Draw trail effect
        for i, pos in enumerate(self.trail):
            alpha = int(255 * (i / len(self.trail))) if self.trail else 0
            trail_color = (0, 100, 255, alpha)  # Blue with increasing transparency
            pygame.draw.circle(screen, trail_color[:3], pos, 3 * (i / len(self.trail) + 0.1))
    
    def get_display_color(self):
        # Change color based on movement
        if self.vel_x != 0 or self.vel_y != 0:
            # Cycle through colors when moving
            cycle = self.color_cycle // 10
            colors = [BLUE, GREEN, YELLOW, RED]
            return colors[cycle % len(colors)]
        return BLUE
```

### Complete Moving Player Example

```python
import pygame
import sys

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jordan's Space Explorer!")
clock = pygame.time.Clock()

# Create player
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()
    
    # Draw
    screen.fill(BLACK)
    
    # Draw trail first (behind player)
    player.draw_trail(screen)
    
    # Draw all sprites
    all_sprites.draw(screen)
    
    # Draw instructions
    font = pygame.font.Font(None, 36)
    instructions = [
        "Use Arrow Keys or WASD to move",
        "Watch the color-changing trail!"
    ]
    for i, instruction in enumerate(instructions):
        text = font.render(instruction, True, WHITE)
        screen.blit(text, (10, 10 + i * 40))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
```

---

## 🌟 Activity 2: Collectible Stars Game

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's game design:</strong><br>
"Now we'll add collectible items and scoring! This introduces collision detection, random generation, and game state management - core concepts in any interactive application. The patterns we use here scale to complex business software."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's gameplay vision:</strong><br>
"Can I make stars that sparkle and make sound when I collect them? Maybe different colored stars are worth different points? And power-ups that make me faster?"
</div>

</div>

### Star Collectible Class

```python
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Create star sprite
        self.size = random.randint(15, 25)
        self.image = pygame.Surface([self.size * 2, self.size * 2])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)  # Make black transparent
        
        # Draw a star shape
        self.star_color = random.choice([YELLOW, WHITE, (255, 215, 0)])  # Gold
        self.draw_star()
        
        # Position randomly
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, WINDOW_HEIGHT - self.rect.height)
        
        # Animation properties
        self.sparkle_timer = 0
        self.points = 10 if self.star_color == YELLOW else 20  # Gold stars worth more!
        
    def draw_star(self):
        # Draw a simple star shape
        center = (self.size, self.size)
        points = []
        
        # Create star points (5-pointed star)
        for i in range(10):
            angle = i * math.pi / 5
            if i % 2 == 0:
                # Outer points
                radius = self.size
            else:
                # Inner points
                radius = self.size // 2
            
            x = center[0] + radius * math.cos(angle - math.pi/2)
            y = center[1] + radius * math.sin(angle - math.pi/2)
            points.append((x, y))
        
        pygame.draw.polygon(self.image, self.star_color, points)
    
    def update(self):
        # Sparkle animation
        self.sparkle_timer += 1
        if self.sparkle_timer > 30:  # Sparkle every half second
            self.sparkle_timer = 0
            # Redraw with slight color variation for sparkle effect
            self.image.fill(BLACK)
            
            # Vary the color slightly for sparkle
            sparkle_color = list(self.star_color)
            for i in range(3):
                sparkle_color[i] = min(255, sparkle_color[i] + random.randint(-30, 30))
            
            self.draw_star_with_color(tuple(sparkle_color))
    
    def draw_star_with_color(self, color):
        center = (self.size, self.size)
        points = []
        
        for i in range(10):
            angle = i * math.pi / 5
            radius = self.size if i % 2 == 0 else self.size // 2
            x = center[0] + radius * math.cos(angle - math.pi/2)
            y = center[1] + radius * math.sin(angle - math.pi/2)
            points.append((x, y))
        
        pygame.draw.polygon(self.image, color, points)
```

### Complete Star Collector Game

```python
import pygame
import random
import math
import sys

pygame.init()

# Initialize sound
pygame.mixer.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)

# Create screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jordan's Star Collector Adventure!")
clock = pygame.time.Clock()

# Game variables
score = 0
stars_collected = 0
game_time = 0

# Sprite groups
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()

# Create player
player = Player(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
all_sprites.add(player)

# Create initial stars
for i in range(10):
    star = Star()
    all_sprites.add(star)
    stars.add(star)

# Sound effects (you can add actual sound files)
# collect_sound = pygame.mixer.Sound("collect.wav")  # Add your sound file
# Use a simple beep for now
def play_collect_sound():
    # Create a simple beep sound programmatically
    try:
        pygame.mixer.Sound.play(pygame.mixer.Sound(pygame.sndarray.make_sound(
            pygame.array.array("i", [int(4096 * math.sin(2 * math.pi * 440 * x / 44100)) 
                                    for x in range(4410)]))))
    except:
        pass  # Skip sound if not available

# Game loop
running = True
while running:
    game_time += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update all sprites
    all_sprites.update()
    
    # Check for collisions between player and stars
    collected_stars = pygame.sprite.spritecollide(player, stars, True)
    for star in collected_stars:
        score += star.points
        stars_collected += 1
        play_collect_sound()
        
        # Create a new star to replace the collected one
        new_star = Star()
        all_sprites.add(new_star)
        stars.add(new_star)
    
    # Draw everything
    screen.fill(BLACK)
    
    # Draw trail
    player.draw_trail(screen)
    
    # Draw all sprites
    all_sprites.draw(screen)
    
    # Draw UI
    font = pygame.font.Font(None, 48)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    stars_text = font.render(f"Stars: {stars_collected}", True, WHITE)
    screen.blit(stars_text, (10, 60))
    
    time_text = font.render(f"Time: {game_time // 60}s", True, WHITE)
    screen.blit(time_text, (10, 110))
    
    # Draw instructions
    instruction_font = pygame.font.Font(None, 24)
    instructions = [
        "Collect the sparkling stars!",
        "Gold stars = 20 points, Yellow stars = 10 points",
        "Use WASD or Arrow Keys to move"
    ]
    for i, instruction in enumerate(instructions):
        text = instruction_font.render(instruction, True, WHITE)
        screen.blit(text, (10, WINDOW_HEIGHT - 80 + i * 25))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
```

---

## 🚀 Activity 3: Space Shooter Game

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia's advanced project:</strong><br>
"Let's create a complete action game! We'll add shooting mechanics, enemy sprites, and game states (playing, game over, restart). This demonstrates event handling, collision systems, and state management used in professional applications."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan's action vision:</strong><br>
"A space shooter sounds amazing! Can I have different types of enemies? Maybe ones that move in patterns? And power-ups that change my weapon?"
</div>

</div>

### Bullet and Enemy Classes

```python
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.Surface([4, 10])
        self.image.fill(YELLOW)
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
        self.speed = 8
        
    def update(self):
        self.rect.y -= self.speed
        
        # Remove bullet if it goes off screen
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.size = random.randint(20, 40)
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(RED)
        
        # Draw simple enemy shape
        pygame.draw.circle(self.image, (150, 0, 0), 
                         (self.size//2, self.size//2), self.size//2)
        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -50)  # Start above screen
        
        self.speed = random.randint(2, 5)
        self.health = 2 if self.size > 30 else 1  # Bigger enemies have more health
        
    def update(self):
        self.rect.y += self.speed
        
        # Remove enemy if it goes off screen
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
    
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
            return True  # Enemy destroyed
        else:
            # Visual feedback for hit but not destroyed
            self.image.fill((100, 0, 0))  # Darker red when damaged
            return False
```

---

## 🎯 Challenge Projects

### Challenge 1: Platformer Game
Create a side-scrolling platformer with:
- Jumping mechanics with gravity
- Moving platforms
- Collectible coins
- Simple enemy AI

### Challenge 2: Puzzle Game
Build a tile-matching or block-stacking game:
- Grid-based movement
- Match detection algorithms
- Level progression system
- Save high scores

### Challenge 3: Racing Game
Develop a top-down racing game:
- Car sprites with realistic movement
- Track boundaries and collision detection
- Lap timing and checkpoints
- Multiple AI opponents

---

## 🏆 Game Development Concepts Learned

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Technical Skills:</strong><br>
• Sprite-based animation and movement<br>
• Collision detection algorithms<br>
• Game loop and timing systems<br>
• Object-oriented game architecture<br>
• Sound integration and effects<br>
• User interface and HUD design
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Game Design Skills:</strong><br>
• Player feedback and rewards<br>
• Difficulty progression and balance<br>
• Visual effects and polish<br>
• Interactive storytelling<br>
• Performance optimization<br>
• User experience in games
</div>

</div>

---

## 🛠️ Professional Game Development Path

### Industry Connections:
- **Indie Game Development:** PyGame skills transfer to commercial indie games
- **Game Engines:** Concepts apply to Unity, Unreal Engine, and Godot
- **Graphics Programming:** Foundation for 3D graphics and shaders
- **Interactive Media:** Skills useful for educational apps and simulations

### Next Steps:
- **Advanced PyGame:** Particle systems, advanced animations
- **Game Engines:** Transition to Unity or Unreal Engine
- **Graphics Programming:** Learn OpenGL or DirectX
- **Game Design:** Study mechanics, balance, and player psychology

---

## 🏠 Take Home Game Projects

### Project 1: Personal Game Idea
Design and build your own game concept:
- Write a game design document
- Create unique sprites and sounds  
- Implement your core game mechanic
- Test with friends and family

### Project 2: Improve Existing Games
Enhance the games we built today:
- Add new enemy types and behaviors
- Create power-ups and special abilities
- Design multiple levels or difficulties
- Add a main menu and settings screen

### Project 3: Game Portfolio
Document your game development journey:
- Screenshot gallery of your games
- Explain your favorite game mechanics
- Share what you learned about programming through games
- Plan your next game development project

---

## 🔮 Next Lesson Preview

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Dr. Pythonia teases:</strong><br>
"Next time, we'll explore data visualization and create interactive charts and graphs! We'll turn boring numbers into exciting visual stories - imagine creating your own dashboard to track your game scores or analyze real-world data!"
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Jordan anticipates:</strong><br>
"Can I create graphs that show my progress in the games we built? Or maybe analyze data from sports or science? This could help with school projects too!"
</div>

</div>

---

**Amazing work today! You've built real games that people can play and enjoy! 🎮✨**

*Remember: Every professional game developer started with simple projects like these. Keep experimenting, keep creating, and most importantly, keep having fun with code!*