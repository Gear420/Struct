#coding=utf-8
from KinectTools import PyKinectV2
from KinectTools.PyKinectV2 import *
from KinectTools import PyKinectRuntime
import math
import ctypes
import _ctypes
import pygame
import sys
import time
from ResultPrints.result_ui import result
from faceRecognition.Login import login
import random

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

class stamina(object):
    def __init__(self,screen,n):
        self.data = {}
        self.SKELETON_COLORS = [pygame.color.THECOLORS["red"],
                           pygame.color.THECOLORS["blue"],
                           pygame.color.THECOLORS["green"],
                           pygame.color.THECOLORS["orange"],
                           pygame.color.THECOLORS["purple"],
                           pygame.color.THECOLORS["yellow"],
                           pygame.color.THECOLORS["violet"]]

        self._clock = pygame.time.Clock()
        self._infoObject = pygame.display.Info()
        self.screen = screen
        self.n = n
        self._done = False

        self.status=0
        self.counts = 0
        self.guide_flag = 0
        self.up_flag = 0
        self.login_flag = 0
        self.down_flag = 0
        self._3d_build_flag=0
        self.dynamic_assessment_flag= 0
        self.save_flag =0
        self.success_flag = 0
        self.result_flag = 0


        self.font = pygame.font.SysFont("SimHei",28)
        self.eng_font = pygame.font.SysFont("consolas",30)
        self.dig_font = pygame.font.Font("dig.TTF",105)
        self.dig_big_font = pygame.font.Font("dig.TTF",150)
        self.count_font = pygame.font.Font("count.ttf",150)


        self._clock = pygame.time.Clock()
        self.time =  3 * 60


        self._kinect = PyKinectRuntime.PyKinectRuntime(
            PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)
        self._frame_surface = pygame.Surface(
            (self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)
        self._bodies = None


        self.data["name"] = "张兴宇"
        import datetime
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data["year"] = 24
        self.data["time"] = nowTime
        self.data["height"] = 0
        self.data["weight"] = 0
        self.data["bust"] = 0
        self.data["waist"] = 0
        self.data["hip"] = 0
        self.data["up"] = 0
        self.data["down"] = 0
        self.data["score1"] = random.randint(75,90)
        self.data["score2"] = random.randint(75,90)
    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState;
        joint1State = joints[joint1].TrackingState;



        if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked):
            return

        if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
            return

        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)

        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except:  # need to catch it due to possible invalid positions (with inf)
            pass

    def draw_body(self, joints, jointPoints, color):
        # Torso
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Head, PyKinectV2.JointType_Neck);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_Neck, PyKinectV2.JointType_SpineShoulder);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder,
                            PyKinectV2.JointType_SpineMid);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineMid, PyKinectV2.JointType_SpineBase);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder,
                            PyKinectV2.JointType_ShoulderRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineShoulder,
                            PyKinectV2.JointType_ShoulderLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_HipLeft);

        # Right Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderRight,
                            PyKinectV2.JointType_ElbowRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowRight,
                            PyKinectV2.JointType_WristRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight,
                            PyKinectV2.JointType_HandRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandRight,
                            PyKinectV2.JointType_HandTipRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight,
                            PyKinectV2.JointType_ThumbRight);

        # Left Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ShoulderLeft,
                            PyKinectV2.JointType_ElbowLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowLeft, PyKinectV2.JointType_WristLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_HandLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandLeft,
                            PyKinectV2.JointType_HandTipLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_ThumbLeft);

        # Right Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipRight, PyKinectV2.JointType_KneeRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeRight,
                            PyKinectV2.JointType_AnkleRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleRight,
                            PyKinectV2.JointType_FootRight);

        # Left Leg
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HipLeft, PyKinectV2.JointType_KneeLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_KneeLeft, PyKinectV2.JointType_AnkleLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_AnkleLeft, PyKinectV2.JointType_FootLeft);




    def draw_ui(self,str):

        self._frame_surface.set_clip(740, 820, 540, 140)
        self._frame_surface.fill((30,30,30))
        self._frame_surface.set_clip()
        self._frame_surface.blit(self.font.render(str, True, (250, 202, 46, 0.3)),
                                 (int(266/375*540+695), int(634/667 * 960)))
    def draw_time(self,time):
        time = time / 60
        time = (int)(time)
        time = (str)(time)
        self._frame_surface.blit(self.dig_font.render(time , True, (250,202,46,0.3)),
                                 (int(266/375*540 + 730),int(634/667 * 960 - 120)))
    def dynamic_assessment(self):
        pass
    def _3d_build(self):
        pass
    def render_face(self):
        self._frame_surface.set_clip((740, 0, 540, 100))
        self._frame_surface.fill((0,0,0))
        self._frame_surface.set_clip((740,400, 540, 660))
        self._frame_surface.fill((0,0,0))
        self._frame_surface.set_clip()

        self.back = pygame.image.load("images/back.png")
        self.go =pygame.image.load("images/go.png")
        self.home = pygame.image.load("images/home.png")
        self.loop = pygame.image.load("images/loop.png")

        self._frame_surface.blit(self.back,(740,0))
        self._frame_surface.blit(self.home,(1200,0))
        self._frame_surface.blit(self.loop,(900,500))
        self._frame_surface.blit(self.go,(1080,500))

    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()

    def render_result(self,data,target_surface):
        a = result(data,target_surface)
        a.render()

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

    def draw_counts_text(self, jointl0, jointl1, jointl2, jointr0, jointr1, jointr2):
        self.counts = self.counts + self.calc_sports_counts(jointl0, jointl1, jointl2, jointr0, jointr1, jointr2)
        counts = (str)(self.counts)
        self._frame_surface.blit(self.count_font.render(counts, True, (0,199,140)),
                                 (int(18/375*540 + 740),int(607/667 * 960 - 80)))

    def draw_angel_text(self,joint0,joint1,joint2,jointr0,jointr1,jointr2):
        angell = self.calc_angel(joint0,joint1,joint2)
        angell = int(angell)
        angell = angell - 80
        if angell > 85:
            angell = (str)(angell)
            self._frame_surface.blit(self.dig_font.render(angell, True, (0,201,87)), (joint1.x,joint1.y))
        else:
            angell = (str)(angell)
            self._frame_surface.blit(self.dig_font.render(angell,True,(255,255,255)),(joint1.x,joint1.y))

        angelr = self.calc_angel(jointr0,jointr1,jointr2)
        angelr = int(angelr)
        angelr = angelr - 80
        if angelr > 85:
            angelr = (str)(angelr)
            self._frame_surface.blit(self.dig_font.render(angelr, True, (0,201,87)), (jointr1.x,jointr1.y))
        else:
            angelr = (str)(angelr)
            self._frame_surface.blit(self.dig_font.render(angelr,True,(255,255,255)),(jointr1.x,jointr1.y))

    def facereg(self):
        return True
    def runc(self):
        if self._bodies is not None:
            for i in range(0, self._kinect.max_body_count):
                body = self._bodies.bodies[i]
                if not body.is_tracked:
                    continue

                joints = body.joints

                joint_points = self._kinect.body_joints_to_color_space(joints)

                self.draw_angel_text(joint_points[PyKinectV2.JointType_AnkleRight],
                                         joint_points[PyKinectV2.JointType_KneeRight],
                                         joint_points[PyKinectV2.JointType_HipRight],
                                         joint_points[PyKinectV2.JointType_AnkleLeft],
                                         joint_points[PyKinectV2.JointType_KneeLeft],
                                         joint_points[PyKinectV2.JointType_HipLeft])

                self.draw_counts_text(joint_points[PyKinectV2.JointType_AnkleRight],
                                          joint_points[PyKinectV2.JointType_KneeRight],
                                          joint_points[PyKinectV2.JointType_HipRight],
                                          joint_points[PyKinectV2.JointType_AnkleLeft],
                                          joint_points[PyKinectV2.JointType_KneeLeft],
                                          joint_points[PyKinectV2.JointType_HipLeft])



    def rund(self):
        if self._bodies is not None:
            for i in range(0, self._kinect.max_body_count):
                body = self._bodies.bodies[i]
                if not body.is_tracked:
                    continue
                joints = body.joints
                joint_points = self._kinect.body_joints_to_color_space(joints)
                self.draw_body(joints, joint_points, self.SKELETON_COLORS[i])
                self.draw_angel_text(joint_points[PyKinectV2.JointType_SpineShoulder],
                                     joint_points[PyKinectV2.JointType_ShoulderRight],
                                     joint_points[PyKinectV2.JointType_ElbowRight],
                                     joint_points[PyKinectV2.JointType_SpineShoulder],
                                     joint_points[PyKinectV2.JointType_ShoulderLeft],
                                     joint_points[PyKinectV2.JointType_ElbowLeft])

                self.draw_counts_text(joint_points[PyKinectV2.JointType_SpineShoulder],
                                      joint_points[PyKinectV2.JointType_ShoulderRight],
                                      joint_points[PyKinectV2.JointType_ElbowRight],
                                      joint_points[PyKinectV2.JointType_SpineShoulder],
                                      joint_points[PyKinectV2.JointType_ShoulderLeft],
                                      joint_points[PyKinectV2.JointType_ElbowLeft])
    def guide(self):
        self._frame_surface.set_clip()
        self._frame_surface.fill((0,0,0))
        self._frame_surface.blit(self.font.render("请等待五秒进入下一个动作",True,(225,225,225)),(790,200))
    def run(self):
        while not self._done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._done = True
                elif event.type == pygame.VIDEORESIZE:
                    self._screen = pygame.display.set_mode(event.dict['size'],
                                                           pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE, 32)

            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None

            if self.login_flag == 0:
                self.render_face()
                if self.facereg():
                    print("face reg suceess!")
                    if self.time <= 0:
                        self.success_flag = 1
                if self.success_flag == 1:
                    self._frame_surface.blit(self.font.render("认证成功..." , True ,(120,120,120)) , (950,450))
                elif self.success_flag == 0:
                    self._frame_surface.blit(self.font.render("认证中..." , True , (120,120,120)), (950,450))
                if self.success_flag == 1 and self.time < 0:
                    time.sleep(3)
                    self.time = 31 * 60
                    self.login_flag = 1
            elif self.login_flag == 1:
                if self.up_flag == 0 and self.guide_flag == 0 and self.down_flag == 0:
                    print(self.time)
                    print("into up")
                    self.draw_ui("上肢力量评估")
                    self.draw_time(self.time)
                    self.rund()
                    if self.time <= 0:
                        self.up_flag = 1
                        self.data["up"] = self.counts
                        self.time = 5 * 60
                elif self.guide_flag ==  0 and self.up_flag == 1 and self.down_flag == 0:
                    print(self.time)
                    print("guide into")
                    self.guide()
                    if self.time <= 0:
                        self.guide_flag = 1
                        self.time = 31 * 60
                elif self.guide_flag == 1 and self.down_flag == 0 and self.up_flag == 1:
                    print(self.time)
                    print("down into")
                    self.draw_ui("下肢力量评估")
                    self.draw_time(self.time)
                    self.runc()
                    if self.time == 0:
                        self.down_flag = 1
                        self.data["down"] = self.counts
                        self.result_flag = 1
                elif self.result_flag == 1:
                    print("into result")
                    self.render_result(self.data,self._frame_surface)


            rect = (740, 0, int(1080/2), int(1920/2))
            surface_to_draw = pygame.Surface.subsurface(self._frame_surface, rect)
            surface_to_draw = pygame.transform.smoothscale(surface_to_draw, (int(2160/self.n),int(3840/self.n)))
            self.screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None
            pygame.display.update()
            self._clock.tick(60)
            self.time = self.time - 1
