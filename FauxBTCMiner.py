from random import randint
#imports whatever is used from the random module instead of typing out random.randint()
#you can just type out randint because of the star
from time import sleep
#you can just type out sleep instead of time.sleep()
from colorama import Fore
#imports Fore(ground) to change the color
from requests import get, exceptions
#imports get(), json(), and RequestsConnectionError
from sys import exit, argv
#imports method to exit the program and command line arguments


def get_btc_price():
    try: return get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate_float']
    except(exceptions.ConnectionError): return 16820.00 #price of BTC as of 12/23/2022

def start_program():
    while True:
        userinput=input("(Y/N) Would you like to start the BTCWallerMiner: ")
        if userinput.upper() not in ['Y','N','YES','NO']:
            print("Incorrect Input")
            continue
        elif userinput.upper() in ["Y","YES"]:
            return 0
        elif userinput.upper() in ["N","NO"]:
            exit()
    #this loop above will ask the user if they would like to start the miner

def gen_rand_line(length):
    ##gen_rand_line needs a an integer for how many characters in the scrambled text
    p=0
    line=""
    while p<length:
        chartype=randint(1,2)
        #randint gives a 50% for a letter or number to be printed
        if chartype==1: line=line+str(randint(1,9))
        else: line=line+chr(randint(97,122))
        p=p+1
    ##return line ##remove '##' if you dont want the extra 0.00 btc information
    line=line+'>'+f"{Fore.RED} 0.00 BTC ($0.00)"+f"{Fore.WHITE}"
    #Fore.COLOR will color the following text
    return line

def btc_miner(min, max):
    ##min is the minimum amount of lines printed
    ##max is the maximum amount of lines printed
    while True:
        BTCfound1=randint(1,100)/100
            #this is the decimal value of the BTC we found
        BTCfound2=BTCfound1*get_btc_price()
            #this is the dollar value of the BTC we found
            #from mining and coindesk api
        
        total_lines=randint(min, max)

        for _ in range(total_lines):
            scrambled_characters_in_line=90
            print(gen_rand_line(scrambled_characters_in_line),end='\n')
            sleep(0.4)
            #sleep() or time.sleep() will pause it for the seconds that is put in the parenthesis

        for _ in range(scrambled_characters_in_line):
            chartype=randint(1,2)
            if chartype==1:
                    print(f"{randint(1,9)}", end="")
            else:
                print(f"{chr(randint(97,122))}", end="")        
            #this is just the same code from before but it is for the "found BTC" row
                
        print(f">{Fore.GREEN} {BTCfound1:.2f} BTC (${BTCfound2:.2f})"+Fore.WHITE)
        #use Fore.COLOR to show the found BTC and only go to 2 decimal places
        while True:
            status=input("(Y/N) Would you like to continue: ")
            if status.upper() not in ["Y","N","YES","NO"]:
                print("Incorrect Input")
                continue
            elif status.upper() in ["Y","YES"]:
                break
            elif status.upper() in ["N","NO"]:
                exit()
            #this is to ask the user if they want to mine more BTC

def main():
    try: min=int(argv[1]); max=int(argv[2])
    except (IndexError, ValueError): min=10; max=20
    start_program()
    btc_miner(min,max)

if __name__=="__main__":
    main()
