import numpy as np
import matplotlib.pyplot as plt
def location_points(img):
    def check(img_check, h, l, h_max, l_max):

        # 边缘情况 左上角检测
        if h == 0 and l == 0:
            if img_check[h][l] > 0 and (img_check[h+1][l] == 0 or img_check[h][l+1] == 0 or img_check[h+1][l+1] == 0):
                return 1
            else:
                return 0
        # 边缘情况 右上角检测
        elif h == 0 and l == l_max:
            if img_check[h][l] > 0 and (img_check[h][l-1] == 0 or img_check[h+1][l] == 0 or img_check[h+1][l-1] == 0):
                return 1
            else:
                return 0
        # 边缘情况 左下角检测
        elif h == h_max and l == 0:
            if img_check[h][l] > 0 and (img_check[h-1][l] == 0 or img_check[h][l+1] == 0 or img_check[h-1][l+1] > 0):
                return 1
            else:
                return 0
        # 边缘情况 右下角检测
        elif h == h_max and l == l_max:
            if img_check[h][l] > 0 and (img_check[h-1][l] == 0 or img_check[h][l-1] == 0 or img_check[h-1][l-1] == 0):
                return 1
            else:
                return 0
        # 上边缘检测
        elif h == 0 and (l > 0 and l < l_max):
            if img_check[h][l] > 0 and (img_check[h+1][l] == 0 or img_check[h][l+1] == 0 or img_check[h][l-1] == 0 or img_check[h+1][l-1] == 0 or img_check[h+1][l+1] > 0):
                return 1
            else:
                return 0
        # 下边缘检测
        elif h == h_max and (l > 0 and l < l_max):
            if img_check[h][l] > 0 and (img_check[h-1][l] == 0 or img_check[h][l+1] == 0 or img_check[h][l-1] == 0 or img_check[h-1][l-1] == 0 or img_check[h-1][l+1] > 0):
                return 1
            else:
                return 0
        # 左边缘检测
        elif l == 0 and (h > 0 and h < h_max):
            if img_check[h][l] > 0 and(img_check[h+1][l] == 0 or img_check[h-1][l] == 0 or img_check[h][l+1] == 0 or img_check[h+1][l+1] == 0 or img_check[h-1][l+1] > 0):
                return 1
            else:
                return 0
        # 右边缘检测
        elif l == l_max and (h > 0 and h < h_max):
            if img_check[h][l] > 0 and(img_check[h+1][l] == 0 or img_check[h-1][l] == 0 or img_check[h][l-1] == 0 or img_check[h+1][l-1] == 0 or img_check[h-1][l-1] > 0):
                return 1
            else:
                return 0
        elif (h > 0 and h < h_max) and (l > 0 and l < l_max):
            if img_check[h][l] > 0 and (img_check[h - 1][l - 1] == 0 or img_check[h - 1][l] == 0 or img_check[h - 1][l + 1] == 0 or img_check[h][l + 1] == 0 or img_check[h + 1][l + 1] == 0 or img_check[h + 1][l] == 0 or img_check[h + 1][l - 1] == 0 or img_check[h][l - 1] == 0):
                return 1
            else:
                return 0
    def location(img_loca, cen_x, cen_y):
        list_x = []
        list_y = []
        cen_xx = cen_x
        cen_yy = cen_y
        up_x_max = 0
        low_x_min = 0
        left_y_min = 0
        right_y_max = 0
        # 列不变找上下
        for x in range(0, cen_xx):
            cen_xx = x
            if img_loca[cen_xx][cen_yy] == 2:
                list_x.append(cen_xx)
                list_y.append(cen_yy)
                up_x_max = cen_x - cen_xx
                break
        cen_xx = cen_x
        cen_yy = cen_y
        for x in range(0, img_loca.shape[0]-cen_xx-1):
            cen_xx = img_loca.shape[0] - x - 1
            if img_loca[cen_xx][cen_yy] == 2:
                list_x.append(cen_xx)
                list_y.append(cen_yy)
                low_x_min = cen_xx - cen_x
                break
        # 行不变找左右
        cen_xx = cen_x
        cen_yy = cen_y
        for y in range(0, cen_y):
            cen_yy = y
            if img_loca[cen_xx][cen_yy] == 2:
                list_x.append(cen_xx)
                list_y.append(cen_yy)
                left_y_min = cen_y - cen_yy
                break
        cen_xx = cen_x
        cen_yy = cen_y
        for y in range(0, img_loca.shape[1]-cen_y-1):
            cen_yy = img_loca.shape[1] - y - 1
            if img_loca[cen_xx][cen_yy] == 2:
                list_x.append(cen_xx)
                list_y.append(cen_yy)
                right_y_max = cen_yy - cen_y
                break
        # 找左上方
        cen_xx = cen_x
        cen_yy = cen_y
        if up_x_max >= left_y_min:
            stride = round((up_x_max / left_y_min))
            for y in range(0, up_x_max + left_y_min):
                if img_loca[cen_xx - stride][cen_yy - 1] == 0 or img_loca[cen_xx - stride][cen_yy - 1] == 2:
                    list_x.append(cen_xx - stride)
                    list_y.append(cen_yy - 1)
                    break
                else:
                    cen_xx = cen_xx - stride
                    cen_yy = cen_yy - 1
        else:
            stride = round((left_y_min/up_x_max))
            for x in range(0, up_x_max + left_y_min):
                if img_loca[cen_xx - 1][cen_yy - stride] == 0 or img_loca[cen_xx - 1][cen_yy - stride] == 2:
                    list_x.append(cen_xx - 1)
                    list_y.append(cen_yy - stride)
                    break
                else:
                    cen_xx = cen_xx - 1
                    cen_yy = cen_yy - stride
        # 找右上方
        cen_xx = cen_x
        cen_yy = cen_y
        if up_x_max >= right_y_max:
            stride = round((up_x_max / right_y_max))
            for y in range(0, up_x_max + right_y_max):
                if img_loca[cen_xx - stride][cen_yy + 1] == 0 or img_loca[cen_xx - stride][cen_yy + 1] == 2:
                    list_x.append(cen_xx - stride)
                    list_y.append(cen_yy + 1)
                    break
                else:
                    cen_xx = cen_xx - stride
                    cen_yy = cen_yy + 1
        else:
            stride = round((right_y_max / up_x_max))
            for x in range(0, up_x_max + left_y_min):
                if img_loca[cen_xx - 1][cen_yy + stride] == 0 or img_loca[cen_xx - 1][cen_yy + stride] == 2:
                    list_x.append(cen_xx - 1)
                    list_y.append(cen_yy + stride)
                    break
                else:
                    cen_xx = cen_xx - 1
                    cen_yy = cen_yy + stride
        # 找左下方
        cen_xx = cen_x
        cen_yy = cen_y
        if low_x_min >= left_y_min:
            stride = round((low_x_min / left_y_min))
            for y in range(0, low_x_min + left_y_min):
                if img_loca[cen_xx + stride][cen_yy - 1] == 0 or img_loca[cen_xx + stride][cen_yy - 1] == 2:
                    list_x.append(cen_xx + stride)
                    list_y.append(cen_yy - 1)
                    break
                else:
                    cen_xx = cen_xx + stride
                    cen_yy = cen_yy - 1
        else:
            stride = round((left_y_min / low_x_min))
            for x in range(0, low_x_min + left_y_min):
                if img_loca[cen_xx + 1][cen_yy - stride] == 0 or img_loca[cen_xx + 1][cen_yy - stride] == 2:
                    list_x.append(cen_xx + 1)
                    list_y.append(cen_yy - stride)
                    break
                else:
                    cen_xx = cen_xx + 1
                    cen_yy = cen_yy - stride
            # 找右下方
        cen_xx = cen_x
        cen_yy = cen_y
        if low_x_min >= right_y_max:
            stride = round((low_x_min / right_y_max))
            for y in range(0, low_x_min + right_y_max):
                if img_loca[cen_xx + stride][cen_yy + 1] == 0 or img_loca[cen_xx + stride][cen_yy + 1] == 2:
                    list_x.append(cen_xx + stride)
                    list_y.append(cen_yy + 1)
                    break
                else:
                    cen_xx = cen_xx + stride
                    cen_yy = cen_yy + 1
        else:
            stride = round((right_y_max / low_x_min))
            for x in range(0, low_x_min + right_y_max):
                if img_loca[cen_xx + 1][cen_yy + stride] == 0 or img_loca[cen_xx + 1][cen_yy + stride] == 2:
                    list_x.append(cen_xx + 1)
                    list_y.append(cen_yy + stride)
                    break
                else:
                    cen_xx = cen_xx + 1
                    cen_yy = cen_yy + stride

        return list_x, list_y
    # img = np.loadtxt('input2.txt', dtype=np.uint8)  #dtype=np.float32
    # plt.matshow(img, cmap=plt.get_cmap('Greens'), alpha=0.8)  # , alpha=0.3
    # plt.show()
    count_x = 0
    count_y = 0
    area = 0
    location_x = 0
    location_y = 0
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i][j] > 0:
                count_x = count_x + i
                count_y = count_y + j
                area = area + 1
                result_check = check(img, i, j, img.shape[0]-1, img.shape[1]-1)
                if result_check == 1:
                    img[i][j] = 2
    center_x = count_x // area
    center_y = count_y // area

    location_x, location_y = location(img, center_x, center_y)
    return location_x, location_y
# plt.matshow(img, cmap=plt.get_cmap('Greens'), alpha=0.8)  # , alpha=0.3
# plt.show()
# np.savetxt(r'output.txt', img, fmt='%d', delimiter=' ')