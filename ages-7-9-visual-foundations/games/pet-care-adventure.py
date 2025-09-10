# Pet Care Adventure - Ages 7-9 Visual Programming Game
# A simplified version focusing on visual block concepts

import tkinter as tk
from tkinter import messagebox
import random

class PetCareAdventureGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🐱 Pet Care Adventure - Ages 7-9")
        self.root.geometry("800x600")
        self.root.configure(bg='#ffeeee')
        
        # Simple game state for young children
        self.pet = {
            'name': 'Fluffy',
            'happiness': 3,  # 1-5 stars
            'hunger': 2,     # 1-5 food bowls
            'energy': 4,     # 1-5 battery bars
            'tricks': []
        }
        
        self.blocks_used = []  # Track programming blocks used
        self.init_ui()
        
    def init_ui(self):
        """Create child-friendly interface"""
        
        # Big friendly title
        title = tk.Label(self.root, text="🐱 Pet Care Adventure!", 
                        font=('Comic Sans MS', 24, 'bold'), 
                        bg='#ffeeee', fg='#ff6b6b')
        title.pack(pady=15)
        
        # Main game area
        game_frame = tk.Frame(self.root, bg='#ffe4e4', relief='raised', bd=3)
        game_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Pet display (left side)
        pet_frame = tk.Frame(game_frame, bg='#ffe4e4')
        pet_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Pet canvas
        self.pet_canvas = tk.Canvas(pet_frame, bg='#87ceeb', height=300, width=400)
        self.pet_canvas.pack(pady=10)
        
        # Status display with pictures
        self.status_frame = tk.Frame(pet_frame, bg='#ffe4e4')
        self.status_frame.pack(fill='x', pady=10)
        
        # Visual programming blocks (right side)
        blocks_frame = tk.Frame(game_frame, bg='#e4f0ff', width=300, relief='groove', bd=2)
        blocks_frame.pack(side='right', fill='y', padx=10, pady=10)
        blocks_frame.pack_propagate(False)
        
        tk.Label(blocks_frame, text="🧩 Drag Blocks to Help Fluffy!", 
                font=('Comic Sans MS', 14, 'bold'), bg='#e4f0ff').pack(pady=10)
        
        self.create_visual_blocks(blocks_frame)
        self.update_display()
        
    def create_visual_blocks(self, parent):
        """Create visual programming blocks for young children"""
        
        # Action blocks with big buttons and emojis
        actions = [
            ("🍎 FEED", "feed", "#4CAF50"),
            ("🎾 PLAY", "play", "#2196F3"), 
            ("🛏️ SLEEP", "sleep", "#9C27B0"),
            ("🎓 TEACH", "teach", "#FF9800")
        ]
        
        for text, action, color in actions:
            block_frame = tk.Frame(parent, bg=color, relief='raised', bd=3)
            block_frame.pack(fill='x', pady=8, padx=10)
            
            btn = tk.Button(block_frame, text=text, 
                           font=('Comic Sans MS', 12, 'bold'),
                           bg=color, fg='white', relief='flat',
                           command=lambda a=action: self.use_block(a))
            btn.pack(fill='both', expand=True, padx=3, pady=3)
        
        # Special combo blocks
        tk.Label(parent, text="🌟 Special Combos:", 
                font=('Comic Sans MS', 12, 'bold'), bg='#e4f0ff').pack(pady=(20,5))
        
        combo_btn = tk.Button(parent, text="🎉 HAPPY COMBO\n(Feed + Play)", 
                             font=('Comic Sans MS', 10, 'bold'),
                             bg='#ff6b6b', fg='white',
                             command=self.happy_combo)
        combo_btn.pack(fill='x', pady=5, padx=10)
        
        # Block sequence display
        tk.Label(parent, text="📋 Blocks Used:", 
                font=('Comic Sans MS', 10, 'bold'), bg='#e4f0ff').pack(pady=(20,5))
        
        self.sequence_text = tk.Text(parent, height=6, width=25, 
                                    font=('Comic Sans MS', 9), bg='white')
        self.sequence_text.pack(padx=10, pady=5)
        
    def use_block(self, action):
        """Execute a visual programming block"""
        
        self.blocks_used.append(action)
        
        if action == "feed":
            if self.pet['hunger'] < 5:
                self.pet['hunger'] = min(5, self.pet['hunger'] + 2)
                self.pet['happiness'] = min(5, self.pet['happiness'] + 1)
                self.show_message("🍎 Yummy! Fluffy loves the food!")
            else:
                self.show_message("🍎 Fluffy is too full right now!")
                
        elif action == "play":
            if self.pet['energy'] > 1:
                self.pet['energy'] = max(1, self.pet['energy'] - 1)
                self.pet['happiness'] = min(5, self.pet['happiness'] + 2)
                self.show_message("🎾 Wheee! Playing is so fun!")
            else:
                self.show_message("🎾 Fluffy is too tired to play!")
                
        elif action == "sleep":
            self.pet['energy'] = min(5, self.pet['energy'] + 2)
            self.show_message("🛏️ Zzz... Fluffy feels much better!")
            
        elif action == "teach":
            if self.pet['energy'] > 2 and self.pet['happiness'] > 2:
                tricks = ["sit", "roll over", "shake hands", "dance", "sing"]
                new_trick = random.choice([t for t in tricks if t not in self.pet['tricks']])
                if new_trick:
                    self.pet['tricks'].append(new_trick)
                    self.pet['happiness'] = min(5, self.pet['happiness'] + 1)
                    self.pet['energy'] = max(1, self.pet['energy'] - 1)
                    self.show_message(f"🎓 Wow! Fluffy learned to {new_trick}!")
                else:
                    self.show_message("🎓 Fluffy knows all the tricks!")
            else:
                self.show_message("🎓 Fluffy needs more energy and happiness to learn!")
        
        self.update_sequence_display()
        self.update_display()
        self.check_achievements()
        
    def happy_combo(self):
        """Execute a special combo block"""
        
        self.blocks_used.append("happy_combo")
        
        # Feed + Play combo
        self.pet['hunger'] = min(5, self.pet['hunger'] + 1)
        if self.pet['energy'] > 1:
            self.pet['energy'] = max(1, self.pet['energy'] - 1)
        self.pet['happiness'] = 5  # Max happiness!
        
        self.show_message("🎉 SUPER COMBO! Fluffy is super happy!")
        self.update_sequence_display()
        self.update_display()
        
    def update_sequence_display(self):
        """Show the sequence of blocks used (programming concept)"""
        
        self.sequence_text.delete(1.0, tk.END)
        
        sequence_text = "Block Sequence:\n"
        for i, block in enumerate(self.blocks_used[-8:], 1):  # Show last 8 blocks
            block_names = {
                "feed": "🍎 FEED",
                "play": "🎾 PLAY", 
                "sleep": "🛏️ SLEEP",
                "teach": "🎓 TEACH",
                "happy_combo": "🎉 COMBO"
            }
            sequence_text += f"{i}. {block_names.get(block, block)}\n"
        
        self.sequence_text.insert(1.0, sequence_text)
        
    def update_display(self):
        """Update the pet display with visual indicators"""
        
        # Clear canvas
        self.pet_canvas.delete("all")
        
        # Draw background
        self.pet_canvas.create_rectangle(0, 0, 400, 300, fill='#87ceeb', outline='')
        
        # Draw pet (big and cute)
        pet_x, pet_y = 200, 150
        
        # Pet body (bigger circle)
        self.pet_canvas.create_oval(pet_x-40, pet_y-40, pet_x+40, pet_y+40, 
                                   fill='#ffb6c1', outline='#ff69b4', width=3)
        
        # Happy face based on happiness level
        if self.pet['happiness'] >= 4:
            # Very happy - big smile
            self.pet_canvas.create_arc(pet_x-20, pet_y-10, pet_x+20, pet_y+20, 
                                      start=0, extent=180, outline='black', width=3)
            self.pet_canvas.create_text(pet_x, pet_y-50, text="😸", font=('Arial', 20))
        elif self.pet['happiness'] >= 2:
            # Happy - normal smile  
            self.pet_canvas.create_arc(pet_x-15, pet_y-5, pet_x+15, pet_y+15,
                                      start=0, extent=180, outline='black', width=3)
            self.pet_canvas.create_text(pet_x, pet_y-50, text="😊", font=('Arial', 20))
        else:
            # Sad - frown
            self.pet_canvas.create_arc(pet_x-15, pet_y+5, pet_x+15, pet_y+25,
                                      start=0, extent=-180, outline='black', width=3)
            self.pet_canvas.create_text(pet_x, pet_y-50, text="😢", font=('Arial', 20))
        
        # Eyes
        self.pet_canvas.create_oval(pet_x-15, pet_y-15, pet_x-5, pet_y-5, fill='black')
        self.pet_canvas.create_oval(pet_x+5, pet_y-15, pet_x+15, pet_y-5, fill='black')
        
        # Pet name
        self.pet_canvas.create_text(pet_x, pet_y+60, text=f"🐱 {self.pet['name']}", 
                                   font=('Comic Sans MS', 16, 'bold'))
        
        # Status indicators around the pet
        if self.pet['hunger'] <= 2:
            self.pet_canvas.create_text(pet_x+50, pet_y-30, text="🍽️", font=('Arial', 16))
        if self.pet['energy'] <= 2:
            self.pet_canvas.create_text(pet_x-50, pet_y-30, text="😴", font=('Arial', 16))
        if self.pet['happiness'] >= 4:
            self.pet_canvas.create_text(pet_x, pet_y-70, text="✨", font=('Arial', 16))
            
        self.update_status_display()
        
    def update_status_display(self):
        """Update status with visual bars and emojis"""
        
        # Clear existing status
        for widget in self.status_frame.winfo_children():
            widget.destroy()
        
        # Status with big visual indicators
        stats = [
            ("😊 Happiness", self.pet['happiness'], "⭐", '#ff69b4'),
            ("🍽️ Hunger", self.pet['hunger'], "🥘", '#4CAF50'),
            ("⚡ Energy", self.pet['energy'], "🔋", '#2196F3')
        ]
        
        for stat_name, value, emoji, color in stats:
            stat_frame = tk.Frame(self.status_frame, bg='#ffe4e4')
            stat_frame.pack(fill='x', pady=5)
            
            # Stat label
            tk.Label(stat_frame, text=stat_name, font=('Comic Sans MS', 12, 'bold'),
                    bg='#ffe4e4').pack(anchor='w')
            
            # Visual indicator bar with emojis
            indicator_frame = tk.Frame(stat_frame, bg='#ffe4e4')
            indicator_frame.pack(fill='x')
            
            for i in range(5):
                if i < value:
                    tk.Label(indicator_frame, text=emoji, font=('Arial', 16),
                           bg='#ffe4e4').pack(side='left')
                else:
                    tk.Label(indicator_frame, text="⚪", font=('Arial', 16),
                           bg='#ffe4e4').pack(side='left')
        
        # Show tricks learned
        if self.pet['tricks']:
            tricks_frame = tk.Frame(self.status_frame, bg='#ffe4e4')
            tricks_frame.pack(fill='x', pady=(10,0))
            
            tk.Label(tricks_frame, text="🎓 Tricks Learned:", 
                    font=('Comic Sans MS', 10, 'bold'), bg='#ffe4e4').pack(anchor='w')
            
            tricks_text = ", ".join(self.pet['tricks'])
            tk.Label(tricks_frame, text=tricks_text, font=('Comic Sans MS', 9),
                    bg='#ffe4e4', wraplength=350).pack(anchor='w')
    
    def show_message(self, message):
        """Show a friendly message to the child"""
        
        messagebox.showinfo("🐱 Fluffy says:", message)
        
    def check_achievements(self):
        """Check for achievements and celebrate"""
        
        # Simple achievements for young children
        if (self.pet['happiness'] == 5 and 
            self.pet['hunger'] >= 3 and 
            self.pet['energy'] >= 3):
            
            if len(self.blocks_used) == 1:
                self.show_message("🎉 First Block Award! You used your first programming block!")
            elif len(self.blocks_used) == 5:
                self.show_message("🌟 Block Master! You've used 5 programming blocks!")
            elif self.pet['happiness'] == 5:
                self.show_message("💖 Perfect Pet Parent! Fluffy is super happy!")
        
        if len(self.pet['tricks']) >= 3:
            self.show_message("🎓 Trick Master! Fluffy knows so many tricks!")
    
    def run(self):
        """Start the game"""
        self.root.mainloop()

# Run the age-appropriate game
if __name__ == "__main__":
    print("🐱 Starting Pet Care Adventure for Ages 7-9...")
    print("🎮 Learn programming through visual blocks and pet care!")
    print()
    
    try:
        game = PetCareAdventureGame()
        game.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have Python with tkinter installed")