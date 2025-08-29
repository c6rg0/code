import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Crabworld here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Crabworld extends World
{

    /**
     * Constructor for objects of class Crabworld.
     * 
     */
    public Crabworld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        prepare();
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
        Crab crab = new Crab();
        addObject(crab,270,181);
        Worm worm = new Worm();
        addObject(worm,54,88);
        Worm worm2 = new Worm();
        addObject(worm2,245,53);
        Worm worm3 = new Worm();
        addObject(worm3,106,341);
        Worm worm4 = new Worm();
        addObject(worm4,76,200);
        Worm worm5 = new Worm();
        addObject(worm5,295,316);
        Worm worm6 = new Worm();
        addObject(worm6,414,252);
        Worm worm7 = new Worm();
        addObject(worm7,454,96);
        Worm worm8 = new Worm();
        addObject(worm8,479,314);
        worm6.setLocation(501,230);
        worm7.setLocation(481,68);
        crab.setLocation(284,194);
        Lobster lobster = new Lobster();
        addObject(lobster,43,26);
        crab.setLocation(533,349);
    }
}
