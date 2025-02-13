# Liste aller Artikel-Deklinationen
ARTICLE_DATA = [
    # Bestimmte Artikel (der/die/das)
    {"article_type": "definite", "case": "nominativ", "gender": "Maskulinum", "singular": "der", "plural": "die"},
    {"article_type": "definite", "case": "akkusativ", "gender": "Maskulinum", "singular": "den", "plural": "die"},
    {"article_type": "definite", "case": "dativ", "gender": "Maskulinum", "singular": "dem", "plural": "den"},
    {"article_type": "definite", "case": "genitiv", "gender": "Maskulinum", "singular": "des", "plural": "der"},
    {"article_type": "definite", "case": "nominativ", "gender": "Femininum", "singular": "die", "plural": "die"},
    {"article_type": "definite", "case": "akkusativ", "gender": "Femininum", "singular": "die", "plural": "die"},
    {"article_type": "definite", "case": "dativ", "gender": "Femininum", "singular": "der", "plural": "den"},
    {"article_type": "definite", "case": "genitiv", "gender": "Femininum", "singular": "der", "plural": "der"},
    {"article_type": "definite", "case": "nominativ", "gender": "Neutrum", "singular": "das", "plural": "die"},
    {"article_type": "definite", "case": "akkusativ", "gender": "Neutrum", "singular": "das", "plural": "die"},
    {"article_type": "definite", "case": "dativ", "gender": "Neutrum", "singular": "dem", "plural": "den"},
    {"article_type": "definite", "case": "genitiv", "gender": "Neutrum", "singular": "des", "plural": "der"},

    # Unbestimmte Artikel (ein/eine)
    {"article_type": "indefinite", "case": "nominativ", "gender": "Maskulinum", "singular": "ein", "plural": "keine"},
    {"article_type": "indefinite", "case": "akkusativ", "gender": "Maskulinum", "singular": "einen", "plural": "keine"},
    {"article_type": "indefinite", "case": "dativ", "gender": "Maskulinum", "singular": "einem", "plural": "keinen"},
    {"article_type": "indefinite", "case": "genitiv", "gender": "Maskulinum", "singular": "eines", "plural": "keiner"},
    {"article_type": "indefinite", "case": "nominativ", "gender": "Femininum", "singular": "eine", "plural": "keine"},
    {"article_type": "indefinite", "case": "akkusativ", "gender": "Femininum", "singular": "eine", "plural": "keine"},
    {"article_type": "indefinite", "case": "dativ", "gender": "Femininum", "singular": "einer", "plural": "keinen"},
    {"article_type": "indefinite", "case": "genitiv", "gender": "Femininum", "singular": "einer", "plural": "keiner"},
    {"article_type": "indefinite", "case": "nominativ", "gender": "Neutrum", "singular": "ein", "plural": "keine"},
    {"article_type": "indefinite", "case": "akkusativ", "gender": "Neutrum", "singular": "ein", "plural": "keine"},
    {"article_type": "indefinite", "case": "dativ", "gender": "Neutrum", "singular": "einem", "plural": "keinen"},
    {"article_type": "indefinite", "case": "genitiv", "gender": "Neutrum", "singular": "eines", "plural": "keiner"},
]

# Liste aller Konjunktionen
CONJUNCTION_DATA = [
    {"conjunction_type": "subordinating", "case_governed": "genitiv", "word": "während"},
    {"conjunction_type": "subordinating", "case_governed": "genitiv", "word": "wegen"},
    {"conjunction_type": "subordinating", "case_governed": "genitiv", "word": "trotz"},
    {"conjunction_type": "subordinating", "case_governed": "genitiv", "word": "statt"},
    {"conjunction_type": "subordinating", "case_governed": "akkusativ", "word": "ohne"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "mit"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "nach"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "bei"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "seit"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "zu"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "aus"},
    {"conjunction_type": "subordinating", "case_governed": "dativ", "word": "von"},
    {"conjunction_type": "coordinating", "case_governed": "nominativ", "word": "und"},
    {"conjunction_type": "coordinating", "case_governed": "nominativ", "word": "oder"},
    {"conjunction_type": "coordinating", "case_governed": "nominativ", "word": "aber"},
    {"conjunction_type": "coordinating", "case_governed": "nominativ", "word": "denn"},
]