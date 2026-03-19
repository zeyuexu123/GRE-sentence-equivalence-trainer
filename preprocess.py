import re
import json

with open('gre_data.txt', 'r', encoding='utf-8') as file:
    raw_text = file.read()

def generate_gre_pairs(text): 

    clean_text = ' '.join(text.split())
    
    entries = re.split(r'\d+\.\s*', clean_text)
    
    pairs = []
    seen = set()
    chinese_translations = {}
    
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
            
        matches = re.findall(
            r'([a-zA-Z\s\-]+?)\s*([\u4e00-\u9fff\s]+?)(?=[a-zA-Z]|$)', 
            entry
        )
        
        if len(matches) >= 2:
            word1, trans1 = matches[0][0].strip(), "".join(matches[0][1].split())
            word2, trans2 = matches[1][0].strip(), "".join(matches[1][1].split())
            
            key = tuple(sorted([word1, word2]))
            if key not in seen:
                seen.add(key)
                pairs.append([word1, word2])
            
            for w, t in [(word1, trans1), (word2, trans2)]:
                if w not in chinese_translations:
                    chinese_translations[w] = set()
                chinese_translations[w].add(t)
    
    return pairs, {k: list(v) for k, v in chinese_translations.items()}


gre_pairs, gre_translations = generate_gre_pairs(raw_text)

pairs_js = "const grePairs = " + json.dumps(gre_pairs, indent=2, ensure_ascii=False) + ";"
translations_js = "const greTranslations = " + json.dumps(gre_translations, indent=2, ensure_ascii=False) + ";"

with open("gre_pair.js", "w", encoding="utf-8") as f:
    f.write(pairs_js)
with open("gre_translation.js", "w", encoding="utf-8") as f:
    f.write(translations_js)

print("Output written to gre_pair.js and gre_translation.js")