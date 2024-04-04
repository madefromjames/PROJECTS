# Wiki Encyclopedia
This project is a Wiki Encyclopedia implemented using Django, allowing users to create, edit, search, and view encyclopedia entries stored in Markdown format.

## Getting Started
The Wiki Encyclopedia project has been hosted using Render Web App. You can access the site by following this link: [Wiki Encyclopedia](https://projects-0qr3.onrender.com/). Please be patient it may take a few seconds to load.

## Understanding
In this project, a Django app called wiki is provided, containing the following components:

### URLs Configuration
- The URL configuration for the app is defined in `encyclopedia/urls.py`. Currently, there is a default route associated with the `views.index` function.
### Utility Functions
- `encyclopedia/util.py` contains utility functions for interacting with encyclopedia entries. These include:
  - `list_entries`: Returns a list of the names of all encyclopedia entries.
  - `save_entry`: Saves a new encyclopedia entry given its title and Markdown content.
  - `get_entry`: Retrieves an encyclopedia entry by its title.
### Encyclopedia Entries
Each encyclopedia entry is stored as a Markdown file inside the `entries/` directory. Sample entries are provided, and additional entries can be added.
### Views
`encyclopedia/views.py` contains view functions for rendering various pages:
- `index`: Renders the index page with a list of all entries.
Additional views are already implemented to fulfill project specifications.
### Templates
Templates for rendering HTML pages are located in `encyclopedia/templates/`. The `index.html` template displays a list of all entries.

## Specifications
### Entry Page
- Visiting `/wiki/TITLE` where `TITLE` is the title of an encyclopedia entry will render a page displaying the contents of the encyclopedia entry with the given title.
- If the entry does not exist, the user will be presented with an error page.

### Index Page
- `index.html` allows users to click on entry names to be taken directly to that entry page.

### Search
- Allow users to search for encyclopedia entries using a search box in the sidebar.
Matching entries will redirect users to the respective entry page.
- If no matches are found, users will be shown a search results page with matching entries displayed.

### New Page
- Allow users to create new encyclopedia entries.
Users will be able to enter a title and Markdown content for the new entry.
- Duplicate title submissions displays an error message.

### Edit Page
- Users are able to edit existing entry content.
Provide a link on each entry page to edit the entry's Markdown content.
- The textarea will be pre-populated with existing content.

## Random Page
- A feature to redirect users to a random encyclopedia entry.

## Markdown to HTML Conversion
Converting Markdown content to HTML using `safe` filter in `entry.html` allows user to view the page in human-friendly language instead of pure `HTML` syntax.