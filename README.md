#twitter_search

Queries the twitter search API for a keyword and saves the results in TSV format.

## Author

* Author: Ryan McGreal
* Email: [ryan@quandyfactory.com](mailto:ryan@quandyfactory.com)
* Repository: [http://github.com/quandyfactory/twitter_search](http://github.com/quandyfactory/twitter_search)

## Licence

Released under the GNU General Public Licence, Version 2: [http://www.gnu.org/licenses/old-licenses/gpl-2.0.html](http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)

## This Version

* Version: 0.3
* Release Date: 2013-04-08
  
## Requirements

* Python 2.5+, no third party libraries

## Usage

From the command line, execute the script with a keyword argument, e.g.

    you@home$ python twitter_search.py \#HamOnt

The script will query the twitter search API recursively (using the `next_page` value from the response) and save the results in a TSV file in the format: `twitter_search_keyword_yyyy-mm-dd_hh_mm_ss.tsv`.

Note that if you are searching for a hashtag, on some systems you will need to escape the [octothorpe](http://en.wiktionary.org/wiki/octothorpe) (the # symbol) to have the `sys` module recognize it as an argument.

## Version History

### Version 0.3

* Release Date: 2013-04-08
* Changes:
    * Fixed bug to ensure content downloads and is saved properly.

### Version 0.2

* Release Date: 2013-02-22
* Changes:
    * Script was refusing to save to file with unicode decode error. I took a dirty shortcut and added a function that strips out non-unicode characters. Obviously this still needs fixing.

### Version 0.1

* Release Date: 2012-09-07
* Changes:
    * First commit.
