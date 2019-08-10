# rela=set()
# entity=set()
# with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/data/movie/kg_part1_rehashed.txt","r") as f:
#     with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/triple.txt","w") as f2:
#
#
#         for i,line in enumerate(f.readlines()):
#             if i==22502:
#                 break
#             entity1=line.split("\t")[0]
#             relation=line.split("\t")[1]
#             entity3=line.split("\t")[2].replace("\n","")
#             rela.add(relation)
#             entity.add(entity1)
#             entity.add(entity3)
#             f2.write(line)
#     with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/relation.txt","w") as f3:
#         for i,line in enumerate(list(rela)):
#             f3.write(line)
#
#             f3.write("\t"+str(i)+"\n")
#
#     with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/entity.txt","w") as f4:
#         for i,line in enumerate(list(entity)):
#             f4.write(line)
#             f4.write("\n")
#             print(i)
# relation=dict()
# with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/relation.txt","r") as f2:
#     for line in f2.readlines():
#         relation[line.split("\t")[0]]=line.split("\t")[1].replace("\n","")
# for i in relation.items():
#     print(i)
# with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/triple.txt","r") as f:
#     with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/triple2id.txt","w") as f3:
#
#             for j,line in enumerate(f.readlines()):
#
#                 for i in relation.items():
#
#                       if i[0]==line.split("\t")[1].replace("\n",""):
#                         print(i[0],i[1])
#                         f3.write(line.split("\t")[0]+"\t")
#                         f3.write(str(i[1])+"\t")
#                         f3.write(line.split("\t")[2])
#                         break
import numpy as np
# with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/triple2id.txt","r") as f:
#     with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/test2id.txt", "w") as f2:
#
#             a=np.random.choice(12500,2250)
#
#             for j,line in enumerate(f.readlines()):
#
#                 for x in a:
#                     if x==j:
#                         print("---"+str(x))
#                         f2.write(line)
#                         break

ss=set()
with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/triple2id.txt","r") as f:
    with  open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/test2id.txt", "r") as f2:
        with open("/data/pycharm_project_9/rultextract/RippleNet-Pytorch/kg_test/train2id.txt", "w") as f3:
            for j, li in enumerate(f2.readlines()):
                ss.add(li)
            for i,line in enumerate(f.readlines()):
                    if line in ss:
                        continue
                    else:
                        f3.write(line)





