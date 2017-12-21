import pickle
import random
def blackjack():
    n=input('What the total money you have? ')
    b=n
    print '''Instructions:
    You win double the amount you place in a round if you get a 21
    While you lose it all in case you dont get a 21
    You can leave the game with the money you have anytime'''
    x=['A(hearts)','A(diamonds)','A(clubs)','A(spades)', '2(hearts)','2(diamonds)','2(clubs)','2(spades)',
               '3(hearts)','3(diamonds)','3(clubs)','3(spades)', '4(hearts)','4(diamonds)','4(clubs)','4(spades)'
               , '5(hearts)','5(diamonds)','5(clubs)','5(spades)','6(hearts)','6(diamonds)','6(clubs)','6(spades)',
               '7(hearts)','7(diamonds)','7(clubs)','7(spades)', '8(hearts)','8(diamonds)','8(clubs)','8(spades)',
               '9(hearts)','9(diamonds)','9(clubs)','9(spades)','10(hearts)','10(diamonds)','10(clubs)','10(spades)'
               , 'J(hearts)','J(diamonds)','J(clubs)','J(spades)', 'Q(hearts)','Q(diamonds)','Q(clubs)','Q(spades)'
               , 'K(hearts)','K(diamonds)','K(clubs)','K(spades)']

    file=open("cards.dat", "wb")
    pickle.dump(x, file)
    file.close()

    file=open("cards.dat", "rb")
    cards=pickle.load(file)
    file.close()

    def blackjack1(cards):
        x=random.randint(0,len(cards))
        
        try:
            print 'You got a ', cards[x]
        except IndexError:
            pass
        randm=cards.pop(x)
        if randm[0] in ['1','J', 'Q', 'K']:
            return 10
        elif randm[0]=='A':
            return 1
        else:
            return int(randm[0])
        
    while True:
        print "Total money with you=",n
        t=input('Enter amount for the round ')
        if t>n:
            print "Insufficent funds"
            break
        else:
            sm=0
            loop=0
            while loop==0:
                if sm==21:
                    print 'YOU WIN~~!!!!'
                    print 'Your score->>',sm
                    t+=(t*(40/100))
                    n=n+t
                    break
                else:
                    sm=blackjack1(cards)+sm
                    print 'Your score->>',sm
                    if sm==21:
                        print 'YOU WIN~~!!!!'
                        print 'Your score->>',sm
                        t+=(t*(40/100))
                        n=n+t
                        break
                    elif sm>21:
                        print 'YOU LOOOOSSSSSTTT~~!!'
                        n=n-t
                        break
                    hello=raw_input('Do you want to continue??(Y/N) ')
        
                    if hello.lower() in ('y', 'yes'):
                        continue
                    elif hello.lower() in ('n', 'no'):
                        print 'Your score->>',sm
                        t=t/2
                        n=n-t
                        loop=1
                        break
                            
                    else:
                        print 'Error'
        print "Another Game? "
        a=raw_input("Enter your choice (y/n)[with the remaining cards] ")
        if a.lower()=='n':
            break
        
    print "Final money with you=",n
    print "You have earned ",n-b
    

