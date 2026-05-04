import pygame
import math
import random
from sys import exit

# --- CONFIGURAÇÕES GLOBAIS ---
TILE_SIZE = 24
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (33, 33, 255)
RED = (255, 0, 0)
PINK = (255, 182, 193)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
POWER_COLOR = (248, 187, 208)

# Estados do Sistema
START = 0
PLAYING = 1
GAMEOVER = 2
WIN = 3 # Novo estado

# Estados da IA
SCATTER = 0
CHASE = 1
FRIGHTENED = 2

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
    [1,9,9,9,0,9,9,1,9,9,9,1,9,9,0,9,9,9,1],
    [1,1,1,1,0,1,9,1,1,1,1,1,9,1,0,1,1,1,1],
    [3,3,3,1,0,1,9,9,9,9,9,9,9,1,0,1,3,3,3],
    [1,1,1,1,0,1,9,1,1,1,1,1,9,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,1],
    [1,2,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,2,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Entity:
    def __init__(self, x, y, color):
        self.start_pos = (x, y)
        self.reset_position()
        self.vel = 2
        self.color = color
        self.dir = (0, 0)
        self.next_dir = (0, 0)

    def reset_position(self):
        self.x, self.y = self.start_pos[0] * TILE_SIZE, self.start_pos[1] * TILE_SIZE
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
        self.lives = 3
        self.mouth_open = 0

    def update(self, maze):
        self.mouth_open = abs(math.sin(pygame.time.get_ticks() * 0.01)) * 30
        if self.is_at_center():
            tx, ty = self.get_tile()
            nx, ny = self.next_dir
            if 0 <= ty+ny < len(maze) and 0 <= tx+nx < len(maze[0]):
                if maze[ty + ny][tx + nx] != 1:
                    self.dir = self.next_dir
            
            dx, dy = self.dir
            if 0 <= ty+dy < len(maze) and 0 <= tx+dx < len(maze[0]):
                if maze[ty + dy][tx + dx] == 1:
                    self.dir = (0, 0)

        self.x += self.dir[0] * self.vel
        self.y += self.dir[1] * self.vel
        
        # Teleporte Túnel
        if self.x < -TILE_SIZE//2: self.x = (len(maze[0])-1) * TILE_SIZE
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
        
        speed = 1 if self.mode == FRIGHTENED else self.vel
        self.x += self.dir[0] * speed
        self.y += self.dir[1] * speed
        
        # Túnel para fantasmas também
        if self.x < -TILE_SIZE//2: self.x = (len(maze[0])-1) * TILE_SIZE
        elif self.x >= len(maze[0]) * TILE_SIZE: self.x = 0

    def decide_direction(self, maze, player, blinky_pos):
        tx, ty = self.get_tile()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        opposite = (-self.dir[0], -self.dir[1])
        
        # Lógica de Alvos
        if self.mode == FRIGHTENED:
            self.target = (random.randint(0, 18), random.randint(0, 18))
        elif self.mode == SCATTER:
            self.target = self.scatter_target
        else: # CHASE
            px, py = player.get_tile()
            if self.color == RED: self.target = (px, py)
            elif self.color == PINK: self.target = (px + player.dir[0]*4, py + player.dir[1]*4)
            elif self.color == CYAN:
                vx, vy = (px + player.dir[0]*2) - blinky_pos[0], (py + player.dir[1]*2) - blinky_pos[1]
                self.target = (blinky_pos[0] + vx*2, blinky_pos[1] + vy*2)
            else: # ORANGE
                dist = self.get_distance((tx, ty), (px, py))
                self.target = (px, py) if dist > 8 else self.scatter_target

        best_dir = self.dir
        min_dist = float('inf')

        valid_moves = []
        for d in directions:
            if d == opposite: continue
            nx, ny = tx + d[0], ty + d[1]
            
            # CORREÇÃO BUG: Verifica se está dentro dos limites e se NÃO é parede (1)
            if 0 <= ny < len(maze) and 0 <= nx < len(maze[0]):
                if maze[ny][nx] != 1:
                    d_dist = self.get_distance((nx, ny), self.target)
                    valid_moves.append((d_dist, d))

        if valid_moves:
            # Escolhe a direção com a menor distância para o alvo
            valid_moves.sort() 
            self.dir = valid_moves[0][1]
        else:
            # Se não houver saída (beco), volta para trás
            self.dir = opposite

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((len(MAZE_DATA[0])*TILE_SIZE, len(MAZE_DATA)*TILE_SIZE + 60))
        pygame.display.set_caption("Pac-Man Parceiro")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Impact", 24)
        self.game_state = START
        self.reset_game()

    def reset_game(self):
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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if self.game_state in [START, GAMEOVER, WIN]:
                    self.reset_game()
                    self.game_state = PLAYING
                elif self.game_state == PLAYING:
                    if event.key == pygame.K_UP: self.player.next_dir = (0, -1)
                    if event.key == pygame.K_DOWN: self.player.next_dir = (0, 1)
                    if event.key == pygame.K_LEFT: self.player.next_dir = (-1, 0)
                    if event.key == pygame.K_RIGHT: self.player.next_dir = (1, 0)

    def check_win(self):
        # Se não houver mais pellets (0) nem power pellets (2), o jogador venceu
        for row in self.maze:
            if 0 in row or 2 in row:
                return False
        return True

    def update(self):
        if self.game_state != PLAYING: return

        self.timer += 1
        if self.frightened_timer > 0:
            self.frightened_timer -= 1
            self.mode = FRIGHTENED
        else:
            cycle_time = self.timer % (27 * FPS)
            self.mode = SCATTER if cycle_time < 7 * FPS else CHASE

        self.player.update(self.maze)
        
        tx, ty = self.player.get_tile()
        if self.maze[ty][tx] == 0:
            self.maze[ty][tx] = 9
            self.player.score += 10
        elif self.maze[ty][tx] == 2:
            self.maze[ty][tx] = 9
            self.player.score += 50
            self.frightened_timer = 7 * FPS

        # Verifica Vitória
        if self.check_win():
            self.game_state = WIN

        blinky_pos = self.ghosts[0].get_tile()
        for g in self.ghosts:
            g.update(self.maze, self.player, blinky_pos, self.mode)
            if g.get_tile() == (tx, ty):
                if self.mode == FRIGHTENED:
                    self.player.score += 200
                    g.reset_position()
                else:
                    self.player.lives -= 1
                    if self.player.lives <= 0:
                        self.game_state = GAMEOVER
                    else:
                        self.player.reset_position()
                        for ghost in self.ghosts: ghost.reset_position()

    def draw_text(self, text, y_offset, color=WHITE, size=30):
        font = pygame.font.SysFont("Impact", size)
        img = font.render(text, True, color)
        rect = img.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()//2 + y_offset))
        self.screen.blit(img, rect)

    def draw(self):
        self.screen.fill(BLACK)
        
        if self.game_state == START:
            self.draw_text("PAC-MAN PARCEIRO", -50, YELLOW, 50)
            self.draw_text("PRESSIONE QUALQUER TECLA PARA JOGAR", 20, WHITE, 20)
        
        elif self.game_state == WIN:
            self.draw_text("PARABÉNS! VOCÊ VENCEU!", -30, CYAN, 45)
            self.draw_text(f"SCORE FINAL: {self.player.score}", 30, WHITE, 25)
            self.draw_text("PRESSIONE PARA RECOMECAR", 80, YELLOW, 18)

        elif self.game_state == GAMEOVER:
            self.draw_text("GAME OVER", -20, RED, 60)
            self.draw_text(f"SCORE: {self.player.score}", 40, WHITE, 25)
            self.draw_text("PRESSIONE PARA TENTAR NOVAMENTE", 80, YELLOW, 18)

        elif self.game_state == PLAYING:
            for y, row in enumerate(self.maze):
                for x, cell in enumerate(row):
                    rect = (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if cell == 1: pygame.draw.rect(self.screen, BLUE, rect, 2, border_radius=4)
                    if cell == 0: pygame.draw.circle(self.screen, WHITE, (x*TILE_SIZE+12, y*TILE_SIZE+12), 2)
                    if cell == 2: pygame.draw.circle(self.screen, POWER_COLOR, (x*TILE_SIZE+12, y*TILE_SIZE+12), 6)

            # Player
            p_x, p_y = int(self.player.x+12), int(self.player.y+12)
            pygame.draw.circle(self.screen, YELLOW, (p_x, p_y), 11)
            angle = self.player.mouth_open
            points = [ (p_x, p_y) ]
            rot = 0
            if self.player.dir == (-1, 0): rot = 180
            elif self.player.dir == (0, -1): rot = 270
            elif self.player.dir == (0, 1): rot = 90
            for a in range(int(-angle), int(angle)):
                rad = math.radians(a + rot)
                points.append((p_x + 12 * math.cos(rad), p_y + 12 * math.sin(rad)))
            if len(points) > 2: pygame.draw.polygon(self.screen, BLACK, points)

            # Fantasmas
            for g in self.ghosts:
                color = (50, 50, 255) if self.mode == FRIGHTENED else g.color
                pygame.draw.circle(self.screen, color, (int(g.x+12), int(g.y+12)), 11)
                pygame.draw.rect(self.screen, color, (int(g.x+1), int(g.y+12), 22, 10))

            info = f"SCORE: {self.player.score}   LIVES: {self.player.lives}"
            txt = self.font.render(info, True, WHITE)
            self.screen.blit(txt, (10, len(MAZE_DATA)*TILE_SIZE + 10))

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == "__main__":
    GameController().run()
