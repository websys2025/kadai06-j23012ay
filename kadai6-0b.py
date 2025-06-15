import requests
import pandas as pd


#課題6-2: オープンデータAPIを使ったポケモンデータ取得プログラム

#オープンデータの名前と概要：
#PokéAPI (RESTful Pokémon API)
#- 全ポケモンの詳細情報を提供する無料のRESTful API
#- ポケモンの基本情報、ステータス、タイプ、アビリティなどを取得可能
#認証不要で完全無料で利用可能
#エンドポイント：
# https://pokeapi.co/api/v2/pokemon/{ポケモン名またはID}  
#機能：
#指定したポケモンの詳細データをJSON形式で取得
#ポケモンの基本ステータス（HP、攻撃力、防御力など）を取得
#タイプ、身長、体重、アビリティなどの情報を取得
# 使い方：
#  1. APIキー不要で即座に利用開始
#  2. ポケモン名リストを指定
#  3. 各ポケモンのAPIを呼び出し
#  4. JSONデータを解析してDataFrameに変換
#  5. ポケモンの基本情報を表示


# PokéAPI エンドポイント
API_URL = "https://pokeapi.co/api/v2/pokemon"

# 取得したいポケモンのリスト
pokemon_names = ["pikachu", "ditto", "charizard", "blastoise", "venusaur"]

pokemon_data = []

print("PokéAPI ポケモンデータ取得プログラム")
print("=" * 50)

for pokemon_name in pokemon_names:
    try:
        print(f"{pokemon_name}のデータを取得中...")
        
        response = requests.get(f"{API_URL}/{pokemon_name}")
        data = response.json()
        
        pokemon_info = {
            "名前": data["name"].capitalize(),
            "ID": data["id"],
            "身長": f"{data['height'] / 10}m",  
            "体重": f"{data['weight'] / 10}kg",  
            "HP": data["stats"][0]["base_stat"],
            "攻撃": data["stats"][1]["base_stat"],
            "防御": data["stats"][2]["base_stat"],
            "タイプ": ", ".join([t["type"]["name"] for t in data["types"]])
        }
        
        pokemon_data.append(pokemon_info)
        print(f"  → 取得完了: {pokemon_info['名前']} (ID: {pokemon_info['ID']})")
        
    except Exception as e:
        print(f"  → {pokemon_name}のデータ取得エラー: {e}")

print("\n" + "=" * 50)

if pokemon_data:
    df = pd.DataFrame(pokemon_data)
    
    col_replace_dict = {
        "名前": "ポケモン名",
        "ID": "図鑑No",
        "身長": "身長",
        "体重": "体重", 
        "HP": "HP",
        "攻撃": "攻撃力",
        "防御": "防御力",
        "タイプ": "タイプ"
    }
    
    new_columns = []
    for col in df.columns:
        if col in col_replace_dict:
            new_columns.append(col_replace_dict[col])
        else:
            new_columns.append(col)
    df.columns = new_columns
    
    print("取得結果:")
    print(df.to_string(index=False))
    
    print(f"\n■ 取得したポケモン数: {len(df)}匹")
    print(f"■ 平均HP: {df['HP'].mean():.1f}")
    print(f"■ 最高攻撃力: {df['攻撃力'].max()}")
    
else:
    print("データを取得できませんでした。")
