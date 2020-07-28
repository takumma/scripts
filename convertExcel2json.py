from excel2json import convert_from_file
import json

xlsx_path = "C:/Users/taku3/work/scripts/1365344_1-0207r.xlsx"
convert_from_file(xlsx_path)

# {
#         "食品群": "07",
#         "食品番号": "07001",
#         "索引番号": 751.0,
#         "食品名": "あけび　果肉　生　　　",
#         "廃 棄 率": 0.0,
#         "エネルギー（kcal）": 82.0,
#         "エネルギー（kJ)": 343.0,
#         "水   分": 77.1,
#         "たんぱく質": 0.5,
#         "アミノ酸組成によるたんぱく質": "-",
#         "脂   質": 0.1,
#         "トリアシルグリセロール当量": "-",
#         "飽和脂肪酸": "-",
#         "一価不飽和脂肪酸": "-",
#         "多価不飽和脂肪酸": "-",
#         "コレステロール": "0",
#         "炭水化物": "22.0",
#         "利用可能炭水化物（単糖当量）": "-",
#         "水溶性食物繊維": 0.6,
#         "不溶性食物繊維": 0.5,
#         "食物繊維総量": 1.1,
#         "灰   分": 0.3,
#         "ナトリウム": "Tr",
#         "カリウム": 95.0,
#         "カルシウム": 11.0,
#         "マグネシウム": 14.0,
#         "リン": 22.0,
#         "鉄": 0.3,
#         "亜鉛": 0.1,
#         "銅": 0.09,
#         "マンガン": 0.15,
#         "ヨウ素": "-",
#         "セレン": "-",
#         "クロム": "-",
#         "モリブデン": "-",
#         "レチノール": "(0)",
#         "α-カロテン": "0",
#         "β-カロテン": "0",
#         "β-クリプトキサンチン": "0",
#         "β-カロテン当量": "0",
#         "レチノール活性当量": "(0)",
#         "ビタミンD": "(0)",
#         "α-トコフェロール": 0.2,
#         "β-トコフェロール": "0",
#         "γ-トコフェロール": "0",
#         "δ-トコフェロール": "0",
#         "ビタミンK": "(0)",
#         "ビタミンB1": 0.07,
#         "ビタミンB2": 0.03,
#         "ナイアシン": 0.3,
#         "ビタミンB6": 0.08,
#         "ビタミンB12": "0",
#         "葉酸": 30.0,
#         "パントテン酸": 0.29,
#         "ビオチン": "-",
#         "ビタミンC": 65.0,
#         "食塩相当量": "0",
#         "アルコール": "-",
#         "硝酸イオン": "",
#         "テオブロミン": "-",
#         "カフェイン": "-",
#         "タンニン": "-",
#         "ポリフェノール": "-",
#         "酢酸": "-",
#         "調理油": "-",
#         "有機酸": "-",
#         "重量変化率": "-",
#         "備考": "試料： みつばあけび\n全果に対する割合： 果肉 20 %、種子 7 %　 "
#     },

# {
#         "\u98df\u54c1\u7fa4": "07",
#         "\u98df\u54c1\u756a\u53f7": "07001",
#         "\u7d22\u5f15\u756a\u53f7": 751.0,
#         "\u98df\u54c1\u540d": "\u3042\u3051\u3073\u3000\u679c\u8089\u3000\u751f\u3000\u3000\u3000",
#         "\u5ec3 \u68c4 \u7387": 0.0,
#         "\u30a8\u30cd\u30eb\u30ae\u30fc\uff08kcal\uff09": 82.0,
#         "\u30a8\u30cd\u30eb\u30ae\u30fc\uff08kJ)": 343.0,
#         "\u6c34   \u5206": 77.1,
#         "\u305f\u3093\u3071\u304f\u8cea": 0.5,
#         "\u30a2\u30df\u30ce\u9178\u7d44\u6210\u306b\u3088\u308b\u305f\u3093\u3071\u304f\u8cea": "-",
#         "\u8102   \u8cea": 0.1,
#         "\u30c8\u30ea\u30a2\u30b7\u30eb\u30b0\u30ea\u30bb\u30ed\u30fc\u30eb\u5f53\u91cf": "-",
#         "\u98fd\u548c\u8102\u80aa\u9178": "-",
#         "\u4e00\u4fa1\u4e0d\u98fd\u548c\u8102\u80aa\u9178": "-",
#         "\u591a\u4fa1\u4e0d\u98fd\u548c\u8102\u80aa\u9178": "-",
#         "\u30b3\u30ec\u30b9\u30c6\u30ed\u30fc\u30eb": "0",
#         "\u70ad\u6c34\u5316\u7269": "22.0",
#         "\u5229\u7528\u53ef\u80fd\u70ad\u6c34\u5316\u7269\uff08\u5358\u7cd6\u5f53\u91cf\uff09": "-",
#         "\u6c34\u6eb6\u6027\u98df\u7269\u7e4a\u7dad": 0.6,
#         "\u4e0d\u6eb6\u6027\u98df\u7269\u7e4a\u7dad": 0.5,
#         "\u98df\u7269\u7e4a\u7dad\u7dcf\u91cf": 1.1,
#         "\u7070   \u5206": 0.3,
#         "\u30ca\u30c8\u30ea\u30a6\u30e0": "Tr",
#         "\u30ab\u30ea\u30a6\u30e0": 95.0,
#         "\u30ab\u30eb\u30b7\u30a6\u30e0": 11.0,
#         "\u30de\u30b0\u30cd\u30b7\u30a6\u30e0": 14.0,
#         "\u30ea\u30f3": 22.0,
#         "\u9244": 0.3,
#         "\u4e9c\u925b": 0.1,
#         "\u9285": 0.09,
#         "\u30de\u30f3\u30ac\u30f3": 0.15,
#         "\u30e8\u30a6\u7d20": "-",
#         "\u30bb\u30ec\u30f3": "-",
#         "\u30af\u30ed\u30e0": "-",
#         "\u30e2\u30ea\u30d6\u30c7\u30f3": "-",
#         "\u30ec\u30c1\u30ce\u30fc\u30eb": "(0)",
#         "\u03b1-\u30ab\u30ed\u30c6\u30f3": "0",
#         "\u03b2-\u30ab\u30ed\u30c6\u30f3": "0",
#         "\u03b2-\u30af\u30ea\u30d7\u30c8\u30ad\u30b5\u30f3\u30c1\u30f3": "0",
#         "\u03b2-\u30ab\u30ed\u30c6\u30f3\u5f53\u91cf": "0",
#         "\u30ec\u30c1\u30ce\u30fc\u30eb\u6d3b\u6027\u5f53\u91cf": "(0)",
#         "\u30d3\u30bf\u30df\u30f3D": "(0)",
#         "\u03b1-\u30c8\u30b3\u30d5\u30a7\u30ed\u30fc\u30eb": 0.2,
#         "\u03b2-\u30c8\u30b3\u30d5\u30a7\u30ed\u30fc\u30eb": "0",
#         "\u03b3-\u30c8\u30b3\u30d5\u30a7\u30ed\u30fc\u30eb": "0",
#         "\u03b4-\u30c8\u30b3\u30d5\u30a7\u30ed\u30fc\u30eb": "0",
#         "\u30d3\u30bf\u30df\u30f3K": "(0)",
#         "\u30d3\u30bf\u30df\u30f3B1": 0.07,
#         "\u30d3\u30bf\u30df\u30f3B2": 0.03,
#         "\u30ca\u30a4\u30a2\u30b7\u30f3": 0.3,
#         "\u30d3\u30bf\u30df\u30f3B6": 0.08,
#         "\u30d3\u30bf\u30df\u30f3B12": "0",
#         "\u8449\u9178": 30.0,
#         "\u30d1\u30f3\u30c8\u30c6\u30f3\u9178": 0.29,
#         "\u30d3\u30aa\u30c1\u30f3": "-",
#         "\u30d3\u30bf\u30df\u30f3C": 65.0,
#         "\u98df\u5869\u76f8\u5f53\u91cf": "0",
#         "\u30a2\u30eb\u30b3\u30fc\u30eb": "-",
#         "\u785d\u9178\u30a4\u30aa\u30f3": "",
#         "\u30c6\u30aa\u30d6\u30ed\u30df\u30f3": "-",
#         "\u30ab\u30d5\u30a7\u30a4\u30f3": "-",
#         "\u30bf\u30f3\u30cb\u30f3": "-",
#         "\u30dd\u30ea\u30d5\u30a7\u30ce\u30fc\u30eb": "-",
#         "\u9162\u9178": "-",
#         "\u8abf\u7406\u6cb9": "-",
#         "\u6709\u6a5f\u9178": "-",
#         "\u91cd\u91cf\u5909\u5316\u7387": "-",
#         "\u5099\u8003": "\u8a66\u6599\uff1a \u307f\u3064\u3070\u3042\u3051\u3073\n\u5168\u679c\u306b\u5bfe\u3059\u308b\u5272\u5408\uff1a \u679c\u8089 20 %\u3001\u7a2e\u5b50 7 %\u3000 "
#     },