import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Cliff here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Cliff extends Actor
{
    
    public Cliff() {
    }
    
    public Cliff(String image) {
        setImage(image);
    }
    public Cliff(boolean flip) {
       
        if(flip) {
            getImage().mirrorHorizontally();
        
        }   
    } 
}  