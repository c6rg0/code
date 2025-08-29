import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class FlappyWorld extends World
{

    public FlappyWorld()
    {    
        // Create a new world with 600x400 cells with a cell size of 1x1 pixels.
        super(600, 400, 1); 
        addObject(new Player(), 100, 300);
        addObject(new Pipe(), 300, 175);
        addObject(new Pipe(), 600, 175);
        addObject(new Score(), 300, 100);

        prepare();
    }
    //adds the Player, Score and the pipes
    public void gameOver(){
        addObject(new GameOver(), 300, 200);

    }

    /**
     * Prepare the world for the start of the program.
     * That is: create the initial objects and add them to the world.
     */
    private void prepare()
    {
    }
}