import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)


public class Score extends Actor
{
    public static int score; 
    public Score() {
        score = 0;
        
    }
    //by default this lets your score be "0" at the begining
    public void act() 
    {
        World myWorld = getWorld();
        myWorld.showText(String.valueOf(score), 300, 100); 
    }    
    //we created a score system
    public static void add(int num) {
        score += num;
    }
}
