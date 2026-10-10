import pygame


class Puller:
    """Represents a puller character anchor on either side of the rope."""

    def __init__(self, x, y, color, label, facing_direction=1):
        self.x = x
        self.y = y
        self.color = color
        self.label = label
        self.facing_direction = facing_direction
        self.lean = 0.0
        self.font = pygame.font.SysFont(None, 24)

    def render(self, surface):
        """Draw avatar and label with leaning posture."""
        lean_offset = int(-self.facing_direction * self.lean * 18)

        # Body - tilted polygon based on lean
        body_points = [
            (self.x - 20 + lean_offset, self.y - 35),
            (self.x + 20 + lean_offset, self.y - 35),
            (self.x + 20, self.y + 35),
            (self.x - 20, self.y + 35)
        ]
        pygame.draw.polygon(surface, self.color, body_points)

        # Head - follows upper body lean
        pygame.draw.circle(surface, (240, 210, 180), (self.x + lean_offset, self.y - 50), 16)

        # Name / control tag
        label_surf = self.font.render(self.label, True, (240, 240, 240))
        surface.blit(label_surf, (self.x - label_surf.get_width() // 2, self.y + 45))