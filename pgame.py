import random

#  all the cards houses
clubs=["ca","c2","c3","c4","c5","c6","c7","c8","c9","ct","cj","cq","ck"]
hearts=["ha","h2","h3","h4","h5","h6","h7","h8","h9","ht","hj","hq","hk"]
spades=["sa","s2","s3","s4","s5","s6","s7","s8","s9","st","sj","sq","sk"]
diamonds=["da","d2","d3","d4","d5","d6","d7","d8","d9","dt","dj","dq","dk"]

# deck
ordered_deck=clubs+hearts+spades+diamonds
deck=clubs+hearts+spades+diamonds
# shuffle deck
random.shuffle(deck)

# loop exit status
def get_die(status):
    # if instruction not followed
    if status==0:
        print ">> Next time put some money on table!"
    elif status==1:
        print ">> Follow the instructions!"
    elif status==2:
        print ">> This player suite doesn't have cards"
    elif status==3:
        print ">> Check for card combination status"
    else:
        print ">> Good bye!"

# get money on the table
def get_money_on_table():

    money_on_table=int(raw_input("<< How much money on the table?\n"))

    if money_on_table <0:
        print ">> Begger!"
        die(0)
    elif money_on_table==0:
        print ">> I see you are not interested"
        die(0)
    else:
        print ">> Each person begins with %s" % money_on_table
        print ">> All the best"

    return money_on_table

# get number of num_players
def get_num_players():
    num_players=int(raw_input("<< Number of players?\n"))

    if num_players==0:
        print ">> Looks like no one is available to play."
    elif num_players==1:
        print ">> Player 1 takes all money home!"
    elif num_players >=2 and num_players <5:
        print ">> Fun begins"
    elif num_players >=5:
        print ">> We don't have a table for more than five Players."
        print ">> Setting number of players to five."
        num_players=5
    else:
        print ">> Uh oh! something went wrong"

    return num_players

# distribute cards functions
def get_distribute_cards(num_players,deck):
    # table + num_players
    dist_centres=num_players+1
    table_cards=deck[0:5]
    card_index_players=6
    # card_distribution=[[table][player1]...[playern]]
    card_distribution=[]
    card_distribution.append(table_cards)
    card_distribution_all=[]
    card_distribution_all=table_cards

    for player in range(0,num_players):
        player_cards=deck[card_index_players:card_index_players+2]
        card_distribution.append(player_cards)
        card_distribution_all=card_distribution_all+player_cards
        card_index_players=card_index_players+3

    return card_distribution, card_distribution_all

# card identifier function
# card pattern is suiteNameNumber ex "cq means <clubs queen>"
def get_card_identifier(card):
    card_id=[]

    for ch in card:
        card_id.append(ch)

    return card_id

# arrange the cards on table and cards with a player
def get_cards_playerwise(card_distribution,num_players):
    table_cards=card_distribution[0]
    player_cards=card_distribution[1:num_players+1]
    cards_playerwise=[]
    for list in player_cards:
        cards_playerwise.append(table_cards+list)
    return cards_playerwise

# what cards does a player have?
def get_cards_of_nth_player(cards_playerwise,playerNumber):
    # player1 means player0
    players_cards=cards_playerwise[playerNumber-1]
    return players_cards

# get suite and values of input cards
def get_suite_and_value(player_cards):
    suite_player_cards=[]
    value_player_cards=[]
    for cards in player_cards:
        card_id=get_card_identifier(cards)
        suite_player_cards.append(card_id[0])
        value_player_cards.append(card_id[1])
    return suite_player_cards, value_player_cards

# define the suites available in given cards
def get_suite_analysis(cards):

    # card suites clubs+diamonds+hearts+spades
    card_suites=[0,0,0,0]
    suite_player_cards, value_player_cards=get_suite_and_value(cards)

    for suite in suite_player_cards:

        if suite=="c":
            card_suites[0]=card_suites[0]+1
        elif suite=="d":
            card_suites[1]=card_suites[1]+1
        elif suite=="h":
            card_suites[2]=card_suites[2]+1
        elif suite=="s":
            card_suites[3]=card_suites[3]+1
        else:
            die(2)
            # suite doesn't have cards

    return card_suites

# numerical analysis of the cards
def get_value_analysis(cards):

    card_values=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    # values starts with twos ends with aces
    suite_player_cards, value_player_cards=get_suite_and_value(cards)
    for value in value_player_cards:
        if value=="2":
            card_values[0]=card_values[0]+1
        elif value=="3":
            card_values[1]=card_values[1]+1
        elif value=="4":
            card_values[2]=card_values[2]+1
        elif value=="5":
            card_values[3]=card_values[3]+1
        elif value=="6":
            card_values[4]=card_values[4]+1
        elif value=="7":
            card_values[5]=card_values[5]+1
        elif value=="8":
            card_values[6]=card_values[6]+1
        elif value=="9":
            card_values[7]=card_values[7]+1
        elif value=="t":
            card_values[8]=card_values[8]+1
        elif value=="j":
            card_values[9]=card_values[9]+1
        elif value=="q":
            card_values[10]=card_values[10]+1
        elif value=="k":
            card_values[11]=card_values[11]+1
        elif value=="a":
            card_values[12]=card_values[12]+1
        else:
            die(2)
            # this player doesn't have cards
    # card_values (twos,threes,fours,fives,sixes,sevens,eights,tens,jacks,queens,kings,aces)
    return card_values

# print the cards on screen for each player (hand+table)
def get_print_cards_inhand_and_table(cards_playerwise,num_players):

    print "\n>> Possibilty of the cards for the Players"

    for player in range(0,num_players):
        cards=cards_playerwise[player]
        player_cardsuites = get_suite_analysis(cards)
        player_cardvalues = get_value_analysis(cards)
        print "\nPlayer%d cards: %r" % (player,cards)
        print "Player%d cardSuite: %r" % (player,player_cardsuites)
        print "Player%d cardValues: %r" % (player,player_cardvalues)

    return

# print the cards on screen for each player in hand
def get_print_cards_inhand(card_distribution,num_players):

    print "\n>> Cards in each Player's hands"

    for player in range(1,num_players+1):
        cards=card_distribution[player]
        player_cardsuites = get_suite_analysis(cards)
        player_cardvalues = get_value_analysis(cards)
        print "\nPlayer%d cards: %r" % (player,cards)
        print "Player%d cardSuite: %r" % (player,player_cardsuites)
        print "Player%d cardValues: %r" % (player,player_cardvalues)

    return

# determine the winner
def get_winner(cards_playerwise,num_players):
    player_cardsuites=[]
    player_cardvalues=[]
    player_cardvalues_diff =[0,0,0,0,0,0,0,0,0,0,0,0,0]
    players_cards_index=[]
    card_diff_list=[]

    # get all the suites and cards at one place
    for player in range(0,num_players):
        player_cardsuites.append(get_suite_analysis(cards_playerwise[player]))
        player_cardvalues.append(get_value_analysis(cards_playerwise[player])

    # get the card values difference
    for i in range(0,num_players-1):
        for j in range(0,13):
            # first player is the base for difference
            player_cardvalues_diff[j]=cards_playerwise[i+1][j]-cards_playerwise[0][j]

            # if the comparison doesn't have the cards as player1
            if player_cardvalues_diff[j]<0:
                negative_index=j
            elif player_cardvalues_diff[j]==1:
                positve_index=j
            else:
                get_die(3)
                # check for card combination conditions
        card_diff_list.append(player_cardvalues_diff)

# possible_cominations=["flush","pairs","straight","high_card"]
#
#     # if the card combination is a flush
#     if clubs>0 and diamonds>0 and hearts>0 and spades>0:
#         possible_cominations=["not_flush"]
#     elif clubs>=5 or diamonds>=5 or hearts>=5 or spades>=5:
#         possible_cominations=["flush"]
#         # is it royal flush


    # royal flush
    # straight flush
    # 4 of a kind
    # full house
    # flush
    # straight
    # 3 of a kind
    # 2 pair
    # 1 pair
    # high card

# --------------------------------MAIN LOOP---------------------------------------------

# number of players
num_players=get_num_players()

# Money on the table
money_on_table=get_money_on_table()

# distribute cards
random.shuffle(deck)
card_distribution, card_distribution_all=get_distribute_cards(num_players,deck)
cards_playerwise=get_cards_playerwise(card_distribution,num_players)
get_print_cards_inhand(card_distribution,num_players)
get_print_cards_inhand_and_table(cards_playerwise,num_players)

# who wins
