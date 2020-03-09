# Spring 相关知识点整理

## Spring 基础

### 什么是 IoC

IoC 就是控制反转，是指创建对象的控制权的转移，以前创建对象的主动权和时机是由自己把控的，而现在这种权力转移到 Spring 容器中，并由容器根据配置文件去创建实例和管理各个实例之间的依赖关系，对象与对象之间松散耦合，也利于功能的复用。DI 依赖注入和控制反转是同一个概念的不同角度的描述，即应用程序在运行时依赖 IoC 容器来动态注入对象需要的外部资源。

### 依赖注入有哪几种方式

Spring 的 IOC 有三种注入方式 ：构造器注入、setter 方法注入、根据注解注入。

### Spring Bean 的生命周期

### Spring 容器中包含了哪些常用组件（至少说 5 个），作用是什么、场景是什么

### Spring 自动注入的原理，有哪些局限

### Spring 源码当中如何来搞定循环依赖

### 如何干净扩展 Spring，比如自定义实现自动注入的注解

### MyBatis 中我歌月徘徊了 Spring 中的哪些扩展？引入了哪些问题

### Spring 支持的几种 bean 的作用域

Spring 容器中的 bean 可以分为 5 个范围：

- singleton：默认，每个容器中只有一个 bean 的实例，单例的模式由 BeanFactory 自身来维护。

- prototype：为每一个 bean 请求提供一个实例。

- request：为每一个网络请求创建一个实例，在请求完成以后，bean 会失效并被垃圾回收器回收。

- session：与 request 范围类似，确保每个 session 中有一个 bean 的实例，在 session 过期后，bean 会随之失效。

- global-session：全局作用域，global-session 和 Portlet 应用相关。当你的应用部署在 Portlet 容器中工作时，它包含很多 portlet。如果你想要声明让所有的 portlet 共用全局的存储变量的话，那么这全局变量需要存储在 global-session 中。全局作用域与 Servlet 中的 session 作用域效果相同。

### Spring 框架中的单例 Beans 是线程安全的么

Spring 框架并没有对单例 bean 进行任何多线程的封装处理。关于单例 bean 的线程安全和并发问题需要开发者自行去搞定。但实际上，大部分的 Spring bean 并没有可变的状态(比如 Service 类和 DAO 类)，所以在某种程度上说 Spring 的单例 bean 是线程安全的。如果你的 bean 有多种状态的话（比如 View Model 对象），就需要自行保证线程安全。最浅显的解决办法就是将多态 bean 的作用域由“singleton”变更为“prototype”。

### Spring 如何处理线程并发问题

在一般情况下，只有无状态的 Bean 才可以在多线程环境下共享，在 Spring 中，绝大部分 Bean 都可以声明为 singleton 作用域，因为 Spring 对一些 Bean 中非线程安全状态采用 ThreadLocal 进行处理，解决线程安全问题。

ThreadLocal 和线程同步机制都是为了解决多线程中相同变量的访问冲突问题。同步机制采用了“时间换空间”的方式，仅提供一份变量，不同的线程在访问前需要获取锁，没获得锁的线程则需要排队。而 ThreadLocal 采用了“空间换时间”的方式。

ThreadLocal 会为每一个线程提供一个独立的变量副本，从而隔离了多个线程对数据的访问冲突。因为每一个线程都拥有自己的变量副本，从而也就没有必要对该变量进行同步了。ThreadLocal 提供了线程安全的共享对象，在编写多线程代码时，可以把不安全的变量封装进 ThreadLocal。

## Spring 事务

### Spring 事务的实现方式和实现原理

Spring 事务的本质其实就是数据库对事务的支持，没有数据库的事务支持，spring 是无法提供事务功能的。真正的数据库层的事务提交和回滚是通过 binlog 或者 redo log 实现的。

### Spring 事务的种类

Spring 支持编程式事务管理和声明式事务管理两种方式：

① 编程式事务管理使用 TransactionTemplate。

② 声明式事务管理建立在 AOP 之上的。其本质是通过 AOP 功能，对方法前后进行拦截，将事务处理的功能编织到拦截的方法中，也就是在目标方法开始之前加入一个事务，在执行完目标方法之后根据执行情况提交或者回滚事务。

### Spring 事务的传播行为

- PROPAGATION_REQUIRED：如果当前没有事务，就创建一个新事务，如果当前存在事务，就加入该事务，该设置是最常用的设置。

- PROPAGATION_SUPPORTS：支持当前事务，如果当前存在事务，就加入该事务，如果当前不存在事务，就以非事务执行。
- PROPAGATION_MANDATORY：支持当前事务，如果当前存在事务，就加入该事务，如果当前不存在事务，就抛出异常。
- PROPAGATION_REQUIRES_NEW：创建新事务，无论当前存不存在事务，都创建新事务。
- PROPAGATION_NOT_SUPPORTED：以非事务方式执行操作，如果当前存在事务，就把当前事务挂起。
- PROPAGATION_NEVER：以非事务方式执行，如果当前存在事务，则抛出异常。
- PROPAGATION_NESTED：如果当前存在事务，则在嵌套事务内执行。如果当前没有事务，则按 REQUIRED 属性执行。

  |                          | 当前没有事务 | 当前有事务 |
  | ------------------------ | ------------ | ---------- |
  | propgation_required      | new          | keep       |
  | propgation_supports      | keep         | keep       |
  | propgation_mandatory     | keep         | error      |
  | propgation_required_new  | new          | hang       |
  | propgation_not_supported | keep         | hang       |
  | propgation_never         | keep         | error      |
  | propgation_nested        | new          | nest       |

### Spring 事务的隔离级别

- ISOLATION_DEFAULT：这是个 PlatfromTransactionManager 默认的隔离级别，使用数据库默认的事务隔离级别。

- ISOLATION_READ_UNCOMMITTED：读未提交，允许另外一个事务可以看到这个事务未提交的数据。
- ISOLATION_READ_COMMITTED：读已提交，保证一个事务修改的数据提交后才能被另一事务读取，而且能看到该事务对已有记录的更新。
- ISOLATION_REPEATABLE_READ：可重复读，保证一个事务修改的数据提交后才能被另一事务读取，但是不能看到该事务对已有记录的更新。
- ISOLATION_SERIALIZABLE：一个事务在执行的过程中完全看不到其他事务对数据库所做的更新。

## Spring AOP

### 解释一下 Spring AOP 里面的几个名词

- 切面（Aspect）：被抽取的公共模块，可能会横切多个对象。 在 Spring AOP 中，切面可以使用通用类（基于模式的风格） 或者在普通类中以 @AspectJ 注解来实现。

- 连接点（Join point）：指方法，在 Spring AOP 中，一个连接点 总是 代表一个方法的执行。
- 通知（Advice）：在切面的某个特定的连接点（Join point）上执行的动作。通知有各种类型，其中包括“around”、“before”和“after”等通知。许多 AOP 框架，包括 Spring，都是以拦截器做通知模型， 并维护一个以连接点为中心的拦截器链。
- 切入点（Pointcut）：切入点是指 我们要对哪些 Join point 进行拦截的定义。通过切入点表达式，指定拦截的方法，比如指定拦截 add*、search*。
- 引入（Introduction）：（也被称为内部类型声明（inter-type declaration））。声明额外的方法或者某个类型的字段。Spring 允许引入新的接口（以及一个对应的实现）到任何被代理的对象。例如，你可以使用一个引入来使 bean 实现 IsModified 接口，以便简化缓存机制。
- 目标对象（Target Object）： 被一个或者多个切面（aspect）所通知（advise）的对象。也有人把它叫做被通知（adviced）对象。 既然 Spring AOP 是通过运行时代理实现的，这个对象永远是一个 被代理（proxied）对象。
- 织入（Weaving）：指把增强应用到目标对象来创建新的代理对象的过程。Spring 是在运行时完成织入。

切入点（point cut）和连接点（join point）匹配的概念是 AOP 的关键，这使得 AOP 不同于其它仅仅提供拦截功能的旧技术。 切入点使得定位通知（advice）可独立于 OO 层次。 例如，一个提供声明式事务管理的 around 通知可以被应用到一组横跨多个对象中的方法上（例如服务层的所有业务操作）。

### Spring 通知有哪些类型

- 前置通知（Before advice）：在某连接点（join point）之前执行的通知，但这个通知不能阻止连接点前的执行（除非它抛出一个异常）。

- 返回后通知（After returning advice）：在某连接点（join point）正常完成后执行的通知：例如，一个方法没有抛出任何异常，正常返回。

- 抛出异常后通知（After throwing advice）：在方法抛出异常退出时执行的通知。

- 后通知（After (finally) advice）：当某连接点退出的时候执行的通知（不论是正常返回还是异常退出）。

- 环绕通知（Around Advice）：包围一个连接点（join point）的通知，如方法调用。这是最强大的一种通知类型。 环绕通知可以在方法调用前后完成自定义的行为。它也会选择是否继续执行连接点或直接返回它们自己的返回值或抛出异常来结束执行。 环绕通知是最常用的一种通知类型。大部分基于拦截的 AOP 框架，例如 Nanning 和 JBoss4，都只提供环绕通知。

## Spring MVC

### SpringMVC 的流程

#### 1. 用户发送请求至前端控制器 DispatcherServlet

#### 2. DispatcherServlet 收到请求后，在 HandlerMapping 中，通过 URL 找到 Handler（也就是 Controller），然后返回给 DispatcherServlet

#### handlerMapping 根据请求 URL 找到具体的处理器，生成处理器对象及处理器拦截器(如果有则生成)一并返回给 DispatcherServlet

#### DispatcherServlet 调用 HandlerAdapter 处理器适配器

#### HandlerAdapter 经过适配调用 具体处理器(Handler，也叫后端控制器)

#### Handler 执行完成返回 ModelAndView

#### HandlerAdapter 将 Handler 执行结果 ModelAndView 返回给 DispatcherServlet

#### DispatcherServlet 将 ModelAndView 传给 ViewResolver 视图解析器进行解析

#### ViewResolver 解析后返回具体 View

#### DispatcherServlet 对 View 进行渲染视图（即将模型数据填充至视图中）

#### DispatcherServlet 响应用户

## Spring Boot

## Spring Data Jpa

## Spring Cloud

### 什么是微服务

Spring Cloud 流应用程序启动器是基于 Spring Boot 的 Spring 集成应用程序，提供与外部系统的集成。Spring Cloud Task，一个生命周期短暂的微服务框架，用于快速构建执行有限数据处理的应用程序。

### 什么是 Spring Cloud

### Spring Cloud 如何实现服务的注册和发现

当我们开始一个项目时，我们通常在属性文件中进行所有的配置。随着越来越多的服务开发和部署，添加和修改这些属性变得更加复杂。有些服务可能会下降，而某些位置可能会发生变化。手动更改属性可能会产生问题。 Eureka 服务注册和发现可以在这种情况下提供帮助。由于所有服务都在 Eureka 服务器上注册并通过调用 Eureka 服务器完成查找，因此无需处理服务地点的任何更改和处理。

### Ribbon 和 Feign 的区别

### Spring Cloud 断路器的作用

### 负载平衡的意义什么

在计算中，负载平衡可以改善跨计算机，计算机集群，网络链接，中央处理单元或磁盘驱动器等多种计算资源的工作负载分布。负载平衡旨在优化资源使用，最大化吞吐量，最小化响应时间并避免任何单一资源的过载。使用多个组件进行负载平衡而不是单个组件可能会通过冗余来提高可靠性和可用性。负载平衡通常涉及专用软件或硬件，例如多层交换机或域名系统服务器进程。

### 什么是 Spring Cloud Bus

### Spring Cloud 和 Dubbo 有什么什么区别

### Spring Cloud 的组件分别是用来干什么的
