/**
 * oscP5sendreceive by andreas schlegel
 * example shows how to send and receive osc messages.
 * oscP5 website at http://www.sojamo.de/oscP5
 */
 
import oscP5.*;
import netP5.*;
  
OscP5 oscP5;
NetAddress myRemoteLocation;

boolean detectado = false;

void setup() {
  size(400,400);
 // frameRate(25);
  /* start oscP5, listening for incoming messages at port 12000 */
  oscP5 = new OscP5(this,7000);
  fill(255,0,0);  
}


void draw() {
  background(0);
  if(detectado){
    fill(255,0,0); 
    ellipse(400/2,400/2,100,100);
  }else{
    fill(255,255,255); 
    ellipse(400/2,400/2,20,20);
  }
}


/* incoming osc message are forwarded to the oscEvent method. */
void oscEvent(OscMessage theOscMessage) {
  /* print the address pattern and the typetag of the received OscMessage */
  //print("### received an osc message.");
  //print(" addrpattern: "+theOscMessage.addrPattern());
  //println(" typetag: "+theOscMessage.typetag());
  int firstValue = theOscMessage.get(0).intValue();
   //println(" values: "+firstValue+", "+secondValue+", "+thirdValue);
   println(" Recibido: "+firstValue);
   if(firstValue == 0){
     detectado = true;
   }else{
     detectado = false;
   }
}
