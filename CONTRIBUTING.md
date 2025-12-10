# Contributing to TextUtils

感谢你考虑为 TextUtils 做出贡献！我们欢迎各种形式的贡献，包括但不限于 bug 报告、功能建议、文档改进和代码贡献。

## Reporting Issues

如果你发现了 bug 或有功能建议，请创建一个 issue。在创建 issue 时，请提供以下信息：

### Bug 报告

- **问题描述**: 清楚地描述问题是什么
- **复现步骤**: 详细的步骤来重现问题
- **预期行为**: 你期望发生什么
- **实际行为**: 实际发生了什么
- **环境信息**:
  - Python 版本
  - 操作系统
  - TextUtils 版本

### 功能建议

- **功能描述**: 清楚地描述你想要的功能
- **使用场景**: 这个功能解决什么问题
- **示例代码**: 如果可能，提供你期望的 API 使用示例

## Submitting Pull Requests

我们欢迎 Pull Request！请遵循以下步骤：

### 1. Fork 项目

在 GitHub 上 fork 这个项目到你的账户。

### 2. 克隆仓库

```bash
git clone https://github.com/你的用户名/TextUtils.git
cd TextUtils
```

### 3. 创建分支

```bash
git checkout -b feature/your-feature-name
```

分支命名建议：
- `feature/功能名` - 新功能
- `bugfix/bug描述` - Bug 修复
- `docs/文档说明` - 文档更新

### 4. 进行修改

在你的分支上进行代码修改。

### 5. 提交代码

```bash
git add .
git commit -m "描述你的修改"
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

在 GitHub 上创建一个从你的分支到主仓库 main 分支的 Pull Request。

## Code Style

请遵循以下代码规范：

### Python 代码规范

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 代码风格指南
- 使用 4 个空格缩进（不使用 tab）
- 每行代码不超过 100 个字符
- 函数和类需要包含 docstring
- 使用类型提示（type hints）

### 命名规范

- 函数名使用 `snake_case`
- 类名使用 `PascalCase`
- 常量使用 `UPPER_CASE`
- 私有成员使用 `_leading_underscore`

### 工具

建议使用以下工具来保持代码质量：

- **black**: 代码格式化
- **flake8**: 代码检查
- **mypy**: 类型检查

## Testing

### 运行测试

所有新功能和 bug 修复都应该包含测试。使用 pytest 运行测试：

```bash
# 安装开发依赖
pip install -e .[dev]

# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_core.py

# 查看测试覆盖率
pytest --cov=textutils --cov-report=html
```

### 编写测试

- 测试文件放在 `tests/` 目录下
- 测试文件命名：`test_*.py`
- 测试函数命名：`test_*`
- 每个函数应该有多个测试用例，覆盖正常情况和边界情况

示例测试：

```python
def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
```

## 文档

- 所有公开的函数和类必须包含 docstring
- Docstring 应该包含：
  - 功能描述
  - 参数说明
  - 返回值说明
  - 使用示例（如果适用）

- 如果修改了 API，请同时更新 README.md

## 提交规范

提交信息应该清晰明了，遵循以下格式：

```
类型: 简短描述（不超过 50 字符）

详细描述（如果需要）
- 要点 1
- 要点 2
```

类型包括：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整（不影响功能）
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

## 行为准则

- 尊重所有贡献者
- 欢迎建设性的反馈
- 保持友好和专业的交流
- 关注问题本身，而不是人

## 问题？

如果你有任何问题，欢迎在 issue 中提问或联系维护者。

感谢你的贡献！🎉

