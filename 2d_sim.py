import pygame, sys, random

# ---------- CONFIG ----------
GRID_SIZE        = 10      # 10×10 grid
CELL_SIZE        = 60      # pixels
WIDTH = HEIGHT   = GRID_SIZE * CELL_SIZE

N_OBSTACLES      = 16      # total wall tiles
MAX_CLUSTER_SIZE = 2       # longest cluster of connected walls
FLASH_TIME       = 150     # ms for red wall flash
ERROR_TIME       = 1000    # ms error message visible

BACKGROUND  = (255, 255, 255)
GRID_LINE   = (200, 200, 200)
FLASH_COLOR = (255,   0,   0)

START_POS   = (0, 0)

# ---------- INIT ----------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Grid")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# --- load & scale images ---
robot_img = pygame.image.load("robot.png").convert_alpha()
robot_img = pygame.transform.scale(robot_img, (CELL_SIZE, CELL_SIZE))

wall_img  = pygame.image.load("wall.png").convert_alpha()
wall_img  = pygame.transform.scale(wall_img,  (CELL_SIZE, CELL_SIZE))

# ---------- HELPERS ----------
def neighbors(x, y):
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        yield x+dx, y+dy

def generate_obstacles():
    obstacles = set()

    def cluster_len(x, y):
        seen, stack = set(), [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in obstacles and (cx, cy) not in seen:
                seen.add((cx, cy))
                stack.extend([n for n in neighbors(cx, cy)])
        return len(seen)

    while len(obstacles) < N_OBSTACLES:
        x, y = random.randrange(GRID_SIZE), random.randrange(GRID_SIZE)
        if (x, y) == START_POS or (x, y) in obstacles:
            continue
        obstacles.add((x, y))
        if any(cluster_len(nx, ny) > MAX_CLUSTER_SIZE
               for nx, ny in neighbors(x, y) if (nx, ny) in obstacles):
            obstacles.remove((x, y))
    return obstacles

def draw(obstacles, dog_pos, flash_wall=None, error_msg=""):
    screen.fill(BACKGROUND)

    # draw grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(
                screen, GRID_LINE,
                (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )

    # draw walls
    for (wx, wy) in obstacles:
        rect = (wx*CELL_SIZE, wy*CELL_SIZE)
        if flash_wall == (wx, wy):
            pygame.draw.rect(screen, FLASH_COLOR,
                             pygame.Rect(*rect, CELL_SIZE, CELL_SIZE))
        else:
            screen.blit(wall_img, rect)

    # draw robot
    screen.blit(robot_img, (dog_pos[0]*CELL_SIZE, dog_pos[1]*CELL_SIZE))

    # draw error popup (centered box)
    if error_msg:
        box_width, box_height = 400, 60
        box_x = (WIDTH - box_width) // 2
        box_y = (HEIGHT - box_height) // 2

        # background and red border
        pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, (255, 0, 0),     (box_x, box_y, box_width, box_height), 3)

        # center the text inside
        text = font.render(error_msg, True, (255, 0, 0))
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()

# ---------- MAIN ----------
def main():
    dog_x, dog_y = START_POS
    obstacles    = generate_obstacles()

    flash_wall   = None
    flash_timer  = 0

    error_msg    = ""
    error_timer  = 0

    running = True
    while running:
        dt = clock.tick(12)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # key press
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_w]: dy = -1
        if keys[pygame.K_s]: dy =  1
        if keys[pygame.K_a]: dx = -1
        if keys[pygame.K_d]: dx =  1

        if keys[pygame.K_r]:        # reset robot & regenerate obstacles
            dog_x, dog_y  = START_POS
            obstacles     = generate_obstacles()
            error_msg     = ""
            flash_wall    = None

        # try to move
        new_x, new_y = dog_x + dx, dog_y + dy
        if (dx or dy) and 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            if (new_x, new_y) not in obstacles:
                dog_x, dog_y = new_x, new_y
            else:
                flash_wall   = (new_x, new_y)
                flash_timer  = FLASH_TIME
                error_msg    = "❌ Wall hit! Change direction"
                error_timer  = ERROR_TIME

        # update timers
        if flash_timer > 0:
            flash_timer -= dt
            if flash_timer <= 0:
                flash_wall = None
        if error_timer > 0:
            error_timer -= dt
            if error_timer <= 0:
                error_msg = ""

        draw(obstacles, (dog_x, dog_y), flash_wall, error_msg)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
