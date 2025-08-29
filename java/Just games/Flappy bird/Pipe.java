import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

public class Pipe extends Actor
{
    
    public Pipe(){ 
        GreenfootImage image = getImage();
        image.scale(512,900);
    
    }
    public void act()
    {
        if(Player.isAlive()){
            setLocation(getX() - 1, getY());
       }
       //generates new pipes as you go
       if(getX() <= 1){
           setLocation(getX() + 700, 75 + Greenfoot.getRandomNumber(255));
       }
       //sets random pipes 
   }
}