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

4.��ȡ����ĳһ���и���ʵʱ���ݣ�d_h.download(_uuid)��_uuid��Ϊ�������л�õ�dict  ���

5.�޸��и���Ϣ�󣬵��ú���d_h.syn_info(patient_info,_uuid), patient_infoΪ�޸ĺ�    �и���Ϣ���ࡱ��ʵ���������ֵ䡣_uuid��Ϊ�������л�õ�dict���

[ע] ������d_h.download()�󣬿�ʼ������ݣ��и���Ϣ���������ݣ�ע�ͣ�����ȡ���ݵ�����Ϊ
     info���и���Ϣ��dict�ͣ���data�����ݣ���ʽ���и���һ������note��ע�ͣ�list�ͣ�
     ���磬self.note=[[x1,y1,z1],[x2,y2,z2]...] �б���ÿһ���Ǹ�3Ԫ�б�x���ᣬy
     ���ᣬz���ݡ�note����ʱ�����ӻ᲻�ϱ䳤��
     
     d_h.run_chk����Ϊ�缫���ԣ�ͬ�и���һ����low_battry����ͬ�и���һ��
