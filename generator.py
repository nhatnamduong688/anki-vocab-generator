# -*- coding: utf-8 -*-
"""
Anki Vocab Generator
Convert CSV vocabulary files to Anki decks (.apkg)
"""
import genanki
import csv
import random
import argparse
import sys
from pathlib import Path


def create_card_model():
    """Create a custom Anki card model with beautiful styling"""
    model_id = random.randrange(1 << 30, 1 << 31)
    
    model = genanki.Model(
        model_id,
        'Vocabulary Phrase Model',
        fields=[
            {'name': 'Phrase'},
            {'name': 'Type'},
            {'name': 'Structure'},
            {'name': 'Definition'},
            {'name': 'Lemma'},
        ],
        templates=[
            {
                'name': 'Phrase Card',
                'qfmt': '''
                    <div class="card">
                        <div class="phrase">{{Phrase}}</div>
                        <div class="meta">
                            <span class="type">{{Type}}</span>
                            <span class="structure">{{Structure}}</span>
                        </div>
                    </div>
                ''',
                'afmt': '''
                    {{FrontSide}}
                    <hr id="answer">
                    <div class="definition">
                        <div class="label">Definition:</div>
                        <div class="content">{{Definition}}</div>
                    </div>
                    {{#Lemma}}
                    <div class="lemma">
                        <div class="label">Lemma:</div>
                        <div class="content">{{Lemma}}</div>
                    </div>
                    {{/Lemma}}
                ''',
            },
        ],
        css='''
            .card {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                text-align: center;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px;
                margin: 10px;
            }
            
            .phrase {
                font-size: 32px;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 15px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            }
            
            .meta {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 10px;
            }
            
            .type {
                background: rgba(255,255,255,0.2);
                color: #ffffff;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: 600;
                text-transform: uppercase;
            }
            
            .structure {
                background: rgba(255,255,255,0.15);
                color: #ffffff;
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 500;
            }
            
            hr#answer {
                border: none;
                height: 2px;
                background: linear-gradient(to right, transparent, #667eea, transparent);
                margin: 25px 0;
            }
            
            .definition, .lemma {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin: 15px 0;
                text-align: left;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            
            .label {
                font-size: 14px;
                font-weight: 700;
                color: #667eea;
                text-transform: uppercase;
                margin-bottom: 8px;
                letter-spacing: 0.5px;
            }
            
            .content {
                font-size: 18px;
                color: #2c3e50;
                line-height: 1.6;
            }
            
            .lemma .content {
                font-style: italic;
                color: #7f8c8d;
                font-size: 16px;
            }
        '''
    )
    
    return model


def parse_csv_to_notes(csv_file, model):
    """Parse CSV file and create Anki notes"""
    notes = []
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                # Get fields with fallback for empty values
                phrase = row.get('text', '').strip()
                phrase_type = row.get('type', '').strip()
                structure = row.get('pos/structure', '').strip()
                definition = row.get('definition', 'No definition available').strip()
                lemma = row.get('lemma', '').strip()
                
                # Skip if no phrase
                if not phrase:
                    continue
                
                # Create note
                note = genanki.Note(
                    model=model,
                    fields=[phrase, phrase_type, structure, definition, lemma],
                    tags=[phrase_type] if phrase_type else []
                )
                
                notes.append(note)
        
        return notes
    
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Error parsing CSV: {e}")
        sys.exit(1)


def create_anki_deck(csv_file, output_file, deck_name="English Vocabulary Phrases"):
    """Main function to create Anki deck from CSV"""
    
    print(f"📚 Creating Anki deck from: {csv_file}")
    
    # Create model
    model = create_card_model()
    print("✅ Card model created")
    
    # Create deck
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(deck_id, deck_name)
    print(f"✅ Deck '{deck_name}' created")
    
    # Parse CSV and add notes
    notes = parse_csv_to_notes(csv_file, model)
    
    for note in notes:
        deck.add_note(note)
    
    print(f"✅ Added {len(notes)} cards to deck")
    
    # Create package and write to file
    package = genanki.Package(deck)
    package.write_to_file(output_file)
    
    print(f"🎉 Successfully created: {output_file}")
    print(f"📊 Total cards: {len(notes)}")
    print(f"\n💡 Import this file into Anki: File → Import → {output_file}")
    
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Convert vocabulary CSV to Anki deck',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python generator.py input.csv
  python generator.py input.csv -o my_deck.apkg
  python generator.py input.csv -n "My Custom Deck Name"
        '''
    )
    
    parser.add_argument('input', help='Input CSV file (from vocab-extractor)')
    parser.add_argument('-o', '--output', default='vocab_deck.apkg',
                        help='Output Anki deck file (default: vocab_deck.apkg)')
    parser.add_argument('-n', '--name', default='English Vocabulary Phrases',
                        help='Deck name (default: English Vocabulary Phrases)')
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not Path(args.input).exists():
        print(f"❌ Error: Input file '{args.input}' not found!")
        sys.exit(1)
    
    # Create deck
    create_anki_deck(args.input, args.output, args.name)


if __name__ == "__main__":
    main()

