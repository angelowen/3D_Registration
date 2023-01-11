import numpy as np
from PIL import Image
from os import listdir
from os.path import join
import numpy as np
from PIL import Image



for idx in range(35):
    filepath = f'./Doll/XYZ_{idx}.xyz'
    data = np.load(f'./Z_train.npy')[idx]
    output = open(filepath,'w')
    for i in range(640):
            for j in range(480):
                if data[j,i]<23:
                    continue
                output.write(str(i))
                output.write(" ")
                output.write(str(480-1-j))
                output.write(" ")
                # print(data[j,i])
                output.write('%.6f'%(data[j,i]))
                output.write("\n")
    output.close()

