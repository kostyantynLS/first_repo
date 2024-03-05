'''
Друге завдання
У вас є текстовий файл, який містить інформацію про котів. 
Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.
'''

import os

def get_cats_info(path_to_cats) -> list:
    cats_id = set()
    resl = list()
    if not os.path.exists(path_to_cats):
        print(f'file {path_to_cats} not exist!')
    else:
        with open(path_to_cats, "r", encoding="utf-8") as cats_file:
            while True:
                lines = cats_file.readline()
                if len(lines)==0:
                    break
                if lines=="\n":
                    continue
                cinfo = dict()
                try:
                    cid, cname, cage = lines.split(',')
                    if not cid in cats_id:
                        cats_id.add(cid)
                        cage = str(int(cage))   #\n
                        cinfo["id"]=cid
                        cinfo["name"]=cname
                        cinfo["age"]=cage
                        resl.append(cinfo)
                    else:
                        print(f'cat with ID {cid} already added!')
                except:
                    print(f'error at line {lines}', end="")

    return resl

cats_info = get_cats_info("goit-algo-hw-04/cats_file.txt")
print(cats_info)