import pygame

turn = 'black'


colored_history = []


def find_piece(x, y):
    for d in all_pieces:
        for g in d:
            for b in g:
                if b.x == x:
                    if b.y == y:
                        return b


def draw_squares(x, y, black):
    print("stop")
    if x > -1:
        if x < 8:
            if y > -1:
                if y < 8:
                    if pie_array[int(x)][int(y)] != black:
                        colored_history.append(pygame.Rect(78 + 80 * x, 78 + 80 * y, 78, 78))
                        pygame.draw.rect(gameDisplay, blue, rects[int(x)][int(y)])
                    if pie_array[int(x)][int(y)] == 0:
                        return False

    return True


class Piece:
    def __init__(self, x, y, black):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(78 + 80 * self.x, 78 + 80 * self.y, 78, 78)
        if black:
            self.black = 2
        else:
            self.black = 1
        self.clicked = False
        pie_array[self.x][self.y] = self.black

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def before_move(self):
        return

    def get_rect(self):
        return self.rect

    def draw(self):
        return

    def event_handler(self, events):
        if events is None:
            return
            # change selected color if rectangle clicked
        if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 1:  # is left button clicked
                for r in colored_history:
                    if r.collidepoint(events.pos):

                        print(self.x == int((r.x - 78) / 80))
                        if self.clicked:
                            print('suo')
                            if find_piece((r.x - 78) / 80, (r.y - 78) / 80) is not None:
                                find_piece((r.x - 78) / 80, (r.y - 78) / 80).black = 0
                            pie_array[int(self.x)][int(self.y)] = 0
                            self.y = (r.y - 78) / 80
                            self.x = (r.x - 78) / 80
                            pie_array[int(self.x)][int(self.y)] = self.black
                            self.rect = r
                            colored_history.clear()
                            return True

                if self.rect.collidepoint(events.pos):  # is mouse over button
                    state = 'pawn clicked'
                    self.before_move()
                    self.clicked = True
                    return False

            self.clicked = False
        return False


class Queen(Piece):
    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(queen, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        colored_history.clear()
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y - d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y - d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x, self.y - d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y, self.black):
                break


class Knight(Piece):

    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(knight, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        draw_squares(self.x+2, self.y + 1,self.black)
        draw_squares(self.x + 2, self.y - 1,self.black)
        draw_squares(self.x - 2, self.y + 1,self.black)
        draw_squares(self.x - 2, self.y - 1,self.black)
        draw_squares(self.x + 1, self.y + 2,self.black)
        draw_squares(self.x + 1, self.y - 2,self.black)
        draw_squares(self.x - 1, self.y + 2,self.black)
        draw_squares(self.x - 1, self.y - 2,self.black)


class Bishop(Piece):
    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(bishop, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        colored_history.clear()
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y - d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y - d, self.black):
                break





class Pawn(Piece):
    moved = 0

    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(pawn, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        colored_history.clear()
        if self.black == 2:
            for d in range(-2 + self.moved, 0):
                draw_squares(self.x, self.y - d, self.black)
                colored_history.append(pygame.Rect(78 + 80 * self.x, 78 + 80 * (self.y-d), 78, 78))
        else:
            for d in range(1, 3 - self.moved):
                draw_squares(self.x, self.y - d, self.black)
                colored_history.append(pygame.Rect(78 + 80 * self.x, 78 + 80 * (self.y-d), 78, 78))

    def event_handler(self, events):
        if super(Pawn, self).event_handler(events):
            if self.moved == 0:
                self.moved += 1
            return True


class King(Piece):
    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(king, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        colored_history.clear()
        back = -1
        front = 2
        left = -1
        right = 2
        if self.x == 7:
            right = 1
        if self.y == 0:
            back = 0
        if self.x == 0:
            left = 0
        if self.y == 7:
            front = 1
        for d in range(back, front):
            for b in range(left, right):
                if b == 0:
                    if d == 0:
                        continue
                draw_squares(self.x + b, self.y + d, self.black)
                colored_history.append(pygame.Rect(78 + 80 * (self.x + b), 78 + 80 * (self.y + d), 78, 78))


class Rook(Piece):
    def __init__(self, x, y, black):
        Piece.__init__(self, x, y, black)

    def draw(self):
        gameDisplay.blit(rook, [78 + 80 * self.x, 78 + 80 * self.y])

    def before_move(self):
        colored_history.clear()
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x, self.y + d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x, self.y - d, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x + d, self.y, self.black):
                break
        for d in range(8):
            if d == 0:
                continue
            if draw_squares(self.x - d, self.y, self.black):
                break


pygame.init()
rects = []
for i in range(8):
    row = []
    for y in range(8):
        row.append(pygame.Rect(78 + 80 * i, 78 + 80 * y, 78, 78))
    rects.append(row)

display_width = 799
display_height = 799

gameDisplay = pygame.display.set_mode((display_width, display_height))


color_black = (0, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
i = 0

clock = pygame.time.Clock()
crashed = False
background = pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\chess.jpg')

pawn = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\pawn.jpg'), (78, 78))
bishop = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\bishop.png'), (78, 78))
rook = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\rook.png'), (78, 78))
king = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\king.png'), (78, 78))
queen = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\queen.png'), (78, 78))
knight = pygame.transform.scale(pygame.image.load('C:\\Users\\yairh\\Documents\\pychess\\knight.png'), (78, 78))

pie_array = [[0 for x in range(8)] for y in range(8)]

all_pieces = []


white_bishops = [Bishop(2, 7, False), Bishop(5, 7, False)]
black_bishops = [Bishop(2, 0, True), Bishop(5, 0, True)]

white_rooks = [Rook(0, 7, False), Rook(7, 7, False)]
black_rooks = [Rook(0, 0, True), Rook(7, 0, True)]


white_knights = [Knight(6, 7, False), Knight(1, 7, False)]
black_knights = [Knight(6, 0, True), Knight(1, 0, True)]

white_pawns = []
for y in range(8):
    white_pawns.append(Pawn(y, 6, False))


black_pawns = []
for y in range(8):
    black_pawns.append(Pawn(y, 1, True))
black_pieces = [black_bishops, black_pawns, black_knights, [Queen(3, 0, True)], [King(4, 0, True)], black_rooks]
white_pieces = [white_bishops, white_pawns, white_knights, [Queen(3, 7, False)], [King(4, 7, False)], white_rooks]
all_pieces.append(black_pieces)
all_pieces.append(white_pieces)

kill = None
last_click = None


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.blit(background, [0, 0])
    for color in all_pieces:
        for some in color:
            for piece in some:
                piece.draw()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            i += 1
    if event.type == pygame.MOUSEBUTTONDOWN:
        last_click = event
    if turn == 'white':
        for some in white_pieces:
            for piece in some:
                if piece.black == 0:
                    some.remove(piece)
                if piece.event_handler(last_click):
                    last_click = None
                    clock.tick(30000)
                    print('oops')
                    turn = 'black'
    else:
        for pieces in black_pieces:
            for piece in pieces:
                if piece.black == 0:
                    pieces.remove(piece)
                if piece.event_handler(last_click):
                    last_click = None
                    clock.tick(30000)
                    print('oops')
                    turn = 'white'



    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()
