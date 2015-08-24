孕妇端：
from tcp.handler import Handler     
AN24属性、方法：

1.扫描蓝牙设备scan_bt(),得到字典列表

2.实例化AN24，AN24实例化传的参数为一个dict型，key是盒子编号，value是地址（以前是  字符串），这个参数通过全局函数scan_bt()获得
  例子：an24 = AN24({'AN24 A001350':'00:80:98:0E:39:77'})

3.实例化数据处理类，Handler（_uuid,_name),uuid为AN24实例属性_uuid,_name为AN24实例  属性_name

4.开始传数据调用AN24实例的data_recv(handle)方法，参数handle为Handler类实例的  handle方法。
  例如：an24 = AN24({'AN24 A001350':'00:80:98:0E:39:77'})
        h = Handler(an24._uuid, an24._name)
	an24.data_recv(h.handle) 

5.孕妇信息界面提交按钮调用函数为实例Handler的handle(patient_info,0)
  patient_info为孕妇信息“类”的实例，不是字典。第二个参数为数字0

6.添加注释后调用函数为实例Handler的handle(note,2),参数note为列表，例如：
  note=[x,y,z], x为横坐标，y纵坐标，z注释内容。


医生端：

import datahandler

1.初始化客户端 d_c = DoctorClient()

2.每一个1/16窗口对应一个数据处理类：DataHandler
  例如：实例化某窗口的时候d_h = DataHandler()

3.获取所有在线孕妇：d_c.get_online_p(),得到一个dict，key是uuid，value是盒子编号

4.获取其中某一个孕妇的实时数据：d_h.download(_uuid)，_uuid，为第三步中获得的dict  里的

5.修改孕妇信息后，调用函数d_h.syn_info(patient_info,_uuid), patient_info为修改后    孕妇信息“类”的实例，不是字典。_uuid，为第三步中获得的dict里的

[注] 调用完d_h.download()后，开始获得数据（孕妇信息，盒子数据，注释），获取数据的属性为
     info（孕妇信息，dict型），data（数据，格式跟孕妇段一样），note（注释，list型）
     比如，self.note=[[x1,y1,z1],[x2,y2,z2]...] 列表里每一项是个3元列表。x横轴，y
     纵轴，z内容。note随着时间增加会不断变长。
     
     d_h.run_chk属性为电极属性，同孕妇段一样；low_battry属性同孕妇段一样
