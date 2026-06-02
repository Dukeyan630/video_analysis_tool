## 2026-06-02

### 今天做了什么
- 新增开发者日志
- 强化SQL语言基础练习
- 检查 video_analysis_project代码
### 遇到的问题
- SQL个题目还是不熟，一个是筛选出平均互动率大于10%的平台，还有一个是查每个平台互动率最高的前两条内容

### 解决方式
- 了解SQL语言的运行顺序，调整了HAVING和ORDER BY的顺序,HAVING 应该在 GROUP BY后面
- 题目3，还是不熟悉的写成了select(select...from....)from posts,实际上是新建一个临时表在里面查询也就是select ... from (select...form posts)
- 还要新增排名字段 row_number() over( partition by 平台 order by 互动率 DESC) as 排名，忘记了order by 排序后才能作为排名
### 还不熟的地方
- SQL 语言基础太差，不熟悉关键词的运行顺序，同时不太熟悉新建临时表查询的操作，需要反复编程