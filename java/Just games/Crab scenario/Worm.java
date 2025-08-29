import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Worm here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Worm extends Actor
{
    /**
     * Act - do whatever the Worm wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
       eat(); 
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