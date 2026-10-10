import math
import pygame


class Rope:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_y = screen_height // 2
        self.marker_x = screen_width // 2

        self.left_win_x = 180
        self.right_win_x = screen_width - 180
        self.pull_step = 12

        self.tension = 0.0
        self.sag_amount = 14.0
        self.wobble_amplitude = 2.5

    def get_y_at(self, x):
        start_x = 60
        end_x = self.screen_width - 60
        if x <= start_x or x >= end_x:
            return self.center_y

        u = (x - start_x) / (end_x - start_x)
        envelope = 4.0 * u * (1.0 - u)

        # Sag curve when relaxed (low tension)
        sag = (1.0 - self.tension) * self.sag_amount * envelope

        # Vibration wobble when under tension
        now = pygame.time.get_ticks()
        wobble = self.tension * self.wobble_amplitude * math.sin(now * 0.045 + x * 0.05) * envelope

        return self.center_y + sag + wobble

    def pull_left(self, strength=1.0):
        self.marker_x -= int(self.pull_step * strength)

    def pull_right(self, strength=1.0):
        self.marker_x += int(self.pull_step * strength)

    def check_winner(self):
        if self.marker_x <= self.left_win_x:
            return "PLAYER"
        if self.marker_x >= self.right_win_x:
            return "COMPUTER"
        return None

    def reset(self):
        self.marker_x = float(self.screen_width // 2)
        self.velocity = 0.0
        self.tension = 0.0

    def render(self, surface):
        start_x = 60
        end_x = self.screen_width - 60

        # Build rope curve points
        points = []
        step = 16
        for x in range(start_x, end_x + 1, step):
            points.append((x, self.get_y_at(x)))
        if points[-1][0] != end_x:
            points.append((end_x, self.get_y_at(end_x)))

        pygame.draw.lines(surface, (180, 140, 90), False, points, 10)

        pygame.draw.line(
            surface,
            (50, 200, 50),
            (self.left_win_x, self.center_y - 40),
            (self.left_win_x, self.center_y + 40),
            4
        )
        pygame.draw.line(
            surface,
            (200, 50, 50),
            (self.right_win_x, self.center_y - 40),
            (self.right_win_x, self.center_y + 40),
            4
        )

        pygame.draw.line(
            surface,
            (120, 120, 120),
            (self.screen_width // 2, self.center_y - 20),
            (self.screen_width // 2, self.center_y + 20),
            2
        )

        flag_y = self.get_y_at(self.marker_x)
        flag_rect = pygame.Rect(int(self.marker_x) - 12, int(flag_y) - 24, 24, 48)
        pygame.draw.rect(surface, (230, 40, 40), flag_rect, border_radius=4)
        pygame.draw.rect(surface, (255, 255, 255), flag_rect, width=2, border_radius=4)