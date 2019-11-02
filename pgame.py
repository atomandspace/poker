import random

#  all the cards houses
clubs=["ca","c2","c3","c4","c5","c6","c7","c8","c9","ct","cj","cq","ck"]
hearts=["ha","h2","h3","h4","h5","h6","h7","h8","h9","ht","hj","hq","hk"]
spades=["sa","s2","s3","s4","s5","s6","s7","s8","s9","st","sj","sq","sk"]
diamonds=["da","d2","d3","d4","d5","d6","d7","d8","d9","dt","dj","dq","dk"]

cardOrder={ 1: "royal_flush", 1: "straight_flush", 2:"four_kind",
3:"full_house",4:"flush", 5:"straight", 6:"three_kind",
7:"two_pair", 8:"pair",9:"high_card"
}
# deck
ordered_deck=clubs+hearts+spades+diamonds
deck=clubs+hearts+spades+diamonds
# shuffle deck
random.shuffle(deck)

# loop exit status
def get_die(status):
    # if instruction not followed
    if status==0:
        print ">> Next time put some money on table! die(0)"
    elif status==1:
        print ">> Follow the instructions! die(1)"
    elif status==2:
        print ">> This player suite doesn't have cards die(2)"
    elif status==3:
        print ">> Check for card combination status die(3)"
    elif status>=3:
        print "No condition met"
        # print ">> get all cards report: die(4)"
    # elif status==5:
    #     print ">> get all cards report: die(5)"
    # elif status==6:
    #     print ">> get all cards report: die(6)"
    # elif status==7:
    #     print ">> get all cards report: die(7)"
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

    for player in range(0,dist_centres):
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
        # print "\nPlayer%d cards: %r" % (player,cards)
        # print "Player%d cardSuite: %r" % (player,player_cardsuites)
        print "Player%d cardValues: %r" % (player,player_cardvalues)

    return

# print the cards on screen for each player in hand
def get_print_cards_inhand(card_distribution,num_players):

    print "\n>> Cards in each Player's hands"

    for player in range(1,num_players+1):
        cards=card_distribution[player]
        player_cardsuites = get_suite_analysis(cards)
        player_cardvalues = get_value_analysis(cards)
        # print "\nPlayer%d cards: %r" % (player-1,cards)
        # print "Player%d cardSuite: %r" % (player-1,player_cardsuites)
        print "Player%d cardValues: %r" % (player-1,player_cardvalues)

    return

# report for cards in hand
def get_players_handcard_report(card_distribution,num_players):
    report=[]
    # separating player hand cards with table cards
    temp=card_distribution[1:-1]

    for contents in temp:
        # print i
        player_cardsuites=get_suite_analysis(contents)
        player_cardvalues=get_value_analysis(contents)
        cards_index=[]
        pair_index=[]
        same_suite=0 # False ,avoiding boolean

        # value analysis
        for i in range(0,13):
            if player_cardvalues[i]==1:
                cards_index.append(i)
            elif player_cardvalues[i]==2:
                pair_index.append(i)
                cards_index.append(i)
                cards_index.append(i)
            else:
                # get_die(5)
                continue

        # suite analysis
        for i in range(0,4):
            if player_cardsuites[i]==2:
                same_suite=1 # True ,avoiding boolean
            else:
                # get_die(6)
                continue

        temp_report=[cards_index,pair_index,same_suite]
        report.append(temp_report)
    return report

# initial analysis for cards in hand+table
def get_players_allcard_report(cards_playerwise,num_players):
    report_index=[]
    report_status=[]

    for contents in cards_playerwise:
        player_cardsuites=get_suite_analysis(contents)
        player_cardvalues=get_value_analysis(contents)

        royal_flush=False
        straight_flush=False
        four_kind=False
        full_house=False
        flush=False
        straight=False
        three_kind=False
        two_pair=False
        pair=False

        straight_flush_index=[]
        four_kind_index=[]
        full_house_index=[]
        flush_index=[]
        straight_index=[]
        three_kind_index=[]
        two_pair_index=[]
        pair_index=[]

        all_cards_index=[] # used for straight and flush determination
        #records index of pair twopair and three kind

        # pair, three kind , fourkind ,straight
        for i in range(0,13):
            # pair (includes pair and two pair)
            if player_cardvalues[i]==2:
                pair_index.append(i)
                pair=True
            # three_ofakind_index
            elif player_cardvalues[i]==3:
                three_kind_index.append(i)
                three_kind=True
            # four_ofakind_index
            elif player_cardvalues[i]==4:
                four_kind_index.append(i)
                four_kind=True
            # all cards index used for straight
            elif player_cardvalues[i]==2 or player_cardvalues[i]==1 or player_cardvalues[i]==3:
                all_cards_index.append(i)
            else:
                # get_die(4)
                continue
# -------------------------------------------------------------
        # flush
        for i in range(0,4):

            if player_cardsuites[i]==5:
                flush=True # True ,avoiding boolean
                flush_index=all_cards_index
                flush_index.sort()
            else:
                continue
#-------------------------------------------------------------
        # two pair availabilty
        # this section is exclusively placed after full house analysis
        # avoid conflicts with current full_house analysis algo
        if len(pair_index)>1:
            pair=False
            two_pair_index=pair_index
            pair_index=[]
            two_pair=True
        elif len(pair_index)==1:
            pair=True
        else:
            pair=False
# -------------------------------------------------------------
        # full house
        if three_kind==True and pair==True:
            pair_index.sort() # highest index for multiple pair
            three_kind_index.sort() # highest index in case of multiple pair
            full_house=True
            full_house_index.append(three_kind_index) # one pair and one one three_kind exist
            full_house_index.append(pair_index)
        elif three_kind==True and two_pair==True:
            three_kind_index.sort() # highest index in case of multiple pair
            two_pair_index.sort()
            full_house_index.append(three_kind_index) # two pair and one one three_kind exist
            full_house_index.append(two_pair_index)
            full_house=True
        else:
            pair_index=pair_index

# ------------------------------------------------------------
        # straight
        if len(all_cards_index)>=5:
            x=all_cards_index
            x.sort()

            if x[0]==8 and x[1]==9 and x[2]==10 and x[3]==11 and x[4]==12:

                if flush==True:
                    royal_flush=True
                else:
                    royal_flush=False

            elif (x[0]+1)==x[1] and (x[1]+1)==x[2] and (x[2]+1)==x[3] and (x[3]+1)==x[4]:

                if flush==True:
                    straight_flush_index=all_cards_index
                    straight_flush=True
                else:
                    straight=True

            else:
                # get_die(6)
                # continue is causing the loop to skip appending reports
                pair_index=pair_index

        else:
            # get_die(7)
            # continue is causing the loop to skip appending reports
            pair_index=pair_index

        temp1=[royal_flush,straight_flush_index,four_kind_index,
        full_house_index,flush_index,straight,
        three_kind_index,two_pair_index, pair_index]

        temp2=[royal_flush,straight_flush,four_kind,full_house,
        flush,straight,three_kind,two_pair,pair]

        report_index.append(temp1)
        report_status.append(temp2)
        # print report
    return report_index, report_status

# table cards analysis
def get_tablecard_report(card_distribution):
    report=[]
    table_cards=card_distribution[0]
    table_cardsuites=get_suite_analysis(table_cards)
    table_cardvalues=get_value_analysis(table_cards)

    royal_flush=False
    straight_flush=False
    four_kind=False
    full_house=False
    flush=False
    straight=False
    three_kind=False
    two_pair=False
    pair=False

    straight_flush_index=[]
    four_kind_index=[]
    full_house_index=[]
    flush_index=[]
    straight_index=[]
    three_kind_index=[]
    two_pair_index=[]
    pair_index=[]

    all_cards_index=[]

    # pair, three kind , fourkind ,straight
    for i in range(0,13):
        # pair (includes pair and two pair)
        if table_cardvalues[i]==2:
            pair_index.append(i)
            pair=True
        # three_ofakind_index
        elif table_cardvalues[i]==3:
            three_kind_index.append(i)
            three_kind=True
        # four_ofakind_index
        elif table_cardvalues[i]==4:
            four_kind_index.append(i)
            four_kind=True
        # all cards index used for straight
        elif table_cardvalues[i]==2 or table_cardvalues[i]==1 or table_cardvalues[i]==3:
            all_cards_index.append(i)
        else:
            # get_die(4)
            continue

    # flush
    for i in range(0,4):

        if table_cardsuites[i]==5:
            flush=True # True ,avoiding boolean
            flush_index=all_cards_index
            flush_index.sort()
        else:
            continue
#-------------------------------------------------------------
    # two pair availabilty
    if len(pair_index)>1:
        pair_available=False
        two_pair_index=pair_index
        pair_index=[]
    elif len(pair_index)==1:
        pair_available=True
    else:
        pair_available=False
#-------------------------------------------------------------

    # full house
    if three_kind==True and pair==True:
        pair_index.sort() # highest index for multiple pair
        three_kind_index.sort() # highest index in case of multiple pair
        full_house_index.append(three_kind_index)
        full_house_index.append(pair_index)
    else:
        # get_die(5)
        # continue is causing the loop to skip appending reports
        pair_index=pair_index
# ------------------------------------------------------------
    # straight
    if len(all_cards_index)>=5:
        x=all_cards_index
        x.sort()

        if x[0]==8 and x[1]==9 and x[2]==10 and x[3]==11 and x[4]==12:

            if flush==True:
                royal_flush=True
            else:
                royal_flush=False

        elif (x[0]+1)==x[1] and (x[1]+1)==x[2] and (x[2]+1)==x[3] and (x[3]+1)==x[4]:

            if flush==True:
                straight_flush_index=all_cards_index
                straight_flush=True
            else:
                straight=True

        else:
            # get_die(6)
            # continue is causing the loop to skip appending reports
            pair_index=pair_index

    else:
        # get_die(7)
        # continue is causing the loop to skip appending reports
        pair_index=pair_index

    report_index=[royal_flush,straight_flush_index,four_kind_index,
    full_house_index,flush_index,straight,three_kind_index,
    two_pair_index, pair_index]

    report_status=[royal_flush,straight_flush,four_kind,full_house,
    flush,straight,three_kind,two_pair,pair]

    return report_index, report_status

# determine the winner
def get_highcard_winner(card_distribution,num_players):

    # in hand card reports
    card_inhand_reports=get_players_handcard_report(card_distribution,num_players)
    # initial_winner=0 # player0
    # print card_inhand_reports
    current_winner=0 # player0
    player0_card_index=card_inhand_reports[0][0]
    player0_card_index.sort()
    player0_pair_index=card_inhand_reports[0][1]
    player0_samesuite_index=card_inhand_reports[0][2]
    # winner iterator
    loop_counter=0

    for card_stat in card_inhand_reports:
        # sorting the cards in increasing order helps in winner determination
        card_stat[0].sort()
        # print "\nHighcard : %r" %(card_stat[0])
        # compare highest index first
        if card_stat[0][1]>player0_card_index[1] or card_stat[0][0]>player0_card_index[0]:
            current_winner=loop_counter
        else:
            continue

        loop_counter=loop_counter+1

    return current_winner

# non high card winner
def get_winner(cards_playerwise,card_distribution,num_players):

    ari,ars=get_players_allcard_report(cards_playerwise,num_players) # all cards report
    tri,trs=get_tablecard_report(card_distribution) # table cards report
    hri=get_players_handcard_report(card_distribution,num_players) # hand card reports
    highcard_winner=get_highcard_winner(card_distribution,num_players)
    #  wps is winning player report_status

    # winner high card winner if it comes to it

    # treat table as a special player with just five cards
    # different function is used for getting report to save computation rss
    # append table reports to the allcard report
    ars_new=ars
    ari_new=ari

    p_sameCard=[]
    which_same_combination=[] # rang(0,9) 9 is high_card and 0 is royal_flush
    wps=ars[highcard_winner] # 0 corresponds to player0
    wp=highcard_winner # wp is winning player 0 corresponds to player0
    winby=9 #winning combination of winner
    # analyzing table cards for winby and wps
    for i in range(0,5):
        if trs[i]==True:
            winby=i
            temp_ars=ars
            temp_ari=ari
            ari.insert(0,tri) # position of players will shift
            ars.insert(0,trs)
            ars_new=ars
            ari_new=ari
            ars=temp_ars
            ari=temp_ari
            wp=0
            wps=trs
            print "table rules"
        else:
            i=i
    p=0 #player counter
    for pr in ars_new:
        print pr
        # status based winner(s)-----------------------------------

        # royal_flush
        if pr[0]==True and winby>=0:
            if wps[0]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(0)
                winby=1
            else:
                wp=p
                winby=0
                wps=ars_new[wp]
        # straight_flush
        elif pr[1]==True and winby>=1:
            if wps[1]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(1)
                winby=1
            else:
                wp=p
                winby=1
                wps=ars_new[wp]
        # four_kind
        elif pr[2]==True and winby>=2:
            if wps[2]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(2)
                winby=2
            else:
                wp=p
                winby=2
                wps=ars_new[wp]
        # full_house
        elif pr[3]==True and winby>=3:
            if wps[3]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(3)
                winby=3
            else:
                wp=p
                winby=3
                wps=ars_new[wp]
        # flush
        elif pr[4]==True and winby>=4:
            if wps[4]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(4)
                winby=4
            else:
                wp=p
                winby=4
                wps=ars_new[wp]
        # straight
        elif pr[5]==True and winby>=5:
            if wps[5]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(5)
                winby=5
            else:
                wp=p
                winby=5
                wps=ars_new[wp]
        # three_kind
        elif pr[6]==True and winby>=6:
            if wps[6]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(6)
                winby=6
            else:
                wp=p
                winby=6
                wps=ars_new[wp]
        # two_pair
        elif pr[7]==True and winby>=7:
            if wps[7]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(7)
                winby=7
            else:
                wp=p
                winby=7
                wps=ars_new[wp]
        # pair
        elif pr[8]==True and winby>=8:
            if wps[8]==True: # +1 as ars inserted with table report
                p_sameCard.append(wp)
                p_sameCard.append(p)
                which_same_combination.append(8)
                winby=8
            else:
                wp=p
                winby=8
                wps=ars_new[wp]
        else:
            # wp=highcard_winner
            # winby=9
            get_die(4)
        # player increment
        print "\np: %d and wp: %d and winby: %d" %(p,wp,winby)
        p=p+1
        # Tie breaker-------------------------------------------
    print "\np_sameCard: %r" %p_sameCard # p_sameCard exists in pairs (1,2)(3,4) etc
    print "ws_comb: %r" % which_same_combination
        # if len(p_sameCard)>0:
            # w
    winner=wp
    return winner, winby #,status

# --------------------------------MAIN LOOP---------------------------------------------

# number of players
num_players=get_num_players()

# Money on the table
money_on_table=get_money_on_table()

# distribute cards
random.shuffle(deck)
card_distribution, card_distribution_all=get_distribute_cards(num_players,deck)
# print card_distribution[0:-1]
cards_playerwise=get_cards_playerwise(card_distribution,num_players)
# print cards_playerwise
# get_print_cards_inhand(card_distribution,num_players)
get_print_cards_inhand_and_table(cards_playerwise,num_players)
print "table: %r" %(get_value_analysis(card_distribution[0]))
# report0=get_players_handcard_report(cards_playerwise,num_players)
# print "%r" %report0

highcard_winner=get_highcard_winner(card_distribution,num_players)
print "High card Winner: Player%r" % highcard_winner

report_index,report_status=get_players_allcard_report(cards_playerwise,num_players)
for i in range(0,len(report_status)):
    print "\nPlayer%d reports: %r" % (i,report_status[i])

# print winner
winner,winby=get_winner(cards_playerwise,card_distribution,num_players)
print "\nPlayer%r WINS by %r"%(winner,cardOrder.get(winby))
