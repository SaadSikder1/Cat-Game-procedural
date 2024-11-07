cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
}
import sys
from termcolor import colored, cprint
print("Welcome to my cat game!")

name = input("Enter the name of your cat: ")
colour = input("Enter the colour of your cat: ")

CatAlive = True
while CatAlive == True:
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. Put your cat to sleep and feed it 4. show stats ")

    if option == '1' and cat_attributes["energy"] > 5:
        cprint("You play with your cat.", "green")
        cat_attributes["energy"] -= 5
        cat_attributes["weight"] -= 0.8
        print("""\                                                                                                                   
                                                                                                                   
                                                                                                       /‰          
                  ÆÆ           ÆÆ                 Æ¿Æ‡           Æƒ                   ÆÆ           ÆÆ  ôÇ          
               ˜ Æu Æ         Æ  Æ               Æz ·Æ          Æ Æ1                 ÈÆ Æ         Æa Æ             
             ·   ó  2è ¦!!!„°$¯  À                     Æ ¦¬|¡¦ Æ   å           ´     Œ   Æ º×÷¯*’ö®  4Ö            
               Æ ÆÆ             ÆÆ Æ            Æ  æ’            ¶Æ Æ             Æ Æ                  ý           
              Æ     ÆÂ  ¥ Æ  ÆÆ     Æ ¨         Æ  ÆíÆÆ  Æ  ¾ ÆÆ     Æ ¸         Æ    ÛÆ  d  Æ  Æ      8Æ          
              Æ  ´     Æ Æ Æ        Æ           Æ  Æ›   Æ §ßÆ        Æ           Æ       ÏÆ Æ Æ     ’  1Æ          
               Æ –      Æ Æ      ‚´Æ  ´         Æ  ÆÉ    Æ«Õ^       Æ´ ³   ¯     ›Æ       LxçÆ        !Æ           
     ÐÏœp                                                                    Æ>     ´               `·       ÆÆ    
    ÆY Æ   OÆ    ˆ               ‘     Æ         Æ                     ÆJ ‚ Æ  ÆØ                          Æ       
  : ôÆ Æ ‘  ÆÆÆÆˆ                  ÆÆÆÆ§        Æ               –  *ÆÆÆÆ  · Æg  ÆÆÆÆ                   ÆÆÆÆÆ       
        L                                      ±                  Æ       ´  …>      ô?                            
     Æ Æ%    ÆÆÆ:—               qÆÆ    ÆÆEÆ íÆ               ·+ÆÔý  ãÆ        Æ Æ   ÆÆÆ ¦           UÆ            
    X× Æ   Æ}                   ¢Æ      Æ Æ  Æ                     Æƒ         Æ Æ  Æ                  ºH           
     Æ Æ    ÆÆÆÆ            ˜ AÆ        Æ Æ  Æt ‚     ‘        *ÆÆÆÆ          ôÆºÆ ´ÆÆÆÆ        ¨   ¨ Æ            
          ‘      ÆæDY                 ˆ               ; ÆÆÆÆÆ§Ö      ˆ                   ÆÆÆÆÆÆ‚š       ’          
                    Æ ´    `Æ `                   º   ˆ Æ                                       Æ    Æy            
                   Æä      Æ                     ‚ Æ~   ¯Æ                                     Æ     Æ             
                    Æ     Æ  “¢`¯¨                      Æ  @j°                                  Æ  òÆ  z¸          
                      b¹h    ì< ¸                    }b    º}                                    ¨u   ­(           
                                                                                                                   
                                                                                                                   """)
        cprint("Your cat loses 5 energy, loses 0.8 weight", "green")
    elif option == '2' and cat_attributes["energy"] > 5:
        cprint("You train your cat. ","green")
        print("""\                                                                                          
                                             œ                                   
                                           &ÆÆ                                            
                                         rÆÆ   ·ÆÆ‚                                                                
                                        ÆÆ      ÆQ                                                                 
                                      ÆÆ‘       ÆÅ                                                                 
                                    ÆÆ×         ÆN                                                                 
                                  ÆÆW          ·ÆÆ7ÆÆ                                                              
                                 ÆÆ                  ÆÊ                                                                                     
                               Æ† QÆ                                                                               
                             WÆ¤ ÆÆëÆ‚               sÆÆÆÆÆÆÆw                                                     
                            ÆÆ   …ÆÆ>                      Æ                                                       
                           ÆÆ                             œÆ                                                       
                           ÆÆ                            ÆÆ                                                        
                            ŒÆ      yÆ       ÆÆÆÆÖ       ÆÆ                                                        
                              ÆÆ     UÆÆ    ÖÆ  ÆÆ      ÆÆ                                                         
                               Æl      Æe     ÆÆ                                                                                                                            
                                    ˆÆ²                                                                            
                                    ‹Æ+                   ÆÆÆ                                                      
                                    …Æº                     ÆÆ                                                     
                                    ·Æ            ­ÆÆÆÆÆÆü    ÆÆ                                                   
                                    (ÆiÆÆ                                                                          
                                     Ð  ÆÆÆ                                                                                      
                                    LÆ         ÆÆ                                   Æ                              
                                     Æ  ÆÆÆÆ   Æ4         $ÆÆ®           {ÆÆ–       Æ                              
                                     Æ  T  †   Æõ       GÆÆÆË              ’Ê“      Æ                              
                                     Æ      ¤  Æ4     h   +                 Æ×    ‚Æ                               
                                     Æ     ÜÆ  Æn     Æm &Œi                #c   ÆÆL                               
                                     ÆÆ    ÆÆ  ÆÆ    ÆÆ  ŠÆi         Ã¦     Æ  ÂÆÆ                                 
                                      ˜ÆÆÆÆ      ÆÆÆÆ—       ?iºº÷’½EÆs   óÆÜ ÆÆ                                   
                                                            (ÆÆÆÆÆÆW±    `çÓ              """)
        cprint("Your cat gains 5 intelligence, loses 5 energy and loses 0.6 weight", "green")
        cat_attributes["intelligence"] += 5
        cat_attributes["energy"] -= 5
        cat_attributes["weight"] -= 0.6
    elif option == '3':
        cprint("You put your cat to sleep. It sleeps well.", "green")
        cat_attributes["energy"] += 70
        cat_attributes["weight"] += 5
        print("""\
                                                                                                                                 
                 ƒÆ<                                                                                               
           U        m                       º¢            ´´´´´’ˆ                                                  
           Æv         Æ                      Æ     ˆ¿ÆÆÆ1        ¸eÆ~‘                                             
              ûÆ  ;    ^                  ùú Æ  OÆ                     †bÐ                                         
                  í                   rÆÆÆ    ´ÅÆ                         ¯Ý                                       
        ´=ÝÙŽÆÆÆpƒ•!v>             •ÆÖ          Æ   Ús                      1È?                                    
                             —TÆk Æÿ              ÆœŸ½                         A                                   
                         0¹w2                      n                            Æ                                  
                          w‰+                      ¯}                           V                                  
                            9Æ                  ¨   é}¦u                       Rê                                  
                             1Å¥ÆÛQ           ÆÆ°  €Ú…                         Œ                                   
                              ‰¯Æ                žÆÆ¬ s*                                                           
                                ôÆ    “ÆÆI                   mÆZ         ¦!     Æ                                  
                                  e          Æ¼ ÆÆ          H   úÆ²    uÆ×      Æ                                  
                                 *ËÆe |ÆÆÆÆ™åÕ¶ÆA           Æ      =i<)        Æ                                   
                                    ÙæÆî         7öº   ?(¿ ‘ ùÆ               —                                    
                                                                ÃÆý     ÆÆK                                        
                                                                    “`                                             
                                                                                                                   
                                                                                                                    """)
        cprint("Your cat gains 70 energy and 5 weight", "green")
    elif option == '4':
        print("Here is your cat's stats: ")
        cprint("Your cat's energy currently is " + str(cat_attributes["energy"]),"green")
        cprint("Your cat's intelligence currently is " + str(cat_attributes["intelligence"]),"green")
        cprint("Your cat's weight currently is " + str(cat_attributes["weight"]),"green")
    else:
        print("It seems your cat does not have enough energy for these actions or you have entered an invalid option.")
        print("Nothing happens.")

# warnings
    if cat_attributes["energy"] <5:
        cprint("Your cat is tired, you should probably put it to sleep.", "yellow")
    if cat_attributes["weight"] < 3:
        cprint("Your cat is severely malnourished. You should probably feed it.", "yellow")


# punishments
    if cat_attributes['energy'] < 0:
        cprint("Your cat runs out of energy, it passes out of exhaustion. ", "red")
        cprint("it gains only 30 energy. You should have rested.", "red")
        cat_attributes["energy"] += 30
    if cat_attributes['weight'] < 0:
        cprint("Your cat has died of severe malnourishment.", "red")
        print("""
                                                @@@@@@@@@@@@@                                              
                                     @@@@@#@@@@@@@@+@@@@@@                                          
                                  @@@==@@-           @@# +@@@                                       
                                 @@=*@#    .=====+- @@  @@+.@@@                                     
                               @@@-@+  .--::::::..:  @    @@-=@@                                    
                              #@=+@         ..              @#.@@                                   
                              @-:@  @@@@@@+  . *++  @@@      @#.@@                                  
                              @ =*    @   #@ . @@    @@@@@@#  @+                                    
                             @@@@  -  @   @@ .  @ .  @%   @@   %@@@                                 
                             @  @ :: *@ @@@  .  @ .. @@ =@@    %@ @@                                
                             @ *@ -. @@  @-  .  @    @@@@   -  @= @@                                
                             @ *@ -  @@   @@ . @@    @@   .:-  @#:*@                                
                             @ *@ : #*+% %+% . %**  @@@  ..    %%:*@                                
                             @ %@ *                         @. =%.+@                                
                             @ .@   : #=*@%@@@@@@@@@@@@@@@  @  +@.=@                                
                          @  @@@@ @ @*    . .               @  .@==@                                
                          @  @@ %  @  .=:---+*=+-------== @@    @..@                                
                          @  # =@  *@ ....                @     @: @ :@@                            
                          @@ @.%% . @ ....::::: @@*@. @#*@@@    =. @:#@                             
                       @@@@.@@ %:        ::::::   @-.  @@   .@@@*  @-@                              
                          @@@@ - @@@. @-         :-    @  ..   @#@ @@     @.                        
                           -%@ @@:     @@.   @@@   .:    .::-   =.@@. @@@                           
                        +@@ @@@@   =::  @@@@#@  @     @@ .:.=  :@.@@@*@                             
                           @@%.@@   +-- =:*@    @  @@@     -*   @@%.. .-                            
                            @.@  @      @@.@    @@@==    #      @..@*@                              
                           %@.@ *@@-@@@@:@ @+   @@.@  @@@@    #@:.@@@                               
                           @%.@ @.%@@ -@:@.*@+*@::-@   %@:@: %@+.@.@=                               
                           @@@@ @@@@@@@+-@@@@:@@@@@@@@@@@@@@@@@+=@@@@
        """)
        CatAlive = False


#once cat dies
cprint("it seems your cat has died.", "blue")
cprint("it had a peaceful funeral.", "blue")