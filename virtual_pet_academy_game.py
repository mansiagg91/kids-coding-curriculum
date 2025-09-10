# Virtual Pet Academy - Complete Interactive Game
# A playable game that teaches programming and AI concepts progressively
# Save this file and run: python virtual_pet_academy_game.py

import tkinter as tk
from tkinter import ttk, messagebox
import json
import random
import time
from datetime import datetime

class VirtualPetAcademyGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🎓 Virtual Pet Academy")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f8ff')
        
        # Game state
        self.player_level = 1  # 1=Play, 2=Observe, 3=Program, 4=AI
        self.pets = {}
        self.environment = {
            'food': 100,
            'toys': ['ball', 'feather_wand', 'puzzle_box'],
            'time': 'morning'
        }
        
        self.init_ui()
        self.create_starter_pets()
        
    def init_ui(self):
        """Initialize the game user interface"""
        
        # Title
        title_label = tk.Label(self.root, text="🎓 Virtual Pet Academy", 
                              font=('Arial', 24, 'bold'), bg='#f0f8ff', fg='#2c3e50')
        title_label.pack(pady=10)
        
        # Main game area
        self.game_frame = tk.Frame(self.root, bg='#ecf0f1', relief='raised', bd=2)
        self.game_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Pet display area
        self.pet_display_frame = tk.Frame(self.game_frame, bg='#ecf0f1')
        self.pet_display_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Control panel
        self.control_frame = tk.Frame(self.game_frame, bg='#bdc3c7', width=300)
        self.control_frame.pack(side='right', fill='y', padx=10, pady=10)
        self.control_frame.pack_propagate(False)
        
        self.setup_control_panel()
        self.setup_pet_display()
        
    def setup_control_panel(self):
        """Setup the game control panel"""
        
        # Level indicator
        self.level_label = tk.Label(self.control_frame, text=f"Level {self.player_level}: Play Mode",
                                   font=('Arial', 14, 'bold'), bg='#bdc3c7')
        self.level_label.pack(pady=10)
        
        # Action buttons
        self.action_frame = tk.Frame(self.control_frame, bg='#bdc3c7')
        self.action_frame.pack(pady=10, fill='x', padx=10)
        
        # Basic actions (always available)
        basic_actions = [
            ("🍎 Feed Pet", self.feed_pet),
            ("🎾 Play", self.play_with_pet),
            ("🛏️ Rest", self.pet_rest),
            ("🎓 Teach Trick", self.teach_trick)
        ]
        
        for text, command in basic_actions:
            btn = tk.Button(self.action_frame, text=text, command=command,
                           bg='#3498db', fg='white', font=('Arial', 10, 'bold'))
            btn.pack(fill='x', pady=2)
        
        # Advanced actions (unlocked at higher levels)
        tk.Label(self.control_frame, text="Advanced Actions:", 
                font=('Arial', 12, 'bold'), bg='#bdc3c7').pack(pady=(20, 5))
        
        self.advanced_frame = tk.Frame(self.control_frame, bg='#bdc3c7')
        self.advanced_frame.pack(fill='x', padx=10)
        
        # Programming interface (Level 3+)
        self.program_btn = tk.Button(self.advanced_frame, text="🧩 Program NPC", 
                                    command=self.open_programming_interface,
                                    bg='#e74c3c', fg='white', font=('Arial', 10, 'bold'),
                                    state='disabled')
        self.program_btn.pack(fill='x', pady=2)
        
        # AI interface (Level 4+)
        self.ai_btn = tk.Button(self.advanced_frame, text="🤖 AI Training", 
                               command=self.open_ai_interface,
                               bg='#9b59b6', fg='white', font=('Arial', 10, 'bold'),
                               state='disabled')
        self.ai_btn.pack(fill='x', pady=2)
        
        # Level up button
        self.level_up_btn = tk.Button(self.control_frame, text="⬆️ Level Up!", 
                                     command=self.level_up,
                                     bg='#27ae60', fg='white', font=('Arial', 12, 'bold'))
        self.level_up_btn.pack(side='bottom', pady=10, fill='x', padx=10)
        
        # Game log
        tk.Label(self.control_frame, text="Game Log:", 
                font=('Arial', 12, 'bold'), bg='#bdc3c7').pack(pady=(10, 5))
        
        self.log_text = tk.Text(self.control_frame, height=8, width=30, 
                               bg='white', font=('Arial', 9))
        self.log_text.pack(fill='x', padx=10, pady=5)
        
        # Scroll bar for log
        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side='right', fill='y')
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
        
    def setup_pet_display(self):
        """Setup the pet display area"""
        
        # Canvas for pet visualization
        self.pet_canvas = tk.Canvas(self.pet_display_frame, bg='#95a5a6', height=400)
        self.pet_canvas.pack(fill='both', expand=True, pady=10)
        
        # Pet status display
        self.status_frame = tk.Frame(self.pet_display_frame, bg='#ecf0f1')
        self.status_frame.pack(fill='x', pady=10)
        
    def create_starter_pets(self):
        """Create initial pets for the game"""
        
        # Player's main pet
        self.pets['Fluffy'] = {
            'name': 'Fluffy',
            'type': 'cat',
            'hunger': 50,
            'energy': 80,
            'happiness': 70,
            'x': 200,
            'y': 200,
            'color': '#ff6b6b',
            'player_pet': True,
            'ai_controlled': False
        }
        
        # NPC pets (will be introduced in later levels)
        self.pets['Buddy'] = {
            'name': 'Buddy', 
            'type': 'dog',
            'hunger': 40,
            'energy': 90,
            'happiness': 80,
            'x': 300,
            'y': 150,
            'color': '#4ecdc4',
            'player_pet': False,
            'ai_controlled': True,
            'personality': 'friendly',
            'visible': False  # Hidden until level 2
        }
        
        self.pets['Luna'] = {
            'name': 'Luna',
            'type': 'rabbit', 
            'hunger': 30,
            'energy': 60,
            'happiness': 50,
            'x': 150,
            'y': 250,
            'color': '#a8e6cf',
            'player_pet': False,
            'ai_controlled': True,
            'personality': 'shy',
            'visible': False  # Hidden until level 2
        }
        
        self.update_display()
        self.log_message("🎉 Welcome to Virtual Pet Academy!")
        self.log_message("🐱 Meet Fluffy, your first pet!")
        
    def update_display(self):
        """Update the pet display and status"""
        
        # Clear canvas
        self.pet_canvas.delete("all")
        
        # Draw environment elements
        self.pet_canvas.create_rectangle(50, 50, 550, 350, outline='#34495e', width=3)
        self.pet_canvas.create_text(300, 30, text="🏫 Pet Academy Classroom", 
                                   font=('Arial', 16, 'bold'), fill='#2c3e50')
        
        # Draw pets
        for pet_name, pet in self.pets.items():
            if pet.get('visible', True):  # Only show visible pets
                self.draw_pet(pet)
        
        # Update status display
        self.update_status_display()
        
    def draw_pet(self, pet):
        """Draw a pet on the canvas"""
        
        x, y = pet['x'], pet['y']
        color = pet['color']
        
        # Pet body (circle)
        self.pet_canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline='#2c3e50', width=2)
        
        # Pet face
        # Eyes
        self.pet_canvas.create_oval(x-10, y-8, x-5, y-3, fill='white', outline='black')
        self.pet_canvas.create_oval(x+5, y-8, x+10, y-3, fill='white', outline='black')
        self.pet_canvas.create_oval(x-8, y-6, x-6, y-4, fill='black')
        self.pet_canvas.create_oval(x+6, y-6, x+8, y-4, fill='black')
        
        # Mouth
        if pet['happiness'] > 50:
            # Happy mouth
            self.pet_canvas.create_arc(x-5, y, x+5, y+8, start=0, extent=180, outline='black', width=2)
        else:
            # Neutral mouth
            self.pet_canvas.create_line(x-3, y+3, x+3, y+3, fill='black', width=2)
        
        # Pet name
        self.pet_canvas.create_text(x, y+35, text=pet['name'], font=('Arial', 10, 'bold'))
        
        # Status indicators
        if pet['hunger'] > 70:
            self.pet_canvas.create_text(x+25, y-25, text="🍽️", font=('Arial', 12))
        if pet['energy'] < 30:
            self.pet_canvas.create_text(x-25, y-25, text="😴", font=('Arial', 12))
        if pet['happiness'] > 80:
            self.pet_canvas.create_text(x, y-35, text="😊", font=('Arial', 12))
        
    def update_status_display(self):
        """Update the status display for all pets"""
        
        # Clear existing status widgets
        for widget in self.status_frame.winfo_children():
            widget.destroy()
        
        # Show status for visible pets
        visible_pets = [pet for pet in self.pets.values() if pet.get('visible', True)]
        
        for i, pet in enumerate(visible_pets):
            pet_frame = tk.Frame(self.status_frame, bg='#ecf0f1', relief='groove', bd=1)
            pet_frame.pack(side='left', padx=5, pady=5, fill='x', expand=True)
            
            # Pet name and type
            name_label = tk.Label(pet_frame, text=f"{pet['name']} the {pet['type'].title()}", 
                                 font=('Arial', 10, 'bold'), bg='#ecf0f1')
            name_label.pack()
            
            # Status bars
            for stat, value in [('Hunger', pet['hunger']), ('Energy', pet['energy']), ('Happiness', pet['happiness'])]:
                stat_frame = tk.Frame(pet_frame, bg='#ecf0f1')
                stat_frame.pack(fill='x', padx=5, pady=2)
                
                tk.Label(stat_frame, text=f"{stat}:", font=('Arial', 8), bg='#ecf0f1').pack(side='left')
                
                # Progress bar
                progress = ttk.Progressbar(stat_frame, length=100, mode='determinate')
                progress.pack(side='right')
                progress['value'] = value
        
    def log_message(self, message):
        """Add a message to the game log"""
        
        timestamp = datetime.now().strftime("%H:%M")
        full_message = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, full_message)
        self.log_text.see(tk.END)  # Scroll to bottom
        
    # Game Actions
    def feed_pet(self):
        """Feed the player's pet"""
        
        if self.environment['food'] > 0:
            pet = self.pets['Fluffy']
            pet['hunger'] = max(0, pet['hunger'] - 30)
            pet['happiness'] = min(100, pet['happiness'] + 10)
            self.environment['food'] -= 10
            
            self.log_message("🍎 You fed Fluffy! Fluffy is happy!")
            
            # NPC reactions (if visible)
            if self.player_level >= 2:
                self.trigger_npc_reactions('feeding')
        else:
            self.log_message("❌ No food available! Need to get more food.")
            
        self.update_display()
        
    def play_with_pet(self):
        """Play with the player's pet"""
        
        pet = self.pets['Fluffy']
        if pet['energy'] > 20:
            pet['happiness'] = min(100, pet['happiness'] + 15)
            pet['energy'] = max(0, pet['energy'] - 15)
            
            self.log_message("🎾 You played with Fluffy! So much fun!")
            
            # NPC reactions
            if self.player_level >= 2:
                self.trigger_npc_reactions('playing')
        else:
            self.log_message("😴 Fluffy is too tired to play right now.")
            
        self.update_display()
        
    def pet_rest(self):
        """Let the pet rest"""
        
        pet = self.pets['Fluffy']
        pet['energy'] = min(100, pet['energy'] + 30)
        
        self.log_message("🛏️ Fluffy takes a nice nap and feels refreshed!")
        self.update_display()
        
    def teach_trick(self):
        """Teach the pet a new trick"""
        
        pet = self.pets['Fluffy']
        if pet['energy'] > 15 and pet['happiness'] > 40:
            tricks = ["sit", "roll over", "play dead", "shake hands", "spin"]
            trick = random.choice(tricks)
            
            pet['happiness'] = min(100, pet['happiness'] + 12)
            pet['energy'] = max(0, pet['energy'] - 10)
            
            self.log_message(f"🎓 Fluffy learned to {trick}! Great job!")
            
            # Check for level up
            self.check_level_progression()
        else:
            self.log_message("😕 Fluffy needs more energy and happiness to learn tricks.")
            
        self.update_display()
        
    def trigger_npc_reactions(self, action):
        """Trigger NPC reactions based on player actions"""
        
        if action == 'feeding' and self.pets['Buddy'].get('visible', False):
            if random.random() < 0.7:  # 70% chance
                self.log_message("🐶 Buddy wags his tail happily watching you feed Fluffy!")
                self.pets['Buddy']['happiness'] = min(100, self.pets['Buddy']['happiness'] + 5)
                
        if action == 'playing' and self.pets['Luna'].get('visible', False):
            if random.random() < 0.4:  # 40% chance (Luna is shy)
                self.log_message("🐰 Luna peeks out from her hiding spot, curious about the fun!")
                self.pets['Luna']['happiness'] = min(100, self.pets['Luna']['happiness'] + 3)
                
    def level_up(self):
        """Progress to the next level"""
        
        if self.player_level < 4:
            self.player_level += 1
            
            if self.player_level == 2:
                # Introduce NPCs
                self.pets['Buddy']['visible'] = True
                self.pets['Luna']['visible'] = True
                self.level_label.config(text=f"Level {self.player_level}: Observe Mode")
                self.log_message("🎉 Level Up! New friends have appeared!")
                self.log_message("🐶 Meet Buddy the friendly dog!")
                self.log_message("🐰 Meet Luna the shy rabbit!")
                
            elif self.player_level == 3:
                # Enable programming
                self.program_btn.config(state='normal')
                self.level_label.config(text=f"Level {self.player_level}: Program Mode")
                self.log_message("🎉 Level Up! You can now program NPC behaviors!")
                
            elif self.player_level == 4:
                # Enable AI
                self.ai_btn.config(state='normal') 
                self.level_label.config(text=f"Level {self.player_level}: AI Mode")
                self.log_message("🎉 Level Up! AI training is now available!")
                
            self.update_display()
        else:
            messagebox.showinfo("Max Level", "You've reached the maximum level! You're now a Pet Academy Master!")
            
    def check_level_progression(self):
        """Check if player is ready for next level"""
        
        pet = self.pets['Fluffy']
        
        # Simple progression criteria
        if (self.player_level == 1 and 
            pet['happiness'] > 80 and 
            pet['energy'] > 60):
            
            messagebox.showinfo("Ready to Level Up!", 
                              "Fluffy is very happy! You're ready to meet new friends. Click 'Level Up!' to continue.")
            
    def open_programming_interface(self):
        """Open the visual programming interface"""
        
        prog_window = tk.Toplevel(self.root)
        prog_window.title("🧩 NPC Programming Interface")
        prog_window.geometry("600x400")
        prog_window.configure(bg='#ecf0f1')
        
        tk.Label(prog_window, text="🧩 Program NPC Behavior", 
                font=('Arial', 16, 'bold'), bg='#ecf0f1').pack(pady=10)
        
        # Simple block programming interface
        blocks_frame = tk.Frame(prog_window, bg='#ecf0f1')
        blocks_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Example programming blocks
        tk.Label(blocks_frame, text="Drag blocks to create Buddy's behavior:", 
                font=('Arial', 12), bg='#ecf0f1').pack(anchor='w')
        
        # Condition blocks
        condition_frame = tk.Frame(blocks_frame, bg='#3498db', relief='raised', bd=2)
        condition_frame.pack(fill='x', pady=5)
        tk.Label(condition_frame, text="WHEN [Pet looks sad] →", 
                font=('Arial', 10, 'bold'), bg='#3498db', fg='white').pack(padx=10, pady=5)
        
        # Action blocks  
        action_frame = tk.Frame(blocks_frame, bg='#e74c3c', relief='raised', bd=2)
        action_frame.pack(fill='x', pady=5, padx=20)
        tk.Label(action_frame, text="   DO [Run to sad pet]", 
                font=('Arial', 10, 'bold'), bg='#e74c3c', fg='white').pack(padx=10, pady=5)
        
        action_frame2 = tk.Frame(blocks_frame, bg='#e74c3c', relief='raised', bd=2)
        action_frame2.pack(fill='x', pady=5, padx=20)
        tk.Label(action_frame2, text="   DO [Play together]", 
                font=('Arial', 10, 'bold'), bg='#e74c3c', fg='white').pack(padx=10, pady=5)
        
        # Test button
        test_btn = tk.Button(blocks_frame, text="🧪 Test Program", 
                            command=lambda: self.test_npc_program(),
                            bg='#27ae60', fg='white', font=('Arial', 12, 'bold'))
        test_btn.pack(pady=20)
        
    def test_npc_program(self):
        """Test the programmed NPC behavior"""
        
        self.log_message("🧪 Testing Buddy's program...")
        self.log_message("🐶 Buddy: 'I'll help any sad pet I see!'")
        
        # Simulate programmed behavior
        if self.pets['Fluffy']['happiness'] < 60:
            self.log_message("🐶 Buddy notices Fluffy is sad and runs over!")
            self.log_message("🐶 Buddy and Fluffy play together!")
            self.pets['Fluffy']['happiness'] = min(100, self.pets['Fluffy']['happiness'] + 20)
            self.pets['Buddy']['happiness'] = min(100, self.pets['Buddy']['happiness'] + 15)
        else:
            self.log_message("🐶 Buddy: 'Everyone looks happy! I'll just wait here.'")
            
        self.update_display()
        
    def open_ai_interface(self):
        """Open the AI training interface"""
        
        ai_window = tk.Toplevel(self.root)
        ai_window.title("🤖 AI Training Center")
        ai_window.geometry("700x500")
        ai_window.configure(bg='#2c3e50')
        
        tk.Label(ai_window, text="🤖 AI Training Center", 
                font=('Arial', 18, 'bold'), bg='#2c3e50', fg='white').pack(pady=10)
        
        # AI training interface
        training_frame = tk.Frame(ai_window, bg='#34495e', relief='raised', bd=2)
        training_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(training_frame, text="Train Luna's AI to overcome shyness:", 
                font=('Arial', 14), bg='#34495e', fg='white').pack(pady=10)
        
        # Training parameters
        param_frame = tk.Frame(training_frame, bg='#34495e')
        param_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(param_frame, text="Confidence Level:", 
                font=('Arial', 12), bg='#34495e', fg='white').pack(anchor='w')
        
        self.confidence_scale = tk.Scale(param_frame, from_=0, to=100, orient='horizontal',
                                        bg='#34495e', fg='white', font=('Arial', 10))
        self.confidence_scale.set(30)  # Luna starts shy
        self.confidence_scale.pack(fill='x', pady=5)
        
        tk.Label(param_frame, text="Social Learning Rate:", 
                font=('Arial', 12), bg='#34495e', fg='white').pack(anchor='w')
        
        self.learning_scale = tk.Scale(param_frame, from_=1, to=10, orient='horizontal',
                                      bg='#34495e', fg='white', font=('Arial', 10))
        self.learning_scale.set(5)
        self.learning_scale.pack(fill='x', pady=5)
        
        # AI training button
        train_btn = tk.Button(training_frame, text="🧠 Train AI", 
                             command=lambda: self.train_ai(),
                             bg='#9b59b6', fg='white', font=('Arial', 14, 'bold'))
        train_btn.pack(pady=20)
        
        # AI status display
        self.ai_status = tk.Text(training_frame, height=8, bg='#ecf0f1', font=('Arial', 10))
        self.ai_status.pack(fill='x', padx=20, pady=10)
        
        self.ai_status.insert(tk.END, "🤖 AI Status: Ready for training\n")
        self.ai_status.insert(tk.END, "📊 Current Luna personality: 70% shy, 30% curious\n")
        self.ai_status.insert(tk.END, "🎯 Training goal: Increase social confidence\n")
        
    def train_ai(self):
        """Train the AI with current parameters"""
        
        confidence = self.confidence_scale.get()
        learning_rate = self.learning_scale.get()
        
        self.ai_status.insert(tk.END, f"\n🧠 Training with confidence={confidence}, learning_rate={learning_rate}\n")
        
        # Simulate AI training results
        if confidence > 60 and learning_rate > 7:
            self.ai_status.insert(tk.END, "✅ Training successful! Luna becomes more social!\n")
            self.pets['Luna']['happiness'] = min(100, self.pets['Luna']['happiness'] + 25)
            self.log_message("🤖 AI Training complete! Luna is now more confident!")
        elif confidence > 40:
            self.ai_status.insert(tk.END, "⚠️ Partial success. Luna is slightly more confident.\n")
            self.pets['Luna']['happiness'] = min(100, self.pets['Luna']['happiness'] + 10)
            self.log_message("🤖 AI Training shows progress. Luna is learning!")
        else:
            self.ai_status.insert(tk.END, "❌ Training needs adjustment. Try higher confidence levels.\n")
            self.log_message("🤖 AI Training needs more work. Keep trying!")
            
        self.update_display()
        self.ai_status.see(tk.END)
        
    def run(self):
        """Start the game"""
        self.root.mainloop()

# Run the complete game
if __name__ == "__main__":
    print("🎓 Starting Virtual Pet Academy...")
    print("🎮 This game teaches programming and AI through pet care!")
    print("📋 Requirements: Python with tkinter (usually pre-installed)")
    print()
    
    try:
        game = VirtualPetAcademyGame()
        game.run()
    except ImportError as e:
        print(f"❌ Missing required module: {e}")
        print("💡 Install with: pip install tkinter")
    except Exception as e:
        print(f"❌ Error starting game: {e}")
        print("💡 Make sure you have Python with GUI support installed")