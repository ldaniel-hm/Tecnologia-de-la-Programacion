from TDA_Bag.BagList import Bag
from collections import defaultdict

class AnagramFinder:
    """
    Encuentra anagramas en una lista de palabras.
    """

    def __init__(self):
        """
        Inicializador de la clase AnagramFinder
        """
        self.anagrams = defaultdict(Bag)  # Un diccionario que mapea palabras ordenadas a un bag de palabras

    def add_word(self, word) -> None:
        """
        Añade una palabra a la lista de anagramas.
        :param word: La palabra a añadir a la lista de anagramas
        """
        sorted_word = ''.join(sorted(word.lower()))  # Ordena la palabra y la convierte a minúsculas
        self.anagrams[sorted_word].add(word)  # Añade la palabra a la lista de anagramas

    def find_anagrams(self) -> list:
        """
        Retorna los anagramas que tienen más de una palabra
        :return: Una lista de bags de anagramas
        """
        return [anagram_group for anagram_group in self.anagrams.values() if len(anagram_group) > 1]


def main():
    # Lista de palabras de ejemplo
    words = ["ramo", "amor", "roma", "perro", "pera", "arco", "carro", "mar", "ram", "casa", "saca",
             "tarde", "dater", "paso", "sopa", "roca", "caro", "rima", "mira"]

    # Instancia del AnagramFinder
    anagram_finder = AnagramFinder()

    # Agregar cada palabra a la instancia del AnagramFinder
    for word in words:
        anagram_finder.add_word(word)

    # Encontrar anagramas
    anagrams = anagram_finder.find_anagrams()

    # Imprimir grupos de anagramas
    for group in anagrams:
        print("Anagramas:", group)


if __name__ == "__main__":
    main()