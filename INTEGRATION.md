# Integration với vocab-extractor

Hướng dẫn tích hợp 2 tools để tạo workflow học từ vựng hoàn chỉnh.

## 🔄 Workflow Pipeline

```
Text File → vocab-extractor → CSV → anki-vocab-generator → Anki Deck
```

## 📋 Chi tiết từng bước

### Step 1: Clone cả 2 repos

```bash
cd ~/PycharmProjects

# Clone vocab-extractor
git clone https://github.com/nhatnamduong688/vocab-extractor.git

# Clone anki-vocab-generator  
git clone https://github.com/nhatnamduong688/anki-vocab-generator.git
```

### Step 2: Cài đặt dependencies

```bash
# Cài cho vocab-extractor
cd vocab-extractor
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_sm

# Cài cho anki-vocab-generator
cd ../anki-vocab-generator
pip3 install -r requirements.txt
```

### Step 3: Sử dụng Pipeline

```bash
# 1. Chuẩn bị text file
echo "Your English text content here..." > article.txt

# 2. Extract vocabulary
cd vocab-extractor
python3 vocab_extractor.py article.txt article_vocab.csv

# 3. Generate Anki deck
cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/article_vocab.csv \
    -o article_deck.apkg \
    -n "Article Vocabulary"

# 4. Import vào Anki
# Open Anki → File → Import → article_deck.apkg
```

## 🎯 Use Cases

### Use Case 1: Học từ vựng từ technical articles

```bash
# Extract từ blog post về React
cd vocab-extractor
python3 vocab_extractor.py react_article.txt react_vocab.csv

# Generate deck
cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/react_vocab.csv \
    -n "React Technical Vocabulary"
```

### Use Case 2: Học từ nhiều sources

```bash
# Extract từ nhiều files
cd vocab-extractor
python3 vocab_extractor.py chapter1.txt ch1.csv
python3 vocab_extractor.py chapter2.txt ch2.csv
python3 vocab_extractor.py chapter3.txt ch3.csv

# Merge CSVs (manual hoặc dùng script)
cat ch1.csv ch2.csv ch3.csv > book_vocab.csv

# Generate 1 deck duy nhất
cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/book_vocab.csv \
    -n "Complete Book Vocabulary"
```

### Use Case 3: Tạo deck theo level

```bash
# Config vocab-extractor cho beginner (chỉ lấy từ đơn)
# Edit vocab_extractor.py:
# CONFIG["INCLUDE"]["single_words"] = True
# CONFIG["INCLUDE"]["phrasal_verbs"] = False
# CONFIG["FILTER"]["allowed_pos"] = ["NOUN", "VERB", "ADJ"]

cd vocab-extractor
python3 vocab_extractor.py beginner_text.txt beginner.csv

cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/beginner.csv \
    -n "Beginner Vocabulary"

# Config vocab-extractor cho advanced (cụm từ phức tạp)
# CONFIG["INCLUDE"]["single_words"] = False
# CONFIG["INCLUDE"]["phrasal_verbs"] = True
# CONFIG["INCLUDE"]["collocations"] = True
# CONFIG["FILTER"]["min_phrase_length"] = 3

cd vocab-extractor
python3 vocab_extractor.py advanced_text.txt advanced.csv

cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/advanced.csv \
    -n "Advanced Phrases"
```

## 🔧 Automation Script

Tạo script để tự động hóa toàn bộ pipeline:

```bash
#!/bin/bash
# vocab-to-anki.sh

INPUT_FILE=$1
DECK_NAME=$2

# Check arguments
if [ -z "$INPUT_FILE" ] || [ -z "$DECK_NAME" ]; then
    echo "Usage: ./vocab-to-anki.sh <input_file> <deck_name>"
    exit 1
fi

# Get file basename
BASENAME=$(basename "$INPUT_FILE" .txt)

echo "🚀 Starting pipeline..."

# Step 1: Extract
echo "📝 Extracting vocabulary..."
cd ~/PycharmProjects/vocab-extractor
python3 vocab_extractor.py "$INPUT_FILE" "${BASENAME}.csv"

# Step 2: Generate
echo "🎴 Generating Anki deck..."
cd ~/PycharmProjects/anki-vocab-generator
python3 generator.py "../vocab-extractor/${BASENAME}.csv" \
    -o "${BASENAME}.apkg" \
    -n "$DECK_NAME"

echo "✅ Done! Import ${BASENAME}.apkg into Anki"
```

**Sử dụng:**
```bash
chmod +x vocab-to-anki.sh
./vocab-to-anki.sh article.txt "My Article Vocab"
```

## 📊 Format CSV được hỗ trợ

### Từ vocab-extractor → anki-vocab-generator

| Column | Required | Description |
|--------|----------|-------------|
| text | ✅ Yes | Cụm từ/từ vựng |
| type | ❌ No | Loại (verb_prep, collocation, etc.) |
| pos/structure | ❌ No | Cấu trúc ngữ pháp |
| lemma | ❌ No | Dạng gốc |
| definition | ✅ Yes | Định nghĩa |

### Minimum viable CSV

```csv
text,definition
hello,a greeting
world,the earth
```

### Full featured CSV (from vocab-extractor)

```csv
text,type,pos/structure,lemma,definition
look up,phrasal_verb,VERB+PART,look up,search for information
api design,collocation,NOUN_NOUN,api design,designing an API
```

## 🎨 Customization

### Tùy chỉnh vocab-extractor

Edit `vocab_extractor.py`:
```python
CONFIG = {
    "FILTER": {
        "allowed_pos": ["VERB", "ADJ"],  # Chỉ lấy động từ và tính từ
        "min_phrase_length": 2,           # Tối thiểu 2 từ
    },
    "INCLUDE": {
        "single_words": False,
        "phrasal_verbs": True,
        "collocations": True,
    }
}
```

### Tùy chỉnh anki-vocab-generator

Edit `generator.py` - CSS section để thay đổi:
- Màu sắc gradient
- Font chữ
- Kích thước
- Layout

## 🔗 Links

- **vocab-extractor**: https://github.com/nhatnamduong688/vocab-extractor
- **anki-vocab-generator**: https://github.com/nhatnamduong688/anki-vocab-generator
- **Anki**: https://apps.ankiweb.net/

## 💡 Tips & Best Practices

1. **Tạo folders có tổ chức**
```
~/learning/
├── sources/          # Text files gốc
├── vocab-csvs/       # CSVs extracted
└── anki-decks/       # .apkg files
```

2. **Đặt tên có ý nghĩa**
```bash
python3 generator.py vocab.csv -n "Frontend Design - Week 1"
python3 generator.py vocab.csv -n "IELTS Reading - Practice 5"
```

3. **Backup CSVs**
- CSVs có thể tái sử dụng
- Có thể merge nhiều CSVs
- Dễ edit trong Excel/Google Sheets

4. **Version control**
```bash
# Commit CSVs để track progress
git add *.csv
git commit -m "Add vocabulary from Chapter 3"
```

---

**Chúc bạn học tốt! 🎓✨**

