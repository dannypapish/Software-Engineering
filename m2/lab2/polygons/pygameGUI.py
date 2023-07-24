from polygons import Polygons
import math
import pygame


class PygameGUI(Polygons):  # Something is missing here
    # TODO 13: Fix this class so that it inherits from the Polygons class

    def __init__(self, num_sides, side_length):
        super().__init__(num_sides, side_length)
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.rotation = 2

    def draw_polygon(self, color, center, rotation):
        points = []
        for i in range(self.num_sides):
            angle = math.radians(360 / self.num_sides * i + rotation)
            x = center[0] + self.radius * math.cos(angle)
            y = center[1] + self.radius * math.sin(angle)
            points.append((x, y))
        pygame.draw.polygon(self.screen, color, points)

    def main_scene(self, center, rotation):

        self.draw_polygon((80, 20, 210), center, rotation)
        self.area = self.num_sides * self.side_length ** 2 / \
            (4 * math.tan(math.pi / self.num_sides))
        self.radius = math.sqrt(self.area / math.pi)
        font = pygame.font.SysFont("Arial", 20)
        text = font.render(f"Area: {self.area:.2f}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        text = font.render(f"Sides: {self.num_sides}", True, (255, 255, 255))
        self.screen.blit(text, (10, 30))
        text = font.render(
            "Up/Down Arrows to change num_sides", True, (255, 255, 255))
        self.screen.blit(text, (10, 550))

    def run_pygame(self, center, rotation):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP]:
                    self.num_sides += 1

                if keys[pygame.K_DOWN]:
                    self.num_sides -= 1

            self.screen.fill((0, 0, 0))
            self.main_scene(center, rotation)
            pygame.display.flip()
            self.clock.tick(60)
            rotation += self.rotation


def main():
    pygame.init()
    pygame.display.set_caption("Pygame Polygon Visualizer")
    pygame.font.init()
    visualizer = PygameGUI(3, 100)
    visualizer.run_pygame((400, 300), 1)
    pygame.quit()


if __name__ == "__main__":
    main()
