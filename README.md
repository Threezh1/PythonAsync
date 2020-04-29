# PythonAsync
Python 协程的利用框架

框架运行的结果为：

```
I'm Threezh1.
Hello World.
Welcome to my blog.
[*] The 1th thread ends
One
Three
Tow
[*] The 2th thread ends
Four
[*] The 3th thread ends
[Finished in 3.2s]
```

一共只花费3秒

## 框架的使用

- SomeFunction() 		需要实现并发的函数
- coroutine_execution() 新建一个线程来执行并发函数
- coroutine_init()		处理线程与调配任务

流程图：

![process.png](https://i.loli.net/2019/08/22/1fUmqKRNigF89DV.png)

需要调整的内容：

一. 传递的参数列表
	
	列表中单个成员最后都会被赋值到目标函数。
	比如：批量获取网站标题，这里的成员就为单个url。

二. 目标函数的参数

	通过调整目标函数的参数个数，可以使框架适用于更加复杂的场景。
	需要注意的是各个函数互相调用，其中的参数要尽量保持一致。

三. 返回结果的获取

	在单个线程当中无法对全局变量进行修改，对结果的处理可以放在coroutine_execution()当中。
	coroutine_execution()中也可以直接return结果，则会返回到coroutine_init()中。


Python协程知识点参考：[协程初体验之简单的利用框架](https://threezh1.com/2019/08/22/%E7%AE%80%E5%8D%95%E7%9A%84%E5%8D%8F%E7%A8%8B%E5%88%A9%E7%94%A8%E6%A1%86%E6%9E%B6/)
