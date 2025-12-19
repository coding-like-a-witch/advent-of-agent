# Day 04 - [源码部署]

**挑战链接**: [Advent of Agents - Day 04](https://adventofagents.com/day/04)

## 关键学习

- **使用 agent-starter-pack 自动生成部署配置**：通过 `uvx agent-starter-pack enhance -d agent_engine` 命令，工具会自动生成所有 Vertex AI Agent Engine 部署所需的代码和配置（包括 `deploy.py`、`agent_engine_app.py`、Makefile 等）。部署时使用 `make deploy` 即可，工具会自动处理源代码打包、上传到云端、构建容器镜像等步骤，无需手动配置。

## 面临的挑战

- **Google Cloud SDK 安装和配置**：
  - 需要安装 Google Cloud SDK (`gcloud`)
  - 运行 `gcloud auth application-default login` 进行身份认证

- **必须启用的 API**：
  - Vertex AI API - 核心服务，用于部署 agent
  - Cloud Resource Manager API - 用于项目资源管理

- **项目 ID 配置**：
  - 必须设置 Google Cloud 项目 ID，否则部署会失败
  - 可以通过环境变量 `export GOOGLE_CLOUD_PROJECT=your-project-id` 设置
  - 或通过 Makefile 参数 `make deploy PROJECT_ID=your-project-id` 传递
  - 或使用 `gcloud config set project your-project-id` 设置默认项目

- **成本优化配置**：
  - 默认 `min-instances=1` 会导致持续计费（约 $50-100/月）
  - 可以手动设置 `min-instances=0` 实现按需启动，空闲时缩容到零
  - **Vertex AI Agent Engine Free Tier**（每月免费额度）：
    - vCPU：前 180,000 vCPU秒（50 小时）免费
    - RAM：前 360,000 GiB秒（100 小时）免费

## 代码示例

```python
# 在此添加你的代码示例
```

## 资源

- [Source-Based Deployment Tutorial(Video)](https://www.youtube.com/watch?v=8RjzMG3BKA0)
- [Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)
- [Agent Engine Deployment Docs](https://docs.cloud.google.com/agent-builder/agent-engine/deploy)

## 问题 / 开放话题

-
-
