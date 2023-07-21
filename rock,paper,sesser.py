def game():
    a=input("\n enter any name:")
    b=input("\n enter any name:")
    if a==b:
        print("both get tie")
    elif a=="rock "and b=="sesser":
        print("rock smashes sesser , a win")
    elif a=="rock" and b=="paper":
        print("paper covers rock , b win")   
    elif a=="paper" and b=="sesser":
        print("sesser cuts paper , b win")
    elif a=="paper" and b=="rock":
        print("paper covers rock , a  win")   
    elif a=="sesser"  and b=="rock":
        print("rock smashes sesser , b win") 
    elif a=="sesser" and b=="paper":
        print("sesser cuts paper , a win")       
game()