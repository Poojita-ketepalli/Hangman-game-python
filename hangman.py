import time
import random
from PyDictionary import PyDictionary

name = input("Enter name to proceed! ")
print("Hello, " + name + ". Time to play hangman!")

def game():
    time.sleep(0.5)
    print("\nselect the mode you want to play:\n")
    print(" 1.Easy \n 2.Medium \n 3.Difficult")
    mode = input()
    while True:
        if mode=="Easy" or mode=="1":
            print("You selected Easy mode!!!!!")
            print("\nStart guessing...")
            words = ["lion","tiger","leopard","elephant","Rabbit","goat","hornbill","cucumber","lotus","orchid","Jackfruit",
                     "wheat","maize","ginger","crocodile","wax","punjab","srilanka","srinagar","jammu and kashmir","kerala",
                     "Andhrapradesh","telangana","odisha","Assam","goa","tamilnadu","potato","noodles","crabs","earthworms",
                     "scissors","knife","glass","happy","sad","emotion"]
            n=len(words)
            #print(n)
            idx = random.randint(1,n)
            word=words[idx]
            dictionary = PyDictionary()
            hint = dictionary.meaning(word)
            print("\nHint is ", hint)
            guesses = ''
            turns = 5
            while turns > 0:
                failed = 0
                for char in word:
                    if char in guesses:
                        print((char + " "), end="")
                    else:
                        print("_ ", end="")
                        failed += 1
                if failed == 0:
                    print("\nYou won the game!!!!!")
                    game()
                else:
                    guess = input("\n\nguess a character:")
                    guesses += guess
                    if guess not in word:
                        turns -= 1
                        print("Your guess is Wrong!!!")
                        print("You have", + turns, 'more guesses')
                        if turns == 0:
                            print("\n You Lose the game")
                            print("The word is ", word)

                            print("Do you want to play again?")
                            ans = input()
                            if ans == "n" or ans == "N":
                                print("Thanks for playing!!!")
                                return
                            else:
                                game()
        elif mode=="Medium" or mode=="2":
            print("You selected Medium mode!!!!!")
            print("\nStart guessing...")
            words = ["annoy","ignore","prefer","attention","instead","problem","calm","investigate","protect","comfortable","invite","proud",
                        "consequences","important","question","curious","jealous","reminds","curve","leader","repeat","decide","list","report","directions","listen","rhyme",
                        "discover","lovely","respect","disappointed","measuring","searching","embarrassed","miserable","special",
                        "enormous","mumble","spotless","exhausted","negative","squirm","explore","nervous","stomped",
                        "fair","nibbled","suddenly","fascinating","note","suggestion","feast","notice","surprise","focus","observing","uncomfortable",
                        "opposite","warning","gigantic","ordinary","wonder","grumpy","positive","worried","huge","precious"]
            word = random.choice(words)
            dictionary = PyDictionary()
            hint = dictionary.meaning(word)
            print("\nHint is ", hint)
            guesses = ''
            turns = 5
            while turns > 0:
                failed = 0
                for char in word:
                    if char in guesses:
                        print((char + " "), end="")
                    else:
                        print("_ ", end="")
                        failed += 1
                if failed == 0:
                    print("\nYou won the game!!!!!")
                    game()
                else:
                    guess = input("\n\nguess a character:")
                    guesses += guess
                    if guess not in word:
                        turns -= 1
                        print("Your guess is Wrong!!!")
                        print("You have", + turns, 'more guesses')
                        if turns == 0:
                            print("\n You Lose the game")
                            print("The word is ", word)

                            print("Do you want to play again?")
                            ans = input()
                            if ans == "n" or ans == "N":
                                print("Thanks for playing!!!")
                                return
                            else:
                                game()
        elif mode=="Difficult" or mode=="3":
            print("You selected Difficult mode!!!!!")
            print("\nStart guessing...")
            words=["abruptly","absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","blitz","blizzard","boggle","bookworm",
                "boxcar","boxful","buckaroo","buffalo","buffoon","buxom","buzzard","buzzing","buzzwords","caliph","cobweb","cockiness","croquet","crypt","curacao","cycle","daiquiri","dirndl",
                "disavow","dizzying","duplex","dwarves","embezzle","equip","espionage","euouae","exodus","faking","fishhook","fixable","fjord","flapjack","flopping","fluffiness","flyby",
                "foxglove","frazzled","frizzled","fuchsia","funny","gabby","galaxy","galvanize","gazebo","giaour","gizmo","glowworm","glyph","gnarly","gnostic","gossip","grogginess",
                "haiku","haphazard","hyphen","iatrogenic","icebox","injury","ivory","ivy","jackpot","jaundice","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu",
                "jockey","jogging","joking","jovial","joyful","juicy","jukebox","jumbo","kayak","kazoo","keyhole","khaki","kilobyte","kiosk","kitsch","kiwifruit","klutz","knapsack","larynx",
                "lengths","lucky","luxury","lymph","marquis","matrix","megahertz","microwave","mnemonic","mystify","naphtha","nightclub","nowadays","numbskull","nymph","onyx","ovary","oxidize","oxygen",
                "pajama","peekaboo","phlegm","pixel","pizazz","pneumonia","polka","pshaw","psyche","puppy","puzzling","quartz","queue","quips","quixotic","quiz","quizzes","quorum","razzmatazz",
                "rhubarb","rhythm","rickshaw","schnapps","scratch","shiv","snazzy","sphinx","spritz","squawk","staff","strength","strengths","stretch","stronghold","stymied","subway","swivel","syndrome",
                "thriftless","thumbscrew","topaz","transcript","transgress","transplant","triphthong","twelfth","twelfths","unknown","unworthy","unzip","uptown","vaporize","vixen","vodka","voodoo",
                "vortex","voyeurism","walkway","waltz","wave","wavy","waxy","wellspring","wheezy","whiskey","whizzing","whomever","wimpy","witchcraft","wizard","woozy","wristwatch","wyvern","xylophone",
                "yachtsman","yippee","yoked","youthful","yummy","zephyr","zigzag","zigzagging","zilch","zipper","zodiac","zombie"]
            word = random.choice(words)
            dictionary=PyDictionary()
            hint=dictionary.meaning(word)
            print("\nHint is ",hint)
            guesses = ''
            turns = 5
            while turns > 0:
                failed = 0
                for char in word:
                    if char in guesses:
                        print ((char+" "),end="")
                    else:
                        print ("_ ",end="")
                        failed += 1
                if failed == 0:
                    print ("\nYou won the game!!!!!" )
                    game()
                else:
                    guess =input("\n\nguess a character:")
                    guesses += guess
                    if guess not in word:
                        turns -= 1
                        print ("Your guess is Wrong!!!")
                        print ("You have", + turns, 'more guesses')
                        if turns == 0:
                            print ("\n You Lose the game")
                            print("The word is ",word)
                            print("Do you want to play again?")
                            ans=str(input())
                            if(ans=="n" or ans=="N"):
                                return
                            else:
                                game()

        else:
            print("Select valid mode:")
            mode = input()

game()