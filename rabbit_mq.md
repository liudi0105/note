#### RabbitMQ 中 Exchange Types 的四种模式

##### 分列模式（fanout）

分列模式不经过 routing key 的匹配，它会把所有发送到该 Exchange 的消息路由到所有与它绑定的 Queue 中。

##### 直接模式（direct）

直接模式不匹配Exchange Types，它会把消息路由到那些 binding key 与 routing key 完全匹配的Queue中。

##### 主题模式（topic）

它与direct类型的Exchage相似，也是将消息路由到binding key与routing key相匹配的Queue中，但这里的匹配规则有些不同，它约定：

- routing key为一个句点号“. ”分隔的字符串（我们将被句点号“. ”分隔开的每一段独立的字符串称为一个单词），如“stock.usd.nyse”、“nyse.vmw”、“quick.orange.rabbit”
- binding key与routing key一样也是句点号“. ”分隔的字符串
- binding key中可以存在两种特殊字符“*”与“#”，用于做模糊匹配，其中“*”用于匹配一个单词，“#”用于匹配多个单词（可以是零个）

