

Author: Mengfei Zhao

Mail: 18037198823@163.com

Date: 2024.05.08

Version: v1

GitHub: https://github.com/Mengfei-Zhao/convert_csv_to_s2p.git



This script can convert the .csv file of S parameters to its .s2p file.

Please delete all headers and tails (include the blank lines at the end) of your .csv file, and make sure your .csv file look like this:

```
Freq(Hz),S11(DB),S11(DEG),S22(DB),S22(DEG),S21(DB),S21(DEG)
10000000,-27.235962,7.171164,-25.624048,-13.239027,-0.28209287,-66.807648
...
...
50000000,x,x,x,x,x,x
```

`data.csv`：the sample .csv file, you can modify your .csv file according to this file.

`out.s2p`: the generated s2p file, you can modify the header of this file according to the actual condition.



## How to use?

`python convert_csv_to_s2p.py -h`: use this to see the help information.

`python convert_csv_to_s2p.py data.csv`: use this to convert your data.csv to the s2p file.