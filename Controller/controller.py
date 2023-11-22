class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setting_btn_clicked(self):
        end_angle_target_setting_text = self.view.get_end_angle_target_setting_value()
        right_angle_target_setting_text = (
            self.view.get_right_angle_target_setting_value()
        )
        face_angle_target_setting_text = self.view.get_face_width_target_setting_value()

        end_angle_max_setting_text = self.view.get_end_angle_max_value()
        right_angle_max_setting_text = self.view.get_right_angle_max_value()
        face_angle_max_setting_text = self.view.get_face_width_max_value()

        end_angle_min_setting_text = self.view.get_end_angle_min_value()
        right_angle_min_setting_text = self.view.get_right_angle_min_value()
        face_angle_min_setting_text = self.view.get_face_width_min_value()

        self.model.set_end_angle_target_setting_value(end_angle_target_setting_text)
        self.view.set_end_angle_target_value(
            self.model.get_end_angle_target_setting_value()
        )

        self.model.set_right_angle_target_setting_value(right_angle_target_setting_text)
        self.view.set_right_angle_target_value(
            self.model.get_right_angle_target_setting_value()
        )

        self.model.set_face_angle_target_setting_value(face_angle_target_setting_text)
        self.view.set_face_width_target_value(
            self.model.get_face_angle_target_setting_value()
        )

        # -------------------- 驗證輸入值 --------------------
        self.view.check_setting_value()
