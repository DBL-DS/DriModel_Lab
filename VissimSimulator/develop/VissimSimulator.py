# Demo for Vissim+
# This demo is programmed to verified the COM interface of Vissim.
# 2017.1.16
# silverHugh

import win32com.client as com
from xlrd import open_workbook
from tkinter.messagebox import *
from tkinter.filedialog import *

# Macro
VISSIM_VERSION = 'Vissim.Vissim-64.700'


# User Interface
class UI:
    # Click Events
    def __commit__(self):
        self.net_name = self.e1.get()
        self.layout_name = self.e2.get()
        self.data_input = self.e3.get()
        if self.net_name == '' or self.layout_name == '':
            showerror(title='数据错误', message='底图路径不全')
        elif self.data_input == '':
            showerror(title='数据错误', message='无输入数据')
        else:
            msg = '请确认车辆输入:\n'
            data = open_workbook(self.get_data())
            vehicle_inputs = data.sheet_by_name(u'vehicle_inputs')
            for i in range(vehicle_inputs.nrows):
                msg += str(vehicle_inputs.row_values(i))
                msg += '\n'
            choice = askyesno(title='数据确认', message=msg)
            if choice == TRUE:
                self.__run_simulation__()

    def __load_net__(self):
        f_types = [('Net', '*.inpx')]
        filename = askopenfilename(initialdir=os.getcwd(), title='Load Net', filetypes=f_types)
        self.e1.delete(0, END)
        self.e1.insert(0, filename)

    def __load_layout__(self):
        f_types = [('Layout', '*.layx')]
        filename = askopenfilename(initialdir=os.getcwd(), title='Load Layout', filetypes=f_types)
        self.e2.delete(0, END)
        self.e2.insert(0, filename)

    def __data_input__(self):
        f_types = [('Excel', '*.xls;*.xlsx')]
        filename = askopenfilename(initialdir=os.getcwd(), title='Data Input', filetypes=f_types)
        self.e3.delete(0, END)
        self.e3.insert(0, filename)

    def __run_simulation__(self):
        try:
            vissim = Vissim()
            vissim.open()
            vissim.load_net(self.get_net())
            vissim.load_layout(self.get_layout())
            vissim.set_data(self.get_data())
            vissim.run()
        except KeyboardInterrupt:
            print('[!] Interrupted')
        except Exception as e:
            showerror('错误', e)
        finally:
            if vissim is not None:
                vissim.close()
            showinfo('仿真结束','仿真已结束！')
            self.inputDlg.quit()
            self.inputDlg.destroy()

    # Getters
    def get_net(self):
        return self.net_name.replace('/', '\\')

    def get_layout(self):
        return self.layout_name.replace('/', '\\')

    def get_data(self):
        return self.data_input.replace('/', '\\')

    # Initialization
    def __init__(self, __type='input'):
        # Private Variables
        self.inputDlg = Tk()
        self.net_name = str
        self.layout_name = str
        self.data_input = str

        if __type == 'input':
            self.inputDlg.geometry('500x180')
            self.inputDlg.resizable(False, False)
            self.inputDlg.title('VissimSimulator')
            self.inputDlg.iconbitmap('icon\\VissimSimulator.ico')

            # Row 1
            Label(self.inputDlg, text='Vissim仿真工具', font=('微软雅黑', 24, 'bold'))\
                .grid(row=0, column=0, columnspan=4)

            # Row 2
            Label(self.inputDlg, text='路网路径:', font=('微软雅黑', 11))\
                .grid(row=1, column=0, sticky=W)
            self.e1 = Entry(self.inputDlg, width=50)
            self.e1.grid(row=1, column=1, sticky=W)
            Label(self.inputDlg, text='    ').grid(row=1, column=2)
            Button(self.inputDlg, text='浏览...', command=self.__load_net__)\
                .grid(row=1, column=3, sticky=W)

            # Row 3
            Label(self.inputDlg, text='底图路径:', font=('微软雅黑', 11))\
                .grid(row=2, column=0, sticky=W)
            self.e2 = Entry(self.inputDlg, width=50)
            self.e2.grid(row=2, column=1, sticky=W)
            Button(self.inputDlg, text='浏览...', command=self.__load_layout__)\
                .grid(row=2, column=3, sticky=W)

            # Row 4
            Label(self.inputDlg, text='数据输入:', font=('微软雅黑', 11))\
                .grid(row=3, column=0, sticky=W)
            self.e3 = Entry(self.inputDlg, width=50)
            self.e3.grid(row=3, column=1, sticky=W)
            Button(self.inputDlg, text='浏览...', command=self.__data_input__)\
                .grid(row=3, column=3, sticky=W)

            # Row 5
            Button(self.inputDlg, text='开始仿真', font=('微软雅黑', 11, 'bold', 'italic'), command=self.__commit__)\
                .grid(row=4, columnspan=4)

    def show(self, __type='input'):
        if __type == 'input':
            self.inputDlg.mainloop()


# Vissim Class
class Vissim():
    def __init__(self):
        self.Vissim = object
        self.data = object

    def open(self):
        self.Vissim = com.Dispatch(VISSIM_VERSION)

    def close(self):
        if self.Vissim is not None:
            self.Vissim = None

    def load_net(self, netPath, additive = False):
        self.Vissim.LoadNet(netPath, additive)

    def load_layout(self, layoutPath):
        self.Vissim.loadLayout(layoutPath)

    def run(self, mode='continuous'):
        # 设置仿真参数
        self.Vissim.Simulation.SetAttValue('NumCores',4)
        self.Vissim.Simulation.SetAttValue('SimPeriod',600)

        # 设置评估结果参数
        self.Vissim.Evaluation.SetAttValue('VehRecWriteFile',True)
        self.Vissim.Evaluation.SetAttValue('VehTravTmRawWriteFile',True)
        self.Vissim.Evaluation.SetAttValue('EvalOutDir',os.getcwd()+'\\results')

        # 根据输入文件设置参数
        self.__set_vehicle_routes__()
        self.__set_link__()
        self.__set_vehicle_inputs__()
        self.__set_vehicle_routing_decisions__()
        self.__set_vehicle_compositions__()
        self.__set_driving_behaviors__()
        if mode == 'step':
            self.Vissim.Simulation.RunSingleStep()
        else:
            self.Vissim.Simulation.RunContinuous()

    def set_data(self,__data):
        self.data = open_workbook(__data)

    def __set_vehicle_routes__(self):
        vehicle_routes = self.data.sheet_by_name(u'vehicle_routes')
        for i in range(vehicle_routes.nrows - 1):
            routes = self.Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(vehicle_routes.cell(i + 1, 0).value)\
                .Link.VehRoutSta.GetAll()
            routes[int(vehicle_routes.cell(i + 1, 1).value) - 1].SetAttValue('Name', vehicle_routes.cell(i + 1, 2).value)
            routes[int(vehicle_routes.cell(i + 1, 1).value) - 1].SetAttValue('DestLink', vehicle_routes.cell(i + 1, 3).value)
            routes[int(vehicle_routes.cell(i + 1, 1).value) - 1].SetAttValue('DestPos', vehicle_routes.cell(i + 1, 4).value)

    def __set_link__(self):
        links = self.data.sheet_by_name(u'links')
        for i in range(links.nrows - 1):
            self.Vissim.Net.Links.ItemByKey(links.cell(i + 1, 1).value)\
                .SetAttValue('Name', links.cell(i + 1, 0).value)
            self.Vissim.Net.Links.ItemByKey(links.cell(i + 1, 1).value)\
                .SetAttValue('LinkBehavType', links.cell(i + 1, 2).value)

    def __set_driving_behaviors__(self):
        driving_behaviors = self.data.sheet_by_name(u'driving_behaviors')
        for i in range(driving_behaviors.nrows - 1):
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('No', driving_behaviors.cell(i + 1, 0).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('Name', driving_behaviors.cell(i + 1, 1).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc0', driving_behaviors.cell(i + 1, 2).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc1', driving_behaviors.cell(i + 1, 3).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc2', driving_behaviors.cell(i + 1, 4).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc3', driving_behaviors.cell(i + 1, 5).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc4', driving_behaviors.cell(i + 1, 6).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc5', driving_behaviors.cell(i + 1, 7).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc6', driving_behaviors.cell(i + 1, 8).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc7', driving_behaviors.cell(i + 1, 9).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc8', driving_behaviors.cell(i + 1, 10).value)
            self.Vissim.Net.DrivingBehaviors.ItemByKey(6)\
                .SetAttValue('W99cc9', driving_behaviors.cell(i + 1, 11).value)
        self.Vissim.Net.LinkBehaviorTypes.ItemByKey(6).SetAttValue('Name','自定义')
        self.Vissim.Net.LinkBehaviorTypes.ItemByKey(6).SetAttValue('DrivBehavDef',6)

    def __set_vehicle_routing_decisions__(self):
        vehicle_routing_decisions = self.data.sheet_by_name(u'vehicle_routing_decisions')
        for i in range(vehicle_routing_decisions.nrows - 1):
            self.Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(i + 1)\
                .SetAttValue('No', vehicle_routing_decisions.cell(i + 1, 0).value)
            self.Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(i + 1)\
                .SetAttValue('Name', vehicle_routing_decisions.cell(i + 1, 1).value)
            self.Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(i + 1)\
                .SetAttValue('Link', vehicle_routing_decisions.cell(i + 1, 2).value)
            self.Vissim.Net.VehicleRoutingDecisionsStatic.ItemByKey(i + 1)\
                .SetAttValue('Pos', vehicle_routing_decisions.cell(i + 1, 3).value)

    def __set_vehicle_compositions__(self):
        vehicle_compositions = self.data.sheet_by_name(u'vehicle_compositions')
        self.Vissim.Net.VehicleCompositions.ItemByKey(2).SetAttValue('Name','test')
        self.Vissim.Net.VehicleCompositions.ItemByKey(2).SetAttValue('No','2')
        rel_flows = self.Vissim.Net.VehicleCompositions.ItemByKey(2).VehCompRelFlows.GetAll()
        for i in range(vehicle_compositions.nrows - 1):
            # 车辆类型
            rel_flows[i].SetAttValue('VehType', vehicle_compositions.cell(i + 1,0).value)
            # 期望速度
            rel_flows[i].SetAttValue('DesSpeedDistr', vehicle_compositions.cell(i + 1, 1).value)
            # 分流比例
            rel_flows[i].SetAttValue('RelFlow', vehicle_compositions.cell(i + 1, 2).value)

    def __set_vehicle_inputs__(self):
        # 从excel表中读取车辆输入部分信息
        vehicle_inputs = self.data.sheet_by_name(u'vehicle_inputs')
        # 循环设置VehicleInput信息，因为No的下标为1-n，所以循环为0-(n-1)，每个i为i+1
        for i in range(vehicle_inputs.nrows - 1):
            # 编号，是VehicleInputs的Key
            self.Vissim.Net.VehicleInputs.ItemByKey(i + 1)\
                .SetAttValue('No', vehicle_inputs.cell(i + 1,0).value)
            # 车辆输入名称
            self.Vissim.Net.VehicleInputs.ItemByKey(i + 1)\
                .SetAttValue('Name', vehicle_inputs.cell(i + 1, 1).value)
            # 车道
            self.Vissim.Net.VehicleInputs.ItemByKey(i + 1)\
                .SetAttValue('Link', vehicle_inputs.cell(i + 1, 2).value)
            # 初始时间的流量
            self.Vissim.Net.VehicleInputs.ItemByKey(i + 1)\
                .SetAttValue('Volume(1)', vehicle_inputs.cell(i + 1, 3).value)
            # 初始实践的车辆构成
            self.Vissim.Net.VehicleInputs.ItemByKey(i + 1)\
                .SetAttValue('VehComp(1)', vehicle_inputs.cell(i + 1, 4).value)


def main():
    ui = UI()
    ui.show()


if __name__ == '__main__':
    main()
