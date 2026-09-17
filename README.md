# AI 合同风险工作台

阶段一 MVP 用于管理合同、人工风险项、整改任务和操作记录。当前版本不接入 AI，为下一阶段的合同分析能力预留可靠的数据与权限边界。

## 技术栈

- 前端：Vue 3、Vite、Element Plus、Pinia、Vue Router
- 后端：FastAPI、SQLAlchemy、SQLite、JWT
- 附件：本地 `backend/uploads/`

## 快速启动

后端：

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

前端：

```powershell
cd frontend
npm install
npm run dev
```

前端开发服务器默认运行在 `http://localhost:5173`，后端 API 为 `http://localhost:8000`。健康检查接口为 `GET /api/health`，接口文档为 `GET /docs`。

详细范围见 [阶段一 MVP](docs/01-阶段一MVP.md)。
