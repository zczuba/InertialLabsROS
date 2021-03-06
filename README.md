# InertialLabsROS

This is for getting a CSV file of INS-DU sensor data using a Rasperry Pi 4 running Ubuntu 18.04

Once you have the Pi set up and inertiallabs_ros_pkgs installed (as detailed here: https://us.inertiallabs.com:31443/projects/INS/repos/inertiallabs-ros-pkgs/browse), here are the steps to read data from the sensor in as a text file and then convert it into a CSV file:

1. Save the txt_to_csv_converter.py file to your desired location

2. Open up three terminal windows/tabs

3. In the first terminal, run the command:
   $ roscore

4. In the second terminal, run the command:
   $ rosrun inertiallabs_ins il_ins _ins_url:=serial:/dev/ttyUSB0:115200 _ins_output_format:=82

5. In the third terminal, run the command:
   $ rostopic echo /Inertial_Labs/ins_data >> <your_file_path/new_file.txt>
   // set whatever filepath you would like for a text file for the data to be saved at

6. Enter ctrl+c into each of the terminals when you are done reading in the data

7. Within the terminal navigate to where the txt_to_csv_converter.py script is saved and run:
   $ python txt_to_csv_converter.py <your_file_path/new_file.txt>
   // use the same file path and file name as used in step 4 when creating the text file

8. The new CSV file will be created where the converter.py resides
