import cv2 as cv


class CentroidColor:
    def __init__(self, color_list):
        self.color_list = color_list

    def get_frame_threshold(self, frame):
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        return (cv.inRange(frame_HSV, (self.color_list["LH"], self.color_list["LS"], self.color_list["LV"]), (self.color_list["HH"], self.color_list["HS"], self.color_list["HS"])))

    def get_centroid(self, frame):
        cX1 = None
        cY1 = None
        frame_threshold1 = self.get_frame_threshold(frame)

        im2, contours, hierarchy = cv.findContours(frame_threshold1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)
        if contours:
            len_max_c = len(contours[0])
            count = 0
        for c in contours:
            if(len(c) > len_max_c):
                len_max_c = len(c)
            count += 1
            M = cv.moments(c)
            if M["m00"] != 0:
                cX1 = int(M["m10"] / M["m00"])
                cY1 = int(M["m01"] / M["m00"])
        return (cX1, cY1)

    def __init__(self, color_list):
        self.color_list = color_list

    def get_frame_threshold(self, frame):
        frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        return (cv.inRange(frame_HSV, (self.color_list["LH"], self.color_list["LS"], self.color_list["LV"]), (self.color_list["HH"], self.color_list["HS"], self.color_list["HS"])))

    def get_centroid(self, frame):
        cX2 = None
        cY2 = None
        frame_threshold2 = self.get_frame_threshold(frame)

        im2, contours, hierarchy = cv.findContours(frame_threshold2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_TC89_L1)
        if contours:
            len_max_c = len(contours[0])
            count = 0
        for c in contours:
            if(len(c) > len_max_c):
                len_max_c = len(c)
            count += 1
            M2 = cv.moments(c)
            if M2["m00"] != 0:
                cX2 = int(M2["m10"] / M2["m00"])
                cY2 = int(M2["m01"] / M2["m00"])
        return (cX2, cY2)
