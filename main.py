try:
    import discum
except:
    print("Discum not found! Installing...")
    import os
    os.system("python3 -m pip install discum")
    import discum
try:
    import enlighten
except:
    print("Enlighten not found! Installing...")
    import os
    os.system("python3 -m pip install enlighten")
    import enlighten
import os
import time
from cfg import TOKEN, LOG_INFO, BADGE, GUILD_DICTIONARY, NO_SCRAPE, NUM_OF_LOOP, TIME_BETWEEN_LOOP, DB_NAME
import sqlite3
import json

#Parse command
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-db", "--database", help="Database file name(ex. mydb.db)", required=False, default=DB_NAME)
parser.add_argument("-c", "--cycle", help="Number of time to rescan(Default 0: no rescan)", type=int, required=False, default=NUM_OF_LOOP)
parser.add_argument("-t", "--time", help="Time between rescan(Default 3600s between rescan)", type=int, required=False, default=TIME_BETWEEN_LOOP)

args = parser.parse_args()
DB_NAME, NUM_OF_LOOP, TIME_BETWEEN_LOOP = args.database, args.cycle, args.time

#create bars
os.system('cls' if os.name == 'nt' else 'clear')
manager = enlighten.get_manager()
numguild=len(GUILD_DICTIONARY.keys())


#db part

con = sqlite3.connect(DB_NAME)
cur = con.cursor()

#check if tables exists
try:
    cur.execute("SELECT * FROM GUILD")
except sqlite3.OperationalError:
    print("Creating table guild...")
    con.execute('''
                    CREATE TABLE GUILD(
                        id INTEGER NOT NULL PRIMARY KEY, 
                        data TEXT
                        )''')
    con.commit()
try:
    cur.execute("SELECT * FROM MEMBER")
except sqlite3.OperationalError:
    print("Creating table member...")
    con.execute('''
                    CREATE TABLE MEMBER(
                        id INTEGER NOT NULL PRIMARY KEY, 
                        data TEXT
                        )''')
    con.commit()      

lenmembersfetched=0

#bot part
bot = discum.Client(token=TOKEN, log=LOG_INFO)

def id_to_data(id): #function that takes the id and trasform it to account creation date
    return str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))

@bot.gateway.command
def getGuildName(resp):
    if resp.event.ready_supplemental: #on bot start
        global guild_name
        guild_name = bot.gateway.session.guild(guild).name

def close_after_fetching(resp, guild_id):
    global lenmembersfetched
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since','avatar','bot'], wait=1) #get all the selected user attributes, wait 1 second between requests
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession() #saves 10 seconds when gateway is run again
    
    return bot.gateway.session.guild(guild_id).members #return a dictionary with all the data

memberscrape_bar = manager.status_bar('Starting...',color='white_on_black',justify=enlighten.Justify.CENTER, position=2)

for x in range(NUM_OF_LOOP):
    guild_bar = manager.counter(total=numguild, desc='Guilds', unit='guilds', leave=False, position=3)
    for guild in GUILD_DICTIONARY:
        guild_bar.update() #add 1 to guild bar
        memberscrape_bar.update('Scraping Member...')
        try:
            members = get_members(guild, GUILD_DICTIONARY[guild]) #server id, server chat
        except KeyError:
            continue
        cur.execute('''SELECT * from GUILD where id = ?''', (int(guild),)) #check if guild id already exists
        check1=cur.fetchone()
        if check1 is None:
            con.execute('''INSERT INTO GUILD VALUES (?, ?)''', (int(guild), guild_name,))

        memberscrape_bar.update('Scraping '+ str(guild_name) +' done.')
        memberparse_bar = manager.counter(total=lenmembersfetched, desc='Member Parsed', unit='member', leave=False, position=1) #create bar for member parsed

        for member in members:
            if int(member) in NO_SCRAPE:
                continue
            if 'bot' in members[member] and members[member]['bot'] == True: #check if the scraped user is a bot if so don't add to the user list
                memberparse_bar.update() #update member parsed bar
                pass
            else:
                cur.execute('''SELECT * from MEMBER where id = ?''', (int(member),)) #check if member id already exist
                data_grabbed=cur.fetchone() #fetch selected data
                
                if data_grabbed is not None: #data found for this id
                    data_parsed=json.loads(data_grabbed[1]) #create a variable with only the data columns and convert it to dictionary from json
                    if not int(guild) in data_parsed['mutual_guilds']: #check if the guild id is not already in the database
                        data_parsed['mutual_guilds'].append(int(guild))
                        cur.execute('''UPDATE MEMBER SET data = ? WHERE id = ?''',(json.dumps(data_parsed), int(member),))
                
                else: #if no data found
                    if 'public_flags' in members[member]: #check if public_flags exists
                        if members[member]['public_flags'] in BADGE: #check if the specif flags is included in the known BADGEs
                            members[member]['public_flags'] = BADGE[members[member]['public_flags']] #change the flag number to the BADGEs name
                    members[member]['created_at']= id_to_data(member) #add created_at key to data using id
                    members[member]['mutual_guilds'] = [int(guild)] #create guild array 
                    con.execute('''INSERT INTO MEMBER VALUES (?, ?)''', (int(member), json.dumps(members[member]),))
                memberparse_bar.update() #update member parsed bar
        memberparse_bar.close()
        con.commit() #save changes to database
    guild_bar.close()
    if NUM_OF_LOOP != 1: #wait bar
        wait_bar = manager.counter(total=TIME_BETWEEN_LOOP, desc='Waiting', unit='seconds', leave=False, position=4)
        for x in range(TIME_BETWEEN_LOOP):
            wait_bar.update()
            time.sleep(1)
        wait_bar.close()

con.close() #close connection to database
print("\n\n\n\n")