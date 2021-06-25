Matlab 相关文件在winshare1660 里面的Matlab标定文件 里面 toopencv.m文件 按需要更改相关变量

文件配置win10,
PCL1.10.1安装在D:\PCL 1.10.1目录下。PCL相关的路径要添加到环境变量，详情请看ABB_Stereo的工程目录下里面的配置属性表
opencv4.5.1 安装在D:\opencv\opencv-4.5.1，需要编译选择立体标定相关的选项打开（默认应该有）

标定流程
一、利用MulitCameraCapture 拍照并保存需要标定的图片
二、根据需要处理标定图片集，并利用Matlab自带的立体相机标定，标定并保存相机参数，另存为mat文件
三、利用toopencv.m 转mat文件里面的matlab标定参数，为opencv的标定参数类型。（相机内参和对齐前后图片大小。机械臂坐标转换矩阵为上一次标定的，是无效的）
四、拍照棋盘格并利用机械臂标出棋盘格点，前后两个棋盘格位置在世界坐标系中必须保持不变，才能保证手眼标定有效。（建议16个标棋盘格点）
五、根据四拍照得到的标定板图片，利用calibration2Camera 里面的 charuco 函数 求出相机外参
六、将四得到的机械臂标的棋盘格点的点坐标（建议16个标棋盘格点）写到toopencv.m文件里面，将五得到的外参也写进去，重新运行得到相机参数（相机内参、对齐前后图片大小和机械臂坐标转换矩阵）
七、替换掉ABB_Stereo 里面的InitData 相机参数路径，根据需要更改ABBRUN里面的位置限制的空间范围
八、运行ABB_Stereo 并抓取。