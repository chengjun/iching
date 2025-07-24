

# I Ching Python project

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/I_Ching_Song_Dynasty_print.jpg/440px-I_Ching_Song_Dynasty_print.jpg)

iching is a packge developed by Cheng-Jun Wang. It employs the method of Shicao prediction to reproduce the prediction of I Ching--the Book of Exchanges. The I Ching ([î tɕíŋ]; Chinese: 易經; pinyin: Yìjīng), also known as the Classic of Changes or Book of Changes in English, is an ancient divination text and the oldest of the Chinese classics.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Yarrow_stalks_for_I_Ching.JPG/440px-Yarrow_stalks_for_I_Ching.JPG)

The Zhou yi provided a guide to cleromancy that used the stalks of the yarrow plant, but it is not known how the yarrow stalks became numbers, or how specific lines were chosen from the line readings. In the hexagrams, broken lines were used as shorthand for the numbers 6 (六) and 8 (八), and solid lines were shorthand for values of 7 (七) and 9 (九). The Great Commentary contains a late classic description of a process where various numerological operations are performed on a bundle of 50 stalks, leaving remainders of 6 to 9.

大衍之数五十，其用四十有九。分而为二以象两，挂一以象三，揲之以四以象四时，归奇于扐以象闰。五岁再闰，故再扐而后挂。天一，地二；天三，地四；天五，地六；天七，地八；天九，地十。天数五，地数五。五位相得而各有合，天数二十有五，地数三十，凡天地之数五十有五，此所以成变化而行鬼神也。乾之策二百一十有六，坤之策百四十有四，凡三百六十，当期之日。二篇之策，万有一千五百二十，当万物之数也。是故四营而成《易》，十有八变而成卦，八卦而小成。引而伸之，触类而长之，天下之能事毕矣。显道神德行，是故可与酬酢，可与祐神矣。子曰：“知变化之道者，其知神之所为乎。”

蓍草卜筮法的操作步骤见： https://github.com/chengjun/iching/wiki

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


蓍草卜筮法是一种古老的占卜方法，源于《易经》，也被称为大衍筮法、揲蓍法。以下是其具体介绍：
- **相关概念**：
    - **卜与筮**：卜为龟卜，是在龟甲上钻孔后用火烧，根据裂纹形象断吉凶；筮为占筮，是用蓍草等进行数学运算来推断吉凶，蓍草卜筮法就是其中一种。
    - **大衍之数**：天地之数为1到10的相合之数，天数（1、3、5、7、9）相加为25，地数（2、4、6、8、10）相加为30，总数55，舍去尾数用整数50，即为大衍之数。也有说法认为《河图》与《洛书》总数100，其中50个阳数，50个阴数，阴阳数两两相合组成50个阴阳数，就是大衍之数。
- **具体步骤**：
    - **准备蓍草**：取五十根蓍草，可用品相类似的物品如牙签、竹棍等代替。从五十根中取出一根存而不用，实际用于占筮的是四十九根，这一根代表天地未生之前的太极。
    - **一变四营**：第一营“分而为二以象两”，手握四十九根蓍草，心想占问之事，然后将其随机分成左右两部分，象征“太极生两仪”。第二营“挂一以象三”，从左边那簇中取出一根蓍草，夹在左手四五指之间，象征继天地之后产生了人。第三营“揲之以四以象四时”，将左右两簇蓍草分别以四根为一组进行计数，象征一年中的四季。第四营“归奇于扐以象闰”，“归奇”指将左右两簇蓍草分组后剩余的蓍草，“扐”指手指间，将两边的余数合到一起夹在左手三四指之间，象征闰月。左右两簇的余数相加不是四就是八。
    - **三变成一爻**：经过第一次“一变四营”后，剩下的蓍草数不是四十四就是四十。第二次变在第一次变后的基础上进行，同样经过“分二、揲四、归奇”，剩下的蓍草数会是四十、三十六或三十二。第三次变在第二次变后的基础上进行，再经过“分二、揲四、归奇”，剩下的蓍草数则为三十六、三十二、二十八或二十四。将这四个数分别除以四，会得到九、八、七、六。其中七、九为奇数，属阳，定为阳爻，七是少阳，为不变爻，九是老阳，为变爻；六、八为偶数，属阴，定为阴爻，八是少阴，为不变爻，六是老阴，为变爻。
    - **十八变成一卦**：每三变画一爻，由下往上画，经过十八变画出六爻，就得到一卦。然后根据爻逢九、六变，七、八不变的原则，求出变卦。
- **解卦方法**：主要依据宋代学者朱熹提出的变爻推论规则。六爻不变，依据本卦卦辞解卦；一爻变，用本卦变爻的爻辞解卦；二爻变，用两个本卦变爻的爻辞解卦，以上爻为主；三爻变，用本卦卦辞结合变卦卦辞解卦，以本卦为主；四爻变，用变卦的两个不变爻的爻辞解卦，以下爻为主；五爻变，用变卦的不变爻的爻辞解卦；六爻都变，如果是乾坤两卦就用“用九”“用六”爻辞解卦，其他卦用变卦卦辞解卦。
