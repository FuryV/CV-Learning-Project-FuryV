import os
import random


def main():
    random.seed(0)  # 设置随机种子，保证随机结果可复现

    files_path = "./VOCdevkit/VOC2012/Annotations"  # XML文件根目录或图片根目录
    assert os.path.exists(files_path), "path: '{}' does not exist.".format(files_path)

    val_rate = 0.5  # 验证比例

    files_name = sorted([file.split(".")[0] for file in os.listdir(files_path)])  # 得到名字并排序
    files_num = len(files_name)  # 得到所有个数
    val_index = random.sample(range(0, files_num), k=int(files_num*val_rate))  # 随机采样
    train_files = []
    val_files = []
    for index, file_name in enumerate(files_name):  # 根据val index向两个数组中分配图片或者xml标注
        if index in val_index:
            val_files.append(file_name)
        else:
            train_files.append(file_name)

    try:
        train_f = open("train.txt", "x")  # 写入txt文件，把list放进去
        eval_f = open("val.txt", "x")
        train_f.write("\n".join(train_files))  # 拼接，两个之间是一个换行符
        eval_f.write("\n".join(val_files))
    except FileExistsError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    main()
