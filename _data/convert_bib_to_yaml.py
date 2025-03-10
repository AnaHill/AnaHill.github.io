import bibtexparser
import yaml
import latexcodec  # Handles special characters like ä, ö, å

# Settings ###########################
# Define your name for highlighting (must match UTF-8 converted format)
HIGHLIGHTED_AUTHOR = "Mäki, Antti-Juhana"

# Define the name of the BibTeX file to be converted
publication_list_file_name = "publications.bib"
# publication_list_file_name = "publications_short.bib"

# Define the name of the output (YAML) file to be saved
save_file_name = "_data/publications.yml"
# save_file_name = "_data/publications_test.yml"
# ###################################

def convert_latex_text(latex_text):
    """Convert LaTeX-encoded characters to proper UTF-8"""
    return latex_text.encode("utf-8").decode("latex").replace("{", "").replace("}", "")

# Load BibTeX file
with open(publication_list_file_name, "r", encoding="utf-8") as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

# Convert BibTeX entries to YAML format
publications = []
for entry in bib_database.entries:
    title = convert_latex_text(entry.get("title", ""))
    journal = convert_latex_text(entry.get("journal", ""))
    authors_raw = convert_latex_text(entry.get("author", ""))

    # Convert "Author1 and Author2 and Author3" → ["Author1", "Author2", "Author3"]
    authors_list = [author.strip() for author in authors_raw.split(" and ")]

    # Extract category and split it into a list
    category_raw = convert_latex_text(entry.get("category", "regular"))
    categories = [cat.strip() for cat in category_raw.split(",")]

    publications.append({
        "article_id": entry.get("ID", ""),  # Add citekey here
        "title": title,
        "authors": authors_list,  
        "highlighted_author": HIGHLIGHTED_AUTHOR,  
        "journal": journal,
        "year": entry.get("year", ""),
        "doi": entry.get("doi", ""),
        "category": categories  # Now properly stored as a list
    })

# Save to YAML
with open(save_file_name, "w", encoding="utf-8") as yaml_file:
    yaml.dump(publications, yaml_file, default_flow_style=False, allow_unicode=True)

print(f"Conversion complete! Check {save_file_name} for the output.")
