# PyQt Template

提供一個使用 PyQt6 和 MVC (Model-View-Controller) 架構的範例程式碼，MVC 架構在 PyQt 應用中的應用方式：

1. Model: 負責管理應用的數據和邏輯。在 PyQt 應用中，這可能是一個簡單的 Python 類別，用於存儲和操作數據。

2. View: 用於呈現用戶界面。在 PyQt 中，這通常包括使用各種 widgets（如按鈕、標籤、文本框等）創建的窗口或對話框。

3. Controller: 負責接收來自 View 的輸入，處理它們（通常是通過與 Model 交互），然後更新 View。在 PyQt 應用中，這通常是通過 slots 和 signals 來實現的。

## Install PyQt6 Library

```bash
pip install PyQt6
```

## Run Code

```bash
python app.py
```
