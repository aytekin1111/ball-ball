import pygame
import math
import random
import time

class Ball:
    def __init__(self, width, height, last_x_pos=0.0):
        # Screen dimensions
        self.width = width
        self.height = height
        
        # Ball properties
        self.radius = 30
        self.velocity = 200  # pixels per second
        self.points_count = 32  # circle smoothness
        
        # Position and movement
        self.x = 0
        self.y = 0
        self.last_x_pos = last_x_pos
        
        # Game properties
        self.type = 0  # 0 = black, 1 = white
        self.destroy = False
        self.erase = False
        self.game_over = False
        self.alpha = 255  # for fade out effect
        
        # Touch/Click tracking
        self.touch_map = {}
        
        # Colors
        self.black_color = (80, 80, 80)
        self.white_color = (240, 240, 240)
        
        self.initialize()
    
    def initialize(self):
        """Initialize ball position, type and color"""
        # Random type: 70% chance black, 30% chance white
        self.type = 1 if random.randint(0, 100) > 70 else 0
        
        # Random X position, but not too close to last ball
        border = 50
        right_side = self.width - self.radius - border
        left_side = self.radius + border
        
        while True:
            self.x = random.randint(left_side, right_side)
            if abs(self.x - self.last_x_pos) > 4 * self.radius:
                break
        
        # Start above screen
        self.y = -self.radius
        
        # Reset flags
        self.destroy = False
        self.erase = False
        self.game_over = False
        self.alpha = 255
    
    def update(self, delta_time):
        """Update ball position and check boundaries"""
        # Move ball down
        self.y += self.velocity * delta_time
        
        # Check if ball reached bottom
        if self.type == 1:  # White ball
            if self.y > self.height + self.radius:
                self.game_over = True
        else:  # Black ball
            if self.y > self.height + self.radius:
                self.erase = True
    
    def render(self, screen):
        """Draw the ball on screen"""
        color = self.white_color if self.type == 1 else self.black_color
        
        # Apply fade effect if destroying
        if self.destroy:
            # Create surface with alpha for transparency
            ball_surface = pygame.Surface((self.radius * 2, self.radius * 2))
            ball_surface.set_alpha(self.alpha)
            ball_surface.fill((0, 0, 0))
            ball_surface.set_colorkey((0, 0, 0))
            
            pygame.draw.circle(ball_surface, color, (self.radius, self.radius), self.radius)
            screen.blit(ball_surface, (self.x - self.radius, self.y - self.radius))
        else:
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
            # Draw border for better visibility
            pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.radius, 2)
    
    def get_last_pos(self):
        """Get X position for next ball placement"""
        return self.x
    
    def handle_mouse_down(self, pos, button_id=0):
        """Handle mouse/touch down event"""
        self.touch_map[button_id] = [False, False]  # [outside_first, inside_touched]
    
    def handle_mouse_up(self, pos, button_id=0):
        """Handle mouse/touch up event"""
        if button_id in self.touch_map:
            del self.touch_map[button_id]
    
    def handle_mouse_move(self, pos, button_id=0):
        """Handle mouse/touch move event"""
        if button_id in self.touch_map:
            if self.is_inside(pos):
                if self.touch_map[button_id][0]:  # Was outside first
                    self.touch_map[button_id][1] = True
            else:
                if self.touch_map[button_id][1]:  # Was inside
                    self.destroy = True
                else:
                    self.touch_map[button_id][0] = True
                self.touch_map[button_id][1] = False
    
    def is_inside(self, pos):
        """Check if position is inside the ball"""
        mx, my = pos
        distance = math.sqrt((mx - self.x) ** 2 + (my - self.y) ** 2)
        return distance < self.radius
    
    def need_to_destroy(self):
        """Check if ball should be destroyed and handle fade effect"""
        if self.destroy:
            self.alpha -= 12  # Fade out speed
            if self.alpha < 0:
                self.alpha = 0
        return self.destroy and self.alpha == 0
    
    def get_type(self):
        """Get ball type (0=black, 1=white)"""
        return self.type
    
    def need_erase(self):
        """Check if ball should be erased"""
        return self.erase
    
    def get_game_over(self):
        """Check if game over condition met"""
        return self.game_over


class BallGame:
    def __init__(self):
        pygame.init()
        
        # Screen settings
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ball Game - Don't Touch White Balls!")
        
        # Game settings
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.score = 0
        self.spawn_timer = 0
        self.spawn_delay = 2.0  # seconds between balls
        
        # Balls list
        self.balls = []
        
        # Colors
        self.bg_color = (50, 50, 50)
        self.text_color = (255, 255, 255)
        
        # Font
        self.font = pygame.font.Font(None, 36)
        
        # Last ball position for spacing
        self.last_x_pos = 0
    
    def spawn_ball(self):
        """Create a new ball"""
        new_ball = Ball(self.width, self.height, self.last_x_pos)
        self.balls.append(new_ball)
        self.last_x_pos = new_ball.get_last_pos()
    
    def update(self, delta_time):
        """Update game state"""
        if self.game_over:
            return
        
        # Update spawn timer
        self.spawn_timer += delta_time
        if self.spawn_timer >= self.spawn_delay:
            self.spawn_ball()
            self.spawn_timer = 0
            # Gradually increase difficulty
            if self.spawn_delay > 0.5:
                self.spawn_delay *= 0.95
        
        # Update all balls
        balls_to_remove = []
        for ball in self.balls:
            ball.update(delta_time)
            
            # Check for game over (white ball reached bottom)
            if ball.get_game_over():
                self.game_over = True
                print(f"Game Over! Final Score: {self.score}")
                return
            
            # Remove balls that need to be erased or destroyed
            if ball.need_erase() or ball.need_to_destroy():
                if ball.need_to_destroy() and ball.get_type() == 0:  # Destroyed black ball
                    self.score += 10
                balls_to_remove.append(ball)
        
        # Remove balls
        for ball in balls_to_remove:
            self.balls.remove(ball)
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.restart_game()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_over:
                    for ball in self.balls:
                        ball.handle_mouse_down(event.pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if not self.game_over:
                    for ball in self.balls:
                        ball.handle_mouse_up(event.pos)
            
            elif event.type == pygame.MOUSEMOTION:
                if not self.game_over and pygame.mouse.get_pressed()[0]:
                    for ball in self.balls:
                        ball.handle_mouse_move(event.pos)
    
    def restart_game(self):
        """Restart the game"""
        self.game_over = False
        self.score = 0
        self.spawn_timer = 0
        self.spawn_delay = 2.0
        self.balls.clear()
        self.last_x_pos = 0
        print("Game Restarted!")
    
    def render(self):
        """Draw everything on screen"""
        self.screen.fill(self.bg_color)
        
        # Draw all balls
        for ball in self.balls:
            ball.render(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.score}", True, self.text_color)
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render("GAME OVER!", True, (255, 0, 0))
            restart_text = self.font.render("Press R to Restart", True, self.text_color)
            
            # Center the text
            go_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
            restart_rect = restart_text.get_rect(center=(self.width//2, self.height//2 + 50))
            
            self.screen.blit(game_over_text, go_rect)
            self.screen.blit(restart_text, restart_rect)
        
        # Draw instructions
        if len(self.balls) == 0 and not self.game_over:
            instruction1 = self.font.render("Click and drag across BLACK balls to destroy them", True, self.text_color)
            instruction2 = self.font.render("Don't let WHITE balls reach the bottom!", True, self.text_color)
            
            inst1_rect = instruction1.get_rect(center=(self.width//2, self.height//2))
            inst2_rect = instruction2.get_rect(center=(self.width//2, self.height//2 + 40))
            
            self.screen.blit(instruction1, inst1_rect)
            self.screen.blit(instruction2, inst2_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        last_time = time.time()
        
        print("Ball Game Started!")
        print("Instructions:")
        print("- Click and drag across BLACK balls to destroy them (+10 points)")
        print("- Don't let WHITE balls reach the bottom (Game Over!)")
        print("- Press R to restart when game over")
        
        while self.running:
            current_time = time.time()
            delta_time = current_time - last_time
            last_time = current_time
            
            self.handle_events()
            self.update(delta_time)
            self.render()
            
            self.clock.tick(60)  # 60 FPS
        
        pygame.quit()


if __name__ == "__main__":
    game = BallGame()
    game.run()