import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Level2 extends World
{

    public Level2()
    {    
        this(new Pengu()); 
        prepare();
    }

    public Level2(Pengu pengu) {
        super(750,500,1);

        addObject(new Cliff("ground2.png"),112,337);
        addObject(new Cliff("ground2.png"),578,270);
    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
    }
}