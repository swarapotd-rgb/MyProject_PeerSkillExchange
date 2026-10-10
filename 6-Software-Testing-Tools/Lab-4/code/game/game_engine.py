import random
import pygame
from game.rope import Rope
from game.player import Puller


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rope = Rope(width, height)
        self.player = Puller(90, height // 2, (50, 120, 220), "PLAYER (A/D)", facing_direction=1)
        self.computer = Puller(width - 90, height // 2, (220, 80, 50), "COMPUTER", facing_direction=-1)

        self.last_key = None
        self.is_pull_locked = False
        self.winner = None
        self.game_state = "PLAYING"

        self.computer_pull_cooldown = 180
        self.last_computer_pull = pygame.time.get_ticks()
        self.is_panicking = False
        self.panic_factor = 0.0

        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.is_sudden_death = False

        self.player_pull_activity = 0.0
        self.computer_pull_activity = 0.0
        self.momentum = 0.0

        self.font_big = pygame.font.SysFont(None, 48)
        self.font_medium = pygame.font.SysFont(None, 32)
        self.font_small = pygame.font.SysFont(None, 26)

    def handle_event(self, event):
        if self.game_state != "PLAYING":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset()
            return

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_a, pygame.K_d):
                if event.key != self.last_key:
                    pull_multiplier = 2.0 if self.is_sudden_death else 1.0
                    self.rope.pull_left(pull_multiplier)
                    self.last_key = event.key
                    self.player_pull_activity = min(self.player_pull_activity + 0.6 * pull_multiplier, 3.0)
        
    def update(self):
        if self.game_state != "PLAYING":
            return

        now = pygame.time.get_ticks()
        self.elapsed_time = now - self.start_time
        self.is_sudden_death = self.elapsed_time >= 45000

        center_x = self.width // 2
        if self.rope.marker_x < center_x:
            self.panic_factor = (center_x - self.rope.marker_x) / (center_x - self.rope.left_win_x)
            self.panic_factor = max(0.0, min(1.0, self.panic_factor))
            self.is_panicking = True
        else:
            self.panic_factor = 0.0
            self.is_panicking = False

        current_cooldown = int(self.computer_pull_cooldown - 60 * self.panic_factor)
        if now - self.last_computer_pull >= current_cooldown:
            min_strength = 0.7 + 0.3 * self.panic_factor
            max_strength = 1.2 + 0.4 * self.panic_factor
            computer_variance = random.uniform(min_strength, max_strength)
            pull_multiplier = 2.0 if self.is_sudden_death else 1.0
            self.rope.pull_right(computer_variance * pull_multiplier)
            self.last_computer_pull = now
            self.computer_pull_activity = min(
                self.computer_pull_activity + 0.5 * computer_variance * pull_multiplier, 3.0
            )

        # Decay pull activities smoothly
        self.player_pull_activity *= 0.95
        self.computer_pull_activity *= 0.95

        # Calculate struggle tension (wobble vs sag)
        struggle = (
            min(self.player_pull_activity, self.computer_pull_activity) * 0.8
            + self.panic_factor * 0.5
            + (self.player_pull_activity + self.computer_pull_activity) * 0.2
        )
        target_tension = max(0.0, min(1.0, struggle))
        self.rope.tension += (target_tension - self.rope.tension) * 0.1

        # Calculate momentum (recent pulls + board control)
        pull_diff = (self.player_pull_activity - self.computer_pull_activity) / 2.0
        pos_diff = (center_x - self.rope.marker_x) / (center_x - self.rope.left_win_x)
        pos_diff = max(-1.0, min(1.0, pos_diff))
        target_momentum = max(-1.0, min(1.0, pull_diff * 0.6 + pos_diff * 0.4))
        self.momentum += (target_momentum - self.momentum) * 0.08

        # Update pullers' leaning postures based on momentum
        if self.momentum > 0:
            player_target_lean = 0.2 + 0.8 * self.momentum
            computer_target_lean = -0.4 * self.momentum
        else:
            computer_target_lean = 0.2 + 0.8 * abs(self.momentum)
            player_target_lean = -0.4 * abs(self.momentum)

        self.player.lean += (player_target_lean - self.player.lean) * 0.1
        self.computer.lean += (computer_target_lean - self.computer.lean) * 0.1

        result = self.rope.check_winner()
        if result:
            self.winner = result
            self.game_state = "GAME_OVER"

    def reset(self):
        self.rope.reset()
        self.last_key = None
        self.is_pull_locked = False
        self.winner = None
        self.game_state = "PLAYING"
        self.last_computer_pull = pygame.time.get_ticks()
        self.is_panicking = False
        self.panic_factor = 0.0
        self.start_time = pygame.time.get_ticks()
        self.elapsed_time = 0
        self.is_sudden_death = False
        self.player_pull_activity = 0.0
        self.computer_pull_activity = 0.0
        self.momentum = 0.0
        self.player.lean = 0.0
        self.computer.lean = 0.0

    def render(self, screen):
        screen.fill((30, 32, 36))

        mud_rect = pygame.Rect(self.width // 2 - 120, self.height // 2 - 80, 240, 160)
        pygame.draw.rect(screen, (45, 38, 30), mud_rect, border_radius=12)

        self.rope.render(screen)
        self.player.render(screen)
        self.computer.render(screen)

        total_seconds = self.elapsed_time // 1000
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        timer_str = f"{minutes}:{seconds:02d}"

        timer_color = (255, 80, 80) if self.is_sudden_death else (220, 220, 220)
        timer_surf = self.font_medium.render(timer_str, True, timer_color)
        screen.blit(timer_surf, (self.width // 2 - timer_surf.get_width() // 2, 12))

        inst_surf = self.font_small.render(
            "Alternate [A] and [D] keys rapidly to pull!", True, (210, 210, 210)
        )
        screen.blit(inst_surf, (self.width // 2 - inst_surf.get_width() // 2, 40))

        if self.is_sudden_death:
            sd_surf = self.font_big.render("SUDDEN DEATH!", True, (255, 60, 60))
            screen.blit(sd_surf, (self.width // 2 - sd_surf.get_width() // 2, 70))

        if self.game_state == "PLAYING" and self.is_panicking:
            panic_surf = self.font_big.render("PANIC!", True, (240, 50, 50))
            screen.blit(
                panic_surf,
                (self.computer.x - panic_surf.get_width() // 2, self.computer.y - 110)
            )

        if self.game_state == "GAME_OVER":
            overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))

            win_text = f"{self.winner} WINS!"
            color = (80, 220, 80) if self.winner == "PLAYER" else (240, 80, 80)
            text_surf = self.font_big.render(win_text, True, color)
            screen.blit(
                text_surf,
                (self.width // 2 - text_surf.get_width() // 2, self.height // 2 - 50)
            )

            restart_surf = self.font_small.render(
                "Press [R] to Play Again", True, (240, 240, 240)
            )
            screen.blit(
                restart_surf,
                (self.width // 2 - restart_surf.get_width() // 2, self.height // 2 + 10)
            )
