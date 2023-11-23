import datetime
import os
import random
import socket

import numpy as np
import pandas as pd
from PyQt6.QtCore import QThread, pyqtSignal


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setting_btn_clicked(self):
        self.model.set_end_angle_target_setting_value(
            self.view.get_end_angle_target_setting_value()
        )
        self.view.set_end_angle_target_value(
            self.model.get_end_angle_target_setting_value()
        )

        self.model.set_right_angle_target_setting_value(
            self.view.get_right_angle_target_setting_value()
        )
        self.view.set_right_angle_target_value(
            self.model.get_right_angle_target_setting_value()
        )

        self.model.set_face_width_target_setting_value(
            self.view.get_face_width_target_setting_value()
        )
        self.view.set_face_width_target_value(
            self.model.get_face_width_target_setting_value()
        )

        # -------------------- 驗證輸入值 --------------------
        self.view.check_setting_value()

        self.view.set_start_btn_status(True)

    def start_btn_clicked(self):
        self.view.close_setting_page_ui()
        self.view.set_start_btn_status(False)
        self.view.set_stop_btn_status(True)

        self.keyence_system_thread = KeyenceController(
            self.model.keyence_ip(), self.model.keyence_port(), self.view, self.model
        )
        if self.keyence_system_thread.connect_tcp_ip():
            self.view.update_keyence_sensor_status("連線成功", "green")
            self.keyence_system_thread.signal.connect(
                self.keyence_system_thread.update_keyence_data
            )
            self.keyence_system_thread.start()
        else:
            self.view.update_keyence_sensor_status("連線失敗", "red")

    def stop_btn_clicked(self):
        self.view.set_start_btn_status(True)

        self.keyence_system_thread.stop()
        if self.keyence_system_thread.isRunning() == False:
            self.view.update_keyence_sensor_status("連線中斷", "red")


class KeyenceController(QThread):
    signal = pyqtSignal(list)

    def __init__(self, ip, port, view, model):
        super().__init__()
        self.is_running = True
        self.host = ip
        self.port = port
        self.view = view
        self.model = model
        self.client = self.connect_tcp_ip()

    def connect_tcp_ip(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        return self.client

    def collect_keyence_sensor_data(self, client_socket):
        senor_a_end_angle, sensor_a_right_angle, sensor_a_face_width = [], [], []
        senor_b_end_angle, sensor_b_right_angle, sensor_b_face_width = [], [], []

        # 接收3次資料，並將資料算平均
        for i in range(3):
            data = client_socket.recv(1024)
            data = data.decode("utf-8")
            data_list = data.split(",")
            data_float = [float(i) for i in data_list]
            senor_a_end_angle.append(data_float[0])
            sensor_a_right_angle.append(data_float[1])
            sensor_a_face_width.append(data_float[2])
            senor_b_end_angle.append(data_float[3])
            sensor_b_right_angle.append(data_float[4])
            sensor_b_face_width.append(data_float[5])

        result = [
            np.mean(senor_a_end_angle),
            np.mean(sensor_a_right_angle),
            np.mean(sensor_a_face_width),
            np.mean(senor_b_end_angle),
            np.mean(sensor_b_right_angle),
            np.mean(sensor_b_face_width),
        ]
        result = [round(i, 2) for i in result]
        return result

    def update_keyence_data(self, result):
        num = random.randint(0, 5)
        # Todo:要改成鋼管的侵入感測器有看到鋼管才會去做判斷
        if num == 0:
            # auto data
            result[1] = round(random.uniform(59.1, 59.2), 2)
            result[0] = round(random.uniform(89.85, 89.89), 2)
            result[2] = round(random.uniform(1, 1.1), 2)
            result[4] = round(random.uniform(59.1, 59.2), 2)
            result[3] = round(random.uniform(89.85, 89.89), 2)
            result[5] = round(random.uniform(1, 1.1), 2)

            self.view.set_sensor_A_end_angle_value(result[1])
            self.view.set_sensor_A_right_angle_value(result[0])
            self.view.set_sensor_A_face_width_value(result[2])

            self.view.set_sensor_B_end_angle_value(result[4])
            self.view.set_sensor_B_right_angle_value(result[3])
            self.view.set_sensor_B_face_width_value(result[5])

            self.detection_value_judgment(result)

    def detection_value_judgment(self, result):
        # -------------------- catch target value --------------------
        end_angle_target_value = float(self.model.get_end_angle_target_setting_value())
        right_angle_target_value = float(
            self.model.get_right_angle_target_setting_value()
        )
        face_width_target_value = float(
            self.model.get_face_width_target_setting_value()
        )

        # -------------------- catch max value --------------------
        self.model.set_end_angle_max_setting_value(self.view.get_end_angle_max_value())
        end_angle_max_value = float(self.model.get_end_angle_max_setting_value())

        self.model.set_right_angle_max_setting_value(
            self.view.get_right_angle_max_value()
        )
        right_angle_max_value = float(self.model.get_right_angle_max_setting_value())

        self.model.set_face_width_max_setting_value(
            self.view.get_face_width_max_value()
        )
        face_width_max_value = float(self.model.get_face_width_max_setting_value())

        # -------------------- catch min value --------------------
        self.model.set_end_angle_min_setting_value(self.view.get_end_angle_min_value())
        end_angle_min_value = float(self.model.get_end_angle_min_setting_value())

        self.model.set_right_angle_min_setting_value(
            self.view.get_right_angle_min_value()
        )
        right_angle_min_value = float(self.model.get_right_angle_min_setting_value())

        self.model.set_face_width_min_setting_value(
            self.view.get_face_width_min_value()
        )
        face_width_min_value = float(self.model.get_face_width_min_setting_value())

        # -------------------- keyence sensor A --------------------
        sensor_A_end_angle_value = float(result[1])
        sensor_A_right_angle_value = float(result[0])
        sensor_A_face_width_value = float(result[2])

        # -------------------- keyence sensor B --------------------
        sensor_B_end_angle_value = float(result[4])
        sensor_B_right_angle_value = float(result[3])
        sensor_B_face_width_value = float(result[5])

        # -------------------- detection value judgment --------------------
        if (
            sensor_A_end_angle_value <= end_angle_target_value + end_angle_max_value
            and sensor_A_end_angle_value >= end_angle_target_value - end_angle_min_value
            and sensor_A_right_angle_value
            <= right_angle_target_value + right_angle_max_value
            and sensor_A_right_angle_value
            >= right_angle_target_value - right_angle_min_value
            and sensor_A_face_width_value
            <= face_width_target_value + face_width_max_value
            and sensor_A_face_width_value
            >= face_width_target_value - face_width_min_value
        ):
            self.view.set_sensor_A_judgment_status("OK", "green")
        else:
            self.view.set_sensor_A_judgment_status("NG", "red")

        if (
            sensor_B_end_angle_value <= end_angle_target_value + end_angle_max_value
            and sensor_B_end_angle_value >= end_angle_target_value - end_angle_min_value
            and sensor_B_right_angle_value
            <= right_angle_target_value + right_angle_max_value
            and sensor_B_right_angle_value
            >= right_angle_target_value - right_angle_min_value
            and sensor_B_face_width_value
            <= face_width_target_value + face_width_max_value
            and sensor_B_face_width_value
            >= face_width_target_value - face_width_min_value
        ):
            self.view.set_sensor_B_judgment_status("OK", "green")
        else:
            self.view.set_sensor_B_judgment_status("NG", "red")

        self.model.set_sensor_A_detection_text(self.view.get_sensor_A_judgment_status())
        sensor_A_result = self.model.get_sensor_A_detection_text()

        self.model.set_sensor_B_detection_text(self.view.get_sensor_B_judgment_status())
        sensor_B_result = self.model.get_sensor_B_detection_text()

        if sensor_A_result == "OK" and sensor_B_result == "OK":
            self.view.set_final_judgment_status("OK", "green")
            self.model.set_final_detection_text(self.view.get_final_judgment_status())
            final_result = self.model.get_final_detection_text()
            self.save_data_to_csv(
                final_result,
                result,
                datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),
            )
            self.get_counter()
        else:
            self.view.set_final_judgment_status("NG", "red")
            self.model.set_final_detection_text(self.view.get_final_judgment_status())
            final_result = self.model.get_final_detection_text()
            self.save_data_to_csv(
                final_result,
                result,
                datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),
            )
            self.view.show_error_data(
                result, datetime.datetime.now().strftime("%H:%M:%S")
            )
            self.get_counter()

    def save_data_to_csv(self, final_result, result, time):
        keyence_data_path = "./KeyenceData/"
        if not os.path.isdir(keyence_data_path):
            os.mkdir(keyence_data_path)

        now = datetime.datetime.now()
        file_name = f"{keyence_data_path}" + now.strftime("%Y%m%d") + ".csv"
        header = not os.path.exists(file_name) or os.stat(file_name).st_size == 0
        with open(file_name, "a", encoding="utf-8") as f:
            if header:
                f.write(
                    "sensor_A_end_angle,sensor_A_right_angle,sensor_A_face_width,"
                    "sensor_B_end_angle,sensor_B_right_angle,sensor_B_face_width,"
                    "final_result,"
                    "date\n"
                )
            f.write(
                f"{result[1]},{result[0]},{result[2]},"
                f"{result[4]},{result[3]},{result[5]},"
                f"{final_result},"
                f"{time}\n"
            )

    def get_counter(self):
        data = pd.read_csv(
            "./KeyenceData/" + datetime.datetime.now().strftime("%Y%m%d") + ".csv"
        )
        ok_data = data[data["final_result"] == "OK"]
        ng_data = data[data["final_result"] == "NG"]

        self.view.set_count(len(ok_data))
        self.view.set_total_count(len(ok_data) + len(ng_data))
        self.view.set_ng_count(len(ng_data))

    def run(self):
        while self.is_running:
            result = self.collect_keyence_sensor_data(self.client)
            self.signal.emit(result)

    def stop(self):
        self.is_running = False
        self.quit()
        self.wait()
        print("KeyenceController stop")
