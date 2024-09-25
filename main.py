print('''
         .--,_
        ['    '\.
         \       `''|
         |         ,]
          `._      ].
            |     \
          _/       -'\
         ,'          ,'
       _/'          \                     ,..-''L_
  |--''              '-;__        |\     /      .,'
   \                      `--.__,'_ '----     ,-'
   `\                             \`-'\__    ,|
,--;/                             /     .| ,/
\__          INDIA/BHARAT                     '|    /_ /  
  ./  _-,                         _|  
  \__/ /                        ,/        "
       |                      _/
       |                    ,/
       \                   /
        |              /.-'
         \           _/                   :
          |         /                      .
           |        |                     .
      .    |        |                     '.
      ;     \       /                     ;\
      '      |     |                
             \    _|                      : 
              \_,/                         "'

''')
print("Welcome to the Geopolitical Strategy Game!")
print("As the Prime Minister of India, make strategic decisions by choosing between two countries at each critical juncture. Your choices will impact India's international relations, economic growth, and technological advancement.")

print("1. Choose an Energy Collaboration:")
print("Option A: Import crude oil from Saudi Arabia.")
print("Option B: Invest in natural gas projects with Qatar.")
q1 = input("Write A or B.")
if q1.lower() in ["b" , "qatar"] :
    print("💥 Game Over: Energy Shortfall Impacts the Economy.")
elif q1.lower() in ["a", "saudi arabia", "saudi" , "arabia"]:
    print("ou have secured a stable supply of crude oil, ensuring that India's energy demands are met. This decision strengthens economic ties with Saudi Arabia and supports the nation's economic growth.")
    print("")
    print("2. Decide on a Trade Agreement:")
    print("Option A: Sign a Free Trade Agreement (FTA) with the European Union (EU).")
    print("Option B: Enhance trade ties with the Association of Southeast Asian Nations (ASEAN).")





    
    q2 = input("Write A or B.")
    if q2 == "B":
        print("💥 Game Over: Missed Opportunity for Economic Advancement.")
    elif q2 == "A":
        print("You have signed an FTA with the European Union, opening doors to high-value trade, advanced technology transfer, and substantial investment opportunities. This decision propels India's economy forward and strengthens international ties.")
   






              
        
        print("Decide on a Trade Agreement:")
        print("Option A: Collaborate with Japan on high-speed rail and infrastructure.")
        print("Option B: Partner with South Korea on electronics and automotive technology.")
 
        q3 = input("Write A or B")
        if q3 == "B":
            print('''+-------------------------------------------------------------------------+
                     |          GAME OVER            |
                     | You chose Option B, causing a |
                     | lag in infrastructure that    |
                     | limits economic growth.       |
                     +-------------------------------+''')
        elif q3 == "A":
            print("Partnering with Japan accelerates India's infrastructure development, enhancing connectivity and boosting economic efficiency.Proceed to Next Choice-")
  


            
            print(" ")
            print("Choose a Health Sector Collaboration")
            print("Option A: Partner with the United Kingdom on healthcare services.")
            print("Option B: Work with Germany on pharmaceutical research.")
            q4 = input("Write A or B.")

            if q4 == "A":
                print('''+---------------------------------------------------------------------------+
                        |          GAME OVER               |
                        | You chose Option A, resulting    |
                        | in stagnated pharmaceutical      |
                        | research and limited healthcare  |
                        | advancements.                    |
                          +-------------------------------+''')
            elif q4 == "B":
                print("Collaborating with Germany enhances India's pharmaceutical research capabilities, fostering innovation and improving healthcare outcomes./nProceed to Next Choice ➡️")
                print(" ")
                print("Decide on an Education Exchange Program:")

                print("Option A: Expand educational ties with Australia.")
                print("Option B: Enhance student exchange with the United States.")
                q5 = input("Write A or B.")
                if q4 == "A":
                    print('''+-----------------------------------------------------------------------------+
                            |          GAME OVER             |
                            | You chose Option A, resulting  |
                            | in fewer high-level research   |
                            | collaborations and limited     |
                            | educational advancements.      |
                            +-------------------------------+''')
                if q5 == "B":
                    print("nhancing student exchange with the USA provides Indian students with access to advanced research and educational opportunities, fostering innovation and expertise.")
                    print("/n /n ")
                    print('''+------------------------------------------------------------------------------------------+   
                            |      **Congratulations!**          | 
                            | You have successfully navigated    |   
                            | all critical choices, strengthening| 
                            | India's position globally.         | 
                            |                                    |   
                           +------------------------------------+  ''')
else:
     print("Wroung Input Restart the game by clicking on the run button")