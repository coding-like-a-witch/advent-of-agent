# Day 03 - 在 Python 代码中加载 YAML 配置的智能体

**挑战链接**: [Advent of Agents - Day 03](https://adventofagents.com/day/03)

![Day 03 Screenshot](figs/day-03.png)

## 关键学习

- Google ADK 提供了内置方法 `load_agent_from_config()` 来从 YAML 文件加载智能体配置
- YAML 配置文件可以包含完整的智能体定义，包括名称、描述、指令、模型和工具
- 工具可以在 YAML 文件中通过 `tools` 部分定义，例如 `google_search`
- ADK Web Developer UI 可以自动检测并加载 Python 代码中定义的智能体
- 使用 `Path(__file__).parent` 可以获取相对于当前脚本文件的路径，方便加载同目录下的 YAML 文件

## 面临的挑战

- 最初尝试手动解析 YAML 文件，但发现 ADK 有更优雅的内置方法
- 需要了解 `Agent` 类和 `LlmAgent` 类的区别，以及何时使用 `load_agent_from_config`
- 确保 YAML 文件中的工具名称与 ADK 提供的工具名称匹配

## 资源

- [ADK Config Agent Documentation](http://google.github.io/adk-docs/agent/config/) - 使用 YAML 配置构建智能体的官方文档
- [ADK Agents API Reference](http://google.github.io/adk-docs/agents/) - 智能体 API 参考文档
- [Google ADK Python Documentation](http://google.github.io/adk-docs/) - ADK Python 完整文档

## 问题 / 开放话题

- 不是必须要用 Gemini Pro 3，在 YAML 配置里把 model 模型改成 free tier 里提供的即可
