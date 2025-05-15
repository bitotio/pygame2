# pygame2
 В коде представлен квадрат с координатами чтобы второй квадрат был внутри
В самом коде представлен 2 квадрата разных цветов
вот есть пример того как делал окно
rect2 = pygame.Rect(270, 200, 100, 100)

rect2.center = rect2.center

pygame.draw.rect(screen, RED, rect2)

pygame.display.flip()
