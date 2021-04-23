# Time Memory Trade Off Attack

> This repository contains our implementatino of the Time Memory Trade Off attack with Hellman tables and Rainbow tables in the course 02255 Modern Cryptology Spring 2021 at DTU. The group members are [Anders Lammert Hartmann](https://github.com/AndersHartmann) 
(Student ID: s153596) and [Amalie Due Jensen](https://github.com/AmalieDue) (Student ID: s160503). Note that our report describing the attack has also been included in this repository.

## Structure

The project contains the following files:

* `hellman_attack.py`: Contains the code for attack with Hellman tables.
* `RainbowAttack.py`: Contains the code for attack with rainbow table.
* `plotting_hellman.py` and `plotting_rainbow.py`: Contains code for creating the plots that have been included in the report.

## Usage

In this project, the usage part is quite simple. An example of how to use the Hellman table implementation is shown below.

```python

# define parameters
M = 89
T = 737

coverage = coverage_in_hellman_tables(M, T)
print(coverage)

```

```python

Out[]:

    coverage = [0, 22771, 45502, 68204, 90880, 113519, 136107, 158707, 181247, 203792,
            226263, 248719, 271129, 293510, 315869, 338217, 360557, 382816, 405037,
            427221, 449392, 471540, 493651, 515733, 537755, 559723, 581711, 603697,
            625605, 647418, 669247, 691034, 712821, 734547, 756279, 777949, 799590,
            821227, 842788, 864298, 885820, 907315, 928702, 950155, 971484, 992876,
            1014159, 1035415, 1056631, 1077841, 1099001, 1120095, 1141203, 1162268,
            1183290, 1204291, 1225314, 1246231, 1267029, 1287863, 1308690, 1329539,
            1350300, 1370986, 1391656, 1412300, 1432936, 1453543, 1474127, 1494640,
            1515095, 1535644, 1556057, 1576395, 1596750, 1617070, 1637371, 1657543,
            1677728, 1697945, 1717964, 1738037, 1758085, 1778152, 1798141, 1818070,
            1837939, 1857774, 1877617, 1897444, 1917222, 1936904, 1956694, 1976314,
            1995948, 2015463, 2035001, 2054551, 2074107, 2093495, 2112883, 2132237,
            2151656, 2170933, 2190229, 2209364, 2228508, 2247612, 2266805, 2285901,
            2305072, 2324124, 2343184, 2362127, 2380979, 2399882, 2418715, 2437429,
            2456101, 2474752, 2493480, 2512146, 2530763, 2549337, 2567924, 2586420,
            ... 
            8078658, 8083116, 8087480, 8091868, 8096289, 8100689, 8105158, 8109523,
            8113908, 8118180, 8122528, 8126767, 8131167, 8135414, 8139786, 8143946,
            8148154, 8152443, 8156658, 8160865, 8165007, 8169174, 8173318, 8177471,
            8181616, 8185721, 8189790, 8193915, 8198021, 8202075, 8206163, 8210238,
            8214343, 8218323, 8222324, 8226345, 8230334, 8234314, 8238217, 8242206,
            8246226, 8250143, 8254110, 8257996, 8261914, 8265791, 8269676, 8273566,
            8277477, 8281358, 8285261, 8289075, 8292928, 8296783, 8300498, 8304311,
            8308087, 8311863, 8315607, 8319331, 8323069, 8326828, 8330494, 8334224,
            8337882, 8341533, 8345217, 8348744, 8352313, 8355883, 8359548, 8363157,
            8366755, 8370361, 8373866, 8377332, 8380837, 8384373, 8387960, 8391497,
            8394993, 8398462, 8401939]


```

The output shown above is the total current point coverage across all the 2^8 tables for t = 1, 2, ..., 737 columns added. The parameters M and T were chosen such that the last point coverage in the output (i.e. with t = 737 columns added) was about 50% of all the 2^24. Let us check whether we actually achieved that:

```python

8401939 / 2**24

```

```python

Out[]:
    0.5007945895195007

```

Yes, we indeed have a point coverage of 50%.

The implementation of the rainbow table works very much the same way:

```python

# define parameters
m_fin = 2**8
t_fin = 500

coverage = coverage_in_rainbow_table(m_fin, t_fin)

```


## API

### Constants

* `BLOCK_SIZE = 16`:

Number of bytes in AES encryption (4 by 4 matrix of bytes).

* `l = 24`:

The effective key size. (An AES-128 key is 128 bits, but in this case 104 bits of the key are fixed to zero, i.e. the effective key-length is 24 bits).

### General functions

* `pkcs7_pad(message: bytes, bytes_per_block: int) -> bytes:`:

A padding function used for AES. If the input does not have the correct length, it is padded using this function.

* `f(k: bytes, i: int) -> int:`:

The reduction function used in both the Hellman implementation and in the rainbow implementation. The function takes as input the key k and the current permutation i. In the Hellman tables, i denotes the table number, and in the rainbow table i denotes the column number. For more details, we recommend reading papers about Hellman and rainbow tables. The function outputs ciphertext which has been added by i and then reduced modulo 2^24.

### Hellman table functions

* `coverage_in_hellman_tables(M: int, T: int) -> list:`:

Compute the point coverage for t = 1, ..., T columns. The function takes as input the parameters M (the number of rows) and T (the number of columns) as inputs, and it returns a list of the point coverage for t = 1, ..., T columns.

### Rainbow table functions

* `coverage_in_rainbow_table(m_fin: int, t_fin: int) -> list:`:

Compute the point coverage for t = 1, ..., t_fin columns. The function takes as input the parameters m_fin (the number of rows) and t_fin (the number of columns) as inputs, and it returns a list of the point coverage for t = 1, ..., t_fin columns.