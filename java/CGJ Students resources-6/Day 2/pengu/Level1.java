import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


public class Level1 extends World
{
    public Level1() {
        this(new Pengu());

        prepare();
    }

    public Level1(Pengu pengu)
    {    

        super(750, 500, 1); 

        addObject(new Cliff(false), 85,441);
        addObject(new Cliff(true), 665, 441);

        addObject(new Cloud(), 369, 315);
        addObject(pengu, 66,244);
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
    }
}
