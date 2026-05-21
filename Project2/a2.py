#!/usr/bin/env python3
"""
Project 2 - Sleeping Coders
"""

import random


class Card:
    """The base card with methods for playing a card and performing a card action.
    Subclasses of Card should override these methods.
    """
    
    def play(self, player, game):
        """
        Called when a player plays a card
        Parameters:
            player (class) -> The player class
            game: a2_support.CodersGame
        """
        
        player_hand = player.get_hand()
        player_cards = player_hand.get_cards()
        Card_position = player_cards.index(self)
        
        player_hand.remove_card(Card_position)
        picked_card = game.pick_card()[0]
        player_hand.add_card(picked_card)
        game.set_action("NO_ACTION")

        
                                         
    def action(self, player, game, slot):
        """
        Called when an action of a special card is performed.
        Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.
        """
        
        pass




    def __str__(self):
        """
        __str__(self) -> str: Returns the string representation of this card, this should be 'Card()
        """
        
        return  f"{self.__class__.__name__}()"
    
    def __repr__(self):
        """
        ___repr__(self): str: same as__str__(self))
        """
        
        return str(self)


    
class NumberCard(Card):
    """
    A card whose aim is to be disposed of by the player.
    A number card has an associated number value.
    """
    
    def __init__(self, number):
        """
        Constructs a new number card
        Parameters:
                number (int): a number value
        """
        
        self._number = number

    def play(self, player, game):
        """
        Called when a player plays a number card
            Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.
                    
        """
        
        super().play(player, game)
        game.next_player()
        

    def action(self, player, game, slot):
        """
        Called when an action of a number card is performed
        Parameters:
            player (class): The player class
            game: a2_support.CodersGame
            slot (int): Position of a card in a list.
        """
        
        super().action(player, game, slot)
        	
    def get_number(self):
        """
        Gets the number of the NumberCard

        get_number(self) -> int: Returns the number value of the card
        """
        
        return self._number

    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return f"NumberCard({self.get_number()})"


    
class TutorCard(Card):
    """
    A card which stores the name of a tutor card
    """
    
    def __init__(self, name):
        """
        Constructs a new Tutor card with a tutor name
        Parameters:
                name(string): An ordered list of Tutors.
        """
        
        self._name = name

    def play(self, player, game):
        """
        Called when a player plays a tutor card
            Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.    
        """
        
        super().play(player, game)
        game.set_action("PICKUP_CODER")
        
        
    def action(self, player, game, slot):
        """
        Called when an action of a tutor card is performed
        Parameters:
            player (class): The player class
            game: a2_support.CodersGame
            slot (int): Position of a card in a list.
        """
        #Gets the list of sleeping coders 
        Coder_card = game.get_sleeping_coder(slot)

        #Adds selected sleeping coder to players hand
        player.get_coders().add_card(Coder_card)

        #Removes sleeping coder from the sleeping coders list
        game.set_sleeping_coder(slot, None)
        
        game.set_action("NO_ACTION")
        game.next_player()
        
    def get_name(self):
        """
        A function to find the name of the tutor card
        returns:
        get_name(self) -> str: Returns the tutor card name
        """
        
        return self._name
    
    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return f"TutorCard({self._name})"

    
class CoderCard(Card):
    """
    A card which stores the name of a coder card.
    """
    
    def __init__(self, name):
        """
        Constructs a new CoderCard with a coder name
        Parameters:
                name(string): An ordered list of name.
        """
        
        self._name = name
        
    def play(self, player, game):
        """
        Called when a player plays a CoderCard
            Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.        
        """
        
        game.set_action("NO_ACTION")

        
    def get_name(self):
        """
        A function to find the name of the coder card
        returns:
        get_name(self) -> str: Returns the coder card name
        """
        
        return self._name

    
    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return f"CoderCard({self.get_name()})"


        
class KeyboardKidnapperCard(Card):
    """
    A card which, when plaeyed, allows the player to steal a coder card from another player
    """

    def play(self, player, game):
        """
        Called when a player plays a KeyboardKidnapperCard
            Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.        
        """
        
        super().play(player, game)
        game.set_action("STEAL_CODER")

    def action(self, player, game, slot):
        """
        Called when an action of a KeyboardKidnapperCard is performed
        Parameters:
            player (class): The player class
            game: a2_support.CodersGame
            slot (int): Position of a card in a list.
        """
        
        player1 = game.current_player()
        
        player2 = game.next_player()
        
        player1_coders = player1.get_coders()

        #locates the coder in player2`s hand at the given slot
        get_coder = player2.get_coders().get_card(slot)

        #Adds the coder to player1`s hand 
        player1_coders.add_card(get_coder)
        
        #reverses the player order in order to remove the card from player2`s hand.
        game.reverse()
        
        player2.get_coders().remove_card(slot)
        
        game.set_action("NO_ACTION")
        
        game.reverse()

        
    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return "KeyboardKidnapperCard({0})".format("")
    
    def __repr__(self):
        """
        ___repr__(self)-> str: same as__str__(self))
        """
        
        return str(self)

    
class AllNighterCard(Card):
    """
    A card which, when played, allows the player to put a coder card from another player back to sellp.
    """
    def play(self, player, game):
        """
        Called when a player plays a AllNighterCard
            Parameters:
                player (class): The player class
                game: a2_support.CodersGame
                slot (int): Position of a card in a list.
                    
        """
        
        super().play(player, game)
        game.set_action("SLEEP_CODER")

    def action(self, player, game, slot):
        """
        Called when an action of a AllNighterCard is performed
        Parameters:
            player (class): The player class
            game: a2_support.CodersGame
            slot (int): Position of a card in a list.
        """
        #Gets the coders in the players hand
        players_coders = player.get_coders()
        
        #Uses the slot to locate the selected coder card.
        get_card_at_slot = players_coders.get_card(slot)
        
        #Gets the list of sleeping coders 
        sleeping_coder_deck = game.get_sleeping_coders()
        
        #Checks for the first empty slot in the sleeping coders list
        for coder_slot, index in enumerate(sleeping_coder_deck):
            # if the slot is empty it adds the coder card to the sleeping coders list at that slot    
            if index == None:
                game.set_sleeping_coder(coder_slot, get_card_at_slot)
                break
            
        #Removes the coder card from the player hand
        players_coders.remove_card(slot)
        
        game.next_player()
        game.set_action("NO_ACTION")

            
    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return "AllNighterCard({0})".format("")
    
    def __repr__(self):
        """
        ___repr__(self)-> str: same as__str__(self))
        """
        
        return str(self)

        
class Deck(object):
    """
    A collection of ordered cards.
    A Deck should have a constructor with a signature of Deck(starting_cards=None)
    """
    
    def __init__(self, starting_cards=None):
        """
        Constructs a new deck of cards
        Parameters:
                starting_cards (None): constructs the deck with an empty list Deck()
        """
        
        if self._cards is None:
            self._cards = []
        self._cards = starting_cards


    def get_cards(self):
        """
        returns:
        get_cards(self) -> List[Card]: Returns a list of cards in the deck
        """
        
        return self._cards
    

    def get_card(self, slot):
        """
        returns:
        get_card(self, slot) -> Card: Return the card at the specified slot in a deck
        """
        
        return self._cards[slot]
    

    def top(self):
        """
        returns:
        top(self) -> Card: Returns the card on the top of the deck, i.e. the last added
        """
        
        return self._cards[-1]
    

    def remove_card(self, slot):
        """
        Removes a card from the given slot in a deck.
        """
        
        self._cards.pop(slot)
    

    def get_amount(self):
        """
        get_amount(self) -> int: Returns the amount of cards in a deck.
        """
        
        return len(self._cards)
    

    def shuffle(self):
        """
        shuffle(self): Shuffles the order of the cards in the deck.
        """
        
        random.shuffle(self._cards)
    

    def pick(self, amount: int= 1):
        """
        pick(self, amount: int=1) -> List[Card]: Takes the first 'amount' of cards off the deck and returns them.
        """
        
        number = 0
        #creates a blank list
        card_List = []
        while number < amount:
            number += 1
            #Adds card to the empty list
            card_List.append(self.top())
            self.remove_card(-1)
        return card_List
            

    def add_card(self, card):
        """Adds a card to the deck.
            Parameter:
                add_card(self, card: Card): Places a card on top of the deck.
        """
        
        self._cards.append([card])
    
    def add_cards(self, cards):
        """
        add_cards(self, cards: List[Card]): Places a list of cards on top of the deck.
        """
        
        self._cards.extend(cards)
    
    def copy(self, other_deck):
        """
        copy(self, other_deck: Deck): Copies all of the cards from the other_deck parameter into the current deck,
        extending the list of cards of the current deck.
        """

        return self.add_cards(other_deck.get_cards())
    
    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        Deck_string = (str(self._cards)).strip('[]')
        return f"Deck({Deck_string})"
    
    def __repr__(self):
        """
        ___repr__(self)-> str: same as__str__(self))
        """
        
        return str(self)
    
class Player(object):
    """
    A player represents one of the games players.
    """
    
    def __init__(self, name):
        """
        Constructs player class
        Parameters:
            name(string): The name of a players.
        
        """
        
        self._name = name
        self._coders = Deck()
        self._deck = Deck()
        
    def get_name(self):
        """
        Returns the name of the player
        returns:
            self._name(string): The name of a players.
        """
        
        return self._name
    
    def get_hand(self):
        """
        Returns the players hand
        returns:
            self._deck (Deck): Returns the players deck of cards
        """
        
        return self._deck
    
    def get_coders(self):
        """
        Returns the players deck of collected coder cards.
        Returns:
            self._coders
        """
        
        return self._coders
    
    def has_won(self):
        """
        Returns True if and only if the player has 4 or more coders.
        Returns:
            True
            False
        """

        return self._coders.get_amount() >= 4


    def __str__(self):
        """
        _str__(self) -> str: Returns the string representation of the NumberCard(number)
        """
        
        return f"Player({self.get_name()}, {self.get_hand()}, {self.get_coders()})"

    def __repr__(self):
        """
        ___repr__(self)-> str: same as__str__(self))
        """

        return str(self)


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
