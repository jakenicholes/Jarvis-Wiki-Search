#Name:   wikipedia_oop.py
#Author: Jake Nicholes
#Date:   2/18/2026

import wikipedia

class WikipediaApp:

    def get_wikipedia(self, search_term):
        try:
            self._summary = wikipedia.summary(search_term, sentences=3)
            return self._summary
        except:
            return "Try something else."
        
def main():
    wikipedia_app = WikipediaApp()

    #Menu Loop
    while True:
        search = input("Enter your search: ")
        answer = wikipedia_app.get_wikipedia(search)
        print(answer)

        menu_choice = input("Search again? (y/n): ")
        if menu_choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()