import asyncio, functools
import time

def SomeFunction(parameter):
	"""
	这里是目标函数，脚本的功能都应在此函数当中。
	参数个数都由自己确定，需要与functools.partial调用的参数一致。
	"""
	time.sleep(1)
	return parameter

async def coroutine_execution(function, param1):
	"""
	通过run_in_executor方法来新建一个线程来执行耗时函数。
	注意：functools.partial调用的参数应与目标函数一致
	"""
	loop = asyncio.get_event_loop()
	result = await loop.run_in_executor(None,functools.partial(function, parameter=param1)) 
	# result为目标函数返回的值
	print(result)

def coroutine_init(function, parameters, threads):
	"""
	处理线程
	coroutine_execution()调用协程函数，可自行修改参数个数内容等。 
	"""
	times = int(len(parameters) / threads) + 1
	if len(parameters) == threads or int(len(parameters) % threads) == 0: times -= 1
	for num in range(times):
		tasks = []
		Minimum = threads * num
		Maximum = threads * (num + 1)
		if num == times - 1 and len(parameters) % threads != 0:
			Minimum = (times - 1) * threads
			Maximum = len(parameters)
		if len(parameters) <= threads:
			Minimum = 0
			Maximum = len(parameters)
		for i in range(Minimum, Maximum):
			# 此处的parameters[i]就是取目标参数的单个值，可自行调整
			future = asyncio.ensure_future(coroutine_execution(function, param1=parameters[i]))
			tasks.append(future)
		loop = asyncio.get_event_loop()
		loop.run_until_complete(asyncio.wait(tasks))
		print("[*] The {}th thread ends".format(str(num + 1)))
	return None

if __name__ == "__main__":
	words = ["Hello World.", "I'm Threezh1.", "Welcome to my blog.", "One", "Tow", "Three", "Four"]
	coroutine_init(SomeFunction, parameters=words, threads=3)