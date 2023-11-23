from Controller.controller import KeyenceController


class Model:
    def __init__(self):
        self.end_angle_target_setting_value = 0
        self.right_angle_target_setting_value = 0
        self.face_width_target_setting_value = 0

        self.end_angle_max_setting_value = 0
        self.right_angle_max_setting_value = 0
        self.face_width_max_setting_value = 0

        self.end_angle_min_setting_value = 0
        self.right_angle_min_setting_value = 0
        self.face_width_min_setting_value = 0

        self.sensor_A_detection_text = ""
        self.sensor_B_detection_text = ""
        self.final_detection_text = ""

    def get_end_angle_target_setting_value(self):
        return self.end_angle_target_setting_value

    def set_end_angle_target_setting_value(self, end_angle_target_setting_value):
        self.end_angle_target_setting_value = end_angle_target_setting_value

    def get_right_angle_target_setting_value(self):
        return self.right_angle_target_setting_value

    def set_right_angle_target_setting_value(self, right_angle_target_setting_value):
        self.right_angle_target_setting_value = right_angle_target_setting_value

    def get_face_width_target_setting_value(self):
        return self.face_width_target_setting_value

    def set_face_width_target_setting_value(self, face_width_target_setting_value):
        self.face_width_target_setting_value = face_width_target_setting_value

    def get_end_angle_max_setting_value(self):
        return self.end_angle_max_setting_value

    def set_end_angle_max_setting_value(self, end_angle_max_setting_value):
        self.end_angle_max_setting_value = end_angle_max_setting_value

    def get_right_angle_max_setting_value(self):
        return self.right_angle_max_setting_value

    def set_right_angle_max_setting_value(self, right_angle_max_setting_value):
        self.right_angle_max_setting_value = right_angle_max_setting_value

    def get_face_width_max_setting_value(self):
        return self.face_width_max_setting_value

    def set_face_width_max_setting_value(self, face_width_max_setting_value):
        self.face_width_max_setting_value = face_width_max_setting_value

    def get_end_angle_min_setting_value(self):
        return self.end_angle_min_setting_value

    def set_end_angle_min_setting_value(self, end_angle_min_setting_value):
        self.end_angle_min_setting_value = end_angle_min_setting_value

    def get_right_angle_min_setting_value(self):
        return self.right_angle_min_setting_value

    def set_right_angle_min_setting_value(self, right_angle_min_setting_value):
        self.right_angle_min_setting_value = right_angle_min_setting_value

    def get_face_width_min_setting_value(self):
        return self.face_width_min_setting_value

    def set_face_width_min_setting_value(self, face_width_min_setting_value):
        self.face_width_min_setting_value = face_width_min_setting_value

    def keyence_ip(self):
        return "192.168.3.10"

    def keyence_port(self):
        return 8500

    def get_sensor_A_detection_text(self):
        return self.sensor_A_detection_text

    def set_sensor_A_detection_text(self, sensor_A_detection_text):
        self.sensor_A_detection_text = sensor_A_detection_text

    def get_sensor_B_detection_text(self):
        return self.sensor_B_detection_text

    def set_sensor_B_detection_text(self, sensor_B_detection_text):
        self.sensor_B_detection_text = sensor_B_detection_text

    def get_final_detection_text(self):
        return self.final_detection_text

    def set_final_detection_text(self, final_detection_text):
        self.final_detection_text = final_detection_text
