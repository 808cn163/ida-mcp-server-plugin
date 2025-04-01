[English](README.md)|中文

# IDA Pro MCP 服务端

IDA Pro MCP 服务端是一个插件，它允许通过模型上下文协议（Model Context Protocol，简称 MCP）接口远程查询和控制 IDA Pro。该插件使得 AI 助手（例如 Claude）可以直接与 IDA Pro 交互，执行二进制分析任务。

## 概述

该服务端提供了一系列工具，使 AI 助手能够执行以下操作：

- 从特定地址获取字节数据
- 获取反汇编代码
- 获取反编译的伪代码
- 查询函数名称
- 获取段（segment）信息
- 列出所有函数
- 查找交叉引用
- 获取导入/导出表
- 获取入口点
- 定义/取消定义函数
- 获取各种数据类型（dword、word、byte、qword、float、double、string）
- 获取二进制文件中的所有字符串
- 获取指定地址处指令的长度

## 安装

> **注意：** 本插件专为 IDA Pro 9.0 及以上版本设计并经过测试。

1. 确保已安装 Python 及相关依赖：

```bash
pip install -r requirements.txt
```

2. 将 `ida-mcp-server.py` 文件复制到 IDA Pro 插件目录：
   - Windows: `%Programfiles%\IDA Pro 9.0\plugins\`
   - Linux: `~/.idapro/plugins/`
   - macOS: `~/Library/Application Support/IDA Pro/plugins/`

## 配置 Claude / VSCode

在 Claude 或 VSCode 的 `mcp.json` 文件中添加以下配置：

```json
{
  "mcpServers": {
    "IDAPro": {
      "url": "http://127.0.0.1:3000/sse",
      "type": "sse"
    }
  }
}
```

## 使用方法

1. 在 IDA Pro 中打开一个二进制文件。
2. 插件将自动加载并在本地启动 MCP 服务端（端口 3000）。
3. 将你的 AI 助手（例如 Claude）连接到该服务端。
4. 使用 AI 助手执行二进制分析任务。

## 可用的分析工具

IDA Pro MCP 服务端提供以下工具：

- `get_bytes`: 获取指定地址处的字节数据
- `get_disasm`: 获取指定地址处的反汇编代码
- `get_decompiled_func`: 获取包含指定地址的函数的伪代码
- `get_function_name`: 获取指定地址处的函数名称
- `get_segments`: 获取所有段（segment）信息
- `get_functions`: 获取二进制文件中的所有函数
- `get_xrefs_to`: 获取指向指定地址的所有交叉引用
- `get_imports`: 获取所有导入函数
- `get_exports`: 获取所有导出函数
- `get_entry_point`: 获取二进制文件的入口点
- `make_function`: 在指定地址创建函数
- `undefine_function`: 取消指定地址处的函数定义
- `get_dword_at`: 获取指定地址处的 dword 数据
- `get_word_at`: 获取指定地址处的 word 数据
- `get_byte_at`: 获取指定地址处的 byte 数据
- `get_qword_at`: 获取指定地址处的 qword 数据
- `get_float_at`: 获取指定地址处的 float 数据
- `get_double_at`: 获取指定地址处的 double 数据
- `get_string_at`: 获取指定地址处的字符串
- `get_string_list`: 获取二进制文件中的所有字符串
- `get_strings`: 获取二进制文件中的所有字符串（包含地址信息）

## 最佳实践

在分析二进制文件时，建议遵循以下步骤：

1. 检查入口点
2. 分析导入表
3. 审查字符串
4. 跟踪关键 API 调用
5. 识别主要功能块
6. 分析控制流
7. 识别恶意行为
8. 分析算法和加密例程
9. 记录分析结果
10. 使用高级分析技术

## 许可证

MIT 许可证

版权所有 (c) 2023 

特此免费授予任何获得本软件及相关文档文件（以下简称“软件”）副本的人无限制地处理本软件的权利，包括但不限于使用、复制、修改、合并、发布、分发、再许可和/或销售本软件的副本，并允许向其提供本软件的人也能如此做，但须遵守以下条件：

上述版权声明和本许可声明应包含在本软件的所有副本或主要部分中。

本软件按“原样”提供，不附带任何形式的明示或暗示保证，包括但不限于适销性、特定用途适用性和非侵权的保证。在任何情况下，作者或版权持有人均不对因本软件或本软件的使用或其他交易而产生的任何索赔、损害或其他责任承担任何责任，无论是在合同诉讼、侵权诉讼还是其他诉讼中。
