# TODOs

### Setup + Learning
- [X] Set up environment: https://realpython.com/python-virtual-environments-a-primer/
    - python -m pip freeze > requirements.txt
- [X] Decide on frameworks/libs to use and concepts to cover
    - Spotipy: https://spotipy.readthedocs.io/en/2.24.0/
    - Typer: https://realpython.com/python-typer-cli/
    - Async programming: https://realpython.com/python-async-features/
    - The Factory method pattern: https://realpython.com/factory-method-python/#the-problems-with-complex-conditional-code
    - Threading: https://realpython.com/intro-to-python-threading/
    - Anonymous functions: https://realpython.com/python-lambda/
    - ...Other packages that may/may not be relevant but could be nice to get experience in: https://realpython.com/python-packages/
- [X] Get dependecies installed and pinned
    - [X] Typer
    - [X] Spotipy
    - [X] Pytest
    - [X] Ruff
- [X] Spotipy basic setup:
    - [X] Register app here https://developer.spotify.com/
    - [X] Add a valid redirect URI to https://developer.spotify.com/dashboard/7fba64219bb94ad1a24a5d78ae2b21ae/settings
    - [X] Set up client ID and client secret: https://youtu.be/kaBVN8uP358?feature=shared
    - [X] Set up an entry-point script to read/output some stuff from Spotify
- [X] Set up environment variables using the python-dotenv package
- [X] Spotipy authorization setup:
    - [X] Follow this tutorial to get authorization flow set up correctly using client ID, client secret, and redirect URI: https://www.youtube.com/watch?v=tmt5SdvTqUI&list=PLqgOPibB_QnzzcaOFYmY2cQjs35y0is9N&index=1
- [ ] Look up the API web interface and mess around with printing some different GET/POST request data 
- [ ] Threading: https://realpython.com/intro-to-python-threading/
- [ ] Async programming: https://realpython.com/python-async-features/
- [ ] The Factory method pattern: https://realpython.com/factory-method-python/#the-problems-with-complex-conditional-code
- [ ] Typer: https://realpython.com/python-typer-cli/
- ...Other packages that may/may not be relevant but could be nice to get experience in: https://realpython.com/python-packages/


### Design + Implementation
- [ ] Identify core problem(s) - what are things you wish Spotify could do that it can't
- [ ] Identify technical decisions (add to this list below)
    - [ ] Draw/list out high-level design (see Rover project for reminder)
    - [ ] Models
    - [ ] Functions, methods
    - [ ] Project organization - files, folders etc
    - [ ] OAuth
    - [ ] How to make deploy/distrubute
- [ ] Make technical decisions from above
- [ ] Implement components of algorithn (from high-level design created in earlier step)
- [ ] Run linter
- [ ] Add logging
- [ ] Evaluate whether to use a client credential flow instead, which offers higher rate limiting: https://spotipy.readthedocs.io/en/2.24.0/#getting-started


### Testing + Debugging
- [ ] Debugging refresher with pdb: https://realpython.com/python-debugging-pdb/
- [ ] Write test cases
- [ ] Implement test cases: https://realpython.com/pytest-python-testing/
- [ ] Stuff to address/fix before deployment
    - [ ] Get packages working from the CL, not just in VS Code
- [ ] Refactoring/optimizing
    - [ ] Split up functions and classes into separate files
    - [ ] Optimize - can it be faster? See if map()/reduce()/filter() can be utilized anywhere
    - [ ] DRY code
    - [ ] No magic strings


### Deployment