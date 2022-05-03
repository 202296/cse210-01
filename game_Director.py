from random import randint

class My_action:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        die_number (int): The number of spots on the side facing up.
        one_five_point (int): The value of 1 and 5.
    """

    def __init__(self):

        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """

        self.die_number = 0
        self.one_five_point = 0

    def die_action(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """

        self.die_number = randint(1,6)
        self.one_five_point = 100 if self.die_number == 1 else 50 if self.die_number == 5 else 0

class Director:
    
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        die_list (List[Die]): A list of Die instances.
        engine (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.die_list = []
        for num in range(5):
            action_inst = My_action()
            self.die_list.append(action_inst)
        self.score = 0
        self.total_score = 0
        self.engine = True

    def game_input(self):

        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """


        game_question = input("Roll the Die: (yes/no) ")
        self.engine = (game_question.lower() == "yes")


    def game_update(self):

         
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        
        
        if not self.engine:
            return
        
        for i in range(len(self.die_list)):
            die = self.die_list[i]
            die.die_action()
            self.score += die.one_five_point
        self.total_score += self.score


    def game_display(self):

        """Displays the dice and the score. Also asks the player if they want to roll again. 
        
        Args:
            self (Director): an instance of Director.
        """

        if not self.engine:
            return


        die_value = ""
        for i in range(len(self.die_list)):
            the_die = self.die_list[i]
            die_value += f'{the_die.die_number} '

        print(f"You have played {die_value}")
        print(f"your total score is {self.total_score}\n")
        self.engine == (self.score > 0)

    def play_game(self):

        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.engine:
            self.game_input()
            self.game_update()
            self.game_display()



die = Director()
die.play_game()
