�и��ˣ�
from tcp.handler import Handler     
AN24���ԡ�������

1.ɨ�������豸scan_bt(),�õ��ֵ��б�

2.ʵ����AN24��AN24ʵ�������Ĳ���Ϊһ��dict�ͣ�key�Ǻ��ӱ�ţ�value�ǵ�ַ����ǰ��  �ַ��������������ͨ��ȫ�ֺ���scan_bt()���
  ���ӣ�an24 = AN24({'AN24 A001350':'00:80:98:0E:39:77'})

3.ʵ�������ݴ����࣬Handler��_uuid,_name),uuidΪAN24ʵ������_uuid,_nameΪAN24ʵ��  ����_name

4.��ʼ�����ݵ���AN24ʵ����data_recv(handle)����������handleΪHandler��ʵ����  handle������
  ���磺an24 = AN24({'AN24 A001350':'00:80:98:0E:39:77'})
        h = Handler(an24._uuid, an24._name)
	an24.data_recv(h.handle) 

5.�и���Ϣ�����ύ��ť���ú���Ϊʵ��Handler��handle(patient_info,0)
  patient_infoΪ�и���Ϣ���ࡱ��ʵ���������ֵ䡣�ڶ�������Ϊ����0

6.���ע�ͺ���ú���Ϊʵ��Handler��handle(note,2),����noteΪ�б����磺
  note=[x,y,z], xΪ�����꣬y�����꣬zע�����ݡ�


ҽ���ˣ�

import datahandler

1.��ʼ���ͻ��� d_c = DoctorClient()

2.ÿһ��1/16���ڶ�Ӧһ�����ݴ����ࣺDataHandler
  ���磺ʵ����ĳ���ڵ�ʱ��d_h = DataHandler()

3.��ȡ���������и���d_c.get_online_p(),�õ�һ��dict��key��uuid��value�Ǻ��ӱ��

4.��ȡ����ĳһ���и���ʵʱ���ݣ�d_h.download_thread(_uuid,"close")��_uuid��Ϊ�������л�õ�dict  ���

5.�޸��и���Ϣ�󣬵��ú���d_h.syn_info(patient_info,_uuid), patient_infoΪ�޸ĺ�    �и���Ϣ���ࡱ��ʵ���������ֵ䡣_uuid��Ϊ�������л�õ�dict���

[ע] ������d_h.download()�󣬿�ʼ������ݣ��и���Ϣ���������ݣ�ע�ͣ�����ȡ���ݵ�����Ϊ
     info���и���Ϣ��dict�ͣ���data�����ݣ���ʽ���и���һ������note��ע�ͣ�list�ͣ�
     ���磬self.note=[[x1,y1,z1],[x2,y2,z2]...] �б���ÿһ���Ǹ�3Ԫ�б�x���ᣬy
     ���ᣬz���ݡ�note����ʱ�����ӻ᲻�ϱ䳤��
     
     d_h.run_chk����Ϊ�缫���ԣ�ͬ�и���һ����low_battry����ͬ�и���һ��


![](https://github.com/justalittlenoob/Project-1/blob/master/pic/login.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E5%AF%BB%E6%89%BE%E8%AE%BE%E5%A4%87.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E5%BC%80%E5%A7%8B%E6%A3%80%E6%B5%8B.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E6%A3%80%E6%B5%8B%E8%BF%87%E7%A8%8B.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E6%9E%81%E4%BD%8D%E7%BD%AE.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E6%9E%81%E6%A3%80%E6%9F%A5.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%8C%BB%E7%94%9F%E7%95%8C%E9%9D%A2.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E5%A4%8D%E6%9D%82%E7%95%8C%E9%9D%A2.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E6%89%BE%E8%AE%BE%E5%A4%87.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E7%AE%80%E5%8D%95%E7%95%8C%E9%9D%A2.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E8%AE%BE%E5%A4%87%E5%88%97%E8%A1%A8.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E8%BF%9E%E6%8E%A5.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87-%E8%BF%9E%E6%8E%A5%E6%88%90%E5%8A%9F.png)  
![](https://github.com/justalittlenoob/Project-1/blob/master/pic/%E7%94%B5%E8%84%91-%E5%AD%95%E5%A6%87%E7%95%8C%E9%9D%A2.png)  
 
