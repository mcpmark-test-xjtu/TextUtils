# TextUtils

一个简单的文本处理工具库，提供常用的文本操作功能。TextUtils 帮助你快速完成字符串和文本的基础处理，适用于脚本编写、数据清洗和教学示例等场景。

## Features

- 字符串反转（reverse_string） - 快速反转任意字符串
- 单词计数（count_words） - 统计文本中的单词数量
- 标题格式转换（to_title_case） - 将文本转换为标题格式
- 空白字符移除（remove_whitespace） - 移除文本中的所有空白字符
- 回文检测（is_palindrome） - 检测文本是否为回文

## Installation

### 从源码安装

```bash
git clone https://github.com/mcpmark-test-xjtu/TextUtils.git
cd TextUtils
pip install -e .
```

### 开发模式安装

```bash
pip install -e .[dev]
```

## Usage

### 示例 1：字符串反转和单词计数

```python
from textutils import reverse_string, count_words

text = "Hello world"
print(reverse_string(text))  # 输出: dlrow olleH
print(count_words(text))     # 输出: 2
```

### 示例 2：回文检测和格式转换

```python
from textutils import is_palindrome, to_title_case

print(is_palindrome("racecar"))                    # 输出: True
print(is_palindrome("A man a plan a canal Panama"))  # 输出: True
print(to_title_case("hello world"))                # 输出: Hello World
```

## API Reference

### reverse_string(text)

反转给定的字符串。

**参数**:
- `text` (str): 要反转的字符串

**返回值**:
- str: 反转后的字符串

**示例**:
```python
from textutils import reverse_string

result = reverse_string("hello")
print(result)  # 输出: olleh
```

### count_words(text)

统计文本中的单词数量。

**参数**:
- `text` (str): 要统计的文本

**返回值**:
- int: 单词数量

**示例**:
```python
from textutils import count_words

result = count_words("Hello world from Python")
print(result)  # 输出: 4
```

### is_palindrome(text, ignore_case=True, ignore_spaces=True)

检查文本是否为回文。

**参数**:
- `text` (str): 要检查的文本
- `ignore_case` (bool, optional): 是否忽略大小写，默认为 True
- `ignore_spaces` (bool, optional): 是否忽略空格，默认为 True

**返回值**:
- bool: 如果是回文返回 True，否则返回 False

**示例**:
```python
from textutils import is_palindrome

print(is_palindrome("racecar"))           # 输出: True
print(is_palindrome("RaceCar"))           # 输出: True（忽略大小写）
print(is_palindrome("race car"))          # 输出: True（忽略空格）
print(is_palindrome("hello"))             # 输出: False
```

## Contributing

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目。

## License

MIT License - 详见 [LICENSE](LICENSE) 文件
