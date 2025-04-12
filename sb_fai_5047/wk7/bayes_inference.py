import numpy as np
import pygame

# Bayes' Rule Calculator in Python (CLI Version) by ChatGPT

def compute_bayes(prior, likelihood, false_positive_rate):
    pH = prior
    pNotH = 1 - prior
    pE_given_H = likelihood
    pE_given_notH = false_positive_rate

    numerator = pE_given_H * pH
    denominator = numerator + (pE_given_notH * pNotH)

    if denominator == 0:
        return None

    posterior = numerator / denominator
    return posterior

if __name__ == "__main__":
    print("Bayes' Rule Calculator")
    prior = float(input("Enter prior probability P(H): "))
    likelihood = float(input("Enter likelihood P(E|H): "))
    false_positive_rate = float(input("Enter false positive rate P(E|¬H): "))

    posterior = compute_bayes(prior, likelihood, false_positive_rate)
    if posterior is not None:
        print(f"Posterior probability P(H|E): {posterior:.4f}")
    else:
        print("Invalid input: denominator in Bayes' rule was 0.")

# --------------------------------------------
# Ghostbusters Grid Visualization with Bayes
# --------------------------------------------

# Sensor model (Pr(Color | Distance))
SENSOR_MODEL = {
    'red':    [0.8, 0.15, 0.04, 0.01],
    'orange': [0.1, 0.6, 0.25, 0.05],
    'yellow': [0.05, 0.2, 0.6, 0.15],
    'green':  [0.01, 0.05, 0.3, 0.64]
}

COLORS = {'red': (255, 0, 0), 'orange': (255, 165, 0), 'yellow': (255, 255, 0), 'green': (0, 255, 0)}

GRID_SIZE = 5
CELL_SIZE = 100
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
font = pygame.font.SysFont(None, 24)

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_normalized_posterior(sensor_reading, ghost_loc, grid_shape):
    rows, cols = grid_shape
    prior = 1 / (rows * cols)
    unnormalized = np.zeros((rows, cols))

    for r in range(rows):
        for c in range(cols):
            d = manhattan_distance((r, c), ghost_loc)
            d = min(d, 3)  # cap distance to match sensor model
            likelihood = SENSOR_MODEL[sensor_reading][d]
            unnormalized[r, c] = likelihood * prior

    total = np.sum(unnormalized)
    if total == 0:
        return unnormalized
    return unnormalized / total

def draw_grid(beliefs):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = beliefs[r, c]
            shade = int(255 * (1 - value / np.max(beliefs)))
            color = (shade, shade, 255)
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)
            text = font.render(f"{value:.2f}", True, (0, 0, 0))
            screen.blit(text, (c * CELL_SIZE + 5, r * CELL_SIZE + 5))

def run():
    clock = pygame.time.Clock()
    ghost_loc = (np.random.randint(GRID_SIZE), np.random.randint(GRID_SIZE))
    sensor_reading = 'yellow'
    beliefs = get_normalized_posterior(sensor_reading, ghost_loc, (GRID_SIZE, GRID_SIZE))

    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_grid(beliefs)
        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sensor_reading = np.random.choice(list(SENSOR_MODEL.keys()))
                    beliefs = get_normalized_posterior(sensor_reading, ghost_loc, (GRID_SIZE, GRID_SIZE))
                    print(f"Sensor Reading: {sensor_reading}")

    pygame.quit()

if __name__ == '__main__':
    run()
