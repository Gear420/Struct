from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import os
import ctypes
import math
import _ctypes
import pygame
import sys
if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread
SKELETON_COLORS = [pygame.color.THECOLORS["red"],
                  pygame.color.THECOLORS["blue"],
                  pygame.color.THECOLORS["green"],
                  pygame.color.THECOLORS["orange"],
                  pygame.color.THECOLORS["purple"],
                  pygame.color.THECOLORS["yellow"],
                  pygame.color.THECOLORS["violet"]]
class dumbbell(object):
    def __init__(self,hz,init_time):
        pygame.init()
        self.hz = hz
        self.time = init_time * self.hz
        self.status = 0
        self.counts = 0

        self.font = pygame.font.SysFont("SimHei",28)
        self.eng_font = pygame.font.SysFont("consolas",30)
        self.dig_font = pygame.font.Font("dig.TTF",105)
        self.dig_big_font = pygame.font.Font("dig.TTF",150)
        self.count_font = pygame.font.Font("count.ttf",150)

        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1),
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
        pygame.display.set_caption("windows")
        self._done = False
        self._clock = pygame.time.Clock()
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)
        self._bodies = None
    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState
        joint1State = joints[joint1].TrackingState
        if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked):
            return
        if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
            return
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)
        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except:
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
        v1_x = joint1.x - joint0.x
        v1_y = joint1.y - joint0.y
        v2_x = joint1.x - joint2.x
        v2_y = joint1.y - joint2.y
        angel=(math.acos((v1_x*v2_x+v1_y*v2_y)/((((v1_x**2.0)+(v1_y**2.0))**0.5)*(((v2_x**2.0)+(v2_y**2.0))**0.5)))) * (180/math.pi)
        return angel

    def calc_sports_counts(self, jointl0, jointl1, jointl2, jointr0, jointr1, jointr2):
        angel_l = self.calc_angel(jointl0, jointl1, jointl2)
        angel_r = self.calc_angel(jointr0, jointr1, jointr2)
        if angel_l < 160 and angel_r < 160:
            self.status = 0
        elif self.status == 0:
            self.status = 1
            return 1
        return 0

    def draw_angel_text(self,joint0,joint1,joint2,jointr0,jointr1,jointr2):
        angell = self.calc_angel(joint0,joint1,joint2)
        angell = (int)(angell)
        angell = angell - 80
        if angell > 85:
            angell = (str)(angell)
            self._frame_surface.blit(self.dig_font.render(angell, True, (0,201,87)), (joint1.x,joint1.y))
        else:
            angell = (str)(angell)
            self._frame_surface.blit(self.dig_font.render(angell,True,(255,255,255)),(joint1.x,joint1.y))

        angelr = self.calc_angel(jointr0,jointr1,jointr2)
        angelr = (int)(angelr)
        angelr = angelr - 80
        if angelr > 85:
            angelr = (str)(angelr)
            self._frame_surface.blit(self.dig_font.render(angelr, True, (0,201,87)), (jointr1.x,jointr1.y))
        else:
            angelr = (str)(angelr)
            self._frame_surface.blit(self.dig_font.render(angelr,True,(255,255,255)),(jointr1.x,jointr1.y))





    def draw_counts_text(self, jointl0, jointl1, jointl2, jointr0, jointr1, jointr2):
        self.counts = self.counts + self.calc_sports_counts(jointl0, jointl1, jointl2, jointr0, jointr1, jointr2)
        counts = (str)(self.counts)
        self._frame_surface.blit(self.count_font.render(counts, True, (0,199,140)), (700,890))
    def draw_ui(self):
        self._frame_surface.set_clip(640, 930, 640, 1080)
        self._frame_surface.fill((30,30,30))
        self._frame_surface.set_clip(640, 1073, 500, 1080)
        self._frame_surface.fill((0, 56, 126))
        self._frame_surface.set_clip(1140, 1073, 640, 1080)
        self._frame_surface.fill((250, 202, 46))
        self._frame_surface.set_clip()
    def draw_video(self):
        pass

    def draw_static_font(self):
        self._frame_surface.blit(self.font.render("肱二头肌训练",True,(250, 202, 46,0.3)),(1060,1025))
        #self._frame_surface.blit(self.font.render("times", True, (250, 202, 46)), (700, 1048))
    def draw_time(self,time):
        if(time>60):
            min_time = time / 60
            min_time = (int)(min_time)
            count_time = time - min_time*60
            str_time = (str)(min_time)
            if min_time >= 10:
                self._frame_surface.blit(self.dig_font.render(str_time, True, (255, 255, 255)), (1050, 900))
            elif min_time < 10:
                str_time = '0' + str_time
                self._frame_surface.blit(self.dig_font.render(str_time, True, (255, 255, 255)), (1030, 900))
            self._frame_surface.blit(self.dig_font.render(":",True,(255,255,255)),(1120,900))
            str_time = (str)(count_time)
            if count_time >= 10:
                self._frame_surface.blit(self.dig_font.render(str_time,True,(255,255,255)),(1140,900))
            elif count_time < 10:
                str_time = '0' + str_time
                self._frame_surface.blit(self.dig_font.render(str_time,True,(255,255,255)),(1140,900))
        else:
            str_time = (str)(time)
            if time >= 10:
                self._frame_surface.blit(self.dig_font.render(str_time,True,(255,255,255)),(1140,900))
            elif time < 10:
                str_time = "0" + str_time
                self._frame_surface.blit(self.dig_font.render(str_time,True,(255,255,255)),(1140,900))
    def run(self):
        while not self._done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._done = True
                elif event.type == pygame.VIDEORESIZE:
                    self._screen = pygame.display.set_mode(event.dict['size'],
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None
            if self._kinect.has_new_body_frame():
                self._bodies = self._kinect.get_last_body_frame()

            self.draw_ui()
            self.draw_static_font()

            time = (int)(self.time / self.hz)
            self.draw_time(time)
            if self._bodies is not None:
                for i in range(0, self._kinect.max_body_count):
                    body = self._bodies.bodies[i]
                    time = (int)(self.time / self.hz)
                    self.draw_time(time)
                    if not body.is_tracked:
                        continue
                    joints = body.joints
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    self.draw_body(joints, joint_points, SKELETON_COLORS[i])
                    self.draw_angel_text(joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderRight],joint_points[PyKinectV2.JointType_ElbowRight],joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderLeft],joint_points[PyKinectV2.JointType_ElbowLeft])
                    self.draw_counts_text(joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderRight],joint_points[PyKinectV2.JointType_ElbowRight],joint_points[PyKinectV2.JointType_SpineShoulder],joint_points[PyKinectV2.JointType_ShoulderLeft],joint_points[PyKinectV2.JointType_ElbowLeft])

            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()

            target_height = int(h_to_w * self._screen.get_width())
            pygame.draw.rect(self._frame_surface,(0,0,0),(0,0,640,1080))
            pygame.draw.rect(self._frame_surface,(0,0,0),(1280,0,1920,1080))
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height));
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
            pygame.display.update()
            self._clock.tick(self.hz)
            self.time = self.time - 1
        self._kinect.close()
        pygame.quit()

if __name__ == "__main__":
    g = dumbbell(60,687)
    g.run()
