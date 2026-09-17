# 阶段一 MVP

## 目标

在不接入 AI 的前提下，完成合同、附件、人工风险项、整改任务与操作记录的业务闭环，并为第二阶段 AI 工具调用保留清晰的数据和权限边界。

## 包含范围

- 账号密码登录和 JWT 鉴权；
- 工作台统计；
- 合同创建、查询、编辑、详情与附件上传下载；
- 风险项创建、编辑、关闭；
- 风险任务分配、截止日期和状态更新；
- 合同、风险、任务的操作记录。

## 当前阶段不包含

AI 对话、RAG、模型 API、向量数据库、复杂审批、电子签章、在线 Office 编辑、真实消息推送、多租户和企业单点登录。

## 核心数据

`users`、`contracts`、`documents`、`risks`、`tasks`、`audit_logs`。附件存本地，风险来源初始为 `manual`，后续可增加 `ai`。

## 第一阶段接口边界

- `POST /api/auth/login`、`GET /api/auth/me`
- `GET /api/dashboard/summary`
- `/api/contracts`：合同与附件
- `/api/contracts/{id}/risks`、`/api/risks/{id}`：风险
- `/api/tasks`、`/api/risks/{risk_id}/tasks`、`/api/tasks/{id}`：任务
- `/api/audit-logs`：操作记录

除登录外的业务接口均要求 JWT，当前用户信息只能由后端从 token 解析。
