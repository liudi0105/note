# Tomcat

## Tomcat 两个核心组件：Connector 和 Container

### Connector 组件

### Container 组件

Container 是容器的父接口，该容器的设计用的是典型的责任链的设计模式，它由四个自容器组件构成，分别是 Engine、Host、Context、Wrapper。这四个组件是负责关系，存在包含关系。通常一个 Servlet class 对应一个 Wrapper，如果有多个 Servlet 则定义多个 Wrapper，如果有多个 Wrapper 就要定义一个更高的 Container，如 Context。 Context 定义在父容器 Host 中，其中 Host 不是必须的，但是要运行 war 程序，就必须要 Host，因为 war 中必有 web.xml 文件，这个文件的解析就需要 Host 了，如果要有多个 Host 就要定义一个 top 容器 Engine 了。而 Engine 没有父容器了，一个 Engine 代表一个完整的 Servlet 引擎。

#### Container

#### Engine

#### Host

#### Context

#### Wrapper
