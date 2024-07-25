# gRPC client 建立方法

## 環境準備

使用 Python 開發，需要先安裝：

- `grpcio`：用來建立 grpc server 和 client 的 library
- `grpcio-tools`：根據事先定義好的 `.proto` 檔，產生 python 模組的 CLI 工具，跟 client 本體無關 (不用放到 docker 容器中)

```sh
pip install grpcio grpcio-tools
```

## 產生協定模組

- 把定義好的協定檔放到專案中預計放置模組的地方
  - 以這個專案為例就是 `example_client/proto/`

```sh
example_client/proto/
└── example.proto # 原始協定檔
```

- 透過事先安裝的 `grpcio-tools` 產生對應模組
  - **注意: 實際模組名稱是 `grpc_tools`，不是 `grpcio-tools`**
  - 各個參數都設定為當前目錄 `.` 即可

```sh
python -m grpc_tools.protoc \
--pyi_out . --python_out . --grpc_python_out . -I . \
example_client/proto/*.proto
```

- 套件會在指定的位置產生 python 模組

```sh
example_client/proto/
├── example.proto # 原始協定檔
├── example_pb2.py # 請求/回覆訊息相關的資料結構
├── example_pb2.pyi # 上者的 python 描述檔 
└── example_pb2_grpc.py # Server, Client 相關的類別
```

## 撰寫 client 程式

在專案中引入產生的模組即可作為 client 使用，請參考 `example_client`

## 啟動範例

使用指令列執行

```sh
python -m example_client
```

## 相關資訊

- [protocol buffer](https://protobuf.dev/)
- [grpc python](https://grpc.io/docs/languages/python/quickstart/)
- [grpc python API](https://grpc.github.io/grpc/python/)
