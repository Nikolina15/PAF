# Napišite funkciju koja kao ulazne parametre prima (x, y) koordinate za dvije točke. Neka ta funkcija na
# ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. Pozovite tu funkciju u svom programu

def jednadžba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        x = x1
        print(f"Jenadžba pravca je x = {x1}")
    elif y1 == y2:
        y = y1
        print(f"Jednadzba pravca je y = {y1}")
    else: 
        k = round((y2-y1)/(x2-x1))
        l = round(y1-(k*x1))
        print(f"Jednadžba pravac je y = {k}x + {l}")
        return k, l
    
jednadžba_pravca(2,4,5,7)