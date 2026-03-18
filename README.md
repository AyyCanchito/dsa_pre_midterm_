# dsa_pre_midterm_



# Playlist con Lista Doblemente Encadenada

Implementación de una playlist de música usando una lista doblemente encadenada en Python. Permite navegar entre 50 canciones (25 de reggaeton y 25 de rock) desde la terminal.

---

## Requisitos

- Python 3.10 o superior

---

## Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

---

## Correr el programa

El proyecto contiene tres archivos principales:

| Archivo                  | Descripción                                              |
|--------------------------|----------------------------------------------------------|
| `linked_list.py`         | Definición de las clases `Node` y `LinkedList`           |
| `demo_playlist.py`       | Demo que carga las 50 canciones e imprime la lista       |
| `playlist_interface.py`  | Interfaz interactiva en consola para navegar la playlist |

Para iniciar la interfaz interactiva ejecutar:

```bash
python3 playlist_interface.py
```

> `playlist_interface.py` importa directamente desde `linked_list.py`, por lo que ambos archivos deben estar en el mismo directorio.

---

## Controles de navegación

Una vez iniciado el programa, se mostrará la primera canción reproduciéndose. Los controles disponibles son:

| Tecla | Acción                    |
|-------|---------------------------|
| `N`   | Avanzar a la siguiente canción   |
| `P`   | Regresar a la canción anterior   |
| `Q`   | Salir de la playlist             |

### Notas

- Al estar en la **primera canción**, la opción `P` no estará disponible.
- Al estar en la **última canción**, la opción `N` no estará disponible.
- La lista **no es circular**: el inicio y el final son límites estrictos.

---

## Ejemplo de uso

```
=============================================
  ♪  Reproduciendo [1/50]
=============================================
  Canción : Gasolina
  Artista : Daddy Yankee
  Álbum   : Barrio Fino
=============================================

  [N] Siguiente canción
  [Q] Salir

  Opción: N

=============================================
  ♪  Reproduciendo [2/50]
=============================================
  Canción : Con Calma
  Artista : Daddy Yankee
  Álbum   : Con Calma
=============================================

  [P] Canción anterior
  [N] Siguiente canción
  [Q] Salir

  Opción: Q

  Cerrando playlist. Hasta luego.
```