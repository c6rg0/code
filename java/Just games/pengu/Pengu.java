import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Pengu here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Pengu extends Mover
{
    private int level; // we havn't assigned a number to our level because 
    //later on we are going to manipulate our code to check if we have 
    //switched from level1 to level2
    private static final int jumpStrengh = 16;
    private int jumped = 0; 
    
    public Pengu () {
        level = 1;
    }    
    
    public void act(){
        checkKeys();
        checkFall();
        checkNextLevel();
    }
    
    private void checkKeys() {
    
        //if statement to check if key are pressed, then it has to move
        if (Greenfoot.isKeyDown("a")){
            setImage("pengu-left.png");
            moveLeft();
        }    
        
        if (Greenfoot.isKeyDown("d")){
           setImage("pengu-right.png");
           moveRight();
        }
        
        if (Greenfoot.isKeyDown("space")){
            if (onGround()) {
                jump();
            
            }
        }
    } 

    private void checkFall() {
            if(onGround()){
                setVSpeed(0); 
        } else  {
        
            fall();
        
        
        
        
        } 
    } 
        
    private void jump() {
        setVSpeed(-jumpStrengh);
        fall(); //bringing us down
        jumped++; //we add one onto the counter each time we jump
  
    }
    
    private void checkNextLevel() {
        if(getX() == getWorld(). getWidth() -1) {
            if (level == 1) {
               level = 2;
               getWorld().removeObject(this);
               Greenfoot.setWorld(new Level2(this)); 
            } else
            level = 1;
            getWorld().removeObject(this);
            Greenfoot.setWorld(new Level2(this));
        }
    }
}
