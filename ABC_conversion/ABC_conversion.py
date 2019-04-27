# coding:utf-8
# @author : csl
# @description : 小工具开发

from tkinter import *
import hashlib
import time
from googletrans import Translator

LOG_LINE_NUM = 0

class MY_GUI_SET():
    """测试小工具"""
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("内部测试工具  开发者：潜行100  问题反馈：QQ35643856")
        self.init_window_name.geometry("1068x681+10+10")
        # init_window["bg"] = "pink"
        self.init_window_name.attributes("-alpha", 0.9)  # 虚化 值越小虚化程度越高

        # 标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮-字符串转MD5
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=10,
                                              command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
        # 按钮-翻译
        self.trans_button = Button(self.init_window_name, text="GOOGLE翻译", bg="lightblue", width=10, command=self.trans_google)
        self.trans_button.grid(row=2, column=11)
        # 按钮-‘’拼接
        self.quotation_marks_button = Button(self.init_window_name, text='引号拼接', bg='lightblue', width=10, command=self.quotation_marks)
        self.quotation_marks_button.grid(row=3, column=11)

    # 功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        # print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                # print(myMd5_Digest)
                # 输出到界面
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")

    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    # 日志动态打印
    def write_log_to_Text(self, logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) + " " + str(logmsg) + "\n"  # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)

    # 检查字符串是否为中文，其中一个为中文则判断为中文
    def check_contain_chinese(self, check_str):
        for ch in check_str:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    # 谷歌翻译
    def trans_google(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "")
        if src:
            try:
                translator = Translator(service_urls=['translate.google.cn'])
                if self.check_contain_chinese(src):  # 判断输入是否为中文
                    trans_result = translator.translate(src, src='zh-cn', dest='en').text
                else:
                    trans_result = translator.translate(src, src='en', dest='zh-cn').text
                # print(trans_result)
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, trans_result)
                self.write_log_to_Text("INFO:trans_google success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "GOOGLE翻译失败，请检查！")
        else:
            self.write_log_to_Text("ERROR:trans_google failed")

    # 查询参数引号拼接
    def quotation_marks(self):
        src = self.init_data_Text.get(1.0, END)
        if src:
            try:
                src_list = src.split()
                quo_str = ""
                self.result_data_Text.delete(1.0, END)
                for src_str in src_list:
                    quo_str += "'" + src_str + "',"
                self.result_data_Text.insert(1.0, quo_str.rstrip(","))
                self.write_log_to_Text("INFO:quotation_marks success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "字符串添加引号拼接失败！请检查！")
        else:
            self.write_log_to_Text("ERROR:quotation_marks failed")



def gui_start():
    init_window = Tk()
    MY_GUI_SET(init_window).set_init_window()

    init_window.mainloop()


gui_start()

