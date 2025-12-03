# 開發流程小抄

1. 進入專案資料夾：
cd your-project

2. 建議開個 venv（如果還沒）：
python -m venv venv
source venv/bin/activate   # Windows 是 venv\Scripts\activate
pip install -r requirements.txt

3. 啟動 Flask：
python run.py

4. 打開瀏覽器：http://127.0.0.1:5000
→ 應該看到：This is Flask app

5. 跑測試：
pytest
