# SimRacing_Playercount_Display
SimRacing Playercount Display

(Following changes made shortly after the deadline at 2/13/2021@1am EST just to give basic functionality instructions)

Currently non-functional :'(

The Python script "sudo python3 concurr.py" must be running before the processing display client/test client starts.  To change the 6 games to any steam games of your choice, change the appid's in line 35 of the processing script:

client.write("{\"idA\": 244210, \"idB\": 365960, \"idC\": 284160, \"idD\": 1066890, \"idE\": 805550, \"idF\": 378860}");

Or since the processing script doesn't currently work, if you'd like to do the same with the test client, change line 10:


send\_string = "{\"idA\": 244210, \"idB\": 365960    , \"idC\": 284160, \"idD\": 1066890, \"idE\": 805550    , \"idF\": 378860}"

The python test client "sudo python3 testclient.py" only updates the LED's based on the API once every time it is run.  Only the future working version of the Processing client can periodically ask for updates.  

Currently the colors are layed out this way:

A: Assetto Corsa: [25,0,0]
B: RFactor 2: [25,11,0]
C: Beamng.Drive: [25,25,0]
D: Automobilista 2: [12,25,0]
E: Assetto Corsa Competizione: [16,0,25]
F: Project Cars 2: [0,0,25]

