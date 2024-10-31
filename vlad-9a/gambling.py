import random
print("Gambling gameeee!!!!")
points = 51
i=0
g=0
print("Ur points:", points)

while True:
    print("how many point u want to put on")
    x=int(input())
    if x > points:
        x=points
        points=0
    
        

    a = random.randint(-3, 4)
    
    score=x*a
    print("      ")
    if ( a ==-3 ):
        print("   00000  ")
        print("        0 ")
        print("-- 000000 ")
        print("        0 ")     
        print("   00000  ")
    if ( a == -2 ):
        print("   00000  ")
        print("       00 ")
        print("--   00   ")
        print("    00    ")     
        print("   000000 ")
    if ( a == -1 ):
        print("   0000   ")
        print("     00   ")
        print("--   00   ")
        print("     00   ")     
        print("   000000 ")
    if ( a == 0 ):
        print("   000000 ")
        print("   00  00 ")
        print("   00  00 ")
        print("   00  00 ")     
        print("   000000 ")
    if ( a == 3 ):
        print("   00000  ")
        print("        0 ")
        print("   000000 ")
        print("        0 ")     
        print("   00000  ")
    if ( a == 2 ):
        print("   00000  ")
        print("       00 ")
        print("     00   ")
        print("    00    ")     
        print("   000000 ")
    if ( a == 1 ):
        print("   $$$$   ")
        print("     $$   ")
        print("     $$   ")
        print("     $$   ")     
        print("   $$$$$$ ")
    if ( a == 4 ):
        print("   $$  $$ ")
        print("   $$  $$ ")
        print("   $$$$$$ ")
        print("       $$ ")     
        print("       $$ ")
    print("        ")

    if score > 0:
        print("$$$$$  Good job!, +",x, "*", a, "=", score, "  $$$$$")
    else:
        
        print("$$$$$  O No, ",x, "*", a, "=", score, "  $$$$$")
    points=points+score
    if points <= 0 :
        points = 0
        print("You loose :(")
        break
    else:
        
        p=0
        d = points
        while ( d > 1 ) :
            d=d/10
            p=p+1
        i = 0
        if (p == 1 ): 
            numb = int(points / 10)
            if ( numb ==5 ):
                print("   000000 ")
                print("   00   ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 6 ):
                print("   000000 ")
                print("       00")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 7 ):
                print("  000000  ")
                print("      00  ")
                print("     00   ")
                print("    00    ")     
                print("   00     ")
            if ( numb == 8 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 3 ):
                print("   000000 ")
                print("       00 ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 2 ):
                print("   00000  ")
                print("       00 ")
                print("     00   ")
                print("    00    ")     
                print("   000000 ")
            if ( numb == 1 ):
                print("   0000   ")
                print("     00   ")
                print("     00   ")
                print("     00   ")     
                print("   000000 ")
            if ( numb == 4 ):
                print("   00  00 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            if ( numb == 9 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            print("        ")

        if (p == 2 ): 
            numb = int(points / 10)
            if ( numb ==5 ):
                print("   000000 ")
                print("   00   ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 6 ):
                print("   000000 ")
                print("       00")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 7 ):
                print("  000000  ")
                print("      00  ")
                print("     00   ")
                print("    00    ")     
                print("   00     ")
            if ( numb == 8 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 3 ):
                print("   000000 ")
                print("       00 ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 2 ):
                print("   00000  ")
                print("       00 ")
                print("     00   ")
                print("    00    ")     
                print("   000000 ")
            if ( numb == 1 ):
                print("   0000   ")
                print("     00   ")
                print("     00   ")
                print("     00   ")     
                print("   000000 ")
            if ( numb == 4 ):
                print("   00  00 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            if ( numb == 9 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            print("        ")
            numb = int(points % 10)
            if ( numb ==5 ):
                print("   000000 ")
                print("   00   ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 6 ):
                print("   000000 ")
                print("       00")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 7 ):
                print("  000000  ")
                print("      00  ")
                print("     00   ")
                print("    00    ")     
                print("   00     ")
            if ( numb == 8 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("   00  00 ")     
                print("   000000 ")
            if ( numb == 3 ):
                print("   000000 ")
                print("       00 ")
                print("   000000 ")
                print("       00 ")     
                print("   000000 ")
            if ( numb == 2 ):
                print("   00000  ")
                print("       00 ")
                print("     00   ")
                print("    00    ")     
                print("   000000 ")
            if ( numb == 1 ):
                print("   0000   ")
                print("     00   ")
                print("     00   ")
                print("     00   ")     
                print("   000000 ")
            if ( numb == 4 ):
                print("   00  00 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            if ( numb == 9 ):
                print("   000000 ")
                print("   00  00 ")
                print("   000000 ")
                print("       00 ")
                print("       00 ")
            print("        ")
                

        

    print("Ur points:", points)
    if points > 1000:
        print("U win!!!")
        break   
    
