from ll import Node, LinkedList


songs = [
    {'song_name': 'Gasolina',               'artist': 'Daddy Yankee',       'album': 'Barrio Fino'},
    {'song_name': 'Con Calma',              'artist': 'Daddy Yankee',       'album': 'Con Calma'},
    {'song_name': 'Despacito',              'artist': 'Luis Fonsi',         'album': 'Vida'},
    {'song_name': 'Dura',                   'artist': 'Daddy Yankee',       'album': 'Dura'},
    {'song_name': 'MIA',                    'artist': 'Bad Bunny',          'album': 'X 100PRE'},
    {'song_name': 'Safaera',                'artist': 'Bad Bunny',          'album': 'YHLQMDLG'},
    {'song_name': 'Dakiti',                 'artist': 'Bad Bunny',          'album': 'El Último Tour Del Mundo'},
    {'song_name': 'Tití Me Preguntó',       'artist': 'Bad Bunny',          'album': 'Un Verano Sin Ti'},
    {'song_name': 'Moscow Mule',            'artist': 'Bad Bunny',          'album': 'Un Verano Sin Ti'},
    {'song_name': 'Efecto',                 'artist': 'Bad Bunny',          'album': 'Un Verano Sin Ti'},
    {'song_name': 'Me Porto Bonito',        'artist': 'Bad Bunny',          'album': 'Un Verano Sin Ti'},
    {'song_name': 'Hawái',                  'artist': 'Maluma',             'album': 'Papi Juancho'},
    {'song_name': 'Felices los 4',          'artist': 'Maluma',             'album': 'F.A.M.E.'},
    {'song_name': 'Ginza',                  'artist': 'J Balvin',           'album': 'Energia'},
    {'song_name': 'Mi Gente',               'artist': 'J Balvin',           'album': 'Vibras'},
    {'song_name': 'X',                      'artist': 'Nicky Jam',          'album': 'Fénix'},
    {'song_name': 'El Amante',              'artist': 'Nicky Jam',          'album': 'Fénix'},
    {'song_name': 'Boom',                   'artist': 'Red One',            'album': 'Boom'},
    {'song_name': 'Trumpets',               'artist': 'Jason Derulo',       'album': 'Everything Is 4'},
    {'song_name': 'Sensación del Bloque',   'artist': 'Daddy Yankee',       'album': 'Barrio Fino'},
    {'song_name': 'Pepas',                  'artist': 'Farruko',            'album': 'La 167'},
    {'song_name': 'Callaíta',               'artist': 'Bad Bunny',          'album': 'Callaíta'},
    {'song_name': 'Mala Mía',               'artist': 'Maluma',             'album': 'F.A.M.E.'},
    {'song_name': 'Loco Contigo',           'artist': 'DJ Snake',           'album': 'Carte Blanche'},
    {'song_name': 'Con Altura',             'artist': 'ROSALÍA',            'album': 'Con Altura'},
    {'song_name': 'Bohemian Rhapsody',      'artist': 'Queen',              'album': 'A Night at the Opera'},
    {'song_name': 'Back in Black',          'artist': 'AC/DC',              'album': 'Back in Black'},
    {'song_name': 'Stairway to Heaven',     'artist': 'Led Zeppelin',       'album': 'Led Zeppelin IV'},
    {'song_name': 'Hotel California',       'artist': 'Eagles',             'album': 'Hotel California'},
    {'song_name': 'Smells Like Teen Spirit','artist': 'Nirvana',            'album': 'Nevermind'},
    {'song_name': 'Sweet Child O Mine',     'artist': "Guns N' Roses",      'album': 'Appetite for Destruction'},
    {'song_name': 'November Rain',          'artist': "Guns N' Roses",      'album': 'Use Your Illusion I'},
    {'song_name': 'Enter Sandman',          'artist': 'Metallica',          'album': 'Metallica'},
    {'song_name': 'Master of Puppets',      'artist': 'Metallica',          'album': 'Master of Puppets'},
    {'song_name': 'Nothing Else Matters',   'artist': 'Metallica',          'album': 'Metallica'},
    {'song_name': 'Paranoid',               'artist': 'Black Sabbath',      'album': 'Paranoid'},
    {'song_name': 'Iron Man',               'artist': 'Black Sabbath',      'album': 'Paranoid'},
    {'song_name': 'Highway to Hell',        'artist': 'AC/DC',              'album': 'Highway to Hell'},
    {'song_name': 'Thunderstruck',          'artist': 'AC/DC',              'album': 'The Razors Edge'},
    {'song_name': 'Under the Bridge',       'artist': 'RHCP',               'album': 'Blood Sugar Sex Magik'},
    {'song_name': 'Californication',        'artist': 'RHCP',               'album': 'Californication'},
    {'song_name': 'Black Hole Sun',         'artist': 'Soundgarden',        'album': 'Superunknown'},
    {'song_name': 'Jeremy',                 'artist': 'Pearl Jam',          'album': 'Ten'},
    {'song_name': 'Even Flow',              'artist': 'Pearl Jam',          'album': 'Ten'},
    {'song_name': 'Heart-Shaped Box',       'artist': 'Nirvana',            'album': 'In Utero'},
    {'song_name': 'Come as You Are',        'artist': 'Nirvana',            'album': 'Nevermind'},
    {'song_name': 'Welcome to the Jungle',  'artist': "Guns N' Roses",      'album': 'Appetite for Destruction'},
    {'song_name': 'Paint It Black',         'artist': 'The Rolling Stones', 'album': 'Aftermath'},
    {'song_name': 'Sympathy for the Devil', 'artist': 'The Rolling Stones', 'album': 'Beggars Banquet'},
    {'song_name': 'Should I Stay or Go',    'artist': 'The Clash',          'album': 'Combat Rock'},
]


playlist = LinkedList()

for i, song in enumerate(songs):
    node = Node(i + 1)
    node.metadata['song_name'] = song['song_name']
    node.metadata['artist'] = song['artist']
    node.metadata['album'] = song['album']
    playlist.insert_at_end(node)


print(f'Total de canciones: {len(playlist)}\n')

for node in playlist:
    print(
        f'{node.data:>2}. {node.metadata["song_name"]:<30}'
        f'  {node.metadata["artist"]:<25}'
        f'  {node.metadata["album"]}'
    )