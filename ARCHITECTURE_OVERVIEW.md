# Writingway 架構概覽

## 程式啟動流程
- **`main.py`** 為程式進入點，載入翻譯與使用者設定，檢查依賴後開啟 `WorkbenchWindow`。
- **`workbench.py`** 管理專案清單，若 `Projects/projects.json` 不存在則建立預設專案。

## 專案編輯環境
- 每個專案使用 `ProjectWindow`，整合以下功能：
  - **ProjectTree**：呈現 Act/Chapter/Scene 階層。
  - **SceneEditor**：編輯場景與摘要。
  - **BottomStack**：提供 AI 產生內容與 TTS。
  - **CompendiumPanel**：管理世界觀資料 (`compendium.json`)。
  - **PromptsPanel**：內嵌提示詞編輯。

## AI 與提示詞管理
- `llm_api_aggregator.py` 統一連接多家 LLM 供應商（OpenAI、Anthropic、Gemini、Ollama 等）。
- 使用者的 API Key 與模型設定存放於 `settings.json` 的 `llm_configs`。
- `muse/prompts_window.py` 提供圖形化介面管理模型、溫度與字數上限等提示詞設定。

## 工作坊與輔助工具
- `workshop/workshop.py` 實作互動式工作坊，可即時對話、語音辨識、FAISS 檢索及 PDF 分析。
- `util/tts_manager.py` 透過 `pyttsx3` 或 macOS `say` 執行文字轉語音。
- `util/text_analysis.py` 等模組進行句子複雜度、被動語態等分析。
- `util/statistics.py` 統計字數與角色出現次數並生成報告。

## 主要特色摘要
- **互動式聊天工作坊**：支援頭腦風暴與情節探索。
- **可自訂提示詞**：調整 AI 協助焦點。
- **專案結構檢視**：視覺化章節、場景與角色。
- **動態世界觀資料庫**：集中管理設定細節。

Writingway 整合 FAISS、LangChain、PyQt5、spaCy 等第三方套件，提供完整的 AI 助寫介面。
