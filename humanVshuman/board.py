class Board:
    def __init__(self, player_x = None, player_o = None):
        self.board = list()
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9']
        ]
        
        self.player = {
            'X': player_x,
            'O': player_o
        }
        
        self.symbol = {
            player_x : 'X',
            player_o : 'O'
        }
        
        self.players = None
        
        self.pos_map = {
            1: '00', 2: '01', 3: '02',
            4: '10', 5: '11', 6: '12',
            7: '20', 8: '21', 9: '22'
        }
        
        self.occupied = list()
        
        self.win_positions = [
            '123',
            '456',
            '789',
            '147',
            '258',
            '369',
            '159',
            '753',
        ]
        self.play()
    
    def get_symbol_at(self, pos):
        coordinate = self.pos_map[int(pos)]
        x = coordinate[0]
        y = coordinate[1]
        return self.board[int(x)][int(y)]
    
    
    def check_win(self):
        if len(self.occupied) == 9:
            return True, None 
        
        for position in self.win_positions:
            cell_1 = self.get_symbol_at(position[0])
            cell_2 = self.get_symbol_at(position[1])
            cell_3 = self.get_symbol_at(position[2])
            
            if cell_1 == cell_2 and cell_1 == cell_3:
                winner = self.player[cell_1]
                return True, winner
        return False, None
    
    
    def display(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board)):
                print( self.board[i][j] + ' |', end='') if j != 2 else print( self.board[i][j] )
            print('-- -- --') if i !=2 else print('\n')
    
    
    def fill(self, pos, inp_symbol):
        coordinates = self.pos_map[pos]
        x = coordinates[0]
        y = coordinates[1]
        self.board[int(x)][int(y)] = inp_symbol
        self.display()
        self.check_win()
        
    def play(self):
        while True:
            player_x = input('Assign a name for player X: ')
            player_o = input('Assign a name for player O: ')
            if len(player_x) == 0 or len(player_o) == 0:
                print('Player name cannot be empty')
            else:
                self.symbol[player_x] = 'X'
                self.symbol[player_o] = 'O'
                self.player['X'] = player_x
                self.player['O'] = player_o
                break
        
        import random
        self.players = [player_x, player_o]
        turn = random.randint(0, 1)
        print('\n' + self.players[turn] + ' has won the toss\n')
        
        self.display()
        
        game_status = self.check_win()
        while game_status[0] is False:
            current_player = self.players[turn]
            input_position = int(input(current_player + ' your turn (' + self.symbol[current_player] + ') : '))
            if input_position in range(1,10) and input_position not in self.occupied:
                self.fill(input_position, self.symbol[current_player])
                self.occupied.append(input_position)
                turn = (turn + 1) % len(self.players)
                game_status = self.check_win()
            else:
                print('\nOOPS: The cell is either already occupied or is invlaid\n')
        
        winner = game_status[1]
        if winner:
            print(winner + ' has won the game')
        else:
            print('Match drawn')
