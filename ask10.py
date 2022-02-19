  from unicodedata import decimal

  f = open("ask10file.txt", "r")
  demoline = f.read()
  templine = ""
  clearline = []
  for i in demoline:
      binary = bin(ord(i))
      #zero amonts do i have to add at the begginning
      add = 9 - len(binary)

      #add zeros
      for i in range(add):
          templine += "0"

      #add all items to templine
      for i in range(2,len(binary)):
          templine += binary[i]

      #add final items to the list
      for i in range(2):
          clearline.append(templine[i])
      for i in reange(-2,0)
          clearline.append(templine[i])

       templine = ""

  finish = False
  number = ""

  #counter for variables divisible by 2,3,5,7 without reminder
  meto2 = 0
  meto3 = 0
  meto5 = 0
  meto7 = 0
  sumnumbers = 0
  while not finish:
      try:
          #takes 16 firts items and puts them for processing
          for i in range(16):
              number += str(clearline.pop(0))

          #converts the sequence to the normal format
          number = int(number, 2)
          sumnumbers += 1
          #check if it divides without reminder
          if number%2 == 0:
              meto2 += 1
          if number%3 == 0:
              meto3 += 1
          if number%5 == 0:
              meto5 += 1
          if number%7 == 0:
              meto7 += 1

          number = ""

      except:
          #converts what is left and check
          try:
              number = int(number,2)
              sumnumbers +=1
              if number%2 == 0:
                  meto2 += 1
              if number%3 == 0:
                  meto3 += 1
              if number %5==0:
                  meto5 +=1
              if number%7 == 0:
                  meto7 += 1

          except:
              finish = True

          finally:
              finish = True

  print("There are:")
  print(int(meto2/sumnumbers*100),"% Even numbers")
  print(int(meto3/sumnumbers*100),"% Which divide by 3")
  print(int(meto5/sumnumbers*100),"% Which divide by 5")
  print(int(meto7/sumnumbers*100),"% Which divide by 7")
