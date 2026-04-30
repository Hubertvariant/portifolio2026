import pygame
import math
import random

# --- CONFIGURAÇÕES GLOBAIS ---
TILE_SIZE = 24
FPS = 60
# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 182, 193)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
POWER_COLOR = (248, 187, 208)

# Estados do Jogo
SCATTER = 0
CHASE = 1
FRIGHTENED = 2

# Mapa Simplificado (1 = Parede, 0 = Caminho/Pellet, 2 = Power Pellet, 3 = Túnel, 9 = Vazio)
MAZE_DATA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,9,1,9,1,1,1,0,1,1,1,1],
    [3,3,3,1,0,1,9,9,9,9,9,9,9,1,0,1,3,3,3],
    [1,1,1,1,0,1,9,1,1,9,1,1,9,1,0,1,1,1,1],
    [9,9,9,9,0,9,9,1,9,9,9,1,9,9,0,9,9,9,9],
    [1,1,1,1,0,1,9,1,1,1,1,1,9,1,0,1,1,1,1],
    [3,3,3,1,0,1,9,9,9,9,9,9,9,1,0,1,3,3,3],
    [1,1,1,1,0,1,9,1,1,1,1,1,9,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
    [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Entity:
    def __init__(self, x, y, color):
        self.x, self.y = x * TILE_SIZE, y * TILE_SIZE
        self.vel = 2
        self.color = color
        self.dir = (0, 0)
        self.next_dir = (0, 0)

    def get_tile(self):
        return int((self.x + TILE_SIZE//2) // TILE_SIZE), int((self.y + TILE_SIZE//2) // TILE_SIZE)

    def is_at_center(self):
        return self.x % TILE_SIZE == 0 and self.y % TILE_SIZE == 0

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, YELLOW)
        self.score = 0

    def update(self, maze):
        if self.is_at_center():
            # Tenta mudar para a direção desejada se não houver parede
            tx, ty = self.get_tile()
            nx, ny = self.next_dir
            if maze[ty + ny][tx + nx] != 1:
                self.dir = self.next_dir
            
            # Para se bater na parede
            dx, dy = self.dir
            if maze[ty + dy][tx + dx] == 1:
                self.dir = (0, 0)

        self.x += self.dir[0] * self.vel
        self.y += self.dir[1] * self.vel
        
        # Teletransporte Túnel
        if self.x < 0: self.x = (len(maze[0])-1) * TILE_SIZE
        elif self.x >= len(maze[0]) * TILE_SIZE: self.x = 0

class Ghost(Entity):
    def __init__(self, x, y, color, scatter_target):
        super().__init__(x, y, color)
        self.mode = SCATTER
        self.scatter_target = scatter_target
        self.target = scatter_target
        self.dir = (0, -1)

    def get_distance(self, node, target):
        return math.sqrt((node[0] - target[0])**2 + (node[1] - target[1])**2)

    def update(self, maze, player, blinky_pos, mode):
        self.mode = mode
        if self.is_at_center():
            self.decide_direction(maze, player, blinky_pos)
        
        speed = self.vel if self.mode != FRIGHTENED else 1
        self.x += self.dir[0] * speed
        self.y += self.dir[1] * speed

    def decide_direction(self, maze, player, blinky_pos):
        tx, ty = self.get_tile()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)] # Ordem de prioridade original
        
        # Inverter direção proibido exceto na mudança de modo (simplificado aqui)
        opposite = (-self.dir[0], -self.dir[1])
        
        best_dir = self.dir
        min_dist = float('inf')

        # Lógica de Alvos (Target Tiles)
        if self.mode == FRIGHTENED:
            self.target = (random.randint(0, 20), random.randint(0, 20))
        elif self.mode == SCATTER:
            self.target = self.scatter_target
        else: # CHASE MODE
            px, py = player.get_tile()
            pdx, pdy = player.dir
            
            if self.color == RED: # Blinky
                self.target = (px, py)
            elif self.color == PINK: # Pinky: 4 à frente
                self.target = (px + pdx*4, py + pdy*4)
            elif self.color == CYAN: # Inky: Vetor Blinky -> Pacman
                v_x, v_y = (px + pdx*2) - blinky_pos[0], (py + pdy*2) - blinky_pos[1]
                self.target = (blinky_pos[0] + v_x*2, blinky_pos[1] + v_y*2)
            elif self.color == ORANGE: # Clyde
                dist = self.get_distance((tx, ty), (px, py))
                self.target = (px, py) if dist > 8 else self.scatter_target

        for d in directions:
            if d == opposite: continue
            nx, ny = tx + d[0], ty + d[1]
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]) and maze[ny][nx] != 1:
                d_dist = self.get_distance((nx, ny), self.target)
                if d_dist < min_dist:
                    min_dist = d_dist
                    best_dir = d
        
        self.dir = best_dir

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((len(MAZE_DATA[0])*TILE_SIZE, len(MAZE_DATA)*TILE_SIZE + 50))
        self.clock = pygame.time.Clock()
        self.maze = [row[:] for row in MAZE_DATA]
        self.player = Player(9, 13)
        self.ghosts = [
            Ghost(9, 7, RED, (18, 0)),
            Ghost(9, 8, PINK, (0, 0)),
            Ghost(8, 8, CYAN, (18, 18)),
            Ghost(10, 8, ORANGE, (0, 18))
        ]
        self.mode = SCATTER
        self.timer = 0
        self.frightened_timer = 0

    def run(self):
        while True:
            self.timer += 1
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: self.player.next_dir = (0, -1)
                if event.key == pygame.K_DOWN: self.player.next_dir = (0, 1)
                if event.key == pygame.K_LEFT: self.player.next_dir = (-1, 0)
                if event.key == pygame.K_RIGHT: self.player.next_dir = (1, 0)

    def update(self):
        # Gerenciador de Modos (7s Scatter / 20s Chase)
        if self.frightened_timer > 0:
            self.frightened_timer -= 1
            self.mode = FRIGHTENED
        else:
            cycle_time = self.timer % (27 * FPS)
            self.mode = SCATTER if cycle_time < 7 * FPS else CHASE

        self.player.update(self.maze)
        
        # Colisão com Itens
        tx, ty = self.player.get_tile()
        if self.maze[ty][tx] == 0:
            self.maze[ty][tx] = 9
            self.player.score += 10
        elif self.maze[ty][tx] == 2:
            self.maze[ty][tx] = 9
            self.player.score += 50
            self.frightened_timer = 7 * FPS

        blinky_pos = self.ghosts[0].get_tile()
        for g in self.ghosts:
            g.update(self.maze, self.player, blinky_pos, self.mode)
            # Colisão Fantasma
            if g.get_tile() == (tx, ty):
                if self.mode == FRIGHTENED:
                    self.player.score += 200
                    g.x, g.y = 9 * TILE_SIZE, 8 * TILE_SIZE # Reset simples
                else:
                    self.__init__() # Game Over: Reseta tudo

    def draw(self):
        self.screen.fill(BLACK)
        # Desenha Labirinto
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                rect = (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if cell == 1: pygame.draw.rect(self.screen, BLUE, rect, 1)
                if cell == 0: pygame.draw.circle(self.screen, WHITE, (x*TILE_SIZE+12, y*TILE_SIZE+12), 2)
                if cell == 2: pygame.draw.circle(self.screen, POWER_COLOR, (x*TILE_SIZE+12, y*TILE_SIZE+12), 6)

        # Desenha Player
        pygame.draw.circle(self.screen, YELLOW, (int(self.player.x+12), int(self.player.y+12)), 10)
        
        # Desenha Fantasmas
        for g in self.ghosts:
            color = (50, 50, 255) if self.mode == FRIGHTENED else g.color
            pygame.draw.circle(self.screen, color, (int(g.x+12), int(g.y+12)), 10)
            pygame.draw.rect(self.screen, color, (int(g.x+2), int(g.y+12), 20, 10))

        # Score
        font = pygame.font.SysFont("Arial", 24)
        txt = font.render(f"SCORE: {self.player.score}  MODE: {'FRIGHT' if self.mode==2 else 'CHASE' if self.mode==1 else 'SCATTER'}", True, WHITE)
        self.screen.blit(txt, (10, len(MAZE_DATA)*TILE_SIZE + 10))
        
        pygame.display.flip()

if __name__ == "__main__":
    game = GameController()
    game.run()
