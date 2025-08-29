import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Player extends Actor
{
        private final double FLAP = 1.8;
        private int y = 300; 
        private double yVel = 0;
        private boolean oldTouchingPipe = false;
        private boolean oldSpace = false;
        private static boolean dead;
    
    public Player(double yVel) {
      GreenfootImage image = getImage();
      image.scale(46,34);
      dead = false;
      this.yVel = yVel;
     
    }
    //this helps rescale the player and add him with velocity related code
    public Player() {
      this(0);
    }
    //making sure the game knows that your location is "0"
       public void act()
    {
       //yVel = yVel + 0.02;
       yVel += 0.02; 
        
       if(spacePressed()) {
            yVel = -FLAP;
        
       }
       //this add a velocity so gravity could be true
   
    
       y += yVel; 
       setLocation(getX(), y);
       setRotation((int)(yVel*16));
       //we added a direction on where the bird is going to go to 
       
       boolean touchingPipe = false;
       //by default, you are not touching the pipe and it makes you not to automatically die on spawn
       for (Pipe pipe: getWorld().getObjects(Pipe.class)) {
            if(Math.abs(pipe.getX() - getX()) <40){
                if(Math.abs(pipe.getY() + 30 - getY()) > 37) {
                    dead = true;
                }
                touchingPipe = true; 
            }
     
        }
        //this generates pipes if you are alive
        if(!oldTouchingPipe && touchingPipe && !dead) {
        Score.add(1);
       } 
       oldTouchingPipe = touchingPipe;
       //this makes the score and adds points to it
       if(isAtEdge()) {
           dead = true;
       
       
       } 
       //this makes the Player "dead" when touching edge
       if(dead){
           FlappyWorld myWorld = (FlappyWorld) getWorld();                                               
           myWorld.gameOver();
           getWorld().removeObject(this);   
       }
       //this add the gameover screen and removes the bird when it dies
      }
    
 
    public boolean spacePressed(){
    
        boolean pressed = false;
        if(Greenfoot.isKeyDown("space")){
            if(!oldSpace){
               pressed = true;
            }
            oldSpace = true;
        }else {
            oldSpace = false;
        }  
         return pressed;
       }
    
    public static boolean isAlive() {
        return !dead;   
      }
      
    }      