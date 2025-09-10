# 🎮 Interactive AI Learning Game: "Virtual Pet Academy"
## From Playing to Programming AI - Progressive Game-Based Learning

### 🌟 Overview
"Virtual Pet Academy" is a progressive learning game where children start by simply playing and caring for virtual pets, then gradually learn to program NPC behaviors, and finally implement AI to create intelligent, autonomous pet companions. This creates a natural learning progression from user to programmer to AI developer.

---

## 🎯 Game Progression Stages

### **Stage 1: Player Experience (Ages 7-9)**
*"Let's Play and Learn!"*

Children start by simply playing the game to understand mechanics and build emotional connection.

#### **🐱 Basic Gameplay**
```
🏠 Virtual Pet Academy

Your Pet: Fluffy the Cat 🐱
Energy: ████████░░ (80%)
Happiness: ███████░░░ (70%) 
Hunger: ██░░░░░░░░ (20%)

🎮 Available Actions:
[🍎 Feed] [🎾 Play] [🛏️ Sleep] [🎓 Teach Trick]

🏆 Achievements Today:
✅ Fed Fluffy 3 times
✅ Taught "sit" command
🎯 Goal: Teach 2 more tricks!
```

#### **🎪 Interactive Pet Behaviors**
The pet responds to actions with realistic behaviors:

- **Feeding**: Pet gets happy, does little dance
- **Playing**: Pet runs around, jumps, shows excitement  
- **Tired**: Pet yawns, moves slowly, seeks bed
- **Learning**: Pet tries trick, sometimes fails, celebrates success

**🗣️ Sample Dialogue:**
**Child:** *clicks Feed button*
**Fluffy:** "Meow! 😸 That was delicious! I feel so much better!"
**Game:** *Fluffy does a happy spin and purrs*

**Child:** *clicks Teach Trick*  
**Fluffy:** "Meow? 🤔 I'll try to learn this new trick!"
**Game:** *Shows Fluffy attempting to sit, wobbling, then succeeding*
**Fluffy:** "I did it! 🎉 Meow meow!"

---

### **Stage 2: NPC Introduction (Ages 10-12)**
*"Meet the Academy Friends!"*

Introduce other pets (NPCs) with simple, rule-based behaviors that children can observe and eventually modify.

#### **🏫 Academy Environment**
```
🎓 Virtual Pet Academy - Classroom View

Your Pets:
🐱 Fluffy (Your main pet)
🐶 Buddy (Friendly NPC - always wants to play)
🐰 Luna (Shy NPC - hides when strangers approach)
🐦 Chirpy (Energetic NPC - loves to explore)

🎯 NPC Behaviors You Can Observe:
• Buddy: Runs to any pet that looks sad
• Luna: Hides behind objects when new pets arrive  
• Chirpy: Flies around collecting shiny objects

📝 Your Mission: Watch and learn their patterns!
```

#### **🔍 Pattern Recognition Activity**
Before programming, children observe and document NPC behaviors:

**📋 Observation Journal:**
```
🐶 Buddy's Behavior Patterns:

When I observe Buddy for 5 minutes:
✅ Saw Buddy run to Luna when she was sad (2 times)
✅ Buddy shared his food with Chirpy (1 time)  
✅ Buddy started playing when Fluffy looked bored (3 times)

🤔 I think Buddy's rule is: "Help friends when they need it"

🐰 Luna's Behavior Patterns:

When new pets arrive:
✅ Luna runs behind the tree (every time!)
✅ Luna peeks out after 30 seconds (if area is quiet)
✅ Luna comes out to play only with familiar pets

🤔 I think Luna's rule is: "Stay safe, warm up slowly"
```

---

### **Stage 3: Basic NPC Programming (Ages 10-12)**
*"Let's Program Pet Behaviors!"*

Children learn to modify simple NPC behaviors using visual programming blocks.

#### **🧩 Visual Block Programming Interface**

**Programming Buddy's Helper Behavior:**
```
┌─────────────────────────────────────────────────────┐
│ 🐶 Programming Buddy the Helper Dog                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ [When] [Any Pet] [Looks Sad] →                      │
│    [Move To] [Sad Pet]                              │
│    [Play Animation] [Tail Wag]                      │
│    [Say] "Don't be sad! Let's play!"                │
│    [Start Activity] [Play Together]                 │
│                                                     │
│ [When] [Buddy Has] [Extra Food] →                   │
│    [Look For] [Hungry Pet]                          │
│    [If Found] →                                     │
│       [Give] [Half Food] [To Hungry Pet]            │
│       [Say] "Sharing is caring!"                    │
│                                                     │
│ [When] [No Pets Need Help] →                        │
│    [Do] [Happy Dance]                               │
│    [Wait] [5 Seconds]                               │
│    [Repeat]                                         │
└─────────────────────────────────────────────────────┘
```

**Programming Luna's Shy Behavior:**
```
┌─────────────────────────────────────────────────────┐
│ 🐰 Programming Luna the Shy Rabbit                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│ [When] [New Pet Arrives] →                          │
│    [Play Sound] "Eep!"                              │
│    [Run To] [Hiding Spot]                           │
│    [Hide For] [30 Seconds]                          │
│                                                     │
│ [While] [Hidden] →                                  │
│    [Every 10 Seconds] →                             │
│       [Peek Out]                                    │
│       [If] [Area Is Quiet] →                        │
│          [Come Out Slowly]                          │
│       [Else] →                                      │
│          [Hide Again]                               │
│                                                     │
│ [When] [Playing With Friends] →                     │
│    [Gradually] [Get More Confident]                 │
│    [Share] [Favorite Hiding Spots]                  │
└─────────────────────────────────────────────────────┘
```

#### **🎯 Learning Objectives**
- **Conditional Logic**: "If this, then that"
- **Loops**: "Repeat this behavior"  
- **Variables**: "Remember this information"
- **Functions**: "Do this sequence of actions"

---

### **Stage 4: Intermediate AI Programming (Ages 13-15)**
*"Create Smart Pet Personalities!"*

Transition to text-based programming with simple AI decision-making systems.

#### **🐍 Python Pet AI Programming**

**Smart Pet Base Class:**
```python
import random
import time

class SmartPet:
    def __init__(self, name, personality_type):
        self.name = name
        self.personality = personality_type
        
        # Basic needs (0-100)
        self.hunger = 50
        self.energy = 80
        self.happiness = 70
        self.social = 60
        
        # AI decision-making weights based on personality
        self.personality_weights = self.get_personality_weights()
        
        # Memory system for learning
        self.memories = []
        self.favorite_activities = {}
        self.friend_relationships = {}
    
    def get_personality_weights(self):
        """Define how personality affects decision-making"""
        personalities = {
            'friendly': {
                'help_others': 0.8,
                'seek_attention': 0.7,
                'share_resources': 0.9,
                'explore': 0.5
            },
            'shy': {
                'help_others': 0.4,
                'seek_attention': 0.2,
                'share_resources': 0.6,
                'explore': 0.3
            },
            'energetic': {
                'help_others': 0.6,
                'seek_attention': 0.8,
                'share_resources': 0.5,
                'explore': 0.9
            },
            'calm': {
                'help_others': 0.7,
                'seek_attention': 0.3,
                'share_resources': 0.8,
                'explore': 0.4
            }
        }
        return personalities.get(self.personality, personalities['friendly'])
    
    def think_and_act(self, environment):
        """AI decision-making system"""
        
        # Analyze current situation
        situation = self.analyze_environment(environment)
        
        # Consider possible actions
        possible_actions = self.get_possible_actions(situation)
        
        # Use AI to choose best action
        chosen_action = self.choose_action(possible_actions, situation)
        
        # Execute action and learn from result
        result = self.execute_action(chosen_action, environment)
        self.learn_from_experience(chosen_action, result)
        
        return chosen_action, result
    
    def analyze_environment(self, environment):
        """Analyze what's happening around the pet"""
        situation = {
            'other_pets': environment.get('pets', []),
            'available_food': environment.get('food', 0),
            'toys_available': environment.get('toys', []),
            'time_of_day': environment.get('time', 'day'),
            'weather': environment.get('weather', 'sunny')
        }
        
        # Check if other pets need help
        situation['pets_needing_help'] = []
        for pet in situation['other_pets']:
            if pet.hunger > 80 or pet.happiness < 30:
                situation['pets_needing_help'].append(pet)
        
        return situation
    
    def get_possible_actions(self, situation):
        """Generate list of possible actions based on current situation"""
        actions = []
        
        # Basic survival actions
        if self.hunger > 70:
            actions.append(('eat', 'high_priority'))
        if self.energy < 30:
            actions.append(('sleep', 'high_priority'))
        
        # Social actions based on personality
        if situation['pets_needing_help'] and self.personality_weights['help_others'] > 0.5:
            actions.append(('help_friend', 'medium_priority'))
        
        if len(situation['other_pets']) > 0 and self.personality_weights['seek_attention'] > 0.6:
            actions.append(('play_with_friends', 'medium_priority'))
        
        # Exploration actions
        if situation['toys_available'] and self.personality_weights['explore'] > 0.5:
            actions.append(('explore_toy', 'low_priority'))
        
        # Self-care actions
        if self.happiness < 50:
            actions.append(('do_favorite_activity', 'medium_priority'))
        
        return actions
    
    def choose_action(self, possible_actions, situation):
        """AI decision-making using weighted random choice"""
        if not possible_actions:
            return ('idle', 'low_priority')
        
        # Priority scoring
        priority_scores = {'high_priority': 3, 'medium_priority': 2, 'low_priority': 1}
        
        # Calculate weighted scores for each action
        action_scores = []
        for action, priority in possible_actions:
            base_score = priority_scores[priority]
            
            # Personality influence
            if action == 'help_friend':
                base_score *= self.personality_weights['help_others']
            elif action == 'play_with_friends':
                base_score *= self.personality_weights['seek_attention']
            elif action == 'explore_toy':
                base_score *= self.personality_weights['explore']
            
            # Experience influence (learn from past)
            if action in self.favorite_activities:
                base_score *= (1 + self.favorite_activities[action] * 0.1)
            
            action_scores.append((action, base_score))
        
        # Weighted random selection
        total_weight = sum(score for _, score in action_scores)
        random_value = random.uniform(0, total_weight)
        
        current_weight = 0
        for action, score in action_scores:
            current_weight += score
            if random_value <= current_weight:
                return action
        
        return possible_actions[0][0]  # Fallback
    
    def execute_action(self, action, environment):
        """Execute the chosen action and return result"""
        result = {'success': True, 'happiness_change': 0, 'message': ''}
        
        if action == 'eat':
            if environment.get('food', 0) > 0:
                self.hunger = max(0, self.hunger - 30)
                result['message'] = f"{self.name} munches happily on some food!"
                result['happiness_change'] = 10
            else:
                result['success'] = False
                result['message'] = f"{self.name} looks around for food but finds none."
        
        elif action == 'help_friend':
            needy_pets = [pet for pet in environment.get('pets', []) 
                         if pet.hunger > 80 or pet.happiness < 30]
            if needy_pets:
                friend = random.choice(needy_pets)
                if friend.hunger > 80 and environment.get('food', 0) > 0:
                    # Share food
                    friend.hunger = max(0, friend.hunger - 20)
                    self.happiness += 15
                    result['message'] = f"{self.name} shares food with {friend.name}!"
                    result['happiness_change'] = 15
                else:
                    # Comfort friend
                    friend.happiness += 10
                    self.happiness += 10
                    result['message'] = f"{self.name} comforts {friend.name}!"
                    result['happiness_change'] = 10
        
        elif action == 'play_with_friends':
            friends = environment.get('pets', [])
            if friends:
                friend = random.choice(friends)
                self.happiness += 15
                friend.happiness += 10
                self.energy -= 10
                result['message'] = f"{self.name} plays happily with {friend.name}!"
                result['happiness_change'] = 15
        
        elif action == 'explore_toy':
            toys = environment.get('toys', [])
            if toys:
                toy = random.choice(toys)
                self.happiness += 12
                self.energy -= 5
                result['message'] = f"{self.name} discovers the {toy} and has fun!"
                result['happiness_change'] = 12
        
        elif action == 'sleep':
            self.energy = min(100, self.energy + 40)
            result['message'] = f"{self.name} takes a refreshing nap."
        
        elif action == 'do_favorite_activity':
            activity = random.choice(['sing', 'dance', 'sunbathe', 'groom'])
            self.happiness += 8
            result['message'] = f"{self.name} decides to {activity} and feels better!"
            result['happiness_change'] = 8
        
        # Apply happiness change
        self.happiness = min(100, max(0, self.happiness + result['happiness_change']))
        
        return result
    
    def learn_from_experience(self, action, result):
        """Learn from action outcomes to improve future decisions"""
        
        # Store memory of this experience
        memory = {
            'action': action,
            'result': result,
            'timestamp': time.time(),
            'my_state': {
                'hunger': self.hunger,
                'energy': self.energy,
                'happiness': self.happiness
            }
        }
        self.memories.append(memory)
        
        # Keep only recent memories (last 50)
        if len(self.memories) > 50:
            self.memories = self.memories[-50:]
        
        # Update favorite activities based on success
        if result['success'] and result['happiness_change'] > 0:
            if action not in self.favorite_activities:
                self.favorite_activities[action] = 0.1
            else:
                self.favorite_activities[action] = min(1.0, 
                    self.favorite_activities[action] + 0.1)
        
        # Reduce preference for unsuccessful actions
        elif not result['success']:
            if action in self.favorite_activities:
                self.favorite_activities[action] = max(0.0,
                    self.favorite_activities[action] - 0.05)
    
    def get_status_report(self):
        """Get current pet status for display"""
        return {
            'name': self.name,
            'personality': self.personality,
            'hunger': self.hunger,
            'energy': self.energy,
            'happiness': self.happiness,
            'social': self.social,
            'favorite_activities': self.favorite_activities,
            'memory_count': len(self.memories)
        }

# Example Usage
def create_pet_academy():
    """Create a virtual pet academy with AI pets"""
    
    # Create AI pets with different personalities
    pets = [
        SmartPet("Buddy", "friendly"),
        SmartPet("Luna", "shy"), 
        SmartPet("Dash", "energetic"),
        SmartPet("Sage", "calm")
    ]
    
    # Academy environment
    environment = {
        'pets': pets,
        'food': 100,
        'toys': ['ball', 'feather_wand', 'puzzle_box', 'tunnel'],
        'time': 'morning',
        'weather': 'sunny'
    }
    
    return pets, environment

def run_academy_simulation():
    """Run the pet academy simulation"""
    pets, environment = create_pet_academy()
    
    print("🎓 Welcome to Virtual Pet Academy!")
    print("🤖 AI pets are thinking and acting on their own...\n")
    
    for round_num in range(1, 6):  # 5 rounds of simulation
        print(f"📅 Round {round_num}:")
        print("-" * 40)
        
        for pet in pets:
            # Each pet thinks and acts based on AI
            action, result = pet.think_and_act(environment)
            print(f"🐾 {result['message']}")
            
            # Show pet's current thoughts
            status = pet.get_status_report()
            print(f"   💭 {pet.name} feels: Hunger={status['hunger']}, "
                  f"Energy={status['energy']}, Happiness={status['happiness']}")
        
        print()
        time.sleep(2)  # Pause between rounds
        
        # Environment changes over time
        environment['food'] = max(0, environment['food'] - 10)
        if round_num == 3:
            environment['time'] = 'afternoon'
            print("🌅 Time passes... It's now afternoon!")

# Run the simulation
if __name__ == "__main__":
    run_academy_simulation()
```

---

### **Stage 5: Advanced AI Integration (Ages 16-18)**
*"Build AI That Learns and Adapts!"*

Implement machine learning and advanced AI techniques for truly intelligent NPCs.

#### **🧠 Neural Network Pet Personality System**

```python
import numpy as np
import tensorflow as tf
from sklearn.cluster import KMeans
import json

class AdvancedAIPet:
    def __init__(self, name, base_personality):
        self.name = name
        self.base_personality = base_personality
        
        # Initialize neural network for decision making
        self.decision_network = self.build_decision_network()
        
        # Advanced memory system with clustering
        self.experience_buffer = []
        self.personality_evolution = [base_personality.copy()]
        
        # Emotional state system
        self.emotional_state = {
            'joy': 0.5, 'sadness': 0.1, 'anger': 0.1, 
            'fear': 0.2, 'curiosity': 0.7, 'affection': 0.6
        }
        
        # Learning parameters
        self.learning_rate = 0.01
        self.exploration_rate = 0.3
        
    def build_decision_network(self):
        """Build neural network for complex decision making"""
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(20,)),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(16, activation='relu'),
            tf.keras.layers.Dense(8, activation='softmax')  # 8 possible actions
        ])
        
        model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def encode_situation(self, environment, internal_state):
        """Convert complex situation into neural network input"""
        
        # Environment features (10 dimensions)
        env_features = [
            len(environment.get('pets', [])) / 10.0,  # Number of other pets
            environment.get('food', 0) / 100.0,       # Available food
            len(environment.get('toys', [])) / 10.0,  # Available toys
            1.0 if environment.get('time') == 'day' else 0.0,  # Time of day
            1.0 if environment.get('weather') == 'sunny' else 0.0,  # Weather
            # Social dynamics
            sum(1 for pet in environment.get('pets', []) if pet.happiness < 30) / 10.0,
            sum(1 for pet in environment.get('pets', []) if pet.hunger > 70) / 10.0,
            # Environmental richness
            environment.get('new_stimuli', 0) / 5.0,
            environment.get('noise_level', 0.5),
            environment.get('crowding', 0.0)
        ]
        
        # Internal state features (10 dimensions)
        internal_features = [
            internal_state['hunger'] / 100.0,
            internal_state['energy'] / 100.0,
            internal_state['happiness'] / 100.0,
            internal_state['social'] / 100.0,
            # Emotional state
            self.emotional_state['joy'],
            self.emotional_state['curiosity'],
            self.emotional_state['affection'],
            self.emotional_state['fear'],
            # Learning metrics
            len(self.experience_buffer) / 1000.0,
            self.exploration_rate
        ]
        
        return np.array(env_features + internal_features).reshape(1, -1)
    
    def predict_action(self, situation_encoding):
        """Use neural network to predict best action"""
        
        # Get action probabilities from neural network
        action_probs = self.decision_network.predict(situation_encoding, verbose=0)[0]
        
        # Add exploration noise
        if np.random.random() < self.exploration_rate:
            # Explore: choose random action sometimes
            action_index = np.random.randint(0, len(action_probs))
        else:
            # Exploit: choose best predicted action
            action_index = np.argmax(action_probs)
        
        # Map index to action
        actions = ['eat', 'sleep', 'play', 'explore', 'help_friend', 
                  'socialize', 'learn_skill', 'creative_activity']
        
        return actions[action_index], action_probs[action_index]
    
    def advanced_thinking(self, environment):
        """Advanced AI thinking with learning and adaptation"""
        
        # Get current internal state
        internal_state = {
            'hunger': getattr(self, 'hunger', 50),
            'energy': getattr(self, 'energy', 80), 
            'happiness': getattr(self, 'happiness', 70),
            'social': getattr(self, 'social', 60)
        }
        
        # Encode situation for neural network
        situation_encoding = self.encode_situation(environment, internal_state)
        
        # Predict action using neural network
        chosen_action, confidence = self.predict_action(situation_encoding)
        
        # Execute action with advanced logic
        result = self.execute_advanced_action(chosen_action, environment)
        
        # Learn from experience using reinforcement learning
        self.learn_from_advanced_experience(
            situation_encoding, chosen_action, result, environment
        )
        
        # Update emotional state based on experience
        self.update_emotional_state(result)
        
        # Evolve personality over time
        self.evolve_personality(result)
        
        return chosen_action, result, confidence
    
    def execute_advanced_action(self, action, environment):
        """Execute actions with complex, context-aware logic"""
        
        result = {
            'success': True, 
            'reward': 0,
            'message': '',
            'social_impact': 0,
            'learning_value': 0
        }
        
        if action == 'help_friend':
            # Advanced helping behavior with empathy
            needy_pets = [pet for pet in environment.get('pets', [])
                         if hasattr(pet, 'emotional_state') and 
                         (pet.emotional_state.get('sadness', 0) > 0.5 or
                          getattr(pet, 'hunger', 0) > 70)]
            
            if needy_pets:
                friend = max(needy_pets, 
                           key=lambda p: p.emotional_state.get('sadness', 0))
                
                # Tailored help based on friend's personality
                if hasattr(friend, 'base_personality'):
                    if friend.base_personality.get('shy', False):
                        # Gentle approach for shy pets
                        result['message'] = f"{self.name} quietly sits near {friend.name}, offering silent comfort"
                        friend.emotional_state['fear'] = max(0, friend.emotional_state['fear'] - 0.2)
                    else:
                        # Direct help for outgoing pets
                        result['message'] = f"{self.name} enthusiastically helps {friend.name}!"
                        friend.emotional_state['joy'] += 0.3
                
                result['reward'] = 15
                result['social_impact'] = 10
                self.emotional_state['affection'] += 0.1
        
        elif action == 'learn_skill':
            # Complex learning with skill progression
            available_skills = ['problem_solving', 'empathy', 'creativity', 'leadership']
            skill_to_learn = np.random.choice(available_skills)
            
            # Learning success based on current emotional state and environment
            learning_multiplier = (
                self.emotional_state['curiosity'] * 2 +
                self.emotional_state['joy'] * 1.5 -
                self.emotional_state['fear'] * 0.5
            )
            
            if learning_multiplier > 1.0:
                result['message'] = f"{self.name} successfully learns {skill_to_learn}!"
                result['reward'] = 20
                result['learning_value'] = 15
                
                # Add skill to personality evolution
                if not hasattr(self, 'learned_skills'):
                    self.learned_skills = {}
                self.learned_skills[skill_to_learn] = \
                    self.learned_skills.get(skill_to_learn, 0) + 1
            else:
                result['message'] = f"{self.name} struggles to focus on learning {skill_to_learn}"
                result['reward'] = 5
                result['learning_value'] = 3
        
        elif action == 'creative_activity':
            # Creative expression based on personality and emotions
            creativity_level = (
                self.emotional_state['joy'] * 0.4 +
                self.emotional_state['curiosity'] * 0.6
            )
            
            if creativity_level > 0.7:
                activities = ['compose_song', 'paint_picture', 'write_story', 'invent_game']
                activity = np.random.choice(activities)
                result['message'] = f"{self.name} creates a beautiful {activity.replace('_', ' ')}!"
                result['reward'] = 18
                
                # Creative activities boost joy and reduce negative emotions
                self.emotional_state['joy'] = min(1.0, self.emotional_state['joy'] + 0.2)
                self.emotional_state['sadness'] = max(0, self.emotional_state['sadness'] - 0.1)
            else:
                result['message'] = f"{self.name} tries to be creative but feels uninspired"
                result['reward'] = 3
        
        # Standard actions with personality influence
        elif action == 'socialize':
            friends = environment.get('pets', [])
            if friends:
                # Choose friend based on compatibility
                compatible_friend = self.choose_compatible_friend(friends)
                if compatible_friend:
                    result['message'] = f"{self.name} enjoys deep conversation with {compatible_friend.name}"
                    result['reward'] = 12
                    result['social_impact'] = 8
                    
                    # Both pets benefit from good socialization
                    self.emotional_state['affection'] += 0.15
                    if hasattr(compatible_friend, 'emotional_state'):
                        compatible_friend.emotional_state['affection'] += 0.1
        
        return result
    
    def choose_compatible_friend(self, available_friends):
        """Choose friend based on personality compatibility"""
        if not available_friends:
            return None
        
        compatibility_scores = []
        for friend in available_friends:
            if hasattr(friend, 'base_personality') and hasattr(friend, 'emotional_state'):
                # Calculate compatibility based on personality and emotional state
                compatibility = 0
                
                # Similar energy levels attract
                my_energy = self.emotional_state['joy'] + self.emotional_state['curiosity']
                friend_energy = friend.emotional_state['joy'] + friend.emotional_state['curiosity']
                energy_compatibility = 1.0 - abs(my_energy - friend_energy)
                compatibility += energy_compatibility * 0.4
                
                # Complementary traits (shy + outgoing can work well)
                if self.base_personality.get('shy', False) != friend.base_personality.get('outgoing', False):
                    compatibility += 0.3
                
                # Shared interests boost compatibility
                my_skills = getattr(self, 'learned_skills', {})
                friend_skills = getattr(friend, 'learned_skills', {})
                shared_skills = set(my_skills.keys()) & set(friend_skills.keys())
                compatibility += len(shared_skills) * 0.1
                
                compatibility_scores.append((friend, compatibility))
            else:
                compatibility_scores.append((friend, 0.5))  # Default compatibility
        
        # Choose friend with highest compatibility
        best_friend, _ = max(compatibility_scores, key=lambda x: x[1])
        return best_friend
    
    def learn_from_advanced_experience(self, situation, action, result, environment):
        """Advanced reinforcement learning from experience"""
        
        # Create training example for neural network
        action_index = ['eat', 'sleep', 'play', 'explore', 'help_friend', 
                       'socialize', 'learn_skill', 'creative_activity'].index(action)
        
        # Create target output (one-hot encoding with reward adjustment)
        target = np.zeros(8)
        target[action_index] = min(1.0, result['reward'] / 20.0)  # Normalize reward
        
        # Store experience for batch learning
        experience = {
            'situation': situation,
            'action': action_index,
            'reward': result['reward'],
            'target': target,
            'success': result['success']
        }
        
        self.experience_buffer.append(experience)
        
        # Batch learning every 10 experiences
        if len(self.experience_buffer) >= 10:
            self.batch_learn()
        
        # Adjust exploration rate based on success
        if result['success'] and result['reward'] > 10:
            self.exploration_rate = max(0.1, self.exploration_rate - 0.01)
        else:
            self.exploration_rate = min(0.5, self.exploration_rate + 0.005)
    
    def batch_learn(self):
        """Learn from batch of experiences using neural network"""
        
        if len(self.experience_buffer) < 5:
            return
        
        # Prepare training data
        situations = np.vstack([exp['situation'] for exp in self.experience_buffer[-10:]])
        targets = np.vstack([exp['target'] for exp in self.experience_buffer[-10:]])
        
        # Train neural network
        self.decision_network.fit(
            situations, targets,
            epochs=1, verbose=0,
            batch_size=min(len(situations), 5)
        )
        
        # Clear old experiences (keep memory manageable)
        if len(self.experience_buffer) > 100:
            self.experience_buffer = self.experience_buffer[-50:]
    
    def update_emotional_state(self, result):
        """Update emotional state based on action results"""
        
        # Joy increases with successful actions
        if result['success'] and result['reward'] > 10:
            self.emotional_state['joy'] = min(1.0, self.emotional_state['joy'] + 0.1)
            self.emotional_state['sadness'] = max(0, self.emotional_state['sadness'] - 0.05)
        
        # Social actions affect affection
        if result.get('social_impact', 0) > 0:
            self.emotional_state['affection'] = min(1.0, 
                self.emotional_state['affection'] + result['social_impact'] * 0.01)
        
        # Learning activities boost curiosity
        if result.get('learning_value', 0) > 0:
            self.emotional_state['curiosity'] = min(1.0,
                self.emotional_state['curiosity'] + 0.05)
        
        # Natural emotional decay (return to baseline over time)
        for emotion in self.emotional_state:
            if emotion in ['joy', 'sadness', 'anger', 'fear']:
                baseline = 0.3 if emotion in ['sadness', 'anger', 'fear'] else 0.6
                decay_rate = 0.02
                current = self.emotional_state[emotion]
                self.emotional_state[emotion] = current + (baseline - current) * decay_rate
    
    def evolve_personality(self, result):
        """Allow personality to evolve based on experiences"""
        
        # Track personality changes over time
        current_personality = self.base_personality.copy()
        
        # Social experiences make pets more outgoing
        if result.get('social_impact', 0) > 5:
            current_personality['outgoing'] = min(1.0,
                current_personality.get('outgoing', 0.5) + 0.02)
            current_personality['shy'] = max(0.0,
                current_personality.get('shy', 0.5) - 0.02)
        
        # Learning experiences boost intelligence traits  
        if result.get('learning_value', 0) > 10:
            current_personality['intelligence'] = min(1.0,
                current_personality.get('intelligence', 0.5) + 0.01)
            current_personality['curiosity_trait'] = min(1.0,
                current_personality.get('curiosity_trait', 0.5) + 0.01)
        
        # Creative activities boost creativity trait
        if 'creative' in result.get('message', '').lower():
            current_personality['creativity'] = min(1.0,
                current_personality.get('creativity', 0.5) + 0.02)
        
        # Store personality evolution
        self.personality_evolution.append(current_personality)
        self.base_personality = current_personality
        
        # Keep personality history manageable
        if len(self.personality_evolution) > 50:
            self.personality_evolution = self.personality_evolution[-25:]
    
    def get_advanced_status(self):
        """Get comprehensive status including AI insights"""
        
        status = {
            'name': self.name,
            'base_personality': self.base_personality,
            'emotional_state': self.emotional_state,
            'learned_skills': getattr(self, 'learned_skills', {}),
            'exploration_rate': self.exploration_rate,
            'experience_count': len(self.experience_buffer),
            'personality_changes': len(self.personality_evolution) - 1,
            'neural_network_accuracy': self.get_network_performance()
        }
        
        return status
    
    def get_network_performance(self):
        """Evaluate how well the neural network is performing"""
        if len(self.experience_buffer) < 10:
            return 0.5  # Default performance
        
        # Simple accuracy measure based on recent successful actions
        recent_experiences = self.experience_buffer[-10:]
        success_rate = sum(1 for exp in recent_experiences if exp['success']) / len(recent_experiences)
        
        return success_rate

# Advanced Academy Simulation
def run_advanced_academy():
    """Run advanced AI pet academy with machine learning"""
    
    print("🧠 Advanced AI Pet Academy - Machine Learning Edition!")
    print("🤖 Pets are learning, evolving, and adapting in real-time...\n")
    
    # Create advanced AI pets
    pets = [
        AdvancedAIPet("Neo", {'outgoing': 0.8, 'intelligence': 0.9, 'creativity': 0.7}),
        AdvancedAIPet("Luna", {'shy': 0.7, 'empathy': 0.9, 'curiosity_trait': 0.8}),
        AdvancedAIPet("Dash", {'energy': 0.9, 'creativity': 0.8, 'leadership': 0.6}),
        AdvancedAIPet("Sage", {'intelligence': 0.9, 'patience': 0.8, 'wisdom': 0.7})
    ]
    
    # Rich environment with dynamic elements
    environment = {
        'pets': pets,
        'food': 100,
        'toys': ['neural_puzzle', 'empathy_simulator', 'creativity_kit', 'logic_game'],
        'time': 'morning',
        'weather': 'sunny',
        'new_stimuli': 3,
        'noise_level': 0.3,
        'crowding': 0.2
    }
    
    for round_num in range(1, 8):  # 7 rounds of advanced simulation
        print(f"🧠 AI Learning Round {round_num}:")
        print("=" * 50)
        
        for pet in pets:
            # Advanced AI thinking and learning
            action, result, confidence = pet.advanced_thinking(environment)
            
            print(f"🤖 {result['message']}")
            print(f"   💭 Action: {action} (Confidence: {confidence:.2f})")
            
            # Show emotional and learning state
            status = pet.get_advanced_status()
            emotions = status['emotional_state']
            print(f"   😊 Emotions: Joy={emotions['joy']:.2f}, "
                  f"Curiosity={emotions['curiosity']:.2f}, "
                  f"Affection={emotions['affection']:.2f}")
            
            if status['learned_skills']:
                skills = ", ".join(status['learned_skills'].keys())
                print(f"   🎓 Skills: {skills}")
            
            print(f"   📈 Learning: {status['experience_count']} experiences, "
                  f"Network accuracy: {status['neural_network_accuracy']:.2f}")
            print()
        
        # Dynamic environment changes
        environment['new_stimuli'] = max(0, environment['new_stimuli'] - 1)
        environment['food'] = max(20, environment['food'] - 15)
        
        if round_num == 3:
            environment['weather'] = 'rainy'
            environment['noise_level'] = 0.6
            print("🌧️ It starts raining... The environment becomes more challenging!")
        
        if round_num == 5:
            environment['toys'].append('advanced_ai_companion')
            print("🤖 A new AI companion toy appears in the academy!")
        
        print()
        time.sleep(3)  # Pause between rounds

if __name__ == "__main__":
    run_advanced_academy()
```

---

## 🎯 Educational Progression Summary

### **Learning Journey Overview**

| Stage | Age Group | Focus | Technology | Key Skills |
|-------|-----------|--------|------------|------------|
| **1. Play** | 7-9 | Game enjoyment | Visual interface | Basic interaction, pattern recognition |
| **2. Observe** | 10-12 | NPC behavior | Visual programming | Logic, cause-effect relationships |
| **3. Program** | 10-12 | NPC control | Block coding | Conditional logic, loops, functions |
| **4. AI Basics** | 13-15 | Smart behaviors | Python scripting | Object-oriented programming, decision trees |
| **5. ML/AI** | 16-18 | Learning systems | Neural networks | Machine learning, data science, AI ethics |

### **🎮 Complete Game Implementation**

Save this as a standalone game that children can actually play:

```python
# Save as: virtual_pet_academy_game.py
# A complete playable game implementing all stages

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
                
                # Color coding
                if value < 30:
                    progress.configure(style='red.Horizontal.TProgressbar')
                elif value < 60:
                    progress.configure(style='yellow.Horizontal.TProgressbar') 
                else:
                    progress.configure(style='green.Horizontal.TProgressbar')
        
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
    game = VirtualPetAcademyGame()
    game.run()
```

---

## 🚀 Integration with Curriculum

This game perfectly demonstrates the progression from **play** → **programming** → **AI development** that prepares students for advanced computer science concepts while maintaining engagement through the beloved pet care theme.

The game can be saved as a standalone Python file that children can actually run and play, making the abstract concepts of AI and programming tangible and fun!