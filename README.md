# mkdocs-to-pdf

mkdocs-to-pdf

```yml
jobs:
  tests_e2e:
    name: Run end-to-end tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - name: Install dependencies
        run: npm ci
      - name: Install playwright browsers
        run: npx playwright install --with-deps
      - name: Run tests
        run: npx playwright test
```

```bash
pip install playwright
playwright install
```
