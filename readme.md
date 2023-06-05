Install Node (using nvm) https://github.com/nvm-sh/nvm

```sh
# Install nvm (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Once that's installed, run this to actually install node
nvm install node

# Activate node
nvm use node
```

---

For development

```sh
# Start the frontend dev server
cd frontend
yarn start
# or
npm run start

# In another shell, start the backend dev server
cd backend
MODE=DEV python app.py
```

---

For production

```sh
# Build the frontend files
bash ./scripts/build.sh

# Start the flask server
cd backend
python app.py
```

---

Material UI - https://mui.com/material-ui/getting-started/overview/
