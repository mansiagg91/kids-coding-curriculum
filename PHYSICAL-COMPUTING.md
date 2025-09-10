# 🤖 Physical Computing Projects
## Connecting Code to the Real World - Ages 7-18

### 🚀 Overview
Transform abstract programming concepts into tangible, interactive experiences through hands-on hardware projects. Students build real devices they can touch, control, and share, making programming feel magical and immediately relevant to the physical world.

---

## 🌟 Ages 7-9: Touch & Play Computing

### **🎨 Magic Drawing Board**
*Duration: 2 weeks | Difficulty: Beginner*

#### **What We Build**
A colorful LED grid that responds to touch, letting kids "draw" with light using simple tap patterns.

**🛠️ Hardware:**
- 8x8 WS2812B LED matrix
- Capacitive touch sensors (4 zones)
- Arduino Uno or micro:bit
- Colorful 3D-printed case

**🎯 Learning Goals:**
- Cause and effect relationships
- Coordinate systems (X, Y positions)
- Color mixing (RGB values)
- Basic input/output concepts

#### **🧩 Visual Programming Blocks**
```
┌─────────────────────────────────────────────────────┐
│ 🎨 Magic Drawing Program                            │
│                                                     │
│ [When Touch Sensor 1 Pressed] →                    │
│    [Set LED Color to] [🔴 Red] [At Position] [X,Y] │
│                                                     │
│ [When Touch Sensor 2 Pressed] →                    │
│    [Set LED Color to] [🔵 Blue] [At Position] [X,Y]│
│                                                     │
│ [When Touch Sensor 3 Pressed] →                    │
│    [Clear All LEDs]                                 │
│                                                     │
│ [When Touch Sensor 4 Pressed] →                    │
│    [Rainbow Animation] [Speed: Fast]               │
└─────────────────────────────────────────────────────┘
```

#### **🎭 Project Extensions**
- **Musical Drawing**: Add buzzer sounds for each color
- **Pattern Games**: Simon Says with light sequences
- **Story Mode**: Draw scenes from favorite books

### **🐱 Interactive Pet Robot**
*Duration: 3 weeks | Difficulty: Beginner+*

#### **What We Build**
A adorable robot pet that responds to voice, follows light, and shows emotions through LEDs and movement.

**🛠️ Hardware:**
- Servo motors for movement
- Ultrasonic sensor for obstacle detection
- Sound sensor for voice response
- RGB LEDs for emotion display
- Speaker for pet sounds

**🎯 Learning Goals:**
- Sensors and actuators
- Conditional logic (if/then)
- Character personality programming
- Empathy through technology

#### **🗣️ Instructor-Student Dialogue**
**Ms. Code:** "Today we're giving our robot pet a personality! What should happen when someone claps their hands?"

**Alex:** "Maybe it should wag its tail and make happy sounds?"

**Ms. Code:** "Perfect! Let's use the sound sensor to detect clapping. When it hears a loud sound, we'll make the servo motor wag and play a happy beep!"

**Sarah:** "Can we make it sad if it's alone for too long?"

**Ms. Code:** "What a caring idea! We can use a timer. If no one interacts with it for 5 minutes, it could make sad sounds and dim its LED eyes."

#### **📱 Simple Code Logic**
```
Pet Behavior Rules:

🔊 If LOUD SOUND detected:
   → Wag tail (servo movement)
   → Play happy chirp
   → Flash green LEDs (joy)

💡 If BRIGHT LIGHT detected:
   → Move toward light
   → Purr sound
   → Blue LEDs (curiosity)

⏰ If NO INTERACTION for 300 seconds:
   → Slow LED fade (sadness)
   → Quiet whimper sound
   → Lower head position

👋 If HAND WAVE detected (distance sensor):
   → Excited tail wag
   → Rainbow LED sequence
   → Playful sound effects
```

---

## 🔧 Ages 10-12: Builder & Inventor Projects

### **🏠 Smart Room Controller**
*Duration: 4 weeks | Difficulty: Intermediate*

#### **What We Build**
A complete room automation system that controls lights, temperature, music, and security using smartphone app and voice commands.

**🛠️ Hardware:**
- Raspberry Pi 4 as main controller
- Relay modules for AC device control
- DHT22 temperature/humidity sensor
- PIR motion sensors
- RGB LED strips
- Bluetooth speaker integration
- Camera module for security

**🎯 Learning Goals:**
- Python programming with real hardware
- Network communication concepts
- API development and mobile apps
- Home automation principles
- Security and privacy considerations

#### **🐍 Python Code Examples**

**Temperature Control System:**
```python
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

class SmartThermostat:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT22
        self.sensor_pin = 4
        self.heater_relay = 18
        self.fan_relay = 19
        self.target_temp = 22  # Celsius
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.heater_relay, GPIO.OUT)
        GPIO.setup(self.fan_relay, GPIO.OUT)
    
    def read_temperature(self):
        """Get current room temperature"""
        humidity, temperature = Adafruit_DHT.read_retry(
            self.sensor, self.sensor_pin
        )
        return temperature, humidity
    
    def control_climate(self):
        """Smart climate control logic"""
        temp, humidity = self.read_temperature()
        
        if temp < self.target_temp - 1:
            self.turn_on_heater()
            print(f"🔥 Heater ON - Current: {temp}°C")
        elif temp > self.target_temp + 1:
            self.turn_on_fan()
            print(f"💨 Fan ON - Current: {temp}°C")
        else:
            self.turn_off_all()
            print(f"✅ Perfect temp: {temp}°C")
    
    def turn_on_heater(self):
        GPIO.output(self.heater_relay, GPIO.HIGH)
        GPIO.output(self.fan_relay, GPIO.LOW)
    
    def turn_on_fan(self):
        GPIO.output(self.fan_relay, GPIO.HIGH)
        GPIO.output(self.heater_relay, GPIO.LOW)
    
    def turn_off_all(self):
        GPIO.output(self.heater_relay, GPIO.LOW)
        GPIO.output(self.fan_relay, GPIO.LOW)

# Main program
thermostat = SmartThermostat()

while True:
    thermostat.control_climate()
    time.sleep(30)  # Check every 30 seconds
```

**Voice-Controlled LED System:**
```python
import speech_recognition as sr
import neopixel
import board

class VoiceLights:
    def __init__(self):
        self.strip = neopixel.NeoPixel(board.D18, 60, brightness=0.8)
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Color dictionary for voice commands
        self.colors = {
            'red': (255, 0, 0),
            'blue': (0, 0, 255),
            'green': (0, 255, 0),
            'purple': (128, 0, 128),
            'orange': (255, 165, 0),
            'rainbow': 'special'
        }
    
    def listen_for_command(self):
        """Listen for voice commands"""
        try:
            with self.microphone as source:
                print("🎤 Listening for color command...")
                audio = self.recognizer.listen(source, timeout=5)
            
            command = self.recognizer.recognize_google(audio).lower()
            print(f"Heard: {command}")
            return command
            
        except sr.UnknownValueError:
            print("Couldn't understand. Try again!")
            return None
        except sr.RequestError:
            print("Speech service error")
            return None
    
    def process_command(self, command):
        """Execute lighting commands"""
        if command is None:
            return
            
        if 'turn off' in command or 'lights off' in command:
            self.all_off()
        elif 'rainbow' in command:
            self.rainbow_effect()
        else:
            # Check for color commands
            for color_name, rgb in self.colors.items():
                if color_name in command:
                    if rgb != 'special':
                        self.set_all_color(rgb)
                    break
    
    def set_all_color(self, color):
        """Set all LEDs to one color"""
        self.strip.fill(color)
        self.strip.show()
        print(f"💡 Lights set to {color}")
    
    def rainbow_effect(self):
        """Beautiful rainbow animation"""
        print("🌈 Rainbow mode activated!")
        colors = [
            (255, 0, 0),    # Red
            (255, 127, 0),  # Orange
            (255, 255, 0),  # Yellow
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (75, 0, 130),   # Indigo
            (148, 0, 211)   # Violet
        ]
        
        for i in range(len(self.strip)):
            color_index = i % len(colors)
            self.strip[i] = colors[color_index]
        self.strip.show()
    
    def all_off(self):
        """Turn off all LEDs"""
        self.strip.fill((0, 0, 0))
        self.strip.show()
        print("💡 All lights off")

# Main program
lights = VoiceLights()

print("🎤 Voice-Controlled Smart Lights Ready!")
print("Try saying: 'Set lights to blue' or 'Rainbow mode' or 'Turn off lights'")

while True:
    command = lights.listen_for_command()
    lights.process_command(command)
```

### **🌱 Automated Garden System**
*Duration: 6 weeks | Difficulty: Intermediate+*

#### **What We Build**
A complete garden monitoring and care system that waters plants, monitors growth, and sends updates to your phone.

**🛠️ Hardware:**
- Soil moisture sensors
- Water pump and tubing system
- pH sensors for soil health
- Camera for growth time-lapse
- Solar panel for power
- WiFi module for remote monitoring

**🎯 Learning Goals:**
- Environmental sensors and data collection
- Automated control systems
- Data logging and analysis
- Sustainable technology concepts
- Mobile app development basics

#### **🌿 Garden Monitoring Code**
```python
import time
import sqlite3
import requests
from datetime import datetime
import RPi.GPIO as GPIO
from picamera import PiCamera

class SmartGarden:
    def __init__(self):
        self.pump_pin = 18
        self.moisture_sensor_pin = 21
        self.camera = PiCamera()
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pump_pin, GPIO.OUT)
        GPIO.setup(self.moisture_sensor_pin, GPIO.IN)
        
        # Database for storing garden data
        self.init_database()
        
        # Thresholds for plant care
        self.dry_threshold = 300
        self.ideal_moisture = 600
    
    def init_database(self):
        """Create database for garden data"""
        conn = sqlite3.connect('garden_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS readings (
                timestamp TEXT,
                moisture_level INTEGER,
                temperature REAL,
                humidity REAL,
                watered BOOLEAN
            )
        ''')
        conn.commit()
        conn.close()
    
    def read_soil_moisture(self):
        """Read moisture sensor (0-1023, lower = wetter)"""
        # Simplified reading - actual implementation varies by sensor
        import spidev
        spi = spidev.SpiDev()
        spi.open(0, 0)
        
        # Read from MCP3008 ADC
        raw = spi.xfer2([1, (8 + 0) << 4, 0])
        moisture = ((raw[1] & 3) << 8) + raw[2]
        
        spi.close()
        return moisture
    
    def water_plants(self, duration=5):
        """Activate water pump for specified seconds"""
        print(f"💧 Watering plants for {duration} seconds...")
        GPIO.output(self.pump_pin, GPIO.HIGH)
        time.sleep(duration)
        GPIO.output(self.pump_pin, GPIO.LOW)
        print("✅ Watering complete!")
    
    def take_growth_photo(self):
        """Capture daily growth photo"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"growth_photos/plant_{timestamp}.jpg"
        
        self.camera.start_preview()
        time.sleep(2)  # Camera warm-up
        self.camera.capture(filename)
        self.camera.stop_preview()
        
        print(f"📸 Growth photo saved: {filename}")
        return filename
    
    def send_phone_notification(self, message):
        """Send update to your phone via webhook"""
        webhook_url = "YOUR_PHONE_WEBHOOK_URL"
        data = {
            "text": message,
            "timestamp": datetime.now().isoformat()
        }
        
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 200:
                print("📱 Phone notification sent!")
        except Exception as e:
            print(f"Failed to send notification: {e}")
    
    def log_data(self, moisture, temp, humidity, watered):
        """Save sensor data to database"""
        conn = sqlite3.connect('garden_data.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO readings 
            (timestamp, moisture_level, temperature, humidity, watered)
            VALUES (?, ?, ?, ?, ?)
        ''', (datetime.now().isoformat(), moisture, temp, humidity, watered))
        conn.commit()
        conn.close()
    
    def garden_care_cycle(self):
        """Main garden monitoring and care logic"""
        moisture = self.read_soil_moisture()
        
        # For demo - normally you'd read real temp/humidity sensors
        temperature = 25.0
        humidity = 60.0
        
        watered = False
        
        print(f"🌱 Soil moisture: {moisture}")
        
        if moisture < self.dry_threshold:
            self.water_plants()
            watered = True
            self.send_phone_notification(
                f"🌱 Plants watered! Moisture was {moisture}, now improving."
            )
        elif moisture > self.ideal_moisture:
            print("💧 Soil is perfectly moist!")
        
        # Log all data
        self.log_data(moisture, temperature, humidity, watered)
        
        # Take daily growth photo at noon
        current_hour = datetime.now().hour
        if current_hour == 12:  # 12 PM
            photo_file = self.take_growth_photo()
            self.send_phone_notification(
                f"📸 Daily growth photo taken: {photo_file}"
            )

# Main program
garden = SmartGarden()

print("🌱 Smart Garden System Started!")
print("Monitoring soil moisture every 30 minutes...")

while True:
    try:
        garden.garden_care_cycle()
        time.sleep(1800)  # Check every 30 minutes
    except KeyboardInterrupt:
        print("\n🛑 Garden system stopped by user")
        GPIO.cleanup()
        break
```

---

## ⚡ Ages 13-15: Connected World Projects

### **🚗 Smart Transportation System**
*Duration: 8 weeks | Difficulty: Advanced*

#### **What We Build**
A miniature smart city with autonomous vehicles, traffic management, and mobile app control using computer vision and IoT sensors.

**🛠️ Hardware:**
- Raspberry Pi vehicles with cameras
- Arduino traffic light controllers
- Ultrasonic sensors for collision detection
- WiFi mesh network for vehicle communication
- Mobile app interface
- 3D-printed city infrastructure

**🎯 Learning Goals:**
- Computer vision and AI
- Network protocols and communication
- Real-time systems programming
- Database design and APIs
- Mobile app development
- System integration and testing

#### **🚦 Traffic Management System**
```javascript
// Smart Traffic Controller - Web-based interface
class SmartTrafficSystem {
    constructor() {
        this.intersections = new Map();
        this.vehicles = new Map();
        this.trafficFlow = {
            northSouth: 0,
            eastWest: 0
        };
        
        // WebSocket for real-time communication
        this.socket = new WebSocket('ws://localhost:8080');
        this.initializeWebSocket();
    }
    
    initializeWebSocket() {
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            this.handleSensorData(data);
        };
    }
    
    handleSensorData(data) {
        switch(data.type) {
            case 'vehicle_detected':
                this.updateVehicleCount(data.intersection, data.direction);
                break;
            case 'traffic_density':
                this.optimizeTrafficFlow(data);
                break;
            case 'emergency_vehicle':
                this.handleEmergencyOverride(data);
                break;
        }
    }
    
    updateVehicleCount(intersection, direction) {
        console.log(`🚗 Vehicle detected at ${intersection}, going ${direction}`);
        
        // Update traffic flow data
        this.trafficFlow[direction]++;
        
        // Analyze if light timing needs adjustment
        this.analyzeTrafficPattern(intersection);
    }
    
    analyzeTrafficPattern(intersection) {
        const nsFlow = this.trafficFlow.northSouth;
        const ewFlow = this.trafficFlow.eastWest;
        
        if (nsFlow > ewFlow * 1.5) {
            // More north-south traffic, extend green time
            this.adjustLightTiming(intersection, 'northSouth', 45, 'eastWest', 15);
        } else if (ewFlow > nsFlow * 1.5) {
            // More east-west traffic
            this.adjustLightTiming(intersection, 'eastWest', 45, 'northSouth', 15);
        } else {
            // Balanced traffic, standard timing
            this.adjustLightTiming(intersection, 'northSouth', 30, 'eastWest', 30);
        }
    }
    
    adjustLightTiming(intersection, primary_dir, primary_time, secondary_dir, secondary_time) {
        const command = {
            type: 'adjust_timing',
            intersection: intersection,
            timing: {
                [primary_dir]: primary_time,
                [secondary_dir]: secondary_time
            }
        };
        
        // Send to Arduino traffic controllers
        this.socket.send(JSON.stringify(command));
        
        console.log(`🚦 Adjusted timing at ${intersection}:`);
        console.log(`   ${primary_dir}: ${primary_time}s`);
        console.log(`   ${secondary_dir}: ${secondary_time}s`);
    }
    
    handleEmergencyOverride(data) {
        console.log(`🚨 EMERGENCY: ${data.vehicleType} approaching ${data.intersection}`);
        
        // Override normal traffic flow
        const emergency_command = {
            type: 'emergency_override',
            intersection: data.intersection,
            direction: data.approach_direction,
            duration: 60  // seconds
        };
        
        this.socket.send(JSON.stringify(emergency_command));
        
        // Notify mobile app users
        this.notifyUsers({
            type: 'emergency_alert',
            message: `Emergency vehicle approaching ${data.intersection}. Traffic delayed.`,
            duration: 60
        });
    }
    
    generateTrafficReport() {
        return {
            timestamp: new Date().toISOString(),
            totalVehicles: this.trafficFlow.northSouth + this.trafficFlow.eastWest,
            peakDirection: this.trafficFlow.northSouth > this.trafficFlow.eastWest ? 'North-South' : 'East-West',
            efficiency: this.calculateEfficiency(),
            recommendations: this.getOptimizationSuggestions()
        };
    }
    
    calculateEfficiency() {
        // Simplified efficiency calculation
        const total = this.trafficFlow.northSouth + this.trafficFlow.eastWest;
        const balance = Math.abs(this.trafficFlow.northSouth - this.trafficFlow.eastWest);
        return Math.max(0, 100 - (balance / total * 100));
    }
}

// Initialize the smart traffic system
const trafficSystem = new SmartTrafficSystem();

// Demo: Simulate some traffic data
setInterval(() => {
    // Simulate random vehicle detection
    const intersections = ['Main_Oak', 'First_Pine', 'Second_Elm'];
    const directions = ['northSouth', 'eastWest'];
    
    const randomIntersection = intersections[Math.floor(Math.random() * intersections.length)];
    const randomDirection = directions[Math.floor(Math.random() * directions.length)];
    
    trafficSystem.handleSensorData({
        type: 'vehicle_detected',
        intersection: randomIntersection,
        direction: randomDirection
    });
}, 3000);  // New vehicle every 3 seconds
```

### **🏠 Neighborhood Security Network**
*Duration: 6 weeks | Difficulty: Advanced*

#### **What We Build**
A collaborative security system where neighbors can share camera feeds, motion alerts, and emergency notifications through a decentralized network.

**🛠️ Hardware:**
- Multiple Raspberry Pi security nodes
- Night vision cameras
- PIR motion sensors
- Audio detection modules
- Emergency notification buttons
- Mesh network communication

#### **🔒 Security Network Code**
```python
import cv2
import numpy as np
import json
import time
import threading
from datetime import datetime
import sqlite3
import hashlib

class NeighborhoodSecurityNode:
    def __init__(self, node_id, location):
        self.node_id = node_id
        self.location = location
        self.camera = cv2.VideoCapture(0)
        self.motion_detector = cv2.createBackgroundSubtractorMOG2()
        
        # Security settings
        self.is_armed = False
        self.motion_threshold = 1000
        self.last_motion_time = 0
        
        # Network for neighbor communication
        self.neighbor_nodes = []
        self.security_database = 'security_events.db'
        
        self.init_database()
        
    def init_database(self):
        """Initialize security events database"""
        conn = sqlite3.connect(self.security_database)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS security_events (
                event_id TEXT PRIMARY KEY,
                timestamp TEXT,
                node_id TEXT,
                event_type TEXT,
                description TEXT,
                image_path TEXT,
                severity INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    
    def detect_motion(self):
        """Computer vision motion detection"""
        ret, frame = self.camera.read()
        if not ret:
            return False, None
            
        # Apply motion detection algorithm
        motion_mask = self.motion_detector.apply(frame)
        
        # Find contours of moving objects
        contours, _ = cv2.findContours(
            motion_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        motion_detected = False
        motion_area = 0
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.motion_threshold:
                motion_detected = True
                motion_area += area
                
                # Draw rectangle around motion
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        return motion_detected, frame
    
    def capture_security_image(self, event_type):
        """Capture and save security event image"""
        ret, frame = self.camera.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"security_images/{self.node_id}_{timestamp}_{event_type}.jpg"
            cv2.imwrite(filename, frame)
            return filename
        return None
    
    def log_security_event(self, event_type, description, severity=1):
        """Log security event to database and notify neighbors"""
        event_id = hashlib.md5(
            f"{self.node_id}{datetime.now().isoformat()}{event_type}".encode()
        ).hexdigest()
        
        image_path = self.capture_security_image(event_type)
        
        # Save to local database
        conn = sqlite3.connect(self.security_database)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO security_events 
            (event_id, timestamp, node_id, event_type, description, image_path, severity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            event_id, 
            datetime.now().isoformat(),
            self.node_id,
            event_type,
            description,
            image_path,
            severity
        ))
        conn.commit()
        conn.close()
        
        # Notify neighbors
        self.broadcast_security_alert({
            'event_id': event_id,
            'node_id': self.node_id,
            'location': self.location,
            'event_type': event_type,
            'description': description,
            'timestamp': datetime.now().isoformat(),
            'severity': severity
        })
        
        print(f"🚨 Security Event Logged: {event_type} at {self.location}")
    
    def broadcast_security_alert(self, alert_data):
        """Send security alert to neighbor nodes"""
        for neighbor in self.neighbor_nodes:
            try:
                # In real implementation, this would use network protocols
                neighbor.receive_security_alert(alert_data)
            except Exception as e:
                print(f"Failed to notify neighbor {neighbor.node_id}: {e}")
    
    def receive_security_alert(self, alert_data):
        """Receive and process alerts from neighbor nodes"""
        print(f"📢 NEIGHBOR ALERT: {alert_data['event_type']} at {alert_data['location']}")
        
        # High severity events trigger additional actions
        if alert_data['severity'] >= 3:
            self.handle_high_priority_alert(alert_data)
    
    def handle_high_priority_alert(self, alert_data):
        """Handle high-priority security alerts"""
        print("🚨 HIGH PRIORITY ALERT - Taking additional security measures")
        
        # Automatically arm this node
        self.is_armed = True
        
        # Increase motion sensitivity
        self.motion_threshold = 500
        
        # Start continuous monitoring for 30 minutes
        threading.Thread(
            target=self.enhanced_monitoring, 
            args=(1800,)  # 30 minutes
        ).start()
    
    def enhanced_monitoring(self, duration):
        """Enhanced monitoring mode for high-alert situations"""
        start_time = time.time()
        
        while time.time() - start_time < duration:
            motion_detected, frame = self.detect_motion()
            
            if motion_detected and self.is_armed:
                self.log_security_event(
                    "enhanced_motion_detected",
                    f"Motion during high-alert period at {self.location}",
                    severity=2
                )
            
            time.sleep(1)  # Check every second during enhanced mode
        
        # Return to normal monitoring
        self.motion_threshold = 1000
        print("✅ Enhanced monitoring period ended")
    
    def start_monitoring(self):
        """Main security monitoring loop"""
        print(f"🏠 Security node {self.node_id} monitoring started at {self.location}")
        
        while True:
            try:
                if self.is_armed:
                    motion_detected, frame = self.detect_motion()
                    
                    if motion_detected:
                        current_time = time.time()
                        
                        # Avoid spam - only log if 30 seconds since last motion
                        if current_time - self.last_motion_time > 30:
                            self.log_security_event(
                                "motion_detected",
                                f"Unauthorized motion detected at {self.location}"
                            )
                            self.last_motion_time = current_time
                
                time.sleep(5)  # Check every 5 seconds
                
            except KeyboardInterrupt:
                print(f"\n🛑 Security monitoring stopped for node {self.node_id}")
                break
            except Exception as e:
                print(f"❌ Monitoring error: {e}")
                time.sleep(10)  # Wait before retrying

# Create neighborhood security network
def create_security_network():
    """Set up a network of security nodes"""
    
    # Create individual security nodes
    node1 = NeighborhoodSecurityNode("NODE_001", "123 Main St - Front Door")
    node2 = NeighborhoodSecurityNode("NODE_002", "125 Main St - Backyard")  
    node3 = NeighborhoodSecurityNode("NODE_003", "127 Main St - Driveway")
    
    # Connect neighbors for alert sharing
    node1.neighbor_nodes = [node2, node3]
    node2.neighbor_nodes = [node1, node3]
    node3.neighbor_nodes = [node1, node2]
    
    return [node1, node2, node3]

# Demo: Start security network
if __name__ == "__main__":
    security_nodes = create_security_network()
    
    # Start monitoring on all nodes (in real deployment, these would be separate devices)
    for node in security_nodes:
        node.is_armed = True
        threading.Thread(target=node.start_monitoring).start()
        time.sleep(1)  # Stagger startup
    
    print("🏘️ Neighborhood Security Network Active!")
    print("All nodes armed and monitoring...")
```

---

## 🚀 Ages 16-18: Professional IoT Systems

### **🏭 Industrial Monitoring Platform**
*Duration: 12 weeks | Difficulty: Professional*

#### **What We Build**
A complete industrial IoT system with sensor networks, predictive maintenance AI, real-time dashboards, and enterprise-grade security.

**🛠️ Hardware:**
- Industrial sensor arrays (temperature, vibration, pressure)
- Edge computing nodes (Raspberry Pi 4 + AI accelerators)
- LoRaWAN long-range communication
- Industrial PLCs for machine control
- Cloud infrastructure integration
- Professional monitoring dashboards

**🎯 Learning Goals:**
- Enterprise IoT architecture
- Machine learning for predictive maintenance
- Real-time data processing
- Industrial communication protocols
- Cloud deployment and scaling
- Cybersecurity for industrial systems

#### **🏭 Industrial Monitoring System**
```python
import asyncio
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
import tensorflow as tf
from sklearn.ensemble import IsolationForest
import paho.mqtt.client as mqtt
import logging

class IndustrialMonitoringSystem:
    def __init__(self, plant_id, mqtt_broker="localhost"):
        self.plant_id = plant_id
        self.mqtt_client = mqtt.Client()
        self.mqtt_broker = mqtt_broker
        
        # Machine learning models
        self.anomaly_detector = IsolationForest(contamination=0.1)
        self.predictive_model = None
        
        # Industrial thresholds
        self.thresholds = {
            'temperature': {'min': 0, 'max': 85, 'critical': 95},
            'vibration': {'min': 0, 'max': 5.0, 'critical': 8.0},
            'pressure': {'min': 10, 'max': 50, 'critical': 60},
            'flow_rate': {'min': 100, 'max': 1000, 'critical': 1200}
        }
        
        # Setup logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        self.init_database()
        self.setup_mqtt()
        
    def init_database(self):
        """Initialize industrial database schema"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        
        # Sensor readings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                machine_id TEXT,
                sensor_type TEXT,
                value REAL,
                status TEXT,
                plant_id TEXT
            )
        ''')
        
        # Maintenance predictions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS maintenance_predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                machine_id TEXT,
                predicted_failure_date TEXT,
                confidence REAL,
                recommendation TEXT
            )
        ''')
        
        # Alert history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alert_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                alert_type TEXT,
                machine_id TEXT,
                severity TEXT,
                message TEXT,
                resolved BOOLEAN
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def setup_mqtt(self):
        """Setup MQTT for industrial communication"""
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_message = self.on_mqtt_message
        
        try:
            self.mqtt_client.connect(self.mqtt_broker, 1883, 60)
            self.mqtt_client.loop_start()
        except Exception as e:
            self.logger.error(f"MQTT connection failed: {e}")
    
    def on_mqtt_connect(self, client, userdata, flags, rc):
        """MQTT connection callback"""
        if rc == 0:
            self.logger.info("Connected to MQTT broker")
            # Subscribe to all sensor topics
            client.subscribe(f"industrial/{self.plant_id}/+/+")
        else:
            self.logger.error(f"MQTT connection failed with code {rc}")
    
    def on_mqtt_message(self, client, userdata, msg):
        """Process incoming sensor data"""
        try:
            # Parse topic: industrial/plant_id/machine_id/sensor_type
            topic_parts = msg.topic.split('/')
            machine_id = topic_parts[2]
            sensor_type = topic_parts[3]
            
            # Parse sensor data
            data = json.loads(msg.payload.decode())
            sensor_value = data['value']
            timestamp = data.get('timestamp', datetime.now().isoformat())
            
            # Process the sensor reading
            self.process_sensor_reading(machine_id, sensor_type, sensor_value, timestamp)
            
        except Exception as e:
            self.logger.error(f"Error processing MQTT message: {e}")
    
    def process_sensor_reading(self, machine_id, sensor_type, value, timestamp):
        """Process and analyze individual sensor readings"""
        
        # Determine status based on thresholds
        status = self.evaluate_sensor_status(sensor_type, value)
        
        # Store reading in database
        self.store_sensor_reading(machine_id, sensor_type, value, status, timestamp)
        
        # Check for anomalies using ML
        is_anomaly = self.detect_anomaly(machine_id, sensor_type, value)
        
        # Generate alerts if necessary
        if status in ['WARNING', 'CRITICAL'] or is_anomaly:
            self.generate_alert(machine_id, sensor_type, value, status, is_anomaly)
        
        # Update predictive maintenance model
        self.update_predictive_model(machine_id, sensor_type, value, timestamp)
    
    def evaluate_sensor_status(self, sensor_type, value):
        """Evaluate sensor status based on thresholds"""
        if sensor_type not in self.thresholds:
            return 'UNKNOWN'
        
        thresholds = self.thresholds[sensor_type]
        
        if value >= thresholds['critical']:
            return 'CRITICAL'
        elif value >= thresholds['max'] or value <= thresholds['min']:
            return 'WARNING'
        else:
            return 'NORMAL'
    
    def detect_anomaly(self, machine_id, sensor_type, current_value):
        """Use machine learning to detect anomalies"""
        try:
            # Get recent historical data
            historical_data = self.get_historical_data(machine_id, sensor_type, hours=24)
            
            if len(historical_data) < 10:
                return False  # Not enough data for anomaly detection
            
            # Prepare data for anomaly detection
            values = np.array(historical_data + [current_value]).reshape(-1, 1)
            
            # Train anomaly detector on recent data
            self.anomaly_detector.fit(values[:-1])
            
            # Check if current value is anomalous
            prediction = self.anomaly_detector.predict([[current_value]])
            
            return prediction[0] == -1  # -1 indicates anomaly
            
        except Exception as e:
            self.logger.error(f"Anomaly detection error: {e}")
            return False
    
    def get_historical_data(self, machine_id, sensor_type, hours=24):
        """Get historical sensor data for analysis"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        
        # Get data from last N hours
        since_time = (datetime.now() - timedelta(hours=hours)).isoformat()
        
        cursor.execute('''
            SELECT value FROM sensor_readings 
            WHERE machine_id = ? AND sensor_type = ? AND timestamp > ?
            ORDER BY timestamp ASC
        ''', (machine_id, sensor_type, since_time))
        
        data = [row[0] for row in cursor.fetchall()]
        conn.close()
        return data
    
    def generate_alert(self, machine_id, sensor_type, value, status, is_anomaly):
        """Generate and distribute alerts"""
        severity = 'HIGH' if status == 'CRITICAL' else 'MEDIUM'
        if is_anomaly:
            severity = 'HIGH'
        
        alert_message = f"{sensor_type.title()} alert on {machine_id}: "
        alert_message += f"Value {value} is {status.lower()}"
        
        if is_anomaly:
            alert_message += " (ML Anomaly Detected)"
        
        # Store alert in database
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO alert_history 
            (timestamp, alert_type, machine_id, severity, message, resolved)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            datetime.now().isoformat(),
            sensor_type,
            machine_id,
            severity,
            alert_message,
            False
        ))
        conn.commit()
        conn.close()
        
        # Send alert via MQTT
        alert_topic = f"alerts/{self.plant_id}/{machine_id}"
        alert_payload = {
            'timestamp': datetime.now().isoformat(),
            'machine_id': machine_id,
            'sensor_type': sensor_type,
            'value': value,
            'severity': severity,
            'message': alert_message
        }
        
        self.mqtt_client.publish(alert_topic, json.dumps(alert_payload))
        
        self.logger.warning(f"ALERT: {alert_message}")
    
    def update_predictive_model(self, machine_id, sensor_type, value, timestamp):
        """Update predictive maintenance models"""
        # This is a simplified example - real predictive maintenance
        # would use more sophisticated ML models and feature engineering
        
        try:
            # Get comprehensive machine data for prediction
            machine_data = self.get_machine_health_data(machine_id)
            
            if len(machine_data) < 100:  # Need enough data for predictions
                return
            
            # Simple failure prediction based on trend analysis
            recent_readings = machine_data[-50:]  # Last 50 readings
            trend = np.polyfit(range(len(recent_readings)), recent_readings, 1)[0]
            
            # Predict failure if trend indicates degradation
            if trend > 0.1 and sensor_type in ['temperature', 'vibration']:
                days_to_failure = self.calculate_failure_timeline(trend, value)
                
                if days_to_failure < 30:  # Maintenance needed within 30 days
                    self.schedule_predictive_maintenance(machine_id, days_to_failure)
        
        except Exception as e:
            self.logger.error(f"Predictive model update error: {e}")
    
    def get_machine_health_data(self, machine_id):
        """Get comprehensive machine health data"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        
        # Get recent readings for all sensors on this machine
        since_time = (datetime.now() - timedelta(days=7)).isoformat()
        
        cursor.execute('''
            SELECT value FROM sensor_readings 
            WHERE machine_id = ? AND timestamp > ?
            ORDER BY timestamp ASC
        ''', (machine_id, since_time))
        
        data = [row[0] for row in cursor.fetchall()]
        conn.close()
        return data
    
    def calculate_failure_timeline(self, trend, current_value):
        """Calculate estimated days until failure"""
        # Simplified failure prediction model
        critical_threshold = 90  # Example critical temperature
        
        if trend <= 0:
            return float('inf')  # No degradation trend
        
        days_to_critical = (critical_threshold - current_value) / (trend * 24)  # Assuming hourly readings
        return max(1, int(days_to_critical))
    
    def schedule_predictive_maintenance(self, machine_id, days_to_failure):
        """Schedule predictive maintenance"""
        predicted_failure_date = (
            datetime.now() + timedelta(days=days_to_failure)
        ).isoformat()
        
        confidence = min(0.95, 0.7 + (30 - days_to_failure) / 100)  # Higher confidence for sooner failures
        
        recommendation = f"Schedule maintenance within {days_to_failure} days"
        if days_to_failure < 7:
            recommendation = "URGENT: Schedule immediate maintenance"
        
        # Store prediction
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO maintenance_predictions 
            (timestamp, machine_id, predicted_failure_date, confidence, recommendation)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            datetime.now().isoformat(),
            machine_id,
            predicted_failure_date,
            confidence,
            recommendation
        ))
        conn.commit()
        conn.close()
        
        # Send maintenance alert
        maintenance_alert = {
            'type': 'predictive_maintenance',
            'machine_id': machine_id,
            'predicted_failure_date': predicted_failure_date,
            'confidence': confidence,
            'recommendation': recommendation
        }
        
        self.mqtt_client.publish(
            f"maintenance/{self.plant_id}/{machine_id}",
            json.dumps(maintenance_alert)
        )
        
        self.logger.info(f"Predictive maintenance scheduled for {machine_id}: {recommendation}")
    
    def store_sensor_reading(self, machine_id, sensor_type, value, status, timestamp):
        """Store sensor reading in database"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO sensor_readings 
            (timestamp, machine_id, sensor_type, value, status, plant_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (timestamp, machine_id, sensor_type, value, status, self.plant_id))
        conn.commit()
        conn.close()
    
    def generate_dashboard_data(self):
        """Generate real-time dashboard data"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        
        # Get recent system overview
        cursor.execute('''
            SELECT machine_id, sensor_type, value, status, timestamp
            FROM sensor_readings 
            WHERE timestamp > datetime('now', '-1 hour')
            ORDER BY timestamp DESC
        ''')
        
        recent_data = cursor.fetchall()
        
        # Get active alerts
        cursor.execute('''
            SELECT alert_type, machine_id, severity, message, timestamp
            FROM alert_history 
            WHERE resolved = 0
            ORDER BY timestamp DESC
        ''')
        
        active_alerts = cursor.fetchall()
        
        # Get maintenance predictions
        cursor.execute('''
            SELECT machine_id, predicted_failure_date, confidence, recommendation
            FROM maintenance_predictions 
            WHERE predicted_failure_date > datetime('now')
            ORDER BY predicted_failure_date ASC
        ''')
        
        maintenance_predictions = cursor.fetchall()
        
        conn.close()
        
        dashboard_data = {
            'plant_id': self.plant_id,
            'timestamp': datetime.now().isoformat(),
            'recent_readings': recent_data,
            'active_alerts': active_alerts,
            'maintenance_schedule': maintenance_predictions,
            'system_health': self.calculate_system_health()
        }
        
        return dashboard_data
    
    def calculate_system_health(self):
        """Calculate overall system health score"""
        conn = sqlite3.connect('industrial_monitoring.db')
        cursor = conn.cursor()
        
        # Count recent alerts by severity
        cursor.execute('''
            SELECT severity, COUNT(*) 
            FROM alert_history 
            WHERE timestamp > datetime('now', '-24 hours') AND resolved = 0
            GROUP BY severity
        ''')
        
        alert_counts = dict(cursor.fetchall())
        
        # Calculate health score (0-100)
        base_score = 100
        base_score -= alert_counts.get('HIGH', 0) * 20
        base_score -= alert_counts.get('MEDIUM', 0) * 10
        base_score -= alert_counts.get('LOW', 0) * 5
        
        conn.close()
        
        return max(0, min(100, base_score))

# Demo: Start industrial monitoring system
async def main():
    """Main application entry point"""
    
    # Create monitoring system for plant
    plant_monitor = IndustrialMonitoringSystem("PLANT_001")
    
    print("🏭 Industrial Monitoring System Started")
    print("Monitoring all machines and sensors...")
    
    # Simulate some sensor data for demo
    import random
    
    machines = ["PUMP_001", "COMPRESSOR_002", "TURBINE_003"]
    sensors = ["temperature", "vibration", "pressure", "flow_rate"]
    
    while True:
        try:
            # Simulate sensor readings
            for machine in machines:
                for sensor in sensors:
                    # Generate realistic sensor values
                    if sensor == "temperature":
                        value = random.uniform(40, 90)
                    elif sensor == "vibration":
                        value = random.uniform(1.0, 6.0)
                    elif sensor == "pressure":
                        value = random.uniform(20, 55)
                    else:  # flow_rate
                        value = random.uniform(300, 900)
                    
                    # Occasionally simulate problematic readings
                    if random.random() < 0.05:  # 5% chance of high reading
                        value *= 1.5
                    
                    plant_monitor.process_sensor_reading(
                        machine, sensor, value, datetime.now().isoformat()
                    )
            
            # Generate dashboard update every minute
            dashboard_data = plant_monitor.generate_dashboard_data()
            print(f"📊 System Health: {dashboard_data['system_health']}%")
            
            await asyncio.sleep(10)  # Check every 10 seconds
            
        except KeyboardInterrupt:
            print("\n🛑 Industrial monitoring system stopped")
            break

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🎯 Implementation Guidelines

### **🏫 Classroom Integration**
- **Safety First**: All physical computing projects include safety protocols
- **Budget-Friendly**: Projects scalable from basic components to advanced setups  
- **Collaborative Learning**: Team-based hardware projects encourage peer teaching
- **Real-World Connections**: Industry partnerships for authentic project contexts

### **👨‍👩‍👧‍👦 Family Engagement**
- **Home Extension**: Take-home kits for continued learning
- **Parent Workshops**: Understanding the technology your children are building
- **Showcase Events**: Community demonstrations of student projects
- **Career Awareness**: Connect projects to technology careers and opportunities

### **🌍 Community Impact**
- **Local Partnerships**: Real problems solved with student-built technology
- **Environmental Focus**: Sustainable technology and green computing concepts
- **Accessibility**: Projects adapted for different physical abilities and resources
- **Global Connections**: Collaborate with students worldwide on shared challenges

---

*Physical computing transforms abstract programming into tangible, real-world experiences that demonstrate the power of code to control and interact with the physical environment. Students build confidence, creativity, and practical skills that prepare them for an increasingly connected world.*