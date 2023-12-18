words = "rana"

guess = []

ok = True

for i in range(len(words)):
  g = input("guess words one by one: ")
  if g == words[i]:
    guess.append(g)
    if("".join(guess) == words):
      print("you guessed All Correct the word is : %s"%(words))
      break
    else:
      print(f"you guessed this correct = {guess}, now try again")
    

    
  else:
    print("you guessed this wrong, now try again")
    for j in range(0,5):
      g = input(f"{guess} guess this next word ")
      if g == words[i]:
        print(f"you guessed this correct{guess}")
        guess.append(g)
        break
      elif j >= 4 :
        print("you guessed All wrong")
        quit()
        
      else:
        print(f"you guessed this wrong, now try again, you have {5-j-1} this attempt")
      
      
  # print("guess %s"%("".join(guess)))


  