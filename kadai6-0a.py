import requests


APP_ID = "130221fbc2d23839417235bfc7fb4f8b5d50790f"


API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"


params = {
    "appId": APP_ID,
    "statsDataId": "0003348231",        
    "cdArea": "00000,13000,27000",      
    "cdCat01": "01100",                 
    "metaGetFlg": "Y",                  
    "cntGetFlg": "N",                  
    "explanationGetFlg": "Y",          
    "annotationGetFlg": "Y",           
    "sectionHeaderFlg": "1",           
    "replaceSpChars": "0",             
    "lang": "J"                         
}

response = requests.get(API_URL, params=params)

data = response.json()
print("家計調査データ取得結果:")
print("=" * 50)
print(data)
#課題6-1: eStat-APIを使った家計調査データ取得プログラム

#取得データの種類：
#  家計調査（二人以上の世帯）- 品目別家計支出
#  全国の世帯における消費支出の動向データ

# エンドポイント：
#  https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData  
#機能：
#  - 政府統計総合窓口（e-Stat）から家計調査データをJSON形式で取得
#  - 都道府県別の家計支出データを取得

# 使い方：
#  1. APP_IDにアプリケーションIDを設定済み
#  2. paramsで家計調査の統計表IDとパラメータを指定
#  3. requests.get()でAPIを呼び出し
#  4. JSONレスポンスを取得・表示
