import processing.net.*;

int shift;
int player_countA;
int player_countB;
int player_countC;
int player_countD;
int player_countE;
int player_countF;
int heightA;
int heightB;
int heightC;
int heightD;
int heightE;
int heightF;
int y = 180;
Client myClient;
int fr = 30;
int speed = 2;
byte[] jsonBytes;
String jsonString;
JSONObject json = new JSONObject();

void setup(){
  size(1920,1080);
  noStroke();
  frameRate(fr);
  shift = 0;
}

void draw(){
  //games requested, send request every minute:
  if(frameCount % (60*fr) == 10){
    myClient = new Client(this, "127.0.0.1", 50007);
    myClient.write("{\"idA\": 244210, \"idB\": 365960, \"idC\": 284160, \"idD\": 1066890, \"idE\": 805550, \"idF\": 378860}");
    println("written, not recieved");
    myClient.readBytes(jsonBytes);
    println("gets here, read ", str(jsonBytes));
    jsonString = new String(jsonBytes);
    println(jsonString);
    json = parseJSONObject(jsonString);
    player_countA = json.getInt("idA");
    player_countB = json.getInt("idB");
    player_countC = json.getInt("idC");
    player_countD = json.getInt("idD");
    player_countE = json.getInt("idE");
    player_countF = json.getInt("idF");
    myClient.stop();
    translate(-5,0);
  }
  background(0);
  heightA = int((float(player_countA)/float(13000))*float(1080));
  heightB = int((float(player_countB)/float(13000))*float(1080));
  heightC = int((float(player_countC)/float(13000))*float(1080));
  heightD = int((float(player_countD)/float(13000))*float(1080));
  heightE = int((float(player_countE)/float(13000))*float(1080));
  heightF = int((float(player_countF)/float(13000))*float(1080));
  
  //draw stacked colored lines
  fill(255,0,0);  //assetto corsa
  rect((width+shift)-5, height-heightA, 5, heightA);
  
  fill(255,204,60); //rFactor 2
  rect((width+shift)-5, (height-heightA)-heightB, 5, heightB);
  
  fill(134,199,255); //beamng.drive
  rect((width+shift)-5, ((height-heightA)-heightB)-heightC, 5, heightC);
  
  fill(128,255,0); //automobilista 2
  rect((width+shift)-5, (((height-heightA)-heightB)-heightC)-heightD, 5, heightD);
  
  fill(150,0,0); //assetto corsa competizione
  rect((width+shift)-5, ((((height-heightA)-heightB)-heightC)-heightD)-heightE, 5, heightE);

  fill(0,0,255); //project cars 2
  rect((width+shift)-5, (((((height-heightA)-heightB)-heightC)-heightD)-heightE)-heightF, 5, heightF);

}
