import argparse
import zxcvbn
import itertools
import re
from datetime import datetime

def analyze_password(password):
    """Analyze password strength using zxcvbn."""
    result = zxcvbn.zxcvbn(password)
    score = result['score']  # 0 (weak) to 4 (strong)
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    suggestions = result['feedback']['suggestions']
    return score, crack_time, suggestions

def generate_leetspeak(word):
    """Generate leetspeak variations of a word."""
    leet_dict = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['$', '5']}
    variations = [word]
    for char, replacements in leet_dict.items():
        if char in word.lower():
            new_variations = []
            for var in variations:
                for repl in replacements:
                    new_variations.append(var.replace(char, repl).replace(char.upper(), repl))
            variations.extend(new_variations)
    return list(set(variations))

def generate_wordlist(inputs, min_year=2000, max_year=2025):
    """Generate a custom wordlist from user inputs with variations."""
    wordlist = set()
    
    # Add raw inputs and combinations
    for r in range(1, len(inputs) + 1):
        for combo in itertools.combinations(inputs, r):
            word = ''.join(combo)
            wordlist.add(word)
            wordlist.add(word.lower())
            wordlist.add(word.upper())
            wordlist.add(word.capitalize())
    
    # Add leetspeak variations
    for word in list(wordlist):
        wordlist.update(generate_leetspeak(word))
    
    # Add year variations (e.g., name2023)
    for word in list(wordlist):
        for year in range(min_year, max_year + 1):
            wordlist.add(f"{word}{year}")
            wordlist.add(f"{year}{word}")
    
    return sorted(wordlist)

def save_wordlist(wordlist, filename):
    """Save wordlist to a .txt file."""
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print(f"Wordlist saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Password Strength Analyzer and Wordlist Generator")
    parser.add_argument('--password', type=str, help="Password to analyze")
    parser.add_argument('--inputs', type=str, nargs='+', help="Inputs for wordlist (e.g., name pet date)")
    parser.add_argument('--output', type=str, default="wordlist.txt", help="Output file for wordlist")
    args = parser.parse_args()

    # Password strength analysis
    if args.password:
        score, crack_time, suggestions = analyze_password(args.password)
        print(f"\nPassword Analysis:")
        print(f"Strength Score: {score}/4")
        print(f"Estimated Crack Time: {crack_time}")
        if suggestions:
            print("Suggestions:")
            for suggestion in suggestions:
                print(f"- {suggestion}")
    
    # Wordlist generation
    if args.inputs:
        print("\nGenerating wordlist from inputs:", args.inputs)
        wordlist = generate_wordlist(args.inputs)
        print(f"Generated {len(wordlist)} words.")
        save_wordlist(wordlist, args.output)

if __name__ == "__main__":
    main()