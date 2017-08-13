/* OpenCV, Display a Picture */

/* using C++ API */

#include <iostream>
#include "highgui.h"

/* $ ./DisplayImage ../../images/person.jpg
*/

int main(int argc, char *argv[])
{
  if (argc < 2) {
    std::cout << "usage: DisplayImage <Image Path>\n";
    return -1;
  }

  /* load the image:
   *
   * module: Image file reading and writing
   */
  cv::Mat img = cv::imread(argv[1]);
  if (!img.data) {
    std::cout << "cannot find the image\n";
    return -1;
  }

  /* create the window and display the image, then wait for a key:
   *
   * module: High-level GUI
   */
  cv::namedWindow("DisplayImage", cv::WINDOW_AUTOSIZE);
  cv::imshow("DisplayImage", img);
  cv::waitKey(0);

  /* destroy the window:
   *
   * module: High-level GUI
   */
  cv::destroyWindow("DisplayImage");

  return 0;
}
