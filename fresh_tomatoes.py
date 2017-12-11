import webbrowser
import os
import codecs


html_content = {
    'main_page_head': '',
    'main_page_content': '',
    'movie_tile_content': '',
    'main_page_footer': ''
}
# Reads html files into a dictionary of unicode content for rendering
for page_section in html_content.keys():
    html_file = codecs.open('templates/' + page_section +
                            '.html', 'r', encoding='utf-8')
    html_content[page_section] = html_file.read()


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Append the tile for the movie with its content filled in
        content += html_content['movie_tile_content'].format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.trailer_youtube_id,
            movie_awards=movie.awards,
            movie_director=movie.director,
            movie_genre=movie.genre,
            movie_boxoffice=movie.boxoffice,
            movie_rated=movie.rated,
            movie_rating=movie.rating,
            movie_runtime=movie.runtime,
            movie_year=movie.year,
            movie_votes=movie.votes,
            movie_actors=movie.actors
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = codecs.open('fresh_tomatoes.html',
                              'w', encoding='utf-8')

    # Replace the placeholder for the movie tiles with
    # the actual dynamically generated content
    rendered_content = html_content[
                        'main_page_content'].format(
                            movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(html_content['main_page_head'] +
                      rendered_content + html_content['main_page_footer'])
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)
