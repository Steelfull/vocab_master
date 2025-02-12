# exercises/generators.py

class ExerciseGenerator:
    def __init__(self, user):
        self.user = user
        self.words = self._load_words()
    
    def _load_words(self):
        return GermanWord.objects.filter(
            user=self.user,
            metadata__isnull=False
        ).exclude(
            Q(metadata__declinations={}) | 
            Q(metadata__conjugations={})
        )

    def generate(self, difficulty=1):
        raise NotImplementedError

class DeclensionGenerator(ExerciseGenerator):
    PATTERNS = {
        1: {'cases': ['nominativ'], 'numbers': ['singular']},
        2: {'cases': ['nominativ', 'akkusativ'], 'numbers': ['singular']},
        3: {'cases': ['dativ', 'genitiv'], 'numbers': ['plural']}
    }
    
    def __init__(self, user, pattern_level=1):
        super().__init__(user)
        self.pattern = self.PATTERNS[pattern_level]
    
    def _generate_prompt(self, word):
        case = random.choice(self.pattern['cases'])
        number = random.choice(self.pattern['numbers'])
        
        return {
            'type': 'declension',
            'template': f"Ergänze die {number} Form im {case.capitalize()}:",
            'target': f"{word.metadata['declinations'][case][number]}",
            'hints': {
                'gender': word.gender,
                'article_table': word.metadata['article_declension']
            }
        }

class ConjugationGenerator(ExerciseGenerator):
    # Ähnliche Struktur für Verben