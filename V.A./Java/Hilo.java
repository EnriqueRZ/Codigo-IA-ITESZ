import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class Hilo extends Thread{

    public String colorC, titulo;
    public BufferedImage img;

    public Hilo(String colorC, String titulo, BufferedImage img){
        this.colorC = colorC;
        this.titulo = titulo;
        this.img = img;
    }

    public void run(){
        int colores;
        String color = "";
        int a, r, g, b, p;
        File f = null;

        for(int i = 0; i < this.img.getWidth(); i++){
            for(int k = 0; k < this.img.getHeight(); k++){
                colores = this.img.getRGB(i, k);

                r = (colores>>16) & 0xff;
                g = (colores>>8) & 0xff;
                b = colores & 0xff;
                color = r+" "+g+" "+b;
                    
                if(!color.equals(this.colorC)){
                    a = r = g = b = 255;
                    p = (a<<24) | (r<<16) | (g<<8) | b;
                    this.img.setRGB(i, k, p);
                }

            }

        }

        try{
            f = new File("/home/rocker/Pictures/"+this.titulo+".png");
            ImageIO.write(this.img, "png", f);
            
        }catch(Exception e){
                System.out.print(e.getMessage());
        }
        
    }

}