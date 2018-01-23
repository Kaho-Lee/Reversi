#Zhihao Zhang 1472413 Jiahao Li
# import function
from tkinter import *
import time
# initialzed all the variable
root = Tk()
root.title("Game:Othello")
#initialize the main frame
screen = Canvas(root, width=490, height=640, background="NavajoWhite4",highlightthickness=0)
#initialize all the global varibale
global game_turn
game_turn = 1
global selection_mode
selection_mode = 0

global the_selected_menu
global no_green_chess
no_green_chess = False

"""
0 = no chess
1 = white
-1 = black
game_turn = 1 white go first
game_turn = -1 black go first
0 = None
"""


class chessboard:
    """
    construct a class for chess pieces operation
    initialize chessboard contain a 8x8 array and 8x8 socre borad
    """
    def __init__(self):

        self._whofirst = 1
        self._chessarry = []
        self._scoreboard= []
        """
        [99  -8  8  6  6   8 -8 99]
        [-8 -24 -4 -3 -3 -4 -24 -8]
        [8  -4   7  4  4  7 -4   8]
        [6  -3   4  0  0  4  -3  6]
        [6  -3   4  0  0  4  -3  6]
        [8  -4   7  4  4  7 -4   8]
        [-8 -24 -4 -3 -3 -4 -24 -8]
        [99  -8  8  6  6   8 -8 99]
        http://www.samsoft.org.uk/reversi/strategy.htm#maxdiscs
        """

        self._chessarry = [ [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]]

        # self._chessarry = [ [1,-1,-1,1,1,1,-1,0],
        #                     [1,1,1,1,1,1,-1,0],
        #                     [1,1,1,1,1,1,-1,0],
        #                     [1,1,-1,1,1,1,-1,0],
        #                     [-1,1,1,1,1,1,-1,0],
        #                     [-1,1,-1,1,1,-1,-1,0],
        #                     [1,1,-1,-1,1,-1,-1,0],
        #                     [1,1,-1,-1,1,-1,-1,0]]

        self._scoreboard =[ [99, -8 ,8,6,6,8,-8,99],
                            [-8,-24,-4,-3,-3,-4,-24,-8],
                            [8,-4,7,4,4,7,-4,8],
                            [6,-3,4,0,0,4,-3,6],
                            [6,-3,4,0,0,4,-3,6],
                            [8,-4,7,4,4,7,-4,8],
                            [-8,-24,-4,-3,-3,-4,-24,-8],
                            [99, -8 ,8,6,6,8,-8,99] ]

        self._chessarry[3][3] = 1
        self._chessarry[3][4] = -1
        self._chessarry[4][3] = -1
        self._chessarry[4][4] = 1



    # this fucntion is to draw the grid on the frame
    def drawGrid(self):
        screen.create_line(65,60,65,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(125,60,125,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(185,60,185,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(245,60,245,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(305,60,305,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(365,60,365,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(425,60,425,540,dash = (5, ),fill = "black",width = "3")
        screen.create_line(0,120,490,120,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,180,490,180,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,240,490,240,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,300,490,300,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,360,490,360,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,420,490,420,dash = (5, ),fill= "black",width = "3")
        screen.create_line(0,480,490,480,dash = (5, ),fill= "black",width = "3")
        screen.create_line(10,630,50,590,fill = "NavajoWhite2",width= '3')
        screen.create_line(10,590,50,630,fill = "NavajoWhite2",width= '3')
        screen.create_oval(430,585,485,635,outline = "NavajoWhite2",width = "3")
        screen.create_text(457,610,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = "R")
        screen.create_text(0,0,anchor = "nw",fill = "NavajoWhite2" ,font = ("Helvetica",15),text = "W =",)
        screen.create_text(245,0,anchor = "nw",fill = "NavajoWhite2",font = ("Helvetica",15),text = "B =")
    # this function is update the chess pieces accoefint to the 8x8 chessarry
    # -1:black 1:white 0:none 2:green
    def update_piece(self):
        for x in range(8):
            for y in range(8):
                if self._chessarry[x][y]==1:
                    screen.create_oval(10+60*x,70+60*y,50+60*x,110+60*y,fill="snow",outline="#aaa")
                elif self._chessarry[x][y]==-1:
                    screen.create_oval(10+60*x,70+60*y,50+60*x,110+60*y,fill="black",outline="#222")
                elif self._chessarry[x][y] == 0:
                    screen.create_oval(10+60*x,70+60*y,50+60*x,110+60*y,fill="NavajoWhite4",outline="NavajoWhite4")
                elif self._chessarry[x][y] == 2:
                    screen.create_oval(20+60*x,80+60*y,40+60*x,100+60*y,fill="dark olive green",outline="dark olive green")


    #use this for draiwng chesspiece
    def draw_piece(self,x,y,role):
        self._chessarry[x][y] = role
        self.update_piece()
    #change the pieces without update frame
    def set_piece(self, x, y, role):
        self._chessarry[x][y] = role
    #check the role of selelcted chess pieces
    def check_chess(self, x, y):
        return self._chessarry[x][y]
    #delected chess piece according its position
    def delete_chess(self,x,y):
        self._chessarry[x][y] = 0
        self.update_piece()
    # delete all the green chess
    def delete_green(self):
        for x in range(8):
            for y in range(8):
                if self.check_chess(x, y) == 2:
                    self.delete_chess(x, y)
    # return the chess_array
    def get_chessarry(self):
        return self._chessarry
    # return the number of black ans white chess pieces
    def check_bw(self):
        count_white = 0
        count_black = 0
        for i in range(8):
            for j in range(8):
                if self._chessarry[i][j] == 1:
                    count_white += 1
                elif self._chessarry[i][j] == -1:
                    count_black += 1
        status = list()
        count_white = str(count_white)
        count_black = str(count_black)
        status.append(count_white)
        status.append(count_black)
        screen.create_rectangle(30,0,60,20,fill = "NavajoWhite4",outline = "NavajoWhite4")
        screen.create_rectangle(270,0,305,20,fill = "NavajoWhite4", outline = "NavajoWhite4")
        screen.create_text(35,0,anchor="nw",fill= "NavajoWhite2",font = ("Helvetica",15),text = count_white)
        screen.create_text(275,0,anchor="nw", fill = "NavajoWhite2",font = ("Helvetica",15),text = count_black)
        return status

    def score(self, role):
        """
        Accoring to the score board, this function will return evaluation score based on chess arragnement and its color
        """
        white_score = 0
        black_score = 0
        # print(self.get_chessarry())
        for i in range(8):
            for j in range(8):
                if a._chessarry[i][j] == 1:
                        white_score += self._scoreboard[i][j]

                elif a._chessarry[i][j] == -1:
                        black_score += self._scoreboard[i][j]
        if role == -1:
            return black_score
        elif role == 1:
            return white_score
    #If there is no place that can be placed a chess, terminate the game.
    def terminate_game(self,role):

        end_list = []
        end_list = self.potential_list(role)

        if len(end_list) == 0:
            return True
        return False

    #Find the potential place that can be placed a chess
    def potential_list(self, role):


        neighbour_opponent = []
        potential_position_list = []
        #finding the position where there is an opponent chess
        for x in range(0,8):
            for y in range(0,8):
                if self.check_chess(x, y) == role:
                    #The reason why I set the range of 'x' and 'y' is that the checked position cannot be beyond the edge.
                    for x_index in range(max(x-1,0),min(x+2, 8)):
                        for y_index in range(max(y-1, 0), min(y+2, 8)):
                            condition = self.check_chess(x_index, y_index)
                            if condition != role and condition != 0 and condition != 2:
                                neighbour_opponent.append([x_index, y_index])
                    #check the line where there're an opponent chess and our chess
                    for enemy in neighbour_opponent:
                        neig_x, neig_y = [enemy[0],enemy[1]]
                        displace_x = neig_x -x
                        displace_y = neig_y -y
                        potential_x = neig_x + displace_x
                        potential_y = neig_y + displace_y
                        while 0<=potential_x<=7 and 0<=potential_y<=7:
                            #if there is a blank space, that position can be placed a chess, white or black. Then break the loop.
                            if self.check_chess(potential_x, potential_y) == 0:
                                potential_position_list.append([potential_x, potential_y])
                                break
                            #if there's an oppponent chess, continuing to check the same line.
                            elif self.check_chess(potential_x, potential_y) != role and self.check_chess(potential_x, potential_y) !=2:
                                potential_x += displace_x
                                potential_y += displace_y
                            #if there is our chess or the position has already been made as a place, breaking the loop.
                            elif self.check_chess(potential_x, potential_y)==2 or self.check_chess(potential_x, potential_y)==role:
                                break
                    neighbour_opponent = []
        return potential_position_list


def man_vs_man(x_chess_cor,y_chess_cor):
    """
    Man vs man mode
    Input : the mouse coordinate
    """
    global game_turn

    if x_chess_cor >= 0 and x_chess_cor <= 7 and y_chess_cor>=0 and y_chess_cor<=7:
        if a.check_chess(x_chess_cor,y_chess_cor) == 2:
            #make sure the mouse can give valid coordinate for place a chess pieces
            if game_turn == 1:
                # white turn
                a.draw_piece(x_chess_cor,y_chess_cor,1)
                a.delete_green()
                flip_the_chess(a, x_chess_cor, y_chess_cor, 1)
                game_turn = -1
                win_or_not(game_turn)
                # check the either white or black win
                potential_position(a,game_turn)

            elif game_turn == -1:
                # black turn
                a.draw_piece(x_chess_cor,y_chess_cor,-1)
                a.delete_green()
                flip_the_chess(a, x_chess_cor, y_chess_cor, -1)
                game_turn = 1
                win_or_not(game_turn)
                # check the either white or black win
                potential_position(a,game_turn)

        else:
            print("not valid")
    else:
        print("not valid")

def man_vs_com(x_chess_cor,y_chess_cor):
    """
    man vs com mode
    input: the mouse coordinate
    """
    global game_turn
    global rrest
    if game_turn == 1:
        if x_chess_cor >= 0 and x_chess_cor <= 7 and y_chess_cor>=0 and y_chess_cor<=7:
            if a.check_chess(x_chess_cor,y_chess_cor) == 2:
                a.draw_piece(x_chess_cor,y_chess_cor,1)
                a.delete_green()
                flip_the_chess(a, x_chess_cor, y_chess_cor, 1)
                game_turn = -1
                win_or_not(game_turn)

        else:
            print("not valid")

    if game_turn == -1:
        # black turn
        com_place_chess()
        # pass into the com_play_chess funtion
        a.delete_green()
        game_turn = 1
        win_or_not(game_turn)
        # print('flip turn')
        potential_position(a,game_turn)

    else:
        print("not valid")



def win_or_not(game_turn):
    """
    check either black or white iwin the game
    Input game turn
    """
    #initialze the global variable
    global no_green_chess
    global selection_mode
    global the_selected_menu
    no_green_chess = a.terminate_game(game_turn)
    #check whether the game can continue or not
    #return True if game stop
    #return false if game continue
    # print("no_green_chess",no_green_chess)
    if no_green_chess:
        #if game stop
        selection_mode = 2
        status = a.check_bw()
        #return the status
        if status[0]<status[1]:
            print("black win")
            export_text()
            screen.create_rectangle(125,590,380,640,fill = "NavajoWhite4",outline = "NavajoWhite4")
            screen.create_text(190,590,anchor = "nw",fill = "NavajoWhite2",font = (25),text = "Black win!!")

        elif status[0]>status[1]:
            print("white win")
            export_text()
            screen.create_rectangle(125,590,380,640,fill = "NavajoWhite4",outline = "NavajoWhite4")
            screen.create_text(190,590,anchor = "nw",fill = "NavajoWhite2",font = (25),text = "White win!!")
        else:
            print("Draw")
            export_text()
            screen.create_rectangle(125,590,380,640,fill = "NavajoWhite4",outline = "NavajoWhite4")
            screen.create_text(210,590,anchor = "nw",fill = "NavajoWhite2",font = (25),text = "Draw!!")
        dis_his()


def mouse(event):
    """
    bonding with the left mouse click and keep looping
    """
    #initialzed all the variable
    global selection_mode
    global the_selected_menu
    global game_turn
    # the coordinate into te frame
    x = event.x
    y = event.y
    # print(x,y)

    if x>=10 and x<=65 and y >= 592 and y<=639:
        # if the coordinate into the the cross then terminate the game
        root.destroy()
    if x>= 430 and y >=596 and x <=490 and y < 640:
        # if the coordinate into the reset then reset the game
        screen.delete("all")
        a._chessarry = [ [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,1,-1,0,0,0],
                            [0,0,0,-1,1,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]]
        print("reset")

        selection_mode = 0
        game_turn = 1
        menu_start_control(x,y)
    # convert the coordiante into the the chess board coordiante
    x_chess_cor = x//60
    y_chess_cor = (y-65)//60

    # main control for the game
    if selection_mode ==0:
        the_selected_menu = menu_start_control(x,y)
    if the_selected_menu == 1:
        start_game()
        man_vs_man(x_chess_cor,y_chess_cor)
        print("status",a.check_bw())
    if the_selected_menu== 2:
        start_game()
        man_vs_com(x_chess_cor,y_chess_cor)
        print("status",a.check_bw())
    if the_selected_menu == 3:
        History_dis()
        dis_his()



def dis_his():
    '''
    calculating the the rate of winning of the previous game history from a text file.
    '''
    f = open("game_history.txt","r")
    content = f.readlines()
    print(content)
    content_list = []
    for item in content:
        item_list = item.strip().split()
        content_list.append(item_list)
    print(content_list)
    #making a list of counters.
    man_vs_man_num = 0
    man_vs_man_b = 0
    man_vs_man_w = 0
    man_vs_com_num = 0
    man_vs_com_b = 0
    man_vs_com_w = 0
    #calculating the total number of game and the the number of winning for each role under different game mode.
    for item in content_list:
        if 'man_vs_man' in item:
            man_vs_man_num += 1
            if 'white_win' in item:
                man_vs_man_w+= 1
            elif 'black_win' in item:
                man_vs_man_b += 1
            print('man_vs_man', man_vs_man_num, man_vs_man_b, man_vs_man_w)
        elif 'man_vs_com' in item:
            man_vs_com_num += 1
            if 'white_win' in item:
                man_vs_com_w += 1
            elif 'black_win' in item:
                man_vs_com_b += 1
            print('man_vs_com', man_vs_com_num, man_vs_com_b, man_vs_com_w)
    #calculating the rate of winning
    man_vs_man_b_rate = 0
    man_vs_man_w_rate = 0
    man_vs_com_w_rate = 0
    if man_vs_man_num > 0:
        man_vs_man_b_rate = man_vs_man_b/man_vs_man_num
        man_vs_man_w_rate = man_vs_man_w/man_vs_man_num
    if man_vs_com_num >0:
        man_vs_com_w_rate = man_vs_com_w/man_vs_com_num
    print(man_vs_man_w_rate,man_vs_man_b_rate,man_vs_com_w_rate)
    return [int(man_vs_man_w_rate*100), int(man_vs_man_b_rate*100), int(man_vs_com_w_rate*100)]

def flip_the_chess(board, x, y, role):
    '''
    After placing a chess, searching the whole board to flip opponent's chesses.
    INput arguments:
    board: the current chess board
    x: the x coordinate where you place a chess
    y: the y coordinate where you place a chess
    role: the current game turn. '-1' is white chess and '1' is black chess
    '''
    current_board = board
    #deleting the tag on those positions where can be placed a chess.
    for i in range(0,8):
        for j in range(0,8):
            if current_board.check_chess(i, j) == 2:
                a.draw_piece(i, j, 0)
    neighbour_opponent=[]

    #If there is an opponent chess on the neighbour position, put it into a list
    for x_index in range(max(x-1,0),min(x+2, 8)):
        for y_index in range(max(y-1, 0), min(y+2, 8)):
            # print('neig', x_index, y_index)
            if current_board.check_chess(x_index, y_index) != role and current_board.check_chess(x_index, y_index) != 0:
                neighbour_opponent.append([x_index,y_index])
    # print('neighbour_opponent', neighbour_opponent)

    #trace the 'flip' line
    flip_coor =[]
    for enemy in neighbour_opponent:
        flip = False
        neig_x, neig_y = [enemy[0],enemy[1]]
        flip_coor.append([neig_x, neig_y])
        displace_x = neig_x -x
        displace_y = neig_y -y
        tem_x = neig_x + displace_x
        tem_y = neig_y + displace_y
        while 0<=tem_x<=7 and 0<=tem_y<=7:
            if current_board.check_chess(tem_x, tem_y)!= role and current_board.check_chess(x, y) !=0:
                flip_coor.append([tem_x, tem_y])
                tem_x += displace_x
                tem_y += displace_y
            elif current_board.check_chess(tem_x, tem_y) == role:
                flip = True
                break
            elif current_board.check_chess(tem_x, tem_y) == 0:
                flip_coor = []
                break
        # print('flip_coor', flip_coor)
        if flip == True:
            for coor in flip_coor:
                x_chess_cor, y_chess_cor = [coor[0], coor[1]]
                a.draw_piece(x_chess_cor,y_chess_cor,role)
        flip_coor = []


def potential_position(board, role):
    '''
    placing a tag on the place where can be placed a chess
    Input arguments:
    board: the current chess board
    role: the current game turn
    '''
    current_board = board
    neighbour_opponent=[]
    neighbour_opponent = a.potential_list(role)
    for enemy in neighbour_opponent:
        a.draw_piece(enemy[0],enemy[1], 2)


def minmax(board, depth, max_score, min_score, role):
    '''
    The min-max algorithm with alpha-beta purning.
    Computer is using black chess, game_turn '-1'.
    Input arguments:
    board: the chess board which wuould be analyzed by this algorithm
    depth: the recurrsion time we want
    max_score: the current max score used in alpha-beta purning
    min_score: the current min score used in alpha-beta purning
    role: the simulated game turn

    return:
    score: the score of a leaf in a minmax tree.
    The score cannnot be larger than the input max_score and smalller than the min_score because of the alpha-beta algorithm
    '''

    input_board = chessboard()
    tem_list = list()
    tem_kist = a.get_chessarry()

    input_board.chessarry = tem_list
    #if the depth is 0 or the the game is supposed to be terminated, return a value from the scoreboard.
    if depth == 0 or input_board.terminate_game(role):
        return input_board.score(role)

    #for black chess. AI's turn. Find the max
    elif role == -1:
        best_child = []
        score = min_score
        #get the potential position where computer can place a chess
        child_node = input_board.potential_list(-1)
        for child in child_node:
            input_board.set_piece(child[0], child[1], -1)
            tem_score = minmax(input_board, depth - 1, max_score, score, 1)
            if tem_score > score:
                score = tem_score
                best_child = [child[0], child[1]]
            input_board.delete_chess(child[0], child[1])
            if score > max_score:
                return max_score
        # input_board.draw_piece(best_child[0], best_child[1], -1)
        return score

    #for white chess. User's turn. Find the min
    elif role == 1:
        best_child = []
        score = max_score
        #get the potential position where user can place a chess
        child_node = input_board.potential_list(1)

        for child in child_node:
            input_board.set_piece(child[0], child[1], 1)
            tem_score = minmax(input_board, depth - 1, score, min_score, -1)
            if tem_score < score:
                score = tem_score
                best_child = [child[0], child[1]]
            input_board.delete_chess(child[0], child[1])
            if score < min_score:
                return min_score
        # input_board.draw_piece(best_child[0], best_child[1], -1)
        return score

def com_place_chess():#black find the max
    '''
    For the man_vs_com game mode, this function can be regrded as placing a chess by computer
    '''
    input_board = chessboard()
    tem_list = list()
    tem_list = a.get_chessarry()
    # print("tem_list:",tem_list)
    input_board._chessarry = tem_list

    child_node = input_board.potential_list(-1)

    score = 0 - float('inf')
    best_child = []
    max_score = float('inf')
    min_score = 0 - float('inf')
    #searching the places where computer can place a chess to find the best position to place a chess
    for child in child_node:
        input_board.set_piece(child[0], child[1], -1)
        tem_score = minmax(input_board, 1, max_score, min_score, 1)
        if tem_score > score:
            score = tem_score
            best_child = child
        input_board.delete_chess(child[0], child[1])


    a.draw_piece(best_child[0], best_child[1], -1)
    flip_the_chess(a, best_child[0], best_child[1], -1)

def export_text():
    '''
    When a game is end, export the information of this game to a text file.
    '''
    status = a.check_bw()
    global the_selected_menu
    #creating a string list to record the game information
    if the_selected_menu == 1:
        game_mode = ["man_vs_man", 'w=']
        game_mode.append(status[0])
        game_mode.append('b=')
        game_mode.append(status[1])
        if status[0] > status[1]:
            game_mode.append('white_win\n')
        elif status[0] < status[1]:
            game_mode.append('black_win\n')
        else:
            game_mode.append('draw\n')

    elif the_selected_menu == 2:
        game_mode = ["man_vs_com", 'w=']
        game_mode.append(status[0])
        game_mode.append('b=')
        game_mode.append(status[1])
        if status[0] > status[1]:
            game_mode.append('white_win\n')
        elif status[0] < status[1]:
            game_mode.append('black_win\n')
        else:
            game_mode.append('draw\n')

    #converting the string list to one string, then write that string to the text file
    out_string = ' '.join(game_mode)
    print(out_string)
    f = open('game_history.txt','a')
    f.write("{}".format(out_string))
    f.close()

def start_game():
    # start game
    a.drawGrid()
    potential_position(a,1)
    a.update_piece()

def menu_start():
    # GUI for the main menu
    screen.create_rectangle(0,0,485,18,fill = "NavajoWhite4",outline = "NavajoWhite4")
    screen.create_text(80,180,anchor = "nw",fill = "NavajoWhite2" ,font = ("Helvetica",35),text = "Othello/Reversi")
    screen.create_rectangle(175,250,330,295,fill = "orange3",outline = "orange3")
    screen.create_text(180,250,anchor = "nw", fill = "NavajoWhite2",font = ("Helvetica",18),text = "Man V.S Man")
    screen.create_rectangle(175,300,330,345,fill = "orange3",outline = "orange3")
    screen.create_text(180,300,anchor = "nw" , fill = "NavajoWhite2",font = ("Helvetica",18),text = "Man V.S Com")
    screen.create_rectangle(175,350,330,395,fill = "orange3",outline = "orange3")
    screen.create_text(180,350,anchor = "nw",fill="NavajoWhite2",font =("Helvetica",18),text = "Game History")
    screen.create_line(10,630,50,590,fill = "NavajoWhite2",width= '3')
    screen.create_line(10,590,50,630,fill = "NavajoWhite2",width= '3')
    screen.create_oval(430,585,485,635,outline = "NavajoWhite2",width = "3")
    screen.create_text(457,610,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = "R")

def History_dis():
    # display the rusult on the frame
    Hist = dis_his()
    print(Hist)
    screen.create_line(10,630,50,590,fill = "NavajoWhite2",width= '3')
    screen.create_line(10,590,50,630,fill = "NavajoWhite2",width= '3')
    screen.create_oval(430,585,485,635,outline = "NavajoWhite2",width = "3")
    screen.create_text(457,610,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = "R")

    screen.create_text(240,190,anchor = "center", fill= "NavajoWhite2",font = ("Helvetica",20),text = "man_vs_man_w_rate")
    screen.create_text(240,220,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = (Hist[0],"%"))
    screen.create_text(240,260,anchor = "center", fill= "NavajoWhite2",font = ("Helvetica",20),text = "man_vs_man_b_rate")
    screen.create_text(240,290,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = (Hist[1],"%"))
    screen.create_text(240,330,anchor = "center", fill= "NavajoWhite2",font = ("Helvetica",20),text = "man_vs_com_w_rate")
    screen.create_text(240,360,anchor = "center",fill = "NavajoWhite2",font = ("Helvetica",20),text = (Hist[2],"%"))

def menu_start_control(x,y):
    """
    control flow for menu selection
    Input: mouse coordinate
    """
    menu_start()
    global selection_mode
    if selection_mode == 0:
        if x>=178 and y >=250 and x<=330 and y <=295:
            #man vs man
            screen.delete("all")
            selection_mode = 1
            return 1
        if x>178 and y >= 300 and x<330 and y <345:
            # man vs Com
            screen.delete("all")
            selection_mode = 1
            return 2
        if x>178 and y>350 and x <330 and y <395:
            # Game History
            screen.delete("all")
            selection_mode = 1
            print("the_selected_menu = 3")
            return 3

a = chessboard()
menu_start()
screen.bind("<Button-1>",mouse)
screen.pack()
root.mainloop()
