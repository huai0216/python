hw4-1 distance.py<br>
所謂的大圓距離即為球面上兩點間的距離<br>
假設(x1,y1)與(x2,y2)為兩點地理上的緯度與經度座標<br>
兩點間的距離公式為:<br>
d = radius*acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y1))<br>
使用者輸入以度數表示地球上的兩點的緯度與經度<br>
接著顯示大圓距離<br>
地球半徑約為6371.01km<br>
公式內緯度與經度代表北與西 負數表示南與東<br>
<br>
hw4-2 currency.py<br>
將輸入的金額轉換為最小的貨幣單位<br>
使用者輸入整數型態以表示總金額<br>
接著輸出依序對50元、10元、5元、1元的組合<br>
以使用最少硬幣來計算
