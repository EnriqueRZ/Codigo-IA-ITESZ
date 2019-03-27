import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class prueba{
    public static void main(String[] args){

        String color = "";
        int a, r, g, b, p;
        File f = null;
        try {

            BufferedImage bff = ImageIO.read(new File("/home/rocker/Pictures/fig_2.png"));

            for(int i = 0; i < bff.getWidth(); i++){
                for(int k = 0; k < bff.getHeight(); k++){
                    int colores = bff.getRGB(i, k);

                    r = (colores>>16) & 0xff;
                    g = (colores>>8) & 0xff;
                    b = colores & 0xff;
                    color = r+" "+g+" "+b;
                    System.out.println(color);
                    
                    if(!color.equals("0 0 255")){
                        a = r = g = b = 255;
                        p = (a<<24) | (r<<16) | (g<<8) | b;
                        bff.setRGB(i, k, p);

                    }

                }

            }

            f = new File("/home/rocker/Pictures/out.png");
            ImageIO.write(bff, "png", f);

        } catch (Exception e) {

            System.out.println(e.getMessage());

        }
        
    }
}