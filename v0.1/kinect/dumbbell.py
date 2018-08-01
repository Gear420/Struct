from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import os
import ctypes
import math
import _ctypes
import pygame
import sys
import time

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

# colors for drawing different bodies
SKELETON_COLORS = [pygame.color.THECOLORS["red"],
                  pygame.color.THECOLORS["blue"],
                  pygame.color.THECOLORS["green"],
                  pygame.color.THECOLORS["orange"],
                  pygame.color.THECOLORS["purple"],
                  pygame.color.THECOLORS["yellow"],
                  pygame.color.THECOLORS["violet"]]


class dumbbell(object):
    def __init__(self):
        pygame.init()
        self.time = 3600

        self.status=0

        self.counts = 0

        self.font = pygame.font.SysFont("Msyh",150)

        self.font_height = self.font.get_height()

        self.num_font = pygame.font.SysFont("Msyh",30)

        self.cn_font = pygame.font.SysFont("Msyh",58)

        self.time_font = pygame.font.SysFont("Msyh",30)
        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        self.time2_font = pygame.font.SysFont("SimHei",70)


        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()

        print(self._infoObject)

        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1),
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
        print(self._screen)
        # Loop until the user clicks the close button.

        pygame.display.set_caption("windows")

        self._done = False

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Kinect runtime object, we want only color and body frames
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)


        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)




        print(self._kinect.color_frame_desc.Width)
        print(self._kinect.color_frame_desc.Height)

        print(self._frame_surface)



        # here we will store skeleton data
        self._bodies = None


    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState;
        joint1State = joints[joint1].TrackingState;

        # both joints are not tracked
        if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked):
            return

        # both joints are not *really* tracked
        if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
            return

        # ok, at least one is good
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)

        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except: # need to catch it due to possible invalid positions (with inf)
            pass

    def draw_body(self, joints, jointPoints, color):
        # Torso
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Head, PyKinectV2.JointType_Neck);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Neck, PyKinectV2.JointType_SpineShoulder);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_SpineMid);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineMid, PyKinectV2.JointType_SpineBase);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_ShoulderRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder, PyKinectV2.JointType_ShoulderLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipLeft);

        # Right Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderRight, PyKinectV2.JointType_ElbowRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowRight, PyKinectV2.JointType_WristRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_HandRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandRight, PyKinectV2.JointType_HandTipRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_ThumbRight);

        # Left Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderLeft, PyKinectV2.JointType_ElbowLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowLeft, PyKinectV2.JointType_WristLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_HandLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandLeft, PyKinectV2.JointType_HandTipLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_ThumbLeft);

        # Right Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipRight, PyKinectV2.JointType_KneeRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeRight, PyKinectV2.JointType_AnkleRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleRight, PyKinectV2.JointType_FootRight);

        # Left Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipLeft, PyKinectV2.JointType_KneeLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeLeft, PyKinectV2.JointType_AnkleLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleLeft, PyKinectV2.JointType_FootLeft);


    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()




    def calc_angel(self,joint0,joint1,joint2):
        # todo
        v1_x = joint1.x - joint0.x
        v1_y = joint1.y - joint0.y
        #v1_z = joint1.z - joint0.z
        v2_x = joint1.x - joint2.x
        v2_y = joint1.y - joint2.y
        #v2_z = joint1.z - joint2.z
        angel=(math.acos((v1_x*v2_x+v1_y*v2_y)/((((v1_x**2.0)+(v1_y**2.0))**0.5)*(((v2_x**2.0)+(v2_y**2.0))**0.5)))) * (180/math.pi)
        return angel

    def calc_sports_counts(self, jointl0, jointl1, jointl2, jointr0, jointr1, jointr2):
        # todo
        angel_l = self.calc_angel(jointl0, jointl1, jointl2)
        angel_r = self.calc_angel(jointr0, jointr1, jointr2)

        if angel_l < 160 and angel_r < 160:
            self.status = 0
        elif self.status == 0:
            self.status = 1
            return 1
        return 0

    def draw_angel_text(self,joint0,joint1,joint2):
        # todo

        angel = self.calc_angel(joint0,joint1,joint2)
        angel = (int)(angel)
        angel = (str)(angel)

        self._frame_surface.blit(self.font.render(angel, True, (250,202,46)), (joint1.x,joint1.y))


    def draw_counts_text(self, jointl0, jointl1, jointl2, jointr0, jointr1, jointr2):
        # todo

        self.counts = self.counts + self.calc_sports_counts(jointl0, jointl1, jointl2, jointr0, jointr1, jointr2)
        counts = (str)(self.counts)

        self._frame_surface.blit(self.font.render(counts, True, (216,0,102)), (640,36))









    def draw_ui(self):

        self._frame_surface.set_clip(640, 0, 500, 10)
        self._frame_surface.fill((0, 56, 126))
        self._frame_surface.set_clip(1140, 0, 640, 10)
        self._frame_surface.fill((250, 202, 46))
        self._frame_surface.set_clip(640, 10, 640, 270)
        self._frame_surface.fill((117, 207, 219))
        self._frame_surface.set_clip(1160,30,530,200)
        self._frame_surface.fill((0,0,0))
        self._frame_surface.set_clip()

        self._frame_surface.blit(self.cn_font.render("Dumbbell评估",True,(0,0,0),(192,192,192)),(790,60))

        self._frame_surface.blit(self.num_font.render("剩余时间：",True,(0,0,0)),(790,140))


        # count = 10
        # for i in range(10):
        #     countstr = (str)(count)
        #     self._frame_surface.blit(self.num_font.render(countstr ,True,(0,0,0)),(940,40))
        #     time.sleep(1000)


        self._frame_surface.blit(self.num_font.render("已完成次数", True, (0, 0, 0)), (640, 10))
        self._frame_surface.blit(self.num_font.render("Times", True, (0, 0, 0)), (650, 160))
        self._frame_surface.set_clip()


        #self.ui_surface.fill(0,0,200)


    def draw_count(self,time):
        time = (str)(time)
        self._frame_surface.blit(self.time2_font.render(time,True,(0, 56, 126)),(950,115))

    def run(self):
        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'],
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

            # --- Game logic should go here



            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None


            if self._kinect.has_new_body_frame():
                self._bodies = self._kinect.get_last_body_frame()



            self.draw_ui()

            #print(self._bodies)
            # --- draw skeletons to _frame_surface
            if self._bodies is not None:

                #print("max_body_counts:")
                #self._kinect.max_body_count = 6
                #print(self._kinect.max_body_count)
                for i in range(0, self._kinect.max_body_count):
                    body = self._bodies.bodies[i]

                    #print(body.is_tracked)

                    if not body.is_tracked:
                        continue

                    joints = body.joints
                    # convert joint coordinates to color space
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    #print(joint_points[PyKinectV2.JointType_SpineShoulder].x,joint_points[PyKinectV2.JointType_SpineShoulder].y)
                    #print(joint_points[PyKinectV2.JointType_ShoulderRight].x,joint_points[PyKinectV2.JointType_ShoulderRight].y)
                    #print(joint_points[PyKinectV2.JointType_ElbowRight].x,joint_points[PyKinectV2.JointType_ElbowRight].y)
                    #self._frame_surface.blit(self.font.render(, True, (0, 0, 0), (0, 0, 255)), (0, 0))
                    self.draw_body(joints, joint_points, SKELETON_COLORS[i])


                    self.draw_angel_text(joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderRight],joint_points[PyKinectV2.JointType_ElbowRight])


                    self.draw_counts_text(joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderRight],joint_points[PyKinectV2.JointType_ElbowRight],joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderLeft],joint_points[PyKinectV2.JointType_ElbowRight])
                    time = (int)(self.time / 60)
                    self.draw_count(time)
                    #self.draw_ui()

            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # # --- (screen size may be different from Kinect's color frame size)



            #print(self._frame_surface.get_height())

            #print(self._frame_surface.get_height()) #1080
            #print(self._frame_surface.get_width())  #1920


            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()

            print(h_to_w)

            target_height = int(h_to_w * self._screen.get_width())

            print(target_height)

            pygame.draw.rect(self._frame_surface,(0,0,0),(0,0,640,1080))
            pygame.draw.rect(self._frame_surface,(0,0,0),(1280,0,1920,1080))




            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height));

            self._screen.blit(surface_to_draw, (0,0))



            surface_to_draw = None


            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            #pygame.display.flip()

            self._clock.tick(60)
            self.time = self.time - 1

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        pygame.quit()



