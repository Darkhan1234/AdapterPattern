# Singleton for Cinema
class CinemaSingleton:
    _instance = None

    def __new__(cls, cinema_name, text_generator):
        if cls._instance is None:
            cls._instance = super(CinemaSingleton, cls).__new__(cls)
            cls._instance.init(cinema_name, text_generator)
        return cls._instance

    def init(self, cinema_name, text_generator):
        self.cinema_name = cinema_name
        self.text_generator = text_generator

    def display_movie_info(self, movie):
        cinema_text_generator = CinemaTextGeneration(self.text_generator)
        cinema_text = cinema_text_generator.generate_cinema_text(movie.title)

        print(f"{self.cinema_name} Info:")
        print(f"Movie Title: {movie.title}")
        print(f"Movie Description: {movie.description}")
        print(cinema_text)

    def get_user_feedback(self):
        feedback = input("Please provide your feedback on the generated cinema text: ")
        # Here you can have logic to store the feedback in a database or file
        print("Thank you for your feedback!")

# Decorator for movie description
class MovieDescriptionDecorator(CinemaTextGeneration):
    def __init__(self, text_generator, movie):
        self.text_generator = text_generator
        self.movie = movie

    def generate_cinema_text(self, title):
        description = f"Welcome to our cinema! Now showing: {title}. Movie Description: {self.movie.description}"
        generated_text = self.text_generator.generate_text(description)
        return generated_text

# Main Application
if __name__ == "__main__":
    gpt_service = GPTService()
    adapter = GPTServiceAdapter(gpt_service)

    movie1 = Movie("Avengers: Endgame", "The epic conclusion to the Infinity Saga.")
    movie2 = Movie("The Shawshank Redemption", "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.")

    cinema1 = CinemaSingleton("Cineplex", adapter)
    cinema2 = CinemaSingleton("Classic Cinema", adapter)

    decorated_movie1 = MovieDescriptionDecorator(adapter, movie1)
    decorated_movie2 = MovieDescriptionDecorator(adapter, movie2)

    cinema1.display_movie_info(decorated_movie1)
    cinema2.display_movie_info(decorated_movie2)

    cinema1.get_user_feedback()

