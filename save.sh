#!/bin/bash
# save.sh - 保存并推送项目到 GitHub

echo "📦 开始保存项目..."

cd "$(dirname "$0")"

# 检查是否是 git 仓库
if [ ! -d ".git" ]; then
  echo "❌ 错误: 不是 Git 仓库"
  exit 1
fi

# 添加所有更改
git add -A

# 检查是否有更改
if git diff --cached --quiet; then
  echo "✅ 没有需要保存的更改"
  exit 0
fi

# 获取提交消息（如果提供了参数则使用，否则使用默认消息）
if [ -n "$1" ]; then
  commit_msg="$1"
else
  commit_msg="update: 项目更新 $(date '+%Y-%m-%d %H:%M')"
fi

# 提交
git commit -m "$commit_msg"

# 推送到远程
echo "🚀 推送到 GitHub..."
git push origin master

echo "✅ 保存完成!"
