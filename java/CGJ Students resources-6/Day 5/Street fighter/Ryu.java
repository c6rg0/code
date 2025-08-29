import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Ryu here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Ryu extends Actor
{
    int direction = 1;
    private int movement= 2;
    GreenfootImage stand = new GreenfootImage("standflip.gif");
    
    public void act() 
    {
        checkKeys();
        Jump();
    }    
    
    public void checkKeys() {
        
        if(Greenfoot.isKeyDown("d"))
        {
            setImage("walk.gif");
            setLocation(getX()+ movement,getY());
            direction = 1;
            
        }
        else if (Greenfoot.isKeyDown("a"))
        {
            setImage("standflip.gif");
            setLocation(getX() - movement,getY());
            direction = 2;
            
        }
        
        else setImage("stand.gif");
    }
       
    public void Jump() {
            if(Greenfoot.isKeyDown("w") && direction == 1) {
            setImage("Jump.gif");
            setLocation(getX()+ movement,getY());
            
        }
        else if (Greenfoot.isKeyDown("w") && direction == 2) {
            setImage("JumpLeft.gif");
            setLocation(getX() - movement,getY());            
        }
        
        else setImage("stand.gif");
    }
}
