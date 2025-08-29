import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Mover extends Actor  
{
    private static final int speed = 7; //runing speed(sideways)
    private static final int acceleration = 2; //down(gravity)
    private int vSpeed = 0; //current vertical speed
    
    //move a bit to the right
    public void moveRight() {
       setLocation(getX() + speed, getY());  
    
    }
    //move a bit to the left
    public void moveLeft() {
        setLocation(getX() - speed, getY()); 

    }
    //to detect firm ground
    public boolean onGround(){
        Object under = getOneObjectAtOffset(0, getImage().getHeight()/2-8, null);
        return under !=null;
    }
    //sets a speed for verticle movement
    public void setVSpeed(int speed) {
        vSpeed = speed;
    }
    //to apply gravity and add a fall
    public void fall(){
        setLocation(getX(),getY() + vSpeed);
        vSpeed = vSpeed + acceleration;
        if(atBottom()) {
            gameEnd();
    
    
        } 
    }
    
    private boolean atBottom () {
        return getY() >= getWorld().getHeight()-2;
    }   

    private void gameEnd() {
    
        Greenfoot.stop();
    }
    
    
}