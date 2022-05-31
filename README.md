# InertialLabsROS

This is for getting a CSV file of INS-DU sensor data using a Rasperry Pi 4 running Ubuntu 18.04

Once you have the Pi set up and inertiallabs_ros_pkgs installed, here are the steps to read data from the sensor in as a text file and then convert it into a CSV file:

1. Open up three terminal windows/tabs

2. In the first terminal, run the command:
   $ roscore

3. In the second terminal, run the command:
   $ rosrun inertiallabs_ins il_ins _ins_url:=serial:/dev/ttyUSB0:115200 _ins_output_format:=82

4. In the third terminal, run the command:
   $ rostopic echo /Inertial_Labs/ins_data >> <your_file_path/new_file.txt>
   // set whatever filepath you would like for a text file for the data to be saved at

5. Enter ctrl+c into each of the terminals when you are done reading in the data

6. Within the terminal navigate to where the converter.py script is saved and run:
   $ python converter.py <your_file_path/new_file.txt>
   // use the same file path and file name as used in step 4 when creating the text file

7. The new CSV file will be created where the converter.py resides
