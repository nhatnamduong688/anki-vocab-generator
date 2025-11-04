# Anki Vocab Generator 🎴

Convert vocabulary CSV files to beautiful Anki flashcard decks (.apkg)

Perfect companion for [vocab-extractor](https://github.com/nhatnamduong688/vocab-extractor) - extract vocabulary from text, then convert to Anki decks!

## Features

✨ **Beautiful card design** with gradient styling  
📚 **Automatic tagging** by phrase type  
🎯 **Smart parsing** with definitions and structure info  
⚡ **Fast generation** - hundreds of cards in seconds  
🎨 **Customizable** card templates and styling  

## Installation

```bash
git clone https://github.com/nhatnamduong688/anki-vocab-generator.git
cd anki-vocab-generator
pip install -r requirements.txt
```

Or install with pip:
```bash
pip install genanki
```

## Quick Start

### 1. Extract vocabulary (using vocab-extractor)

```bash
python vocab_extractor.py input.txt output.csv
```

### 2. Generate Anki deck

```bash
python generator.py output.csv
```

This creates `vocab_deck.apkg` ready to import into Anki!

### 3. Import to Anki

Open Anki → **File → Import** → Select `vocab_deck.apkg`

## Usage

### Basic Usage

```bash
python generator.py input.csv
```

### Custom output file

```bash
python generator.py input.csv -o my_custom_deck.apkg
```

### Custom deck name

```bash
python generator.py input.csv -n "Front-end Design Vocabulary"
```

### All options

```bash
python generator.py input.csv -o frontend_vocab.apkg -n "Front-end Design Terms"
```

## CSV Format

The tool expects CSV files with these columns:

```csv
text,type,pos/structure,lemma,definition
apply to component,verb_prep,VERB+ADP+NOUN,apply to component,put into service...
api design,collocation,NOUN_NOUN,api design,the act of working out the form...
```

**Required columns:**
- `text` - The phrase or word
- `definition` - Definition or meaning

**Optional columns:**
- `type` - Phrase type (verb_prep, collocation, noun_phrase, etc.)
- `pos/structure` - Part of speech or structure
- `lemma` - Base form

## Card Design

### Front of Card
- 🎨 **Gradient background** (purple theme)
- 📝 **Large phrase** display
- 🏷️ **Tags** showing type and structure

### Back of Card
- ✅ Everything from front
- 📖 **Definition** in clean box
- 🔤 **Lemma** (base form) if available

### Customization

Edit the CSS in `generator.py` (line 52-135) to customize:
- Colors and gradients
- Font sizes and styles
- Layout and spacing
- Background effects

## Examples

### Input CSV
```csv
text,type,pos/structure,lemma,definition
look up,phrasal_verb,VERB+PART,look up,search for information
error message,collocation,NOUN_NOUN,error message,a message indicating an error
```

### Generated Cards

**Card 1 - Front:**
```
┌────────────────────────────┐
│                            │
│       LOOK UP              │
│   [phrasal_verb] [VERB+PART]│
│                            │
└────────────────────────────┘
```

**Card 1 - Back:**
```
┌────────────────────────────┐
│       LOOK UP              │
│   [phrasal_verb] [VERB+PART]│
├────────────────────────────┤
│ Definition:                │
│ search for information     │
│                            │
│ Lemma: look up             │
└────────────────────────────┘
```

## Integration with vocab-extractor

Perfect workflow:

```bash
# Step 1: Extract phrases from text
cd vocab-extractor
python vocab_extractor.py article.txt phrases.csv

# Step 2: Generate Anki deck
cd ../anki-vocab-generator
python generator.py ../vocab-extractor/phrases.csv -o article_vocab.apkg

# Step 3: Import to Anki
# Open Anki and import article_vocab.apkg
```

## Advanced Features (Coming Soon)

- [ ] 🎵 Audio pronunciation (TTS)
- [ ] 📝 Example sentences from APIs
- [ ] 🖼️ Image support
- [ ] 🌍 Multiple languages
- [ ] 📊 Difficulty levels
- [ ] 🔄 Batch processing multiple CSVs
- [ ] 🎨 Multiple card themes
- [ ] 🔌 CLI with more options

## Troubleshooting

### "No module named 'genanki'"
```bash
pip install genanki
```

### "File not found"
Make sure the CSV file path is correct:
```bash
python generator.py /full/path/to/your/file.csv
```

### Cards not showing properly in Anki
Re-import and make sure to select "Update existing notes" if importing again.

## Requirements

- Python 3.6+
- genanki>=1.13.0

Optional:
- gtts (for audio)
- beautifulsoup4 (for examples)

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## License

MIT License

## Related Projects

- [vocab-extractor](https://github.com/nhatnamduong688/vocab-extractor) - Extract vocabulary from text files

## Author

Created with ❤️ for efficient vocabulary learning

---

**Happy Learning! 🎓**

