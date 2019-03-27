#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"
 
using namespace cv;
using namespace std;

int main() {
  
    cv::Mat img;
    img = cv::imread("/home/rocker/Documents/I.A./Vision Artificial/C++/fig_2.png" , CV_LOAD_IMAGE_COLOR);

    cout << "Tamño: " << endl << img.rows << " " << img.cols << endl;

    for(int i = 0; i < img.rows; i++){
        for(int j = 0; j < img.cols; j++){
            Vec3b intensity2 = img.at<Vec3b>(i, j);    
            int blue = intensity2.val[0];
            int green = intensity2.val[1];
            int red = intensity2.val[2];

            cout << " " << blue << " " << green << " " << red << endl << endl;
        }
    }
    //printf("'\a' << Printer error!!!\n"); 

    if(! img.data ) {
        std::cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    }
    
  
    return 0;
}
