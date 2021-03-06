[TOC]
# 测试
linux内核提供了



# 系统调用
这些系统调用按照功能逻辑大致可分为

- 进程控制
- 文件系统控制
- 系统控制
- 存管管理
- 网络管理
- socket 控制
- 用户管理
- 进程间通信

熟练了解和掌握上面这些系统调用是对系统程序员的必备要求，但对于一个开发内核者或内核开发者来[1]说死记硬背下这些调用还远远不够。如果你仅仅知道存在的调用而不知道为什么它们会存在，或只知道如何使用调用而不知道这些调用在系统中的主要用途，那么你离驾驭系统还有不小距离。

要弥补这个鸿沟

第一: 你必须明白系统调用在内核里的主要用途。虽然上面给出了数种分类，不过总的概括来讲系统调用主要在系统中的用途无非以下几类：

- 控制硬件——系统调用往往作为硬件资源和用户空间的抽象接口，比如读写文件时用到的 write/read 调用
- 设置系统状态或读取内核数据——因为系统调用是用户空间和内核的唯一通讯手段[2]，所以用户设置系统状态，比如开/关某项内核服务（设置某个内核变量），或读取内核数据都必须通过系统调用。比如 getpgid、getpriority、setpriority、sethostname
- 进程管理——一系列调用接口是用来保证系统中进程能以多任务，在虚拟内存环境下得以运行。比如 fork、clone、execve、exit 等

第二: 什么服务应该存在于内核；或者说什么功能应该实现在内核而不是在用户空间。这个问题并不没有明确的答案，有些服务你可以选择在内核完成，也可以在用户空间完成。选择在内核完成通常基于以下考虑

- 服务必须获得内核数据，比如一些服务必须获得中断或系统时间等内核数据
- 从安全角度考虑，在内核中提供的服务相比用户空间提供的毫无疑问更安全，很难被非法访问到
- 从效率考虑，在内核实现服务避免了和用户空间来回传递数据以及保护现场等步骤，因此效率往往要比实现在用户空间高许多。比如,httpd 等服务
- 如果内核和用户空间都需要使用该服务，那么最好实现在内核空间，比如随机数产生

## 关系
系统调用、用户编程接口（API）、系统命令、和内核函数的关系

### 系统调用
系统调用并非直接和程序员或系统管理员打交道，它仅仅是一个通过软中断机制向内核提交请求，获取内核服务的接口

备注: 
> - 程序不能随便调用资源(比如CPU、内存)不安全，所有操作都是内核操作的，内核提供了：管理进程、管理内存、文件系统、设备控制、网络管理
> - 所以程序想要运行需要资源那么需要和内核沟通，而系统调用就是操作入口

### 用户编程接口
用户编程接口（API）,是特定开发语言封装了特定的系统调用

### 系统命令
系统命令相对编程接口更高了一层，它是内部引用 API 的可执行程序，比如我们常用的系统命令 ls、hostname 等。Linux 的系统命令格式遵循系统 V 的传统，多数放在/bin 和/sbin 下


> 而在实际使用中程序员调用的多是用户编程接口——API，而管理员使用的则多是系统命令

### 内核函数和系统调用关系
- 内核函数也是普通的函数，只是在内核实现因此要满足一些内核编程的要求
- 系统调用是用户进入内核的接口
- 不同的系统调用会找不同的内核函数


> 从用户角度向内核看，依次是系统命令、编程接口、系统调用和内核函数
