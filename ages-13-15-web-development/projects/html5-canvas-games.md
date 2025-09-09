# 🎮 HTML5 Canvas Games - Interactive Web Game Development

## 🌟 Game-Based Web Development Learning

Transform web development education through interactive games that teach HTML5 Canvas, JavaScript animations, responsive design, and modern web APIs while creating engaging player experiences.

---

## 🎯 Project 1: Browser Breakout Game

### Game Concept
Classic brick-breaking game built entirely with HTML5 Canvas and JavaScript, featuring particle effects, power-ups, and responsive design.

<div style="display: flex; justify-content: space-between; margin: 20px 0;">

<div style="width: 45%; background: #e8f4fd; padding: 15px; border-radius: 10px;">
<strong>Ms. WebDev's Teaching Goals:</strong><br>
"This project teaches fundamental game programming concepts while mastering HTML5 Canvas API, collision detection algorithms, and smooth animations. You'll learn the same techniques used in professional web games and interactive data visualizations."
</div>

<div style="width: 45%; background: #fff3cd; padding: 15px; border-radius: 10px;">
<strong>Sam's Gaming Vision:</strong><br>
"Can I add power-ups that change the ball behavior? Maybe different brick types that take multiple hits? And can I make it work perfectly on both desktop and mobile?"
</div>

</div>

### Complete Implementation

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canvas Breakout Game</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            font-family: 'Arial', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
        }
        
        .game-container {
            text-align: center;
            background: rgba(0, 0, 0, 0.2);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        canvas {
            border: 3px solid #fff;
            border-radius: 10px;
            background: #000;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
            display: block;
            margin: 0 auto 20px;
        }
        
        .game-ui {
            display: flex;
            justify-content: space-between;
            max-width: 800px;
            margin: 0 auto;
            font-size: 18px;
            font-weight: bold;
        }
        
        .controls {
            margin-top: 15px;
            font-size: 14px;
            opacity: 0.8;
        }
        
        .power-up-display {
            margin-top: 10px;
            padding: 10px;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            min-height: 20px;
        }
        
        @media (max-width: 900px) {
            canvas {
                max-width: 90vw;
                height: auto;
            }
            
            .game-ui {
                flex-direction: column;
                gap: 10px;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🎮 Canvas Breakout Challenge</h1>
        <canvas id="gameCanvas" width="800" height="500"></canvas>
        
        <div class="game-ui">
            <div>Score: <span id="score">0</span></div>
            <div>Lives: <span id="lives">3</span></div>
            <div>Level: <span id="level">1</span></div>
        </div>
        
        <div class="power-up-display" id="powerUpDisplay">
            Ready to play! Use mouse or arrow keys to move paddle.
        </div>
        
        <div class="controls">
            🖱️ Mouse • ⬅️➡️ Arrow Keys • 📱 Touch (Mobile)
        </div>
    </div>

    <script>
        class BreakoutGame {
            constructor() {
                this.canvas = document.getElementById('gameCanvas');
                this.ctx = this.canvas.getContext('2d');
                
                // Game state
                this.gameState = 'playing'; // playing, paused, gameOver, levelComplete
                this.score = 0;
                this.lives = 3;
                this.level = 1;
                
                // Game objects
                this.paddle = {
                    x: this.canvas.width / 2 - 60,
                    y: this.canvas.height - 30,
                    width: 120,
                    height: 15,
                    speed: 8,
                    color: '#00ff88'
                };
                
                this.ball = {
                    x: this.canvas.width / 2,
                    y: this.canvas.height / 2,
                    radius: 8,
                    dx: 4,
                    dy: -4,
                    speed: 4,
                    color: '#ffff00',
                    trail: []
                };
                
                this.bricks = [];
                this.particles = [];
                this.powerUps = [];
                
                // Power-up states
                this.activePowerUps = {
                    multiBall: false,
                    widePaddle: false,
                    fastBall: false,
                    stickyPaddle: false
                };
                
                this.powerUpTimers = {};
                
                // Input handling
                this.keys = {};
                this.mouse = { x: 0, y: 0 };
                
                this.setupEventListeners();
                this.createBricks();
                this.gameLoop();
            }
            
            setupEventListeners() {
                // Keyboard events
                document.addEventListener('keydown', (e) => {
                    this.keys[e.key] = true;
                    if (e.key === ' ') e.preventDefault();
                });
                
                document.addEventListener('keyup', (e) => {
                    this.keys[e.key] = false;
                });
                
                // Mouse events
                this.canvas.addEventListener('mousemove', (e) => {
                    const rect = this.canvas.getBoundingClientRect();
                    this.mouse.x = (e.clientX - rect.left) * (this.canvas.width / rect.width);
                });
                
                // Touch events for mobile
                this.canvas.addEventListener('touchmove', (e) => {
                    e.preventDefault();
                    const rect = this.canvas.getBoundingClientRect();
                    const touch = e.touches[0];
                    this.mouse.x = (touch.clientX - rect.left) * (this.canvas.width / rect.width);
                });
                
                // Prevent context menu on right click
                this.canvas.addEventListener('contextmenu', (e) => e.preventDefault());
            }
            
            createBricks() {
                this.bricks = [];
                const rows = 5 + this.level;
                const cols = 10;
                const brickWidth = 70;
                const brickHeight = 20;
                const padding = 5;
                const offsetTop = 60;
                const offsetLeft = (this.canvas.width - (cols * (brickWidth + padding) - padding)) / 2;
                
                const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3'];
                
                for (let r = 0; r < rows; r++) {
                    for (let c = 0; c < cols; c++) {
                        const brick = {
                            x: offsetLeft + c * (brickWidth + padding),
                            y: offsetTop + r * (brickHeight + padding),
                            width: brickWidth,
                            height: brickHeight,
                            color: colors[r % colors.length],
                            hits: r < 2 ? 1 : 2, // Top 2 rows need 2 hits
                            maxHits: r < 2 ? 1 : 2,
                            points: r < 2 ? 10 : 20
                        };
                        this.bricks.push(brick);
                    }
                }
            }
            
            update() {
                if (this.gameState !== 'playing') return;
                
                this.updatePaddle();
                this.updateBall();
                this.updateParticles();
                this.updatePowerUps();
                this.checkCollisions();
                this.updatePowerUpTimers();
            }
            
            updatePaddle() {
                // Mouse control (primary)
                this.paddle.x = this.mouse.x - this.paddle.width / 2;
                
                // Keyboard control (secondary)
                if (this.keys['ArrowLeft'] || this.keys['a']) {
                    this.paddle.x -= this.paddle.speed;
                }
                if (this.keys['ArrowRight'] || this.keys['d']) {
                    this.paddle.x += this.paddle.speed;
                }
                
                // Keep paddle on screen
                this.paddle.x = Math.max(0, Math.min(this.canvas.width - this.paddle.width, this.paddle.x));
            }
            
            updateBall() {
                // Add to trail
                this.ball.trail.push({ x: this.ball.x, y: this.ball.y });
                if (this.ball.trail.length > 10) {
                    this.ball.trail.shift();
                }
                
                // Move ball
                this.ball.x += this.ball.dx;
                this.ball.y += this.ball.dy;
                
                // Wall collisions
                if (this.ball.x + this.ball.radius > this.canvas.width || this.ball.x - this.ball.radius < 0) {
                    this.ball.dx = -this.ball.dx;
                    this.createParticles(this.ball.x, this.ball.y, '#ffffff', 5);
                }
                
                if (this.ball.y - this.ball.radius < 0) {
                    this.ball.dy = -this.ball.dy;
                    this.createParticles(this.ball.x, this.ball.y, '#ffffff', 5);
                }
                
                // Ball goes out of bounds (bottom)
                if (this.ball.y > this.canvas.height) {
                    this.lives--;
                    this.updateUI();
                    
                    if (this.lives <= 0) {
                        this.gameState = 'gameOver';
                    } else {
                        this.resetBall();
                    }
                }
            }
            
            updateParticles() {
                for (let i = this.particles.length - 1; i >= 0; i--) {
                    const particle = this.particles[i];
                    particle.x += particle.vx;
                    particle.y += particle.vy;
                    particle.vy += 0.1; // gravity
                    particle.life -= 0.02;
                    particle.alpha = particle.life;
                    
                    if (particle.life <= 0) {
                        this.particles.splice(i, 1);
                    }
                }
            }
            
            updatePowerUps() {
                for (let i = this.powerUps.length - 1; i >= 0; i--) {
                    const powerUp = this.powerUps[i];
                    powerUp.y += powerUp.speed;
                    powerUp.rotation += 0.1;
                    
                    // Remove if off screen
                    if (powerUp.y > this.canvas.height) {
                        this.powerUps.splice(i, 1);
                    }
                    
                    // Check collision with paddle
                    if (this.isColliding(powerUp, this.paddle)) {
                        this.activatePowerUp(powerUp.type);
                        this.powerUps.splice(i, 1);
                        this.createParticles(powerUp.x, powerUp.y, powerUp.color, 15);
                    }
                }
            }
            
            checkCollisions() {
                // Ball-paddle collision
                if (this.isColliding(this.ball, this.paddle)) {
                    this.ball.dy = -Math.abs(this.ball.dy);
                    
                    // Add spin based on where ball hits paddle
                    const hitPos = (this.ball.x - this.paddle.x) / this.paddle.width;
                    this.ball.dx = (hitPos - 0.5) * 8;
                    
                    this.createParticles(this.ball.x, this.ball.y, this.paddle.color, 8);
                }
                
                // Ball-brick collisions
                for (let i = this.bricks.length - 1; i >= 0; i--) {
                    const brick = this.bricks[i];
                    
                    if (this.isColliding(this.ball, brick)) {
                        // Determine collision side for more realistic physics
                        const ballCenterX = this.ball.x;
                        const ballCenterY = this.ball.y;
                        const brickCenterX = brick.x + brick.width / 2;
                        const brickCenterY = brick.y + brick.height / 2;
                        
                        const dx = ballCenterX - brickCenterX;
                        const dy = ballCenterY - brickCenterY;
                        
                        if (Math.abs(dx / brick.width) > Math.abs(dy / brick.height)) {
                            this.ball.dx = -this.ball.dx;
                        } else {
                            this.ball.dy = -this.ball.dy;
                        }
                        
                        // Damage brick
                        brick.hits--;
                        this.score += 5;
                        
                        if (brick.hits <= 0) {
                            this.score += brick.points;
                            this.createParticles(brick.x + brick.width/2, brick.y + brick.height/2, brick.color, 12);
                            
                            // Chance to spawn power-up
                            if (Math.random() < 0.15) {
                                this.spawnPowerUp(brick.x + brick.width/2, brick.y + brick.height/2);
                            }
                            
                            this.bricks.splice(i, 1);
                        } else {
                            // Brick damaged but not destroyed - visual feedback
                            brick.color = this.darkenColor(brick.color);
                            this.createParticles(brick.x + brick.width/2, brick.y + brick.height/2, brick.color, 6);
                        }
                        
                        this.updateUI();
                        
                        // Check win condition
                        if (this.bricks.length === 0) {
                            this.level++;
                            this.gameState = 'levelComplete';
                            setTimeout(() => {
                                this.createBricks();
                                this.resetBall();
                                this.gameState = 'playing';
                            }, 2000);
                        }
                        
                        break; // Only process one collision per frame
                    }
                }
            }
            
            isColliding(circle, rect) {
                if (circle.radius) {
                    // Circle-rectangle collision
                    const distX = Math.abs(circle.x - rect.x - rect.width/2);
                    const distY = Math.abs(circle.y - rect.y - rect.height/2);
                    
                    if (distX > (rect.width/2 + circle.radius)) return false;
                    if (distY > (rect.height/2 + circle.radius)) return false;
                    
                    if (distX <= rect.width/2) return true;
                    if (distY <= rect.height/2) return true;
                    
                    const dx = distX - rect.width/2;
                    const dy = distY - rect.height/2;
                    return (dx*dx + dy*dy <= circle.radius*circle.radius);
                } else {
                    // Rectangle-rectangle collision
                    return circle.x < rect.x + rect.width &&
                           circle.x + circle.width > rect.x &&
                           circle.y < rect.y + rect.height &&
                           circle.y + circle.height > rect.y;
                }
            }
            
            spawnPowerUp(x, y) {
                const types = ['multiBall', 'widePaddle', 'fastBall', 'stickyPaddle'];
                const colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'];
                const type = types[Math.floor(Math.random() * types.length)];
                
                const powerUp = {
                    x: x - 15,
                    y: y - 15,
                    width: 30,
                    height: 30,
                    type: type,
                    color: colors[types.indexOf(type)],
                    speed: 2,
                    rotation: 0
                };
                
                this.powerUps.push(powerUp);
            }
            
            activatePowerUp(type) {
                const duration = 10000; // 10 seconds
                
                switch(type) {
                    case 'widePaddle':
                        if (!this.activePowerUps.widePaddle) {
                            this.paddle.width *= 1.5;
                            this.activePowerUps.widePaddle = true;
                            this.setPowerUpTimer('widePaddle', duration);
                        }
                        break;
                        
                    case 'fastBall':
                        if (!this.activePowerUps.fastBall) {
                            this.ball.dx *= 1.5;
                            this.ball.dy *= 1.5;
                            this.activePowerUps.fastBall = true;
                            this.setPowerUpTimer('fastBall', duration);
                        }
                        break;
                        
                    // Add more power-up types here
                }
                
                this.updatePowerUpDisplay();
            }
            
            setPowerUpTimer(type, duration) {
                if (this.powerUpTimers[type]) {
                    clearTimeout(this.powerUpTimers[type]);
                }
                
                this.powerUpTimers[type] = setTimeout(() => {
                    this.deactivatePowerUp(type);
                }, duration);
            }
            
            deactivatePowerUp(type) {
                switch(type) {
                    case 'widePaddle':
                        this.paddle.width = 120; // Reset to original
                        this.activePowerUps.widePaddle = false;
                        break;
                        
                    case 'fastBall':
                        this.ball.dx = Math.sign(this.ball.dx) * 4; // Reset to original speed
                        this.ball.dy = Math.sign(this.ball.dy) * 4;
                        this.activePowerUps.fastBall = false;
                        break;
                }
                
                this.updatePowerUpDisplay();
            }
            
            updatePowerUpTimers() {
                // Visual countdown for power-ups could be added here
            }
            
            createParticles(x, y, color, count) {
                for (let i = 0; i < count; i++) {
                    const particle = {
                        x: x,
                        y: y,
                        vx: (Math.random() - 0.5) * 6,
                        vy: (Math.random() - 0.5) * 6,
                        color: color,
                        life: 1,
                        alpha: 1,
                        size: Math.random() * 3 + 1
                    };
                    this.particles.push(particle);
                }
            }
            
            darkenColor(color) {
                // Simple color darkening function
                const hex = color.replace('#', '');
                const r = Math.max(0, parseInt(hex.substr(0, 2), 16) - 40);
                const g = Math.max(0, parseInt(hex.substr(2, 2), 16) - 40);
                const b = Math.max(0, parseInt(hex.substr(4, 2), 16) - 40);
                return `rgb(${r}, ${g}, ${b})`;
            }
            
            resetBall() {
                this.ball.x = this.canvas.width / 2;
                this.ball.y = this.canvas.height / 2;
                this.ball.dx = (Math.random() > 0.5 ? 1 : -1) * 4;
                this.ball.dy = -4;
                this.ball.trail = [];
            }
            
            draw() {
                // Clear canvas with gradient
                const gradient = this.ctx.createLinearGradient(0, 0, 0, this.canvas.height);
                gradient.addColorStop(0, '#1a1a2e');
                gradient.addColorStop(1, '#16213e');
                this.ctx.fillStyle = gradient;
                this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                
                this.drawBall();
                this.drawPaddle();
                this.drawBricks();
                this.drawParticles();
                this.drawPowerUps();
                this.drawUI();
            }
            
            drawBall() {
                // Draw ball trail
                this.ctx.save();
                for (let i = 0; i < this.ball.trail.length; i++) {
                    const pos = this.ball.trail[i];
                    const alpha = i / this.ball.trail.length * 0.5;
                    this.ctx.globalAlpha = alpha;
                    this.ctx.fillStyle = this.ball.color;
                    this.ctx.beginPath();
                    this.ctx.arc(pos.x, pos.y, this.ball.radius * alpha, 0, Math.PI * 2);
                    this.ctx.fill();
                }
                this.ctx.restore();
                
                // Draw main ball with glow effect
                this.ctx.save();
                this.ctx.shadowColor = this.ball.color;
                this.ctx.shadowBlur = 20;
                this.ctx.fillStyle = this.ball.color;
                this.ctx.beginPath();
                this.ctx.arc(this.ball.x, this.ball.y, this.ball.radius, 0, Math.PI * 2);
                this.ctx.fill();
                this.ctx.restore();
            }
            
            drawPaddle() {
                // Draw paddle with gradient and glow
                this.ctx.save();
                this.ctx.shadowColor = this.paddle.color;
                this.ctx.shadowBlur = 15;
                
                const gradient = this.ctx.createLinearGradient(0, this.paddle.y, 0, this.paddle.y + this.paddle.height);
                gradient.addColorStop(0, this.paddle.color);
                gradient.addColorStop(1, this.darkenColor(this.paddle.color));
                
                this.ctx.fillStyle = gradient;
                this.ctx.fillRect(this.paddle.x, this.paddle.y, this.paddle.width, this.paddle.height);
                this.ctx.restore();
            }
            
            drawBricks() {
                for (const brick of this.bricks) {
                    this.ctx.save();
                    
                    // Brick shadow/glow
                    this.ctx.shadowColor = brick.color;
                    this.ctx.shadowBlur = 5;
                    
                    // Brick gradient based on health
                    const gradient = this.ctx.createLinearGradient(0, brick.y, 0, brick.y + brick.height);
                    gradient.addColorStop(0, brick.color);
                    gradient.addColorStop(1, this.darkenColor(brick.color));
                    
                    this.ctx.fillStyle = gradient;
                    this.ctx.fillRect(brick.x, brick.y, brick.width, brick.height);
                    
                    // Health indicator
                    if (brick.hits < brick.maxHits) {
                        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
                        this.ctx.fillRect(brick.x + 2, brick.y + 2, brick.width - 4, brick.height - 4);
                    }
                    
                    this.ctx.restore();
                }
            }
            
            drawParticles() {
                for (const particle of this.particles) {
                    this.ctx.save();
                    this.ctx.globalAlpha = particle.alpha;
                    this.ctx.fillStyle = particle.color;
                    this.ctx.beginPath();
                    this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                    this.ctx.fill();
                    this.ctx.restore();
                }
            }
            
            drawPowerUps() {
                for (const powerUp of this.powerUps) {
                    this.ctx.save();
                    this.ctx.translate(powerUp.x + powerUp.width/2, powerUp.y + powerUp.height/2);
                    this.ctx.rotate(powerUp.rotation);
                    
                    // Glow effect
                    this.ctx.shadowColor = powerUp.color;
                    this.ctx.shadowBlur = 10;
                    
                    this.ctx.fillStyle = powerUp.color;
                    this.ctx.fillRect(-powerUp.width/2, -powerUp.height/2, powerUp.width, powerUp.height);
                    
                    // Power-up icon (simplified)
                    this.ctx.fillStyle = 'white';
                    this.ctx.font = '16px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.fillText(powerUp.type[0].toUpperCase(), 0, 5);
                    
                    this.ctx.restore();
                }
            }
            
            drawUI() {
                if (this.gameState === 'levelComplete') {
                    this.ctx.save();
                    this.ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                    
                    this.ctx.fillStyle = '#00ff88';
                    this.ctx.font = 'bold 48px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.fillText('Level Complete!', this.canvas.width/2, this.canvas.height/2);
                    
                    this.ctx.fillStyle = 'white';
                    this.ctx.font = '24px Arial';
                    this.ctx.fillText(`Get ready for Level ${this.level}`, this.canvas.width/2, this.canvas.height/2 + 60);
                    this.ctx.restore();
                }
                
                if (this.gameState === 'gameOver') {
                    this.ctx.save();
                    this.ctx.fillStyle = 'rgba(0, 0, 0, 0.8)';
                    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                    
                    this.ctx.fillStyle = '#ff6b6b';
                    this.ctx.font = 'bold 48px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.fillText('Game Over', this.canvas.width/2, this.canvas.height/2);
                    
                    this.ctx.fillStyle = 'white';
                    this.ctx.font = '24px Arial';
                    this.ctx.fillText(`Final Score: ${this.score}`, this.canvas.width/2, this.canvas.height/2 + 60);
                    this.ctx.fillText('Refresh to play again', this.canvas.width/2, this.canvas.height/2 + 100);
                    this.ctx.restore();
                }
            }
            
            updateUI() {
                document.getElementById('score').textContent = this.score;
                document.getElementById('lives').textContent = this.lives;
                document.getElementById('level').textContent = this.level;
            }
            
            updatePowerUpDisplay() {
                const display = document.getElementById('powerUpDisplay');
                const active = Object.keys(this.activePowerUps).filter(key => this.activePowerUps[key]);
                
                if (active.length > 0) {
                    display.textContent = `Active Power-ups: ${active.join(', ')}`;
                    display.style.background = 'rgba(0, 255, 136, 0.2)';
                } else {
                    display.textContent = 'No active power-ups';
                    display.style.background = 'rgba(255, 255, 255, 0.1)';
                }
            }
            
            gameLoop() {
                this.update();
                this.draw();
                requestAnimationFrame(() => this.gameLoop());
            }
        }
        
        // Start the game
        window.addEventListener('load', () => {
            new BreakoutGame();
        });
    </script>
</body>
</html>
```

---

## 🏃‍♂️ Project 2: Endless Runner with Parallax Scrolling

### Advanced Web Game Techniques

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parallax Runner Game</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: #87CEEB;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: Arial, sans-serif;
        }
        
        .game-wrapper {
            text-align: center;
        }
        
        canvas {
            border: 2px solid #333;
            background: linear-gradient(to bottom, #87CEEB 0%, #98FB98 100%);
            display: block;
            margin: 0 auto;
        }
        
        .game-controls {
            margin-top: 20px;
            display: flex;
            justify-content: space-between;
            max-width: 800px;
            font-size: 18px;
            font-weight: bold;
        }
        
        @media (max-width: 850px) {
            canvas {
                max-width: 95vw;
                height: auto;
            }
        }
    </style>
</head>
<body>
    <div class="game-wrapper">
        <h1>🏃‍♂️ Parallax Adventure Runner</h1>
        <canvas id="gameCanvas" width="800" height="400"></canvas>
        
        <div class="game-controls">
            <div>Score: <span id="score">0</span></div>
            <div>Distance: <span id="distance">0</span>m</div>
            <div>Speed: <span id="speed">1</span>x</div>
        </div>
        
        <p>Press SPACE or click to jump • Avoid obstacles • Collect coins</p>
    </div>

    <script>
        class ParallaxRunner {
            constructor() {
                this.canvas = document.getElementById('gameCanvas');
                this.ctx = this.canvas.getContext('2d');
                
                // Game state
                this.gameState = 'playing';
                this.score = 0;
                this.distance = 0;
                this.gameSpeed = 2;
                this.maxSpeed = 8;
                
                // Player object
                this.player = {
                    x: 100,
                    y: this.canvas.height - 100,
                    width: 40,
                    height: 60,
                    dy: 0,
                    jumpPower: -12,
                    gravity: 0.5,
                    grounded: true,
                    color: '#4169E1',
                    // Animation properties
                    frameX: 0,
                    frameY: 0,
                    animationSpeed: 0.15,
                    animationCounter: 0
                };
                
                // Game objects arrays
                this.obstacles = [];
                this.coins = [];
                this.particles = [];
                this.clouds = [];
                
                // Parallax background layers
                this.backgroundLayers = [
                    { objects: [], speed: 0.2, color: '#32CD32', height: 30 }, // Far hills
                    { objects: [], speed: 0.4, color: '#228B22', height: 50 }, // Mid hills  
                    { objects: [], speed: 0.6, color: '#006400', height: 80 }, // Near hills
                    { objects: [], speed: 1.0, color: '#8B4513', height: 10 }  // Ground details
                ];
                
                // Initialize background elements
                this.initializeBackground();
                
                // Input handling
                this.setupControls();
                
                // Start game loop
                this.gameLoop();
                
                // Spawn objects periodically
                this.spawnTimer = 0;
                this.lastObstacle = 0;
            }
            
            initializeBackground() {
                // Create clouds
                for (let i = 0; i < 5; i++) {
                    this.clouds.push({
                        x: Math.random() * this.canvas.width * 2,
                        y: Math.random() * 100 + 20,
                        size: Math.random() * 30 + 20,
                        speed: Math.random() * 0.5 + 0.2
                    });
                }
                
                // Initialize parallax layers
                this.backgroundLayers.forEach((layer, index) => {
                    for (let i = 0; i < 10; i++) {
                        layer.objects.push({
                            x: i * 100 + Math.random() * 50,
                            y: this.canvas.height - layer.height - Math.random() * 20,
                            width: Math.random() * 60 + 40,
                            height: layer.height + Math.random() * 20
                        });
                    }
                });
            }
            
            setupControls() {
                // Keyboard controls
                document.addEventListener('keydown', (e) => {
                    if (e.code === 'Space' && this.player.grounded) {
                        this.jump();
                        e.preventDefault();
                    }
                });
                
                // Mouse/touch controls
                this.canvas.addEventListener('click', () => {
                    if (this.player.grounded) {
                        this.jump();
                    }
                });
                
                this.canvas.addEventListener('touchstart', (e) => {
                    e.preventDefault();
                    if (this.player.grounded) {
                        this.jump();
                    }
                });
            }
            
            jump() {
                if (this.player.grounded) {
                    this.player.dy = this.player.jumpPower;
                    this.player.grounded = false;
                    this.createJumpParticles();
                }
            }
            
            update() {
                if (this.gameState !== 'playing') return;
                
                // Increase game speed over time
                this.gameSpeed = Math.min(this.maxSpeed, 2 + this.distance / 500);
                
                // Update distance and score
                this.distance += this.gameSpeed * 0.1;
                this.score += Math.floor(this.gameSpeed * 0.1);
                
                this.updatePlayer();
                this.updateObstacles();
                this.updateCoins();
                this.updateParticles();
                this.updateBackground();
                this.spawnObjects();
                this.checkCollisions();
                this.updateUI();
            }
            
            updatePlayer() {
                // Apply gravity
                if (!this.player.grounded) {
                    this.player.dy += this.player.gravity;
                    this.player.y += this.player.dy;
                }
                
                // Ground collision
                const groundY = this.canvas.height - 40; // Ground level
                if (this.player.y + this.player.height >= groundY) {
                    this.player.y = groundY - this.player.height;
                    this.player.dy = 0;
                    this.player.grounded = true;
                }
                
                // Running animation when grounded
                if (this.player.grounded) {
                    this.player.animationCounter += this.player.animationSpeed;
                    if (this.player.animationCounter >= 1) {
                        this.player.animationCounter = 0;
                        this.player.frameX = (this.player.frameX + 1) % 4; // 4 frame running cycle
                    }
                }
            }
            
            updateObstacles() {
                for (let i = this.obstacles.length - 1; i >= 0; i--) {
                    const obstacle = this.obstacles[i];
                    obstacle.x -= this.gameSpeed;
                    
                    // Remove obstacles that are off screen
                    if (obstacle.x + obstacle.width < 0) {
                        this.obstacles.splice(i, 1);
                    }
                }
            }
            
            updateCoins() {
                for (let i = this.coins.length - 1; i >= 0; i--) {
                    const coin = this.coins[i];
                    coin.x -= this.gameSpeed;
                    coin.rotation += 0.1;
                    coin.bob += 0.1;
                    coin.y = coin.baseY + Math.sin(coin.bob) * 5; // Bobbing animation
                    
                    // Remove coins that are off screen
                    if (coin.x + coin.size < 0) {
                        this.coins.splice(i, 1);
                    }
                }
            }
            
            updateParticles() {
                for (let i = this.particles.length - 1; i >= 0; i--) {
                    const particle = this.particles[i];
                    particle.x += particle.vx;
                    particle.y += particle.vy;
                    particle.vy += 0.1; // gravity
                    particle.life -= 0.02;
                    
                    if (particle.life <= 0) {
                        this.particles.splice(i, 1);
                    }
                }
            }
            
            updateBackground() {
                // Update clouds
                this.clouds.forEach(cloud => {
                    cloud.x -= cloud.speed;
                    if (cloud.x + cloud.size < 0) {
                        cloud.x = this.canvas.width + cloud.size;
                        cloud.y = Math.random() * 100 + 20;
                    }
                });
                
                // Update parallax layers
                this.backgroundLayers.forEach(layer => {
                    layer.objects.forEach(obj => {
                        obj.x -= this.gameSpeed * layer.speed;
                        if (obj.x + obj.width < 0) {
                            obj.x = this.canvas.width + Math.random() * 100;
                        }
                    });
                });
            }
            
            spawnObjects() {
                this.spawnTimer += this.gameSpeed;
                
                // Spawn obstacles
                if (this.spawnTimer - this.lastObstacle > 100 + Math.random() * 100) {
                    this.spawnObstacle();
                    this.lastObstacle = this.spawnTimer;
                }
                
                // Spawn coins occasionally
                if (Math.random() < 0.005 * this.gameSpeed) {
                    this.spawnCoin();
                }
            }
            
            spawnObstacle() {
                const types = ['cactus', 'rock', 'log'];
                const type = types[Math.floor(Math.random() * types.length)];
                
                let obstacle = {
                    x: this.canvas.width,
                    y: this.canvas.height - 40,
                    type: type
                };
                
                switch(type) {
                    case 'cactus':
                        obstacle.width = 20;
                        obstacle.height = 60;
                        obstacle.color = '#228B22';
                        obstacle.y -= obstacle.height;
                        break;
                    case 'rock':
                        obstacle.width = 40;
                        obstacle.height = 30;
                        obstacle.color = '#696969';
                        obstacle.y -= obstacle.height;
                        break;
                    case 'log':
                        obstacle.width = 60;
                        obstacle.height = 20;
                        obstacle.color = '#8B4513';
                        obstacle.y -= obstacle.height;
                        break;
                }
                
                this.obstacles.push(obstacle);
            }
            
            spawnCoin() {
                const coin = {
                    x: this.canvas.width,
                    baseY: this.canvas.height - 60 - Math.random() * 100,
                    y: 0,
                    size: 20,
                    rotation: 0,
                    bob: 0,
                    color: '#FFD700',
                    collected: false
                };
                coin.y = coin.baseY;
                this.coins.push(coin);
            }
            
            checkCollisions() {
                // Check obstacle collisions
                this.obstacles.forEach(obstacle => {
                    if (this.isColliding(this.player, obstacle)) {
                        this.gameState = 'gameOver';
                        this.createCrashParticles();
                    }
                });
                
                // Check coin collection
                for (let i = this.coins.length - 1; i >= 0; i--) {
                    const coin = this.coins[i];
                    if (this.isColliding(this.player, coin)) {
                        this.score += 50;
                        this.createCoinParticles(coin.x, coin.y);
                        this.coins.splice(i, 1);
                    }
                }
            }
            
            isColliding(rect1, rect2) {
                return rect1.x < rect2.x + rect2.width &&
                       rect1.x + rect1.width > rect2.x &&
                       rect1.y < rect2.y + rect2.height &&
                       rect1.y + rect1.height > rect2.y;
            }
            
            createJumpParticles() {
                for (let i = 0; i < 8; i++) {
                    this.particles.push({
                        x: this.player.x + this.player.width / 2,
                        y: this.player.y + this.player.height,
                        vx: (Math.random() - 0.5) * 4,
                        vy: Math.random() * -2,
                        color: '#DEB887',
                        life: 1,
                        size: Math.random() * 3 + 1
                    });
                }
            }
            
            createCoinParticles(x, y) {
                for (let i = 0; i < 12; i++) {
                    this.particles.push({
                        x: x,
                        y: y,
                        vx: (Math.random() - 0.5) * 6,
                        vy: (Math.random() - 0.5) * 6,
                        color: '#FFD700',
                        life: 1,
                        size: Math.random() * 4 + 2
                    });
                }
            }
            
            createCrashParticles() {
                for (let i = 0; i < 20; i++) {
                    this.particles.push({
                        x: this.player.x + this.player.width / 2,
                        y: this.player.y + this.player.height / 2,
                        vx: (Math.random() - 0.5) * 8,
                        vy: (Math.random() - 0.5) * 8,
                        color: Math.random() > 0.5 ? '#FF4500' : '#FF6347',
                        life: 1,
                        size: Math.random() * 5 + 2
                    });
                }
            }
            
            draw() {
                // Clear canvas
                this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
                
                // Draw sky gradient
                const skyGradient = this.ctx.createLinearGradient(0, 0, 0, this.canvas.height / 2);
                skyGradient.addColorStop(0, '#87CEEB');
                skyGradient.addColorStop(1, '#B0E0E6');
                this.ctx.fillStyle = skyGradient;
                this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height / 2);
                
                this.drawClouds();
                this.drawParallaxBackground();
                this.drawGround();
                this.drawPlayer();
                this.drawObstacles();
                this.drawCoins();
                this.drawParticles();
                this.drawGameStateOverlay();
            }
            
            drawClouds() {
                this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                this.clouds.forEach(cloud => {
                    this.ctx.beginPath();
                    this.ctx.arc(cloud.x, cloud.y, cloud.size, 0, Math.PI * 2);
                    this.ctx.arc(cloud.x + cloud.size * 0.7, cloud.y, cloud.size * 0.8, 0, Math.PI * 2);
                    this.ctx.arc(cloud.x - cloud.size * 0.7, cloud.y, cloud.size * 0.6, 0, Math.PI * 2);
                    this.ctx.fill();
                });
            }
            
            drawParallaxBackground() {
                this.backgroundLayers.forEach((layer, index) => {
                    this.ctx.fillStyle = layer.color;
                    layer.objects.forEach(obj => {
                        if (index < 3) {
                            // Hills - draw as rounded shapes
                            this.ctx.beginPath();
                            this.ctx.ellipse(obj.x + obj.width/2, obj.y + obj.height/2, 
                                           obj.width/2, obj.height/2, 0, 0, Math.PI * 2);
                            this.ctx.fill();
                        } else {
                            // Ground details - draw as rectangles
                            this.ctx.fillRect(obj.x, obj.y, obj.width, obj.height);
                        }
                    });
                });
            }
            
            drawGround() {
                // Main ground
                this.ctx.fillStyle = '#8FBC8F';
                this.ctx.fillRect(0, this.canvas.height - 40, this.canvas.width, 40);
                
                // Ground texture lines
                this.ctx.strokeStyle = '#7AB17A';
                this.ctx.lineWidth = 2;
                for (let i = 0; i < this.canvas.width; i += 20) {
                    this.ctx.beginPath();
                    this.ctx.moveTo(i, this.canvas.height - 35);
                    this.ctx.lineTo(i + 10, this.canvas.height - 30);
                    this.ctx.stroke();
                }
            }
            
            drawPlayer() {
                this.ctx.save();
                
                // Player shadow
                this.ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
                this.ctx.ellipse(this.player.x + this.player.width/2, 
                               this.canvas.height - 35, 
                               this.player.width/2, 8, 0, 0, Math.PI * 2);
                this.ctx.fill();
                
                // Draw player with simple running animation
                this.ctx.fillStyle = this.player.color;
                
                if (this.player.grounded) {
                    // Running pose - alternate leg positions
                    const legOffset = this.player.frameX % 2 === 0 ? 5 : -5;
                    
                    // Body
                    this.ctx.fillRect(this.player.x + 10, this.player.y + 10, 20, 25);
                    
                    // Head
                    this.ctx.fillRect(this.player.x + 12, this.player.y, 16, 16);
                    
                    // Arms
                    this.ctx.fillRect(this.player.x + 5, this.player.y + 15, 8, 3);
                    this.ctx.fillRect(this.player.x + 27, this.player.y + 15, 8, 3);
                    
                    // Legs (animated)
                    this.ctx.fillRect(this.player.x + 12 + legOffset, this.player.y + 35, 6, 25);
                    this.ctx.fillRect(this.player.x + 22 - legOffset, this.player.y + 35, 6, 25);
                } else {
                    // Jumping pose
                    this.ctx.fillRect(this.player.x + 10, this.player.y + 10, 20, 25);
                    this.ctx.fillRect(this.player.x + 12, this.player.y, 16, 16);
                    
                    // Arms up
                    this.ctx.fillRect(this.player.x + 5, this.player.y + 12, 8, 3);
                    this.ctx.fillRect(this.player.x + 27, this.player.y + 12, 8, 3);
                    
                    // Legs together
                    this.ctx.fillRect(this.player.x + 15, this.player.y + 35, 10, 25);
                }
                
                this.ctx.restore();
            }
            
            drawObstacles() {
                this.obstacles.forEach(obstacle => {
                    this.ctx.fillStyle = obstacle.color;
                    
                    switch(obstacle.type) {
                        case 'cactus':
                            // Draw cactus
                            this.ctx.fillRect(obstacle.x + 6, obstacle.y, 8, obstacle.height);
                            // Cactus arms
                            this.ctx.fillRect(obstacle.x, obstacle.y + 15, 6, 3);
                            this.ctx.fillRect(obstacle.x + 14, obstacle.y + 20, 6, 3);
                            break;
                            
                        case 'rock':
                            // Draw rock as circle
                            this.ctx.beginPath();
                            this.ctx.ellipse(obstacle.x + obstacle.width/2, 
                                           obstacle.y + obstacle.height/2,
                                           obstacle.width/2, obstacle.height/2, 0, 0, Math.PI * 2);
                            this.ctx.fill();
                            break;
                            
                        case 'log':
                            // Draw log
                            this.ctx.fillRect(obstacle.x, obstacle.y, obstacle.width, obstacle.height);
                            // Log rings
                            this.ctx.strokeStyle = '#654321';
                            this.ctx.lineWidth = 2;
                            for (let i = 0; i < 3; i++) {
                                this.ctx.beginPath();
                                this.ctx.arc(obstacle.x + obstacle.width - 10, 
                                           obstacle.y + obstacle.height/2, 
                                           3 + i * 2, 0, Math.PI * 2);
                                this.ctx.stroke();
                            }
                            break;
                    }
                });
            }
            
            drawCoins() {
                this.coins.forEach(coin => {
                    this.ctx.save();
                    this.ctx.translate(coin.x + coin.size/2, coin.y + coin.size/2);
                    this.ctx.rotate(coin.rotation);
                    
                    // Coin glow
                    this.ctx.shadowColor = coin.color;
                    this.ctx.shadowBlur = 10;
                    
                    // Coin body
                    this.ctx.fillStyle = coin.color;
                    this.ctx.beginPath();
                    this.ctx.arc(0, 0, coin.size/2, 0, Math.PI * 2);
                    this.ctx.fill();
                    
                    // Coin inner circle
                    this.ctx.fillStyle = '#FFA500';
                    this.ctx.beginPath();
                    this.ctx.arc(0, 0, coin.size/3, 0, Math.PI * 2);
                    this.ctx.fill();
                    
                    this.ctx.restore();
                });
            }
            
            drawParticles() {
                this.particles.forEach(particle => {
                    this.ctx.save();
                    this.ctx.globalAlpha = particle.life;
                    this.ctx.fillStyle = particle.color;
                    this.ctx.beginPath();
                    this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
                    this.ctx.fill();
                    this.ctx.restore();
                });
            }
            
            drawGameStateOverlay() {
                if (this.gameState === 'gameOver') {
                    this.ctx.save();
                    this.ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
                    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                    
                    this.ctx.fillStyle = '#FF4500';
                    this.ctx.font = 'bold 48px Arial';
                    this.ctx.textAlign = 'center';
                    this.ctx.fillText('Game Over!', this.canvas.width/2, this.canvas.height/2 - 20);
                    
                    this.ctx.fillStyle = 'white';
                    this.ctx.font = '24px Arial';
                    this.ctx.fillText(`Final Score: ${this.score}`, this.canvas.width/2, this.canvas.height/2 + 30);
                    this.ctx.fillText(`Distance: ${Math.floor(this.distance)}m`, this.canvas.width/2, this.canvas.height/2 + 60);
                    this.ctx.fillText('Refresh to play again', this.canvas.width/2, this.canvas.height/2 + 90);
                    
                    this.ctx.restore();
                }
            }
            
            updateUI() {
                document.getElementById('score').textContent = this.score;
                document.getElementById('distance').textContent = Math.floor(this.distance);
                document.getElementById('speed').textContent = (this.gameSpeed / 2).toFixed(1);
            }
            
            gameLoop() {
                this.update();
                this.draw();
                requestAnimationFrame(() => this.gameLoop());
            }
        }
        
        // Initialize game when page loads
        window.addEventListener('load', () => {
            new ParallaxRunner();
        });
    </script>
</body>
</html>
```

---

## 🎯 Project 3: Tower Defense Strategy Game

### Complex Game Logic and AI

```javascript
class TowerDefenseGame {
    constructor() {
        this.canvas = document.getElementById('gameCanvas');
        this.ctx = this.canvas.getContext('2d');
        
        // Game state
        this.gameState = 'playing';
        this.wave = 1;
        this.lives = 20;
        this.money = 100;
        
        // Game grid
        this.gridSize = 40;
        this.cols = this.canvas.width / this.gridSize;
        this.rows = this.canvas.height / this.gridSize;
        
        // Path for enemies
        this.path = this.generatePath();
        
        // Game objects
        this.towers = [];
        this.enemies = [];
        this.projectiles = [];
        this.effects = [];
        
        // Tower types
        this.towerTypes = {
            basic: { cost: 20, damage: 15, range: 80, fireRate: 30, color: '#4169E1' },
            rapid: { cost: 35, damage: 8, range: 60, fireRate: 15, color: '#FF4500' },
            heavy: { cost: 60, damage: 40, range: 100, fireRate: 60, color: '#8B4513' },
            freeze: { cost: 50, damage: 5, range: 70, fireRate: 45, color: '#00CED1', special: 'freeze' }
        };
        
        // Enemy types
        this.enemyTypes = {
            basic: { health: 30, speed: 1, reward: 5, color: '#FF6B6B' },
            fast: { health: 20, speed: 2, reward: 8, color: '#4ECDC4' },
            tank: { health: 80, speed: 0.5, reward: 15, color: '#45B7D1' },
            flying: { health: 25, speed: 1.5, reward: 12, color: '#96CEB4', flying: true }
        };
        
        // UI state
        this.selectedTower = null;
        this.selectedTowerType = 'basic';
        this.mousePos = { x: 0, y: 0 };
        
        this.setupEventListeners();
        this.spawnWave();
        this.gameLoop();
    }
    
    generatePath() {
        // Create a simple S-shaped path
        const path = [];
        let currentX = 0;
        let currentY = Math.floor(this.rows / 2);
        
        // Move right
        for (let x = 0; x < this.cols / 3; x++) {
            path.push({ x: x, y: currentY });
        }
        
        // Curve down
        for (let y = currentY; y < this.rows - 2; y++) {
            path.push({ x: Math.floor(this.cols / 3), y: y });
        }
        
        // Move right
        for (let x = Math.floor(this.cols / 3); x < (this.cols * 2) / 3; x++) {
            path.push({ x: x, y: this.rows - 2 });
        }
        
        // Curve up
        for (let y = this.rows - 2; y > 1; y--) {
            path.push({ x: Math.floor((this.cols * 2) / 3), y: y });
        }
        
        // Move right to end
        for (let x = Math.floor((this.cols * 2) / 3); x < this.cols; x++) {
            path.push({ x: x, y: 1 });
        }
        
        return path;
    }
    
    setupEventListeners() {
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            this.mousePos.x = e.clientX - rect.left;
            this.mousePos.y = e.clientY - rect.top;
        });
        
        this.canvas.addEventListener('click', (e) => {
            this.handleClick(e);
        });
        
        // Tower selection buttons
        document.querySelectorAll('.tower-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                this.selectedTowerType = btn.dataset.type;
                this.selectedTower = null;
                this.updateUI();
            });
        });
    }
    
    handleClick(e) {
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const gridX = Math.floor(x / this.gridSize);
        const gridY = Math.floor(y / this.gridSize);
        
        // Check if clicking on existing tower
        const clickedTower = this.towers.find(tower => 
            tower.gridX === gridX && tower.gridY === gridY
        );
        
        if (clickedTower) {
            this.selectedTower = clickedTower;
            return;
        }
        
        // Try to place new tower
        if (this.canPlaceTower(gridX, gridY)) {
            this.placeTower(gridX, gridY, this.selectedTowerType);
        }
    }
    
    canPlaceTower(gridX, gridY) {
        // Check if position is valid
        if (gridX < 0 || gridX >= this.cols || gridY < 0 || gridY >= this.rows) {
            return false;
        }
        
        // Check if on path
        if (this.path.some(p => p.x === gridX && p.y === gridY)) {
            return false;
        }
        
        // Check if tower already exists
        if (this.towers.some(tower => tower.gridX === gridX && tower.gridY === gridY)) {
            return false;
        }
        
        // Check if player has enough money
        const towerType = this.towerTypes[this.selectedTowerType];
        return this.money >= towerType.cost;
    }
    
    placeTower(gridX, gridY, type) {
        const towerType = this.towerTypes[type];
        
        if (this.money >= towerType.cost) {
            const tower = {
                gridX: gridX,
                gridY: gridY,
                x: gridX * this.gridSize + this.gridSize / 2,
                y: gridY * this.gridSize + this.gridSize / 2,
                type: type,
                ...towerType,
                fireTimer: 0,
                target: null,
                level: 1,
                kills: 0
            };
            
            this.towers.push(tower);
            this.money -= towerType.cost;
            this.updateUI();
        }
    }
    
    spawnWave() {
        const enemiesInWave = 5 + this.wave * 2;
        let spawnDelay = 0;
        
        for (let i = 0; i < enemiesInWave; i++) {
            setTimeout(() => {
                const enemyType = this.selectEnemyType();
                this.spawnEnemy(enemyType);
            }, spawnDelay);
            
            spawnDelay += 1000; // 1 second between spawns
        }
        
        // Next wave after all enemies are spawned + extra time
        setTimeout(() => {
            if (this.enemies.length === 0) {
                this.wave++;
                this.money += 20; // Bonus money between waves
                this.spawnWave();
                this.updateUI();
            }
        }, spawnDelay + 5000);
    }
    
    selectEnemyType() {
        const types = ['basic', 'basic', 'fast', 'tank']; // Weighted selection
        if (this.wave > 3) types.push('flying');
        return types[Math.floor(Math.random() * types.length)];
    }
    
    spawnEnemy(type) {
        const enemyType = this.enemyTypes[type];
        const startPos = this.path[0];
        
        const enemy = {
            x: startPos.x * this.gridSize + this.gridSize / 2,
            y: startPos.y * this.gridSize + this.gridSize / 2,
            type: type,
            ...enemyType,
            maxHealth: enemyType.health,
            pathIndex: 0,
            effects: [] // For status effects like freeze
        };
        
        this.enemies.push(enemy);
    }
    
    update() {
        if (this.gameState !== 'playing') return;
        
        this.updateTowers();
        this.updateEnemies();
        this.updateProjectiles();
        this.updateEffects();
        
        // Check game over conditions
        if (this.lives <= 0) {
            this.gameState = 'gameOver';
        }
    }
    
    updateTowers() {
        this.towers.forEach(tower => {
            tower.fireTimer++;
            
            // Find target
            if (!tower.target || !this.isInRange(tower, tower.target) || tower.target.health <= 0) {
                tower.target = this.findNearestEnemy(tower);
            }
            
            // Fire at target
            if (tower.target && tower.fireTimer >= tower.fireRate) {
                this.fireTower(tower);
                tower.fireTimer = 0;
            }
        });
    }
    
    findNearestEnemy(tower) {
        let nearest = null;
        let nearestDistance = Infinity;
        
        this.enemies.forEach(enemy => {
            if (tower.type === 'flying' || !enemy.flying) { // Ground towers can't hit flying enemies
                const distance = this.getDistance(tower, enemy);
                if (distance <= tower.range && distance < nearestDistance) {
                    nearest = enemy;
                    nearestDistance = distance;
                }
            }
        });
        
        return nearest;
    }
    
    fireTower(tower) {
        const projectile = {
            x: tower.x,
            y: tower.y,
            targetX: tower.target.x,
            targetY: tower.target.y,
            target: tower.target,
            damage: tower.damage,
            speed: 5,
            special: tower.special,
            color: tower.color
        };
        
        this.projectiles.push(projectile);
    }
    
    updateEnemies() {
        for (let i = this.enemies.length - 1; i >= 0; i--) {
            const enemy = this.enemies[i];
            
            // Apply status effects
            this.updateEnemyEffects(enemy);
            
            // Move enemy along path
            if (enemy.pathIndex < this.path.length - 1) {
                const currentTarget = this.path[enemy.pathIndex + 1];
                const targetX = currentTarget.x * this.gridSize + this.gridSize / 2;
                const targetY = currentTarget.y * this.gridSize + this.gridSize / 2;
                
                const dx = targetX - enemy.x;
                const dy = targetY - enemy.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 5) {
                    enemy.pathIndex++;
                } else {
                    const effectiveSpeed = enemy.effects.includes('freeze') ? enemy.speed * 0.3 : enemy.speed;
                    enemy.x += (dx / distance) * effectiveSpeed;
                    enemy.y += (dy / distance) * effectiveSpeed;
                }
            } else {
                // Enemy reached the end
                this.lives--;
                this.enemies.splice(i, 1);
                this.updateUI();
                continue;
            }
            
            // Remove dead enemies
            if (enemy.health <= 0) {
                this.money += enemy.reward;
                this.createDeathEffect(enemy);
                this.enemies.splice(i, 1);
                this.updateUI();
            }
        }
    }
    
    updateEnemyEffects(enemy) {
        // Process status effects
        for (let j = enemy.effects.length - 1; j >= 0; j--) {
            const effect = enemy.effects[j];
            effect.duration--;
            
            if (effect.duration <= 0) {
                enemy.effects.splice(j, 1);
            }
        }
    }
    
    updateProjectiles() {
        for (let i = this.projectiles.length - 1; i >= 0; i--) {
            const projectile = this.projectiles[i];
            
            // Move projectile toward target
            const dx = projectile.targetX - projectile.x;
            const dy = projectile.targetY - projectile.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < projectile.speed) {
                // Hit target
                if (projectile.target.health > 0) {
                    projectile.target.health -= projectile.damage;
                    
                    // Apply special effects
                    if (projectile.special === 'freeze') {
                        projectile.target.effects.push({
                            type: 'freeze',
                            duration: 120 // 2 seconds at 60 FPS
                        });
                    }
                    
                    this.createHitEffect(projectile.target);
                }
                
                this.projectiles.splice(i, 1);
            } else {
                projectile.x += (dx / distance) * projectile.speed;
                projectile.y += (dy / distance) * projectile.speed;
            }
        }
    }
    
    updateEffects() {
        for (let i = this.effects.length - 1; i >= 0; i--) {
            const effect = this.effects[i];
            effect.life -= 0.02;
            effect.y -= 1;
            
            if (effect.life <= 0) {
                this.effects.splice(i, 1);
            }
        }
    }
    
    createHitEffect(enemy) {
        this.effects.push({
            x: enemy.x,
            y: enemy.y,
            type: 'hit',
            life: 1,
            color: '#FFFF00'
        });
    }
    
    createDeathEffect(enemy) {
        for (let i = 0; i < 8; i++) {
            this.effects.push({
                x: enemy.x + (Math.random() - 0.5) * 20,
                y: enemy.y + (Math.random() - 0.5) * 20,
                type: 'explosion',
                life: 1,
                color: enemy.color
            });
        }
    }
    
    getDistance(obj1, obj2) {
        const dx = obj1.x - obj2.x;
        const dy = obj1.y - obj2.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
    
    isInRange(tower, enemy) {
        return this.getDistance(tower, enemy) <= tower.range;
    }
    
    draw() {
        // Clear canvas
        this.ctx.fillStyle = '#90EE90';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.drawGrid();
        this.drawPath();
        this.drawTowers();
        this.drawEnemies();
        this.drawProjectiles();
        this.drawEffects();
        this.drawUI();
        this.drawPreview();
    }
    
    drawGrid() {
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        this.ctx.lineWidth = 1;
        
        // Vertical lines
        for (let x = 0; x <= this.canvas.width; x += this.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(x, 0);
            this.ctx.lineTo(x, this.canvas.height);
            this.ctx.stroke();
        }
        
        // Horizontal lines
        for (let y = 0; y <= this.canvas.height; y += this.gridSize) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y);
            this.ctx.lineTo(this.canvas.width, y);
            this.ctx.stroke();
        }
    }
    
    drawPath() {
        this.ctx.strokeStyle = '#8B4513';
        this.ctx.lineWidth = this.gridSize * 0.6;
        this.ctx.lineCap = 'round';
        this.ctx.lineJoin = 'round';
        
        this.ctx.beginPath();
        this.path.forEach((point, index) => {
            const x = point.x * this.gridSize + this.gridSize / 2;
            const y = point.y * this.gridSize + this.gridSize / 2;
            
            if (index === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        });
        this.ctx.stroke();
        
        // Draw path border
        this.ctx.strokeStyle = '#654321';
        this.ctx.lineWidth = this.gridSize * 0.4;
        this.ctx.beginPath();
        this.path.forEach((point, index) => {
            const x = point.x * this.gridSize + this.gridSize / 2;
            const y = point.y * this.gridSize + this.gridSize / 2;
            
            if (index === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        });
        this.ctx.stroke();
    }
    
    drawTowers() {
        this.towers.forEach(tower => {
            // Draw range if selected
            if (tower === this.selectedTower) {
                this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.arc(tower.x, tower.y, tower.range, 0, Math.PI * 2);
                this.ctx.stroke();
            }
            
            // Draw tower base
            this.ctx.fillStyle = '#696969';
            this.ctx.fillRect(tower.x - 15, tower.y - 15, 30, 30);
            
            // Draw tower
            this.ctx.fillStyle = tower.color;
            this.ctx.beginPath();
            this.ctx.arc(tower.x, tower.y, 12, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Draw barrel pointing at target
            if (tower.target) {
                const dx = tower.target.x - tower.x;
                const dy = tower.target.y - tower.y;
                const angle = Math.atan2(dy, dx);
                
                this.ctx.save();
                this.ctx.translate(tower.x, tower.y);
                this.ctx.rotate(angle);
                this.ctx.fillStyle = '#2F4F4F';
                this.ctx.fillRect(0, -3, 18, 6);
                this.ctx.restore();
            }
            
            // Draw upgrade indicator
            if (tower.kills > 5) {
                this.ctx.fillStyle = '#FFD700';
                this.ctx.beginPath();
                this.ctx.arc(tower.x + 10, tower.y - 10, 4, 0, Math.PI * 2);
                this.ctx.fill();
            }
        });
    }
    
    drawEnemies() {
        this.enemies.forEach(enemy => {
            // Draw enemy shadow
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.3)';
            this.ctx.beginPath();
            this.ctx.arc(enemy.x, enemy.y + (enemy.flying ? 5 : 2), 8, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Draw enemy
            this.ctx.fillStyle = enemy.color;
            if (enemy.effects.some(e => e.type === 'freeze')) {
                this.ctx.fillStyle = '#87CEEB'; // Frozen color
            }
            
            const enemyY = enemy.flying ? enemy.y - 5 : enemy.y;
            
            if (enemy.type === 'tank') {
                // Draw tank as rectangle
                this.ctx.fillRect(enemy.x - 12, enemyY - 8, 24, 16);
            } else if (enemy.flying) {
                // Draw flying enemy as diamond
                this.ctx.save();
                this.ctx.translate(enemy.x, enemyY);
                this.ctx.rotate(Math.PI / 4);
                this.ctx.fillRect(-8, -8, 16, 16);
                this.ctx.restore();
            } else {
                // Draw regular enemy as circle
                this.ctx.beginPath();
                this.ctx.arc(enemy.x, enemyY, 10, 0, Math.PI * 2);
                this.ctx.fill();
            }
            
            // Health bar
            const barWidth = 16;
            const barHeight = 4;
            const healthPercent = enemy.health / enemy.maxHealth;
            
            this.ctx.fillStyle = '#FF0000';
            this.ctx.fillRect(enemy.x - barWidth/2, enemyY - 18, barWidth, barHeight);
            
            this.ctx.fillStyle = '#00FF00';
            this.ctx.fillRect(enemy.x - barWidth/2, enemyY - 18, barWidth * healthPercent, barHeight);
        });
    }
    
    drawProjectiles() {
        this.projectiles.forEach(projectile => {
            this.ctx.fillStyle = projectile.color;
            this.ctx.beginPath();
            this.ctx.arc(projectile.x, projectile.y, 3, 0, Math.PI * 2);
            this.ctx.fill();
            
            // Trail effect
            this.ctx.strokeStyle = projectile.color;
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            const dx = projectile.targetX - projectile.x;
            const dy = projectile.targetY - projectile.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            const trailLength = Math.min(10, distance);
            this.ctx.moveTo(projectile.x, projectile.y);
            this.ctx.lineTo(projectile.x - (dx/distance) * trailLength, 
                          projectile.y - (dy/distance) * trailLength);
            this.ctx.stroke();
        });
    }
    
    drawEffects() {
        this.effects.forEach(effect => {
            this.ctx.save();
            this.ctx.globalAlpha = effect.life;
            this.ctx.fillStyle = effect.color;
            
            if (effect.type === 'hit') {
                // Draw hit spark
                for (let i = 0; i < 4; i++) {
                    const angle = (i / 4) * Math.PI * 2;
                    const x = effect.x + Math.cos(angle) * (1 - effect.life) * 15;
                    const y = effect.y + Math.sin(angle) * (1 - effect.life) * 15;
                    this.ctx.beginPath();
                    this.ctx.arc(x, y, 2, 0, Math.PI * 2);
                    this.ctx.fill();
                }
            } else {
                // Draw explosion particle
                this.ctx.beginPath();
                this.ctx.arc(effect.x, effect.y, 4 * effect.life, 0, Math.PI * 2);
                this.ctx.fill();
            }
            
            this.ctx.restore();
        });
    }
    
    drawPreview() {
        // Show tower placement preview
        if (!this.selectedTower) {
            const gridX = Math.floor(this.mousePos.x / this.gridSize);
            const gridY = Math.floor(this.mousePos.y / this.gridSize);
            
            if (this.canPlaceTower(gridX, gridY)) {
                const x = gridX * this.gridSize + this.gridSize / 2;
                const y = gridY * this.gridSize + this.gridSize / 2;
                const towerType = this.towerTypes[this.selectedTowerType];
                
                // Draw preview tower
                this.ctx.save();
                this.ctx.globalAlpha = 0.7;
                this.ctx.fillStyle = towerType.color;
                this.ctx.beginPath();
                this.ctx.arc(x, y, 12, 0, Math.PI * 2);
                this.ctx.fill();
                
                // Draw preview range
                this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.3)';
                this.ctx.lineWidth = 2;
                this.ctx.beginPath();
                this.ctx.arc(x, y, towerType.range, 0, Math.PI * 2);
                this.ctx.stroke();
                
                this.ctx.restore();
            }
        }
    }
    
    drawUI() {
        // Game state overlay
        if (this.gameState === 'gameOver') {
            this.ctx.save();
            this.ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            
            this.ctx.fillStyle = '#FF4500';
            this.ctx.font = 'bold 48px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText('Game Over!', this.canvas.width/2, this.canvas.height/2);
            
            this.ctx.fillStyle = 'white';
            this.ctx.font = '24px Arial';
            this.ctx.fillText(`Wave Reached: ${this.wave}`, this.canvas.width/2, this.canvas.height/2 + 50);
            this.ctx.fillText('Refresh to play again', this.canvas.width/2, this.canvas.height/2 + 80);
            
            this.ctx.restore();
        }
    }
    
    updateUI() {
        document.getElementById('wave').textContent = this.wave;
        document.getElementById('lives').textContent = this.lives;
        document.getElementById('money').textContent = this.money;
        document.getElementById('enemies').textContent = this.enemies.length;
    }
    
    gameLoop() {
        this.update();
        this.draw();
        requestAnimationFrame(() => this.gameLoop());
    }
}
```

This implementation continues with more advanced game mechanics, AI behaviors, and complex interactions - exactly what makes games such powerful learning tools for web development concepts!