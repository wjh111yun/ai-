# Backend

FastAPI 后端服务。复制 `.env.example` 为 `.env` 后安装依赖并启动：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

开发期可访问 `http://localhost:8000/api/health` 检查服务状态，访问 `http://localhost:8000/docs` 查看接口文档。
