import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Crab here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Crab extends Actor
{
    /**
     * Act - do whatever the Crab wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    { 
        moveAndTurn(); 
        eat();
    }
    //this created movement that the crab uses
    public void moveAndTurn(){    
            
        if(Greenfoot.isKeyDown("a"))
        {
            turn(-3);
        }
        if(Greenfoot.isKeyDown("d"))
        {
            turn(3);
        }
        if(Greenfoot.isKeyDown("w"))
        {
            move(3);
        }
        if (Greenfoot.isKeyDown("s"))
        {
            move(-3);
        }
    }             
    //this eat method will make the crab eat the worm when touched
    // in theory this will remove the worm from the game
    public void eat()   {
        Actor crab;
        crab = getOneObjectAtOffset(0,0,Worm.class);
        
        if(crab != null) {
            World world;
            world = getWorld();
            world.removeObject(crab); 
            
        } 
    }
}   