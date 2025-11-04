# Quick Start Guide 🚀

## Workflow hoàn chỉnh: Text → CSV → Anki

### Bước 1: Trích xuất từ vựng từ text

```bash
cd vocab-extractor
python3 vocab_extractor.py input.txt output.csv
```

**Kết quả:** File `output.csv` chứa 240 cụm từ

### Bước 2: Tạo Anki deck

```bash
cd ../anki-vocab-generator
python3 generator.py ../vocab-extractor/output.csv
```

**Kết quả:** File `vocab_deck.apkg` với 240 flashcards

### Bước 3: Import vào Anki

1. Mở **Anki**
2. **File → Import**
3. Chọn file `vocab_deck.apkg`
4. Click **Import**

Done! Bạn đã có 240 flashcards để học! 🎉

---

## Tùy chỉnh

### Đặt tên deck khác

```bash
python3 generator.py input.csv -n "Từ vựng IELTS"
```

### Đặt tên file output khác

```bash
python3 generator.py input.csv -o ielts_vocab.apkg
```

### Kết hợp cả hai

```bash
python3 generator.py input.csv -o ielts_vocab.apkg -n "IELTS Vocabulary 2024"
```

---

## Demo với file mẫu

```bash
python3 generator.py example_input.csv -o demo_deck.apkg -n "Demo Deck"
```

---

## Tips

### 💡 Tip 1: Tạo nhiều decks theo chủ đề

```bash
# Deck 1: Front-end terms
python3 generator.py frontend_vocab.csv -n "Front-end Vocabulary"

# Deck 2: Back-end terms  
python3 generator.py backend_vocab.csv -n "Back-end Vocabulary"

# Deck 3: Design patterns
python3 generator.py design_patterns.csv -n "Design Patterns"
```

### 💡 Tip 2: Chia theo level

```bash
python3 generator.py beginner.csv -n "English Vocab - Beginner"
python3 generator.py intermediate.csv -n "English Vocab - Intermediate"
python3 generator.py advanced.csv -n "English Vocab - Advanced"
```

### 💡 Tip 3: Tạo deck từ nhiều nguồn

```bash
# Từ articles
python3 ../vocab-extractor/vocab_extractor.py article1.txt vocab1.csv
python3 generator.py vocab1.csv -n "Article 1 Vocab"

# Từ books
python3 ../vocab-extractor/vocab_extractor.py book_chapter.txt vocab2.csv
python3 generator.py vocab2.csv -n "Book Chapter Vocab"
```

---

## Cấu trúc Card

### Front (Câu hỏi)
```
┌─────────────────────────────┐
│     [Gradient Background]   │
│                             │
│      API DESIGN             │
│                             │
│  [collocation] [NOUN_NOUN]  │
│                             │
└─────────────────────────────┘
```

### Back (Trả lời)
```
┌─────────────────────────────┐
│      API DESIGN             │
│  [collocation] [NOUN_NOUN]  │
├─────────────────────────────┤
│ Definition:                 │
│ The act of working out      │
│ the form of something       │
│                             │
│ Lemma: api design           │
└─────────────────────────────┘
```

---

## Troubleshooting

### ❌ Lỗi: "No module named 'genanki'"

**Giải pháp:**
```bash
pip3 install genanki
```

### ❌ Lỗi: "File not found"

**Kiểm tra:**
1. File CSV có tồn tại không?
2. Đường dẫn đúng chưa?

```bash
# Sử dụng đường dẫn tuyệt đối
python3 generator.py /Users/yourname/path/to/file.csv
```

### ❌ Cards không hiển thị đúng trong Anki

**Giải pháp:**
- Re-import lại file
- Chọn "Update existing notes" khi import lần 2

---

## Câu hỏi thường gặp

### Q: Tôi có thể edit cards sau khi import không?

A: Có! Trong Anki, chọn card → Browse → Edit để sửa nội dung.

### Q: Tôi có thể thay đổi màu sắc card không?

A: Có! Edit file `generator.py` ở phần CSS (dòng 52-135) hoặc edit trong Anki (Tools → Manage Note Types → Cards → Styling).

### Q: Làm sao để thêm audio phát âm?

A: Feature này sẽ có trong version tiếp theo. Tạm thời có thể thêm manual trong Anki hoặc dùng addon như AwesomeTTS.

### Q: Tôi có thể tạo deck cho các ngôn ngữ khác không?

A: Hiện tại tool được optimize cho tiếng Anh. Nhưng bạn có thể dùng với CSV bất kỳ có format tương tự.

---

**Happy Learning! 📚✨**

