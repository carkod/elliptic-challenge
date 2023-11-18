# Elliptic coding challenge

In either Javascript, Typescript or Python, write a script which takes a crypto address hash as an argument (currency of your choosing), and outputs a CSV containing at least the balance of the address, along with any other metadata you can find. Feel free to use any publically available resources to achieve this.

## How to run it

Assuming that you already have Python 3 installed (most OS maybe except Windows) have it installed by default.

1. Starting from the project folder, create an environment with the dependency

`python -m venv /path/to/new/virtual/environment`

2. Activate environment

`source ./venv/bin/activate `

3. Install dependencies

`pip install -r requirements.txt`

4. Run the program

`python -m main.py <address>` replace `<address>` with an ethereum address

e.g. `python -m main.py 0x55d398326f99059ff775485246999027b3197955`
If successfull, you'll get `Data written to ethereum.csv`

5. Find the `etheurum.csv` in the project folder.

## Considerations
Given the timeframe of one hour, I didn't create anything more sophisticated. The API offers a lot more data than just the balance.
With the foundation created in this project, we can easily extend the functionality by adding additional endpoints, if we want to
explore more Ethereum data. I also wrote some examples of interfaces that I would add to the program for two main reasons: maintainability
and reference.

Additionally, if we were to explore blockchains other than Ethereum, I'd start by exploring available data and maybe thereafter, create a `class` with the different services, and the functions of `write_to_csv` and data requests would reside in that class. This ensures modularity and will make creating new csv's a breeze.

On the other hand, if we want data that no API offers, we can also scrape websites. With Python, I'd use BeautifulSoup and create
functions to filter out the HTML.

I'd stick mostly to Restful API endpoints or some other programming interface such as GraphQL as they provide the most reliable data structure, with semantic versioning. This would make the code much easier to maintain. Scraping HTML makes code very brittle. I've done similar things with
our [Discourse python module](https://github.com/canonical/canonicalwebteam.discourse), you can see [my PRs too](https://github.com/canonical/canonicalwebteam.discourse/pulls?q=is%3Apr+author%3Acarkod+), so I speak from experience.
