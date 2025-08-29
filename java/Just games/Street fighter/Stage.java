import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Stage extends World
{

    private Ryu ryu;
    
    public Stage()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(1000, 600, 1); 
        ryu = new Ryu();
        addObject(ryu, 524, 434);
    }

}
