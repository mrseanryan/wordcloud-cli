import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

import util_file

def _generate(text, mask):
    # Create and generate a word cloud image:
    wordcloud = WordCloud(
                            scale = 4,
                            collocations = False,  # do not repeat words
                            mask = mask,
                            background_color = 'white',
                            contour_width = 2,
                            contour_color = 'white'
                            # colormap = 'Paired'
                          ).generate(text)
    
    filename = f"{name_of_word_column}_masked" if mask is not None else name_of_word_column
    path_to_output_image = f"temp/{filename}.png"
    print(f"Saving image to {path_to_output_image}")
    wordcloud.to_file(path_to_output_image)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def generate_wordcloud_from_df(df, name_of_word_column, mask_image_path):
    texts = df[name_of_word_column]

    texts_filtered = []
    for text in texts:
        if text:
            text = str(text).strip()
            if text:
                texts_filtered.append(text)

    text = " ".join(texts_filtered)

    mask = np.array(Image.open(mask_image_path))

    _generate(text, None)
    _generate(text, mask)

def print_usage():
    print(f"USAGE: {sys.argv[0]} <path to data file> <name or index of word column>")

# git-filter-repo can pick up arguments passed here.
# - we restrict which arguments user can use, as otherwise this tool will behave in unexpected ways.
def validate_usage():
    len_args = len(sys.argv)
    if len_args == 4:
        path_to_data = sys.argv[1]
        name_of_word_column = sys.argv[2]
        mask_image_path = sys.argv[3]
        return (path_to_data, name_of_word_column, mask_image_path)
    else:
        print_usage()
        sys.exit(44)

def read_text_file_to_df(path_to_data, name_of_word_column):
    all_words = []
    lines = util_file.read_lines_from_file(path_to_data)
    for line in lines:
        words = line.split()
        all_words += words
    all_words_dict = dict()
    all_words_dict[name_of_word_column] = all_words
    return pd.DataFrame(all_words_dict)

def load_data(path_to_data, name_of_word_column):
    if path_to_data.endswith('.parquet'):
        return pd.read_parquet(path_to_data)
    if path_to_data.endswith('.csv'):
        return pd.read_csv(path_to_data)
    if path_to_data.endswith('.txt'):
        return read_text_file_to_df(path_to_data, name_of_word_column)

if __name__ == '__main__':
    (path_to_data, name_of_word_column, mask_image_path) = validate_usage()

    print(f"Reading from {path_to_data}")
    df = load_data(path_to_data, name_of_word_column)
    generate_wordcloud_from_df(df, name_of_word_column, mask_image_path)
