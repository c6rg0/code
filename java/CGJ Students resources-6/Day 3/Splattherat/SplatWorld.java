import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


public class SplatWorld extends World
{

    /**
     * Constructor for objects of class SplatWorld.
     * 
     */
    public SplatWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600 , 336, 1); 
        addObject(new Score(),6, 6);

        
    }

    public void act() 
    {
        if (Greenfoot.getRandomNumber(3000)< 3){
            int x = Greenfoot.getRandomNumber
                (getWidth());
            int y = Greenfoot.getRandomNumber
                (getHeight());

            
            addObject(new Ribiit(), x, y);
        }
        
           if (Greenfoot.getRandomNumber(2500)< 3){
            int x = Greenfoot.getRandomNumber
                (getWidth());
            int y = Greenfoot.getRandomNumber
                (getHeight());

            addObject(new Rat(), x, y);
        }
        
    
    }

    
}