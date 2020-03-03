# 消息队列知识点整理

## 什么是消息队列

消息队列中间件是分布式系统中重要的组件，主要解决应用解耦，异步消息，流量削锋等问题，实现高性能，高可用，可伸缩和最终一致性架构。目前使用较多的消息队列有 ActiveMQ，RabbitMQ，ZeroMQ，Kafka，MetaMQ，RocketMQ

## 消息队列应用场景

### 通过异步处理提高系统性能（削峰、减少响应所需时间）

时间上解耦

### 降低系统耦合性

空间上解耦

## 使用消息队列带来的一些问题

- **系统可用性降低**：你需要考虑消息丢失或者说 MQ 挂掉等等的情况。
- **系统复杂性提高**：你需要保证消息没有被重复消费、处理消息丢失的情况、保证消息传递的顺序性等等问题。
- **一致性问题：** 消息队列带来的异步确实可以提高系统响应速度。但如果消息没有被正确消费就会导致数据不一致的情况。

## JMS VS AMQP

| 对比方向     | JMS                                 | AMQP             |
| ------------ | ----------------------------------- | ---------------- |
| 定义         | Java API                            | 协议             |
| 跨语言       | 否                                  | 是               |
| 跨平台       | 否                                  | 是               |
| 支持消息类型 | 支持多种消息类型 ，我们在上面提到过 | byte[]（二进制） |

JMS 提供两种消息模型：

1. Peer-2-Peer;
2. Pub/sub

AMQP 提供了五种消息模型：

1. direct exchange；
2. fanout exchange；
3. topic change；
4. headers exchange；
5. system exchange。

本质来讲，AMQP 的后四种和 JMS 的 pub/sub 模型没有太大差别，仅是在路由机制上做了更详细的划分；

## 如何保证消息的可靠性传输（如何处理消息丢失的问题）

## RabbitMQ 中 Exchange Types 的四种模式

### 分列模式（fanout）

分列模式不经过 routing key 的匹配，它会把所有发送到该 Exchange 的消息路由到所有与它绑定的 Queue 中。

### 直接模式（direct）

直接模式不匹配 Exchange Types，它会把消息路由到那些 binding key 与 routing key 完全匹配的 Queue 中。

### 主题模式（topic）

它与 direct 类型的 Exchage 相似，也是将消息路由到 binding key 与 routing key 相匹配的 Queue 中，但这里的匹配规则有些不同，它约定：

- routing key 为一个句点号“. ”分隔的字符串（我们将被句点号“. ”分隔开的每一段独立的字符串称为一个单词），如“stock.usd.nyse”、“nyse.vmw”、“quick.orange.rabbit”
- binding key 与 routing key 一样也是句点号“. ”分隔的字符串
- binding key 中可以存在两种特殊字符“_”与“#”，用于做模糊匹配，其中“_”用于匹配一个单词，“#”用于匹配多个单词（可以是零个）
