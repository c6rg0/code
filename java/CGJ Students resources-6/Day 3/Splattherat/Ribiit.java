import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


public class Ribiit extends Actor
{
    /**
     * Act - do whatever the Rat wants to do. This method is called whenever
     * the 'Act' or 'Run' button gets pressed in the environment.
     */
    public void act() 
    {
        if(Greenfoot.mouseClicked(this)) {
                int x = Greenfoot.getRandomNumber
            (getWorld().getWidth());
                int y = Greenfoot.getRandomNumber
            (getWorld().getHeight());
        
                getWorld().addObject(new Ribiit(), x, y);
                getWorld().removeObject(this);
                Score.add(50);
        }
    }   
    
}
