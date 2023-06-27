def count_words_in_text(string, extra_actions = None):
    """
    string: book contents with lines separated by newlines '\\n'.
    encoding: encoding string to open file
    extra_actions: iterable with callables that will operate in the text. Must receive 2 arguments,
        a line number and the line content, and return the modified line.
    """
    if extra_actions == None:
        extra_actions = []

    word_counts = {}

    for i, line in enumerate(string.split('\n')):
        line = line.strip()
        line = line.strip(',.!?-;:')
        
        if len(line) == 0:
            continue

        for extra_action in extra_actions:
            line = extra_action(i, line)
        
        line = line.lower()
        words = line.split()
    
        for word in words:
            if word not in word_counts.keys():
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    
    return word_counts

def remove_filler_words(word_counts):
    filler_words = [
    'o', 'a', 'de', 'e', 'que', 'do', 'da', 'os', 'para', 'as', 'seu', 'como', 'na',
    'dos', 'se', 'em', 'com', 'no', 'ao', 'sua', 'á', 'com', 'é', 'elle', 'das', 'quando',
    'onde', 'seus', 'ella', 'uma', 'um', 'mais', 'teu', 'mas', 'já', 'te', 'por',
    'nos', 'tua', 'tu', 'foi', 'porque', 'entre', 'sobre', 'ainda', 'depois', 'só',
    'lhe', 'assim', 'era', 'até', 'aos', 'tem', 'não'
    ]
    for word in filler_words:
        if word in word_counts.keys():
            word_counts.pop(word)
    return word_counts

def analyze_iracema_word_count(path, encoding='utf8'):
    """
    path: path to .txt file
    encoding: encoding string to open file

    Returns:
    word list sorted by count
    total number of words
    total number of interesting words
    """
    
    lines = open(path, 'r', encoding=encoding).readlines()
    lines = lines[452:3800]
    text = '\n'.join(lines)
    
    word_counts = count_words_in_text(text, extra_actions = [lambda i, line: '' if line.isupper() else line])
    total_words = sum(word_counts.values())
    
    word_counts = remove_filler_words(word_counts)
    total_interesting_words = sum(word_counts.values())
    
    word_list = sorted(list(word_counts.items()), key = lambda x: x[1], reverse=True)

    return word_list, total_words, total_interesting_words
    