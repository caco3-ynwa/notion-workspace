# Go 模块

此目录预留给 Go 实现，目前还没有 Go 业务代码。

- `cmd/notion-sync/main.go`：未来的命令入口。
- `internal/`：模块内部使用的包。
- `go.mod`：Go 模块定义；安装 Go 后在本目录管理依赖。

添加入口后，可在仓库根目录执行 `bash scripts/build_go.sh`，产物写入 `dist/go/notion-sync`。
Python 产物位于 `dist/python/`，两者不会相互覆盖。
