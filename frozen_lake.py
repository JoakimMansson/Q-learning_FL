import copy
import random

#Rewards
#Reach goal(G): +1

#Reach hole(H): -1

#Reach frozen(F): 0


class FrozenLake():


    def __init__(self) -> None:
        self.board = [
            ["S", "F", "F"],
            ["F", "H", "F"],
            ["F", "H", "F"],
            ["F", "F", "G"],
        ]

        self.copy_board = copy.deepcopy(self.board)

        #[y][x]
        self.position_x = 0
        self.position_y = 0

        # [[y,x], [y,x]]
        self.position_holes = []


        self.position_goal_y, self.position_goal_x = self.__find_goal()
        self.__find_holes()
        
        
        print("START BOARD")
        self.print_board()

    def __find_goal(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == "G":
                    return y, x


    def __find_holes(self):
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == "H":
                    self.position_holes.append([y,x])


    def get_current_state(self):
        # F F S <- state = 3
        # F H F
        # F H F
        # F F G
        size_y = len(self.board)
        size_x = len(self.board[0])
        for y in range(size_y):
            for x in range(size_x):
                if self.board[y][x] == "S":
                    if x == 0:
                        current_state = x
                    else:
                        current_state = y*size_x + x
                    
                    return current_state



    def print_board(self):
        print("------------------------")
        for i in range(len(self.board)):
            row_x = ""
            for j in range(len(self.board[0])):
                row_x += self.board[i][j]

            print(row_x)

    def __check_is_hole(self):
        for hole in self.position_holes:
            if hole[0] == self.position_y and hole[1] == self.position_x:
                return True
        return False

    
    def __is_out_of_bound(self, position_x, position_y):
        if (0 <= position_y and position_y < len(self.board)) and (0 <= position_x and position_x < len(self.board[0])):
            return False
        return True

    def __reset_position(self):
        for y in range(len(self.copy_board)):
            for x in range(len(self.copy_board[0])):
                if self.copy_board[y][x] == "S":
                    self.position_x = x
                    self.position_y = y
                    return


    def reset_board(self):
        self.board = copy.deepcopy(self.copy_board)
        self.__reset_position()
    

    def get_dimensions_board(self):
        y = len(self.board)
        x = len(self.board[0])
        return y, x


    # This function handles the reward output
    # Standard reward returns
    # win: 1
    # frozen: 0
    # hole: - 1
    def __check_rewards(self):
        if self.position_x == self.position_goal_x and self.position_y == self.position_goal_y:
            self.reset_board()
            print("YOU WON!!")
            return 1
        elif self.__check_is_hole():
            print("YOU HIT A HOLE!")
            return 0
        else:
            return 0

    def __update_x(self, new_position_x):
        self.position_x = new_position_x

    def __update_y(self, new_position_y):
        self.position_y = new_position_y


    # 0 = right
    # 1 = left
    # 2 = up
    # 3 = down
    def make_move_index(self, move_index):
        if move_index == 0:
            return self.go_right()
        if move_index == 1:
            return self.go_left()
        if move_index == 2:
            return self.go_up()
        if move_index == 3:
            return self.go_down()


    def go_left(self):
        temp_pos_x = self.position_x - 1
        if not self.__is_out_of_bound(temp_pos_x, self.position_y):
            self.board[self.position_y][temp_pos_x], self.board[self.position_y][self.position_x] = self.board[self.position_y][self.position_x], self.board[self.position_y][temp_pos_x]
            self.__update_x(temp_pos_x)
            
        #self.print_board()
        return self.get_current_state(), self.__check_rewards()


    def go_right(self):
        temp_pos_x = self.position_x + 1

        if not self.__is_out_of_bound(temp_pos_x, self.position_y):
            
            self.board[self.position_y][temp_pos_x], self.board[self.position_y][self.position_x] = self.board[self.position_y][self.position_x], self.board[self.position_y][temp_pos_x]
            self.__update_x(temp_pos_x)
        
        #self.print_board()
        return self.get_current_state(), self.__check_rewards()
        

    def go_up(self):
        temp_pos_y = self.position_y - 1
        if not self.__is_out_of_bound(self.position_x, temp_pos_y):
            self.board[temp_pos_y][self.position_x], self.board[self.position_y][self.position_x] = self.board[self.position_y][self.position_x], self.board[temp_pos_y][self.position_x]
            self.__update_y(temp_pos_y)

        #self.print_board()
        return self.get_current_state(), self.__check_rewards()


    def go_down(self):
        temp_pos_y = self.position_y + 1
        if not self.__is_out_of_bound(self.position_x, temp_pos_y):
            self.board[temp_pos_y][self.position_x], self.board[self.position_y][self.position_x] = self.board[self.position_y][self.position_x], self.board[temp_pos_y][self.position_x]
            self.__update_y(temp_pos_y)
        
        #self.print_board()
        return self.get_current_state(), self.__check_rewards()




def main():
    lake_game = FrozenLake()
    state, reward = lake_game.make_move_index(0)
    state, reward = lake_game.make_move_index(3)
    state, reward = lake_game.make_move_index(3)

    state, reward = lake_game.make_move_index(3)
    
    state, reward = lake_game.make_move_index(0)
   
    print(state, reward)
    lake_game.print_board()



if __name__ == "__main__":
    main()
