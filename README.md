

# I Ching Python project

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/I_Ching_Song_Dynasty_print.jpg/440px-I_Ching_Song_Dynasty_print.jpg)

iching is a packge developed by Cheng-Jun Wang. It employs the method of Shicao prediction to reproduce the prediction of I Ching--the Book of Exchanges. The I Ching ([î tɕíŋ]; Chinese: 易經; pinyin: Yìjīng), also known as the Classic of Changes or Book of Changes in English, is an ancient divination text and the oldest of the Chinese classics.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Yarrow_stalks_for_I_Ching.JPG/440px-Yarrow_stalks_for_I_Ching.JPG)

The Zhou yi provided a guide to cleromancy that used the stalks of the yarrow plant, but it is not known how the yarrow stalks became numbers, or how specific lines were chosen from the line readings. In the hexagrams, broken lines were used as shorthand for the numbers 6 (六) and 8 (八), and solid lines were shorthand for values of 7 (七) and 9 (九). The Great Commentary contains a late classic description of a process where various numerological operations are performed on a bundle of 50 stalks, leaving remainders of 6 to 9.

大衍之数五十，其用四十有九。分而为二以象两，挂一以象三，揲之以四以象四时，归奇于扐以象闰。五岁再闰，故再扐而后挂。天一，地二；天三，地四；天五，地六；天七，地八；天九，地十。天数五，地数五。五位相得而各有合，天数二十有五，地数三十，凡天地之数五十有五，此所以成变化而行鬼神也。乾之策二百一十有六，坤之策百四十有四，凡三百六十，当期之日。二篇之策，万有一千五百二十，当万物之数也。是故四营而成《易》，十有八变而成卦，八卦而小成。引而伸之，触类而长之，天下之能事毕矣。显道神德行，是故可与酬酢，可与祐神矣。子曰：“知变化之道者，其知神之所为乎。”

# Install
```python
pip install iching
```

# A Quick Start

```python
from iching import iching


iching.predict(19850927, 20180119)
```

![](http://7lrzgn.com1.z0.glb.clouddn.com/download.png)


