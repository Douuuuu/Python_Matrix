# Python_Matrix
Some algorithms about matrix in Python.

由来：
    这个项目最开始只是想熟悉熟悉Python的列表，在写完了矩阵相加函数之后却又不由自主地想到了很多其他的。
    
我关于多维矩阵的相乘的一些想法：

    我在线性代数中学到了二维矩阵的相乘如何运算，基于这个运算我想到了通过递归的方法调用n次算法就可以实现维度为2n的运算。（通过我的思考我觉得应该是2n而不是2^n）
    
    可是如果是三维的呢？想象一下把二维矩阵中的每一个元素换成一个横向量，现在有学过的两个横向量的乘法有点乘和叉乘，点乘因为会降维，所以我觉得不可取，
    应该使用叉乘或者按位相乘（我也不确定，后边我去查查资料吧）这样的话对于任意维度的两个  满足条件  的两个n维矩阵都可以通过n mod(2)次叉乘运算和n/2的下取整次二维运算得到一个相乘之后的n维矩阵。
    
    那么满足的条件应该是什么条件呢？
    在二维的矩阵中两个矩阵能够相乘的条件是左矩阵的列数和右矩阵的行数相等。设三位矩阵matrix_3_1的各维度长度分别为i,j,k;三维矩阵matrix_3_2的各维度长度分别为p,q,r。其维度分别为v1，v2，v3.
    如果当递归运算到高维度时还有比它低的维度没有参与到递归运算中，那么就会出现当前运算结果而终止运算，所以只能从低维到高维进行递归。例如开始直接对v3进行运算则只会进行v3的运算。
    如果先一维运算v1再二维运算v2和v3则应满足i=p且k=q;如果先二维运算v1和v2再一维运算v3则应满足j=p且k=r。
    
    
    
