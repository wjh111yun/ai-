# AI 合同风险工作台

## 项目目标

阶段一（MVP）不接入 AI，交付“合同—风险—任务—处理记录”的可演示闭环。技术栈为 Vue 3 + Vite + Element Plus + Pinia（前端），FastAPI + SQLAlchemy + SQLite（后端），JWT 鉴权，本地 `backend/uploads/` 附件存储。

## 目录结构

- `frontend/`：Vue 单页应用；业务页面在 `src/views/`，请求封装在 `src/api/`。
- `backend/`：FastAPI 服务；`app/api/` 路由，`app/models/` 数据模型，`app/schemas/` 请求响应模型，`app/services/` 业务逻辑，`app/core/` 配置与安全能力。
- `docs/`：需求、设计与接口文档。
- `backend/uploads/`：本地附件，禁止提交 Git。

## 常用命令

```powershell
# 后端
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# 前端
cd frontend
npm install
npm run dev
```

## 命名规范

- Python 文件、变量、函数使用 `snake_case`；类使用 `PascalCase`。
- API 路径使用复数资源名与小写连字符；所有业务接口以 `/api` 开头。
- Vue 组件使用 `PascalCase.vue`；视图页面按业务命名。
- 数据库存储枚举值使用小写英文，例如 `todo`、`doing`、`done`。

## 禁止修改或提交

- 不提交 `.env`、`backend/uploads/`、`*.db`、虚拟环境、`node_modules/` 和构建产物。
- 不保存明文密码；密码哈希、JWT 密钥和当前用户身份必须由后端处理。
- 除登录和健康检查外，接口默认应要求 JWT；不要信任前端传入的操作人 ID。

## 任务完成后检查

- 后端：运行 `uvicorn app.main:app --reload --port 8000`，访问 `/api/health` 与 `/docs`。
- 前端：运行 `npm run build`；开发环境确认可访问后端健康检查接口。
- 提交前：检查 `.gitignore` 覆盖敏感文件与本地附件，并更新相关 README 或 docs。
