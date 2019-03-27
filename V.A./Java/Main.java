import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;


public class Main{
    public static void main(String[] args){


        try {

            BufferedImage bff = ImageIO.read(new File("/home/rocker/Pictures/fig_2.png"));
            BufferedImage bff1 = ImageIO.read(new File("/home/rocker/Pictures/fig_2.png"));
            BufferedImage bff2 = ImageIO.read(new File("/home/rocker/Pictures/fig_2.png"));
            
            
            Hilo hilo1 = new Hilo("255 255 0", "unoP", bff);
            Hilo hilo2 = new Hilo("0 0 255", "dosP", bff1);
            Hilo hilo3 = new Hilo("255 0 0", "tresP", bff2);

            hilo1.start();
            hilo2.start();
            hilo3.start();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
    }
}