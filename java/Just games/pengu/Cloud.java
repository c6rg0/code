import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


public class Cloud extends Actor
{
    private int speed = 4; //moving sideways
    private int leftTurn = 270; 
    private int rightTurn = 480;
    
    
     public void act()
    {
       setLocation(getX() + speed, getY()); 
       
        Actor actor = getOneIntersectingObject(null);
        
        if(actor != null) {
            actor.setLocation( actor.getX()+ speed,actor.getY());
        }    
        
        if (atTurningPoint()) {
            speed = -speed;
        }
    }
    
    public boolean atTurningPoint() {
        return (getX() <= leftTurn || getX() >= rightTurn);
    
    
   }
}