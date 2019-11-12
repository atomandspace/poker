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
    print "get_die(%d)" %status

# get money on the table
def get_money_on_table():

    money_on_table=int(raw_input("<< How much money on the table?\n"))

    if money_on_table >0:
        print ">> Each person begins with %s" % money_on_table
        print ">> All the best"
    elif money_on_table==0:
        print ">> You have to invest atleast something."
    else:
        get_die(0)

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
        get_die(1)

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
            get_die(2)
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
            get_die(3)
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
            elif player_cardvalues[i]==0:
                i=i
            else:
                get_die(4)

        # suite analysis
        for i in range(0,4):
            if player_cardsuites[i]==2:
                same_suite=1 # True ,avoiding boolean
            else:
                # get_die(5)
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

        royal_flush_index=[]
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
                three_kind_index=i
                three_kind=True
            # four_ofakind_index
            elif player_cardvalues[i]==4:
                four_kind_index=i
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
            # print "%dpl>> %r"%(i,player_cardsuites[i])

            if player_cardsuites[i]==5:
                flush=True # True ,avoiding boolean
                flush_index=all_cards_index
                flush_index.sort()
                # print "Player%d, %r"%(i,flush_index)
                # print "suites %r and cards %r"%(player_cardsuites,player_cardvalues)
#-------------------------------------------------------------
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
            full_house=True
            # pair and two pair index have same source
            full_house_index=[three_kind_index,max(pair_index)]
        elif three_kind==True and two_pair==True:
            full_house=True
            # print "full_house_index: %r" %full_house_index
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
                    royal_flush_index=[8,9,10,11,12]
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

        temp1=[royal_flush_index,straight_flush_index,four_kind_index,
        full_house_index,flush_index,straight_index,
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

    royal_flush_index=[]
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
            # get_die(6)
            continue

    # flush
    for i in range(0,4):

        if table_cardsuites[i]==5:
            flush=True # True ,avoiding boolean
            flush_index=all_cards_index
            flush_index.sort()
        else:
            continue
            get_die(7)
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
                royal_flush_index=[8,9,10,11,12]
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

    report_index=[royal_flush_index,straight_flush_index,four_kind_index,
    full_house_index,flush_index,straight_index,three_kind_index,
    two_pair_index, pair_index]

    report_status=[royal_flush,straight_flush,four_kind,full_house,
    flush,straight,three_kind,two_pair,pair]

    return report_index, report_status

# determine the winner
def get_highcard_winner(card_distribution,num_players):

    # in hand card reports
    cih=get_players_handcard_report(card_distribution,num_players)
    # initial_winner=0 # player0
    player0_cards=cih[0][0]
    wp=0
    i=0
    joint_winner_status=False
    joint_winner_index=[wp]# rest of the winners will be appended
    joint_winner=[]
    for card in cih:
        print "card %r"%card[0]
        if max(card[0])>=max(cih[wp][0]) and sum(card[0])>sum(cih[wp][0]):
            wp=i
        elif max(card[0])>=max(cih[wp][0]) and sum(card[0])==sum(cih[wp][0]):
            joint_winner_status=True
            joint_winner_index[0]=wp
            joint_winner_index.append(i)
        elif max(card[0])<max(cih[wp][0]):
            wp=wp
        else:
            get_die(7)
        i=i+1
    joint_winner=[joint_winner_status,joint_winner_index]
    old_winby=9
    return wp,old_winby,joint_winner

def get_allcard_winner(cards_playerwise,card_distribution,num_players):
    ari,ars=get_players_allcard_report(cards_playerwise,num_players) # all cards report
    tri,trs=get_tablecard_report(card_distribution) # table cards report

    wp=num_players-2 # wp is winning player 0 corresponds to player0
    old_winby=9 #winning combination of winner
    new_winby=9
    joint_winner_status=False
    joint_winner_index=[]
    wps=ars[0]
    wpi=ari[0]
    p=0
    for ps in ars:
        print  "p %d and lenp %d"%(p,len(ps))
        # reset the joint_winner_status if any player has higher than tied cards
        if old_winby <new_winby:
            joint_winner_status=False
            joint_winner_index=[]
            new_winby=old_winby

        # royal_flush
        elif ps[0]==True and old_winby>=0:
            pi=ari[p][0]
            wpi=ari[wp][0]
            if wps[0]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=0
                wps=ars[wp]
            elif wps[0]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=0
                wps=ars[wp]
        # straight_flush
        elif ps[1]==True and old_winby>=1:
            pi=ari[p][1]
            wpi=ari[wp][1]
            if wps[1]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=1
                wps=ars[wp]
            elif wps[1]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                winby=1
                wps=ars[wp]
        # four_kind
        elif ps[2]==True and old_winby>=2:
            pi=ari[p][2]
            wpi=ari[wp][2]
            if wps[2]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=2
                wps=ars[wp]
            elif wps[2]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=2
                wps=ars[wp]
        # full_house
        elif ps[3]==True and old_winby>=3:
            pi=ari[p][3]
            print pi
            wpi=ari[wp][3]
            print wpi
            if wps[3]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p:
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=3
                wps=ars[wp]

            elif wps[3]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=3
                wps=ars[wp]
        # flush
        elif ps[4]==True and old_winby>=4:
            # pi=ari[p][4]
            # wpi=ari[wp][4]
            # print "p %r"%p
            # print ps
            # print pi
            # print "sum %r" %sum(pi)
            # print wp
            # print wps
            # print wpi
            # print sum(wpi)

            if wps[4]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=4
                wps=ars[wp]
                print "if"
            elif wps[4]==True and max(pi)<max(wpi):
                wp=wp
                print "elif"
            else:
                wp=3
                old_winby=4
                wps=ars[wp]
                # print "else %d%d" %(p,wp)
        # straight
        elif ps[5]==True and old_winby>=5:
            pi=ari[p][5]
            wpi=ari[wp][5]
            if wps[5]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=5
                wps=ars[wp]
            elif wps[5]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=5
                wps=ars[wp]
        # three_kind
        elif ps[6]==True and old_winby>=6:
            pi=ari[p][6]
            wpi=ari[wp][6]
            if wps[6]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=6
                wps=ars[wp]
            elif wps[6]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=6
                wps=ars[wp]
        # two_pair
        elif ps[7]==True and old_winby>=7:
            pi=ari[p][7]
            wpi=ari[wp][7]
            if wps[7]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p: # +1 as ars inserted with table report
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=7
                wps=ars[wp]

            elif wps[7]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=7
                wps=ars[wp]
        # pair
        elif ps[8]==True and old_winby>=8:
            pi=ari[p][8]
            wpi=ari[wp][8]

            if wps[8]==True and max(pi)>=max(wpi)and sum(pi)==sum(wpi)and wp!=p:
                joint_winner_status=True
                joint_winner_index=[wp,p]
                wp=p
                old_winby=8
                wps=ars[wp]
            elif wps[8]==True and max(pi)<max(wpi):
                wp=wp
            else:
                wp=p
                old_winby=8
                wps=ars[wp]
        # player increment
        p=p+1


    winner=wp
    joint_winner=[joint_winner_status,joint_winner_index]
    return winner, old_winby,joint_winner

# non high card winner
def get_winner(cards_playerwise,card_distribution,num_players):

    ari,ars=get_players_allcard_report(cards_playerwise,num_players) # all cards report
    tri,trs=get_tablecard_report(card_distribution) # table cards report

    for ps in ars:
        for i in range(0,8):
            # print "%r :: %r :: %r" %(trs[i],tri[i],ps[i])
            if trs[i]==True and ps[i]==True and tri[i]==ps[i]:
                print ">>Table has best combination:"
                print ">>Player having best cards wins!"
                get_die(9)
                wp,old_winby,joint_winner=get_highcard_winner(card_distribution,num_players)
            else:
                wp,old_winby,joint_winner=get_allcard_winner(cards_playerwise,card_distribution,num_players)
                # print "JointWinner: %r, %r" % (joint_winner[0],joint_winner[1])
    winner=wp
    return winner, old_winby,joint_winner #,status

# --------------------------------MAIN LOOP---------------------------------------------

# number of players
num_players=get_num_players()
# Money on the table
money_on_table=get_money_on_table()

# random distribute cards
random.shuffle(deck)
card_distribution, card_distribution_all=get_distribute_cards(num_players,deck)

# test cases : flush
# card_distribution=[['s4', 'd4', 'c4', 'sa', 's6'],
# ['sk', 'dk'], ['c9', 's8'], ['h3', 's6'], ['s7', 's9']]

# test cases : straight


# test cases: flush


print card_distribution[0:-1]
cards_playerwise=get_cards_playerwise(card_distribution,num_players)


report_index,report_status=get_players_allcard_report(cards_playerwise,num_players)
for i in range(0,len(report_status)):
    print "\nPlayer%d reports: %r" % (i,report_status[i])

# print winner
winner,old_winby,joint_winner=get_winner(cards_playerwise,card_distribution,num_players)
old_winby_string=cardOrder.get(old_winby)
if joint_winner[0]==True:
    print ">>Round winners are: Player%r; They all had %s" % (joint_winner[1], old_winby_string)
else:
    print ">>Round winner is Player%d, he won by %s" %(winner, old_winby_string)

# print winning hands
ks=0
for contents in report_status:
    print "Player%d old_winby status: %r" %(ks,contents[old_winby])
    ks=ks+1

ki=0
for contents in report_index:
    print "Player%d old_winby index: %r" %(ki,contents[old_winby])
    ki=ki+1
