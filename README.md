# 配布目的でないのならば tkinter で十分

tkinter は個人のツールとして使う

## 配置は grid だけ覚える

widget.grid(options)

|  options  |  説明  |
| ---- | ---- |
|row|配置する行|
|column|配置する列|
|rowspan|要素がまたがる行数|
|columnspan|要素がまたがる列数を指定|
|ipadx|内側の横の間隔|
|ipady|内側の縦の間隔|
|padx|外側の横の間隔|
|pady|外側の縦の間隔|
|sticky|ウィジェットがセルよりも小さい場合、ウィジェットがstickyセルの側面と角を示すためにstickyが使用されます。<br>方向は、N、E、S、W、NE、NW、SE、SWの各コンパスの方向とゼロによって定義されます。<br>これらは文字列連結でもかまいません。例えば、NESWはウィジェットがセルの全領域を占めるようにします。|

### ウィジェットの種類や使い方は検索して調べる
