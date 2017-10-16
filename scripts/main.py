#!/usr/bin/env python
from evakit import *
from Tkinter import *

if __name__ == '__main__':
    try:
        rospy.init_node('example_node', anonymous=True)
        rate = rospy.Rate(10)  # 10hz

        my_bumper = bumper()

        my_ir0 = ir(0)
        my_ir1 = ir(1)

        my_sonar0 = sonar(0)
        my_sonar1 = sonar(1)

        my_motor = motor()

        my_odometer = odom()
        
        #my_motor.stop() #if you want to stop motors
        def  f_button1():
            my_motor.set_linear_speed(0.2)
            my_motor.set_angular_speed(0.0)
            my_motor.run()
        def  f_button2():
            my_motor.set_linear_speed(-0.2)
            my_motor.set_angular_speed(0.0)
            my_motor.run()
        def  f_button3():
            my_motor.set_linear_speed(0.0)
            my_motor.set_angular_speed(-0.4)
            my_motor.run()
        def  f_button4():
            my_motor.set_linear_speed(0.0)
            my_motor.set_angular_speed(0.4)
            my_motor.run()
        def  f_button5():
            my_motor.stop()
        
        root = Tk()
        root.title("EVAKIT_TEST")

        IR0_range = IntVar()
        label_IR0 = Label(root, text="IR0 range=").grid(row=0, column=0, sticky=E)
        
        IR1_range = IntVar()
        label_IR1 = Label(root, text="IR1 range=").grid(row=1, column=0, sticky=E)
        
        Sonar0_range = IntVar()
        label_Sonar0_range = Label(root, text="Sonar0 range=").grid(row=2, column=0, sticky=E)
        
        Sonar1_range = IntVar()
        label_Sonar1_range = Label(root, text="Sonar1 range=").grid(row=3, column=0, sticky=E)
        
        state_Bumper0 = IntVar()
        label_state_Bumper0 = Label(root, text="Bumper0 state=").grid(row=4, column=0, sticky=E)

        Odometer_pos_x = IntVar()
        Odometer_pos_y = IntVar()
        Odometer_pos_z = IntVar()
        Odometer_vel_x = IntVar()
        Odometer_vel_z = IntVar()
        Odometer_ori_z = IntVar()
        Odometer_ori_w = IntVar()

        Sonar0_ok = StringVar()
        Sonar1_ok = StringVar()

        ir0_ok = StringVar()
        ir1_ok = StringVar()

        label_Odometer_pos_x = Label(root, text="pos_x=").grid(row=5, column=0, sticky=E)
        label_Odometer_pos_y = Label(root, text="pos_y=").grid(row=6, column=0, sticky=E)
        label_Odometer_pos_z = Label(root, text="pos_z=").grid(row=7, column=0, sticky=E)
        label_Odometer_vel_x = Label(root, text="vel_x=").grid(row=8, column=0, sticky=E) 
        label_Odometer_vel_z = Label(root, text="vel_z=").grid(row=9, column=0, sticky=E)
        label_Odometer_ori_z = Label(root, text="ori_z=").grid(row=10, column=0, sticky=E) 
        label_Odometer_ori_w = Label(root, text="ori_w=").grid(row=11, column=0, sticky=E)

        entry_IR0_range = Entry(root,textvariable=IR0_range,bd=3).grid(row=0, column=1)
        entry_IR0_ok = Entry(root, textvariable=ir0_ok, bd=3).grid(row=0, column=2)

        entry_IR1_range = Entry(root, textvariable=IR1_range,bd=3).grid(row=1, column=1)
        entry_IR1_ok = Entry(root, textvariable=ir1_ok, bd=3).grid(row=1, column=2)

        entry_Sonar0_range = Entry(root, textvariable=Sonar0_range, bd=3).grid(row=2, column=1)
        entry_Sonar0_ok = Entry(root, textvariable=Sonar0_ok, bd=3).grid(row=2, column=2)

        entry_Sonar1_range = Entry(root, textvariable=Sonar1_range, bd=3).grid(row=3, column=1)
        entry_Sonar1_ok = Entry(root, textvariable=Sonar1_ok, bd=3).grid(row=3, column=2)

        entry_state_Bumper0 = Entry(root, textvariable=state_Bumper0, bd=3).grid(row=4, column=1)

        entry_Odometer_pos_x = Entry(root, textvariable=Odometer_pos_x, bd=3).grid(row=5, column=1)
        entry_Odometer_pos_y = Entry(root, textvariable=Odometer_pos_y, bd=3).grid(row=6, column=1)
        entry_Odometer_pos_z = Entry(root, textvariable=Odometer_pos_z, bd=3).grid(row=7, column=1)
        entry_Odometer_vel_x = Entry(root, textvariable=Odometer_vel_x, bd=3).grid(row=8, column=1)
        entry_Odometer_vel_z = Entry(root, textvariable=Odometer_vel_z, bd=3).grid(row=9, column=1)
        entry_Odometer_ori_z = Entry(root, textvariable=Odometer_ori_z, bd=3).grid(row=10, column=1)
        entry_Odometer_ori_w = Entry(root, textvariable=Odometer_ori_w, bd=3).grid(row=11, column=1)

        button_1=Button(root,text="FORW",command=f_button1).grid(row=12,column=1)
        button_2=Button(root,text="BACK",command=f_button2).grid(row=14,column=1)
        button_3=Button(root,text="RIGHT",command=f_button3).grid(row=13,column=2)
        button_4=Button(root,text="LEFT",command=f_button4).grid(row=13,column=0)
        button_5=Button(root,text="STOP",command=f_button5).grid(row=13,column=1)
        
        my_motor.stop()

        while not rospy.is_shutdown():
            
            rospy.loginfo("---------------------------------")
            # ir0 functions and their usage
            range_ir0 = my_ir0.get_range()
            rospy.loginfo("range of ir0 =" + str(range_ir0))
            # ir1 functions and their usage
            range_ir1 = my_ir1.get_range()
            rospy.loginfo("range of ir1 =" + str(range_ir1))
            # sonar0 functions and their usage
            range_sonar0 = my_sonar0.get_range()
            rospy.loginfo("range of sonar0 =" + str(range_sonar0))
            # sonar1 functions and their usages
            range_sonar1 = my_sonar1.get_range()
            rospy.loginfo("range of sonar1 =" + str(range_sonar1))

            # bumper function and its usage
            state_bumper0 = my_bumper.get_state()
            rospy.loginfo("state of bumper=" + str(state_bumper0))
            # odom functions and their usage
            odometer_pos_x = my_odometer.get_pos_x()
            odometer_pos_y = my_odometer.get_pos_y()
            odometer_pos_z = my_odometer.get_pos_z()
            odometer_vel_x = my_odometer.get_vel_x()
            odometer_vel_z = my_odometer.get_vel_z()
            odometer_ori_z = my_odometer.get_ori_z()
            odometer_ori_w = my_odometer.get_ori_w()
            rospy.loginfo("x position of robot=" + str(odometer_pos_x))
            rospy.loginfo("y position of robot=" + str(odometer_pos_y))
            rospy.loginfo("z position of robot=" + str(odometer_pos_z))
            rospy.loginfo("x velocity of robot=" + str(odometer_vel_x))
            rospy.loginfo("z velocity of robot=" + str(odometer_vel_z))
            rospy.loginfo("z orientation of robot=" + str(odometer_ori_z))
            rospy.loginfo("w orientation of robot=" + str(odometer_ori_w))
            rospy.loginfo("---------------------------------")
    
            IR0_range.set(range_ir0)
            IR1_range.set(range_ir1)

            Sonar0_ok.set(str(my_sonar0.is_it_work()))
            Sonar1_ok.set(str(my_sonar1.is_it_work()))

            ir0_ok.set(str(my_ir0.is_it_work()))
            ir1_ok.set(str(my_ir1.is_it_work()))

            Sonar0_range.set(range_sonar0)
            Sonar1_range.set(range_sonar1)
            
            state_Bumper0.set(state_bumper0)
            
            Odometer_pos_x.set(odometer_pos_x)
            Odometer_pos_y.set(odometer_pos_y)
            Odometer_pos_z.set(odometer_pos_z)
            Odometer_vel_x.set(odometer_vel_x)
            Odometer_vel_z.set(odometer_vel_z)
            Odometer_ori_z.set(odometer_ori_z)
            Odometer_ori_w.set(odometer_ori_w)
            #close_b = Button(root, text="CLOSE", command=quit).grid(row=8, column=2)
            root.update()
            rate.sleep()
            #root.mainloop()

    except rospy.ROSInterruptException:
        pass