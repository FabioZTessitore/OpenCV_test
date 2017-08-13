/* OpenCV, Display a Picture */

/* using C API */

#include <stdio.h>
#include "highgui.h"

/* $ ./DisplayImage ../../images/person.jpg
*/

int main(int argc, char *argv[])
{
  if (argc < 2) {
    printf("usage: DisplayImage <Image Path>\n");
    return -1;
  }

  /* load the image:
   *
   * module: Image file reading and writing
   */
  IplImage* img = cvvLoadImage(argv[1]); /* macro for cvLoadImage((name),1); */
  if (!img) {
    printf("cannot find the image\n");
    return -1;
  }

  /* create the window and display the image, then wait for a key:
   *
   * module: High-level GUI
   */
  cvNamedWindow("DisplayImage", CV_WINDOW_AUTOSIZE);
  cvShowImage("DisplayImage", img);
  cvWaitKey(0 /* delay, 0 means forever */);

  /* release memory, core functionality */
  cvReleaseImage(&img);

  /* destroy the window:
   *
   * module: High-level GUI
   */
  cvDestroyWindow("DisplayImage");

  return 0;
}
