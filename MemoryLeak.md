## 关于Python中的内存泄漏问题

### Author:liu.sy.chn@hotmail.com

#### 问题描述
Python的自动垃圾回收机制是基于对每个对象进行引用计数统计，这为我们节省了大量的内存回收工作。但是要注意，Python编写的代码仍会出现内存泄漏的问题。  
常见的内存泄漏主要是由**循环引用**所引起的，可参照相关资料 [http://www.cnblogs.com/xybaby/p/7491656.html](http://www.cnblogs.com/xybaby/p/7491656.html)  
而本次我们需注意一个因变量类型所引起的内存泄漏问题，代码如下所示。
<pre><code>
for m in range(len(ListData)):
    ListData[m].Establish()
    for n in range(len(ListData)):
        if(m == n):
            continue
        else:
            dis = ListData[m].Distance(ListData[n].origen)
            if(dis <= 168)：   
                a,b,c,d,e,f = ListData[m].Change(EachAA[n].origen)
                b = min(int(np.floor(b*50)),19)
                c = min(int(np.floor(c*90) + 10),19)   
                E += cd[ListData[m].name][ListData[n].name][b][c][d][e][f]
</code></pre>
从垃圾的自动回收方面看，该代码没有什么问题。但实际运行上则会出现非常明显的内存泄漏。问题即出现在min()与np.floor()的组合上。每次调用numpy.floor()函数,都会生成一个<type 'numpy.float64'>类型的对象，而min()函数则返回一个<type 'int'>对象。所以每次执行这两条语句，都会导致内存“多分配，少回收”的现象，最终造成内存泄漏。
