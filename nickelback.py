# Example set

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}

Die_Nickelback = {(a, b) for a, b in songs if a not in ('Nickelback')}

print(songs, 'songs')
print(Die_Nickelback, 'Die_Nickelback')
