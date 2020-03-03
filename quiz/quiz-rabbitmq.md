# RabbitMQ 知识点整理

## 简介

## 核心概念

### Producer

### Message

### Consumer

### AMQP

### Queue

### Message acknowledgment

message ackonwledgment 即消息回执，消费者在消费完消息后发送一个回执给 rabbitmq，rabbtiMq 收到回执后才将消息从队列中删除，如果没有收到回执并检测到消费者的 RabbitMQ 连接断开，那么会将该消息发送给其他消费者进行处理。这里不存在 timeout 概念，一个消费者处理消息时间再长也不会导致该消息被发送给其他消费者，除非它的 RabbitMQ 连接断开。

### Message durability

消息持久化，即 RabbitMQ 服务重启的情况下，也不会丢失消息，我们可以将 Queue 与 Message 都设置为（durable），这样可以保证绝大部分情况下我们的 RabbitMQ 消息不会丢失。小概率丢失事件无法避免（比如 RabbitMQ 服务器已经接收到生产者的消息，但还没来得及持久化该消息时 RabbitMQ 服务器就断电了），如果我们需要对这种情况也要处理，那么我们要用到事务。

### Prefetch count

### Exchange

在 RabbitMQ 中生产者不会直接将消息发送队列。实际的情况是，生产者将消息发送到 Exchange，由 Exchange 将消息路由到一个或多个 Queue 中（或者丢弃）。

### RoutingKey

RoutingKey 针对生产者而言，发送消息时一般需要指定 RoutingKey，而这个 RoutingKey 需要与 Exchange Type 及 BindingKey 联合使用才能最终生效。

### BindingKey

在绑定 Exchange 与 Queue 的同时，一般会指定一个 binding key；生产者将消息发送给 Exchange 时，一般会指定一个 routing key；当 BindingKey 与 RoutingKey 一致，或者符合模式匹配，消息就会被路由到对应的 Queue 中。在绑定多个 Queue 到同一个 Exchange 的时候，这些 Binding 允许使用相同的 BindingKey。binding key 并不是在所有情况下都生效，它依赖于 Exchange Type，比如 fanout 类型的 Exchange 就会无视 BindingKey，而是将消息路由到所有绑定到该 Exchange 的 Queue。

### Exchange Types

RabbitMQ 常用的 Exchange Type 有 fanoutk、direct、topic、headers 这四种

## 不同 Exchange Type 下消息配置的过程

### fanout

### topic

### direct

### headers
