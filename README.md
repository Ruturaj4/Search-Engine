# Search-Engine

#### 1. Document processing and indexing.

You will be provided with a zip file that contains 91 HTML documents collected from Wikipedia.

- [X] Pre-process the documents by removing all HTML tags and convert everything into lower case.
- [X] Implement a stop list and a stemmer to pre-process the documents (for the stop list and stemmer, you are allowed to use third-party open source code).
- [X] Build an inverted index (including dictionary and posting lists) for the documents. Please make sure to keep all the frequency information.

#### 2. Vector Space model.

The goal is to provide a TF-IDF-based ranking for the documents.

- [X] Since you have already collected frequency information in step 1, please further compute IDF for each term.
- [X] For each document, calculate the length of the corresponding document vector.
- [X] For each incoming query, pre-process the query with the stop list and stemmer. Identify candidate documents that contain at least one query term.
- [X] Meanwhile, compute the length of the query vector.
- [X] Finally, compute the TF-IDF similarity score between the query and each candidate document (there is no need to construct the complete document vector, or loop through all dimensions in the vector space).
- [X] Sort the documents by the score.

#### 3. Niche crawler.

- [X] Identify a domain of interest (e.g., Wikipedia, NFL, etc.). Ideally, the size of the domain should be manageable, and the link structure is not too complicated to follow.
The crawler should contain at least three components:
- [X] (1) a multi-threaded spider that fetches and parses webpages,
- [X] (2) the URL frontier which stores to-be-crawled URLs; and
- [X] (3) the URL repository that stores crawled URLs.
Please be polite to the site. Please collect a few hundreds to a few thousands of pages.

#### 4. Web interface.
- [X] Feed the collected documents to the search engine that you implemented in step 2.

- [X] Implement a Web-based interface to take user queries and return answers (document names, snapshot with search term(s) highlighted, and URL) to the user. You only need to provide a reasonable (not so fancy) interface, you can use WYSIWYG editors to generate HTML. Keep this version of your search engine, since it will be compared with two future versions.

#### 5. Add term proximity into your scoring mechanism.

- [X] Define your own score that reflects the proximity of search terms in each document.

- [X] Define your own algorithm to integrate term proximity score with the tf-idf score from step 2.

#### 6. Add one of the following to your search engine:

- [ ] Search personalization: use cookies to track users. Record each search and each click-through. For a new query, add a small component of the "search history" as query expansion.
- [ ] Relevance feedback. For each query, allow the user to identify a set of "positive" and "negative" results. Use user feedback to update the query and return new (refined) results to the user.

#### 7. Please evaluate and compare the performance of the original search engine (step 4), and the new versions (step 5 and 6).
