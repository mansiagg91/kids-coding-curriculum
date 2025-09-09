# 🎮 PyGame Sprite Adventures - Complete Game Projects

## 🌟 Project Collection Overview

These game projects use sprites, animations, and interactive mechanics to create engaging learning experiences. Each project builds programming skills through fun, hands-on game development.

---

## 🏃‍♂️ Project 1: Sprite Adventure Runner

### Game Concept
A side-scrolling adventure where your character runs through different environments, collects items, and avoids obstacles.

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Learning Objectives:</strong><br>
• Sprite animation with multiple frames<br>
• Scrolling background systems<br>
• Collision detection with different object types<br>
• Score tracking and power-up systems<br>
• Game state management (playing, paused, game over)
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Student Goals:</strong><br>
"I want to create different worlds my character can run through - maybe a forest level, a space level, and an underwater level. Can I make my character have different animations for running, jumping, and collecting items?"
</div>

</div>

### Complete Implementation

```python
import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_frames):
        super().__init__()
        
        self.frames = sprite_frames
        self.current_frame = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.animation_speed = 0.2
        self.animation_counter = 0
        
    def animate(self):
        self.animation_counter += self.animation_speed
        if self.animation_counter >= 1:
            self.animation_counter = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

class Player(AnimatedSprite):
    def __init__(self, x, y):
        # Create simple running animation frames
        frames = self.create_player_frames()
        super().__init__(x, y, frames)
        
        self.speed = 5
        self.jump_speed = -15
        self.gravity = 0.8
        self.velocity_y = 0
        self.on_ground = False
        self.lives = 3
        
        # Animation states
        self.is_running = True
        self.is_jumping = False
        
    def create_player_frames(self):
        # Create simple animated character frames
        frames = []
        colors = [BLUE, (0, 100, 255), (0, 200, 255), (0, 100, 255)]
        
        for i, color in enumerate(colors):
            frame = pygame.Surface([40, 60])
            frame.fill(WHITE)
            frame.set_colorkey(WHITE)
            
            # Draw simple character
            # Body
            pygame.draw.ellipse(frame, color, [10, 15, 20, 30])
            # Head
            pygame.draw.circle(frame, color, [20, 12], 8)
            # Legs (animated position)
            leg_offset = i * 2 - 3
            pygame.draw.rect(frame, color, [15 + leg_offset, 45, 4, 15])
            pygame.draw.rect(frame, color, [21 - leg_offset, 45, 4, 15])
            # Arms
            pygame.draw.rect(frame, color, [8, 20, 6, 3])
            pygame.draw.rect(frame, color, [26, 20, 6, 3])
            
            frames.append(frame)
        
        return frames
    
    def update(self, platforms):
        keys = pygame.key.get_pressed()
        
        # Horizontal movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            
        # Jumping
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False
            self.is_jumping = True
        
        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        # Check platform collisions
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling down
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.is_jumping = False
        
        # Ground collision
        if self.rect.bottom >= WINDOW_HEIGHT - 50:
            self.rect.bottom = WINDOW_HEIGHT - 50
            self.velocity_y = 0
            self.on_ground = True
            self.is_jumping = False
        
        # Keep player on screen horizontally
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        
        # Animate only when moving and not jumping
        if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and self.on_ground:
            self.animate()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)
        # Add some texture
        for i in range(0, width, 20):
            pygame.draw.rect(self.image, (0, 200, 0), [i, 0, 2, height])
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Collectible(AnimatedSprite):
    def __init__(self, x, y, collectible_type="coin"):
        frames = self.create_collectible_frames(collectible_type)
        super().__init__(x, y, frames)
        
        self.type = collectible_type
        self.points = 10 if collectible_type == "coin" else 50
        self.animation_speed = 0.3
        
    def create_collectible_frames(self, collectible_type):
        frames = []
        colors = [YELLOW, (255, 255, 150), YELLOW, (255, 255, 100)] if collectible_type == "coin" else [PURPLE, (200, 0, 200), PURPLE, (150, 0, 150)]
        
        for color in colors:
            frame = pygame.Surface([30, 30])
            frame.fill(WHITE)
            frame.set_colorkey(WHITE)
            
            if collectible_type == "coin":
                pygame.draw.circle(frame, color, [15, 15], 12)
                pygame.draw.circle(frame, (200, 200, 0), [15, 15], 8)
            else:  # gem
                pygame.draw.polygon(frame, color, [
                    [15, 5], [25, 15], [15, 25], [5, 15]
                ])
            
            frames.append(frame)
        
        return frames
    
    def update(self):
        self.animate()

class Enemy(AnimatedSprite):
    def __init__(self, x, y):
        frames = self.create_enemy_frames()
        super().__init__(x, y, frames)
        
        self.speed = random.randint(1, 3)
        self.direction = random.choice([-1, 1])
        
    def create_enemy_frames(self):
        frames = []
        colors = [RED, (200, 0, 0), RED, (150, 0, 0)]
        
        for color in colors:
            frame = pygame.Surface([35, 35])
            frame.fill(WHITE)
            frame.set_colorkey(WHITE)
            
            # Draw simple enemy (spiky circle)
            pygame.draw.circle(frame, color, [17, 17], 15)
            # Add spikes
            for angle in range(0, 360, 45):
                import math
                x = 17 + 20 * math.cos(math.radians(angle))
                y = 17 + 20 * math.sin(math.radians(angle))
                pygame.draw.line(frame, color, [17, 17], [x, y], 3)
            
            frames.append(frame)
        
        return frames
    
    def update(self, platforms):
        self.rect.x += self.speed * self.direction
        
        # Reverse direction at screen edges or platform edges
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.direction *= -1
        
        self.animate()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sprite Adventure Runner!")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.score = 0
        self.level = 1
        self.game_state = "playing"  # playing, paused, game_over
        
        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # Create player
        self.player = Player(100, WINDOW_HEIGHT - 200)
        self.all_sprites.add(self.player)
        
        # Create level
        self.create_level()
        
        # Fonts
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
    def create_level(self):
        # Create platforms
        platform_data = [
            (0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50),  # Ground
            (200, WINDOW_HEIGHT - 150, 150, 20),
            (400, WINDOW_HEIGHT - 250, 150, 20),
            (650, WINDOW_HEIGHT - 180, 150, 20),
            (850, WINDOW_HEIGHT - 300, 100, 20),
        ]
        
        for x, y, width, height in platform_data:
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)
            self.all_sprites.add(platform)
        
        # Create collectibles
        collectible_positions = [
            (250, WINDOW_HEIGHT - 180, "coin"),
            (450, WINDOW_HEIGHT - 280, "coin"),
            (700, WINDOW_HEIGHT - 210, "gem"),
            (880, WINDOW_HEIGHT - 330, "gem"),
            (500, WINDOW_HEIGHT - 100, "coin"),
        ]
        
        for x, y, c_type in collectible_positions:
            collectible = Collectible(x, y, c_type)
            self.collectibles.add(collectible)
            self.all_sprites.add(collectible)
        
        # Create enemies
        enemy_positions = [
            (300, WINDOW_HEIGHT - 90),
            (550, WINDOW_HEIGHT - 90),
            (750, WINDOW_HEIGHT - 90),
        ]
        
        for x, y in enemy_positions:
            enemy = Enemy(x, y)
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.game_state = "paused" if self.game_state == "playing" else "playing"
                if event.key == pygame.K_r and self.game_state == "game_over":
                    self.restart_game()
        
        return True
    
    def update(self):
        if self.game_state != "playing":
            return
        
        # Update all sprites
        self.player.update(self.platforms)
        self.enemies.update(self.platforms)
        self.collectibles.update()
        
        # Check collectible collisions
        collected = pygame.sprite.spritecollide(self.player, self.collectibles, True)
        for item in collected:
            self.score += item.points
            # Create particle effect (simple)
            self.create_collect_effect(item.rect.centerx, item.rect.centery)
        
        # Check enemy collisions
        if pygame.sprite.spritecollide(self.player, self.enemies, False):
            self.player.lives -= 1
            if self.player.lives <= 0:
                self.game_state = "game_over"
            else:
                # Respawn player at safe position
                self.player.rect.x = 50
                self.player.rect.y = WINDOW_HEIGHT - 200
        
        # Check if all collectibles are collected
        if len(self.collectibles) == 0:
            self.level += 1
            self.create_level()
    
    def create_collect_effect(self, x, y):
        # Simple particle effect for collecting items
        for i in range(5):
            # You could create actual particle sprites here
            pass
    
    def draw(self):
        # Draw background
        self.screen.fill((135, 206, 235))  # Sky blue
        
        # Draw ground texture
        for x in range(0, WINDOW_WIDTH, 50):
            pygame.draw.line(self.screen, (0, 150, 0), 
                           (x, WINDOW_HEIGHT - 50), (x + 25, WINDOW_HEIGHT - 25), 2)
        
        # Draw all sprites
        self.all_sprites.draw(self.screen)
        
        # Draw UI
        self.draw_ui()
        
        # Draw game state overlays
        if self.game_state == "paused":
            self.draw_pause_screen()
        elif self.game_state == "game_over":
            self.draw_game_over_screen()
    
    def draw_ui(self):
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        
        # Level
        level_text = self.font.render(f"Level: {self.level}", True, BLACK)
        self.screen.blit(level_text, (10, 50))
        
        # Lives
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, BLACK)
        self.screen.blit(lives_text, (10, 90))
        
        # Instructions
        if self.level == 1 and self.score == 0:
            instructions = [
                "Use A/D or Arrow Keys to move",
                "SPACE or UP to jump",
                "Collect coins and gems!",
                "Avoid the spiky enemies",
                "Press P to pause"
            ]
            for i, instruction in enumerate(instructions):
                text = pygame.font.Font(None, 24).render(instruction, True, BLACK)
                self.screen.blit(text, (WINDOW_WIDTH - 250, 10 + i * 25))
    
    def draw_pause_screen(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.big_font.render("PAUSED", True, WHITE)
        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.screen.blit(pause_text, pause_rect)
        
        continue_text = self.font.render("Press P to continue", True, WHITE)
        continue_rect = continue_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 60))
        self.screen.blit(continue_text, continue_rect)
    
    def draw_game_over_screen(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.big_font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50))
        self.screen.blit(game_over_text, game_over_rect)
        
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        self.screen.blit(score_text, score_rect)
        
        restart_text = self.font.render("Press R to restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50))
        self.screen.blit(restart_text, restart_rect)
    
    def restart_game(self):
        # Clear all sprites
        self.all_sprites.empty()
        self.platforms.empty()
        self.collectibles.empty()
        self.enemies.empty()
        
        # Reset game state
        self.score = 0
        self.level = 1
        self.game_state = "playing"
        
        # Recreate player and level
        self.player = Player(100, WINDOW_HEIGHT - 200)
        self.all_sprites.add(self.player)
        self.create_level()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()

# Run the game
if __name__ == "__main__":
    game = Game()
    game.run()
```

---

## 🌌 Project 2: Space Sprite Shooter

### Enhanced Version with Multiple Enemy Types

```python
import pygame
import random
import math

class SpaceShooterGame:
    def __init__(self):
        pygame.init()
        
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.FPS = 60
        
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Sprite Shooter!")
        self.clock = pygame.time.Clock()
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        
        # Game state
        self.score = 0
        self.wave = 1
        self.lives = 3
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.power_ups = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        
        # Create player
        self.player = SpacePlayer(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT - 100)
        self.all_sprites.add(self.player)
        
        # Spawn initial wave
        self.spawn_enemy_wave()
        
        # Font
        self.font = pygame.font.Font(None, 36)
    
    def spawn_enemy_wave(self):
        enemy_count = 3 + self.wave * 2
        for i in range(enemy_count):
            enemy_type = random.choice(['basic', 'fast', 'strong', 'zigzag'])
            enemy = SpaceEnemy(enemy_type)
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)
    
    # ... (rest of implementation)
```

---

## 🏆 Project Extensions & Challenges

### Challenge 1: Multi-Level Adventure
- Create different themed worlds (forest, space, underwater)
- Design unique enemies for each world
- Add boss battles at the end of each world
- Implement save/load game functionality

### Challenge 2: Character Customization
- Allow players to choose different character sprites
- Add unlockable costumes and abilities
- Create a character upgrade system
- Implement different character classes with unique abilities

### Challenge 3: Multiplayer Features
- Add local co-op gameplay
- Create competitive mini-games
- Implement a high-score sharing system
- Design collaborative puzzle challenges

---

## 📱 Mobile-Friendly Adaptations

### Touch Controls
```python
class TouchControls:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.create_virtual_buttons()
    
    def create_virtual_buttons(self):
        # Create virtual D-pad and action buttons
        button_size = 80
        margin = 20
        
        # Movement buttons
        self.left_button = pygame.Rect(margin, self.screen_height - button_size - margin, button_size, button_size)
        self.right_button = pygame.Rect(margin + button_size + 10, self.screen_height - button_size - margin, button_size, button_size)
        
        # Action buttons
        self.jump_button = pygame.Rect(self.screen_width - button_size - margin, self.screen_height - button_size - margin, button_size, button_size)
        self.action_button = pygame.Rect(self.screen_width - button_size*2 - margin - 10, self.screen_height - button_size - margin, button_size, button_size)
    
    def handle_touch(self, pos, pressed):
        # Return which controls are active based on touch position
        controls = {
            'left': pressed and self.left_button.collidepoint(pos),
            'right': pressed and self.right_button.collidepoint(pos),
            'jump': pressed and self.jump_button.collidepoint(pos),
            'action': pressed and self.action_button.collidepoint(pos)
        }
        return controls
    
    def draw(self, screen):
        # Draw virtual buttons
        pygame.draw.rect(screen, (100, 100, 100), self.left_button)
        pygame.draw.rect(screen, (100, 100, 100), self.right_button)
        pygame.draw.rect(screen, (100, 100, 100), self.jump_button)
        pygame.draw.rect(screen, (100, 100, 100), self.action_button)
        
        # Add button labels
        font = pygame.font.Font(None, 24)
        
        left_text = font.render("←", True, (255, 255, 255))
        screen.blit(left_text, (self.left_button.centerx - 10, self.left_button.centery - 12))
        
        right_text = font.render("→", True, (255, 255, 255))
        screen.blit(right_text, (self.right_button.centerx - 10, self.right_button.centery - 12))
        
        jump_text = font.render("↑", True, (255, 255, 255))
        screen.blit(jump_text, (self.jump_button.centerx - 8, self.jump_button.centery - 12))
        
        action_text = font.render("A", True, (255, 255, 255))
        screen.blit(action_text, (self.action_button.centerx - 8, self.action_button.centery - 12))
```

---

## 🎨 Art Assets & Sprite Creation

### Creating Custom Sprite Sheets
```python
class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()
    
    def get_image(self, x, y, width, height, scale=1):
        # Extract a single sprite from the sheet
        image = pygame.Surface([width, height])
        image.blit(self.sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((0, 0, 0))  # Assuming black background
        return image
    
    def get_animation_frames(self, y_row, frame_count, frame_width, frame_height, scale=1):
        # Get multiple frames for animation
        frames = []
        for frame in range(frame_count):
            x = frame * frame_width
            frames.append(self.get_image(x, y_row * frame_height, frame_width, frame_height, scale))
        return frames

# Usage example:
# sprite_sheet = SpriteSheet("character_sprites.png")
# walk_frames = sprite_sheet.get_animation_frames(0, 4, 32, 32, 2)  # Row 0, 4 frames, 32x32 pixels, 2x scale
```

---

## 📚 Educational Extensions

### Math Integration
- **Trajectory Calculations:** Teach physics through projectile motion in games
- **Coordinate Geometry:** Use sprite positioning to reinforce x,y coordinate systems
- **Angles and Trigonometry:** Implement rotating sprites and circular movement patterns
- **Statistics:** Track and analyze game performance data

### Science Connections  
- **Biology:** Create ecosystem simulation games with predator/prey relationships
- **Chemistry:** Build molecular bonding games with sprite-based atoms
- **Physics:** Demonstrate concepts like gravity, momentum, and collisions through gameplay
- **Environmental Science:** Design games that teach about conservation and sustainability

### Art and Design Skills
- **Color Theory:** Experiment with sprite palettes and visual aesthetics  
- **Animation Principles:** Learn timing, easing, and character movement
- **User Interface Design:** Create intuitive and appealing game menus and HUDs
- **Storytelling:** Develop narrative elements and character development through games

---

**These sprite-based projects demonstrate how games make programming education engaging and memorable. Students learn complex programming concepts while creating projects they're genuinely excited to share and play!** 🎮✨