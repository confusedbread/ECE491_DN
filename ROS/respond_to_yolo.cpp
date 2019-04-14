//
//  respond_to_yolo.cpp
//  
//
//  Created by Steve Grosz on 4/13/19.
//

#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
#include <std_msgs/String.h>

ros::Publisher vel_pub;
ros::Subscriber yolo_sub;

geometry_msgs::Twist my_twist;

void move_forward (){
  my_twist.linear.x = 0.5;
  vel_pub.publish(my_twist);
}

void stop (void){
  my_twist.linear.x = 0.0;
  my_twist.linear.y = 0.0;
  my_twist.linear.z = 0.0;
  my_twist.angular.x = 0.0;
  my_twist.angular.y = 0.0;
  my_twist.angular.z = 0.0;
  vel_pub.publish(my_twist);
}

void respond_to_yolo (const std_msgs::String& msg)
{
  std::string text = msg.data.c_str();
  ROS_INFO("%s \n", text);
  
  if (text == "Ambulance") {
    stop();
  } else if (text == "Fire Truck") {
    stop();
  } else {
    move_forward();
  }
}

int main(int argc, char **argv)
{
  // ROS environment
  ros::init(argc, argv, "respond_to_yolo");
  ros::NodeHandle n;
  
  vel_pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 2);
  yolo_sub = n.subscribe("yolo_output", 2, respond_to_yolo);
  
  ros::spin();
  
  return 0;
}

