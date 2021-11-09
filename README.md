# Python_Matrix
Some algorithms about matrix in Python.
由来：
    这个项目最开始只是想熟悉熟悉Python的列表，在写完了矩阵相加函数之后却又不由自主地想到了很多其他的。
我关于多维矩阵的相乘的一些想法：
    我在线性代数中学到了二维矩阵的相乘如何运算，基于这个运算我想到了通过递归的方法调用n次算法就可以实现维度为2n的运算。（通过我的思考我觉得应该是2n而不是2^n）
    
    可是如果是三维的呢？想象一下把二维矩阵中的每一个元素换成一个横向量，现在有学过的两个横向量的乘法有点乘和叉乘，点乘因为会降维，所以我觉得不可取，
    应该使用点乘（当然我也不确定对不对，后边我去查查资料吧）这样的话对于任意维度的两个  满足条件  的两个n维矩阵都可以通过n mod(2)次叉乘运算和n/2的下取整次二维运算得到一个相乘之后的n维矩阵。
    
    那么满足的条件应该是什么条件呢？
    在二维的矩阵中两个矩阵能够相乘的条件是左矩阵的列数和右矩阵的行数相等。设三位矩阵matrix_3_1的各维度长度分别为i,j,k;三维矩阵matrix_3_2的各维度长度分别为p,q,r。其维度分别为v1，v2，v3.
    对于 matrix_3_1*matrix_3_2 若先进行一维运算则运算不能成立，可知只能先进行二维运算。
    若先对v1和v2进行运算则应满足j=p且k=r,结果为v1=i  ,v2=q  ,v3=k=r;
    若先对v2和v3进行运算则应满足i=p且k=q,结果为v1=i=p,v2=j  ,v3=r;
    若先对v1和v3进行运算则应满足j=q且i=r,结果为v1=i  ,v2=j=q,v3=r.
    可知运算的顺序不能确定v2的维度，是否应该有一种固定的顺序来进行计算。
    
    
    
