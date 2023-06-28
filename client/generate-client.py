#!/usr/bin/env python3
from pathlib import Path

import os

def writeToFile(path, content):
  file = open(path, "w")
  file.write(content)
  file.close()
  
def writeToBeginningOfFile(path, content):
  read_file = open(path, "r")
  file_content = read_file.read()
  read_file.close()
  file = open(path, "w")
  file_content = content + file_content 
  file.seek(0)
  file.write(file_content)
  file.close()

# ----------------------------------------- Set according to directory  ----------------------------
# ----------------------------------------- 🛑🛑 run code from directory 🛑🛑  ----------------------------
current_path = (Path.cwd())
print(Path.cwd())
src_path = "src"
component_folder = "components"
page_folder = "pages"
style_folder = "styles"
public_folder = "public"
images_folder = "images"

path_src = os.path.join(current_path, src_path)
component_directory = os.path.join(path_src, component_folder)
page_directory = os.path.join(path_src, page_folder)
styles_directory = os.path.join(path_src, style_folder)
public_directory = os.path.join(path_src, public_folder)
images_directory = os.path.join(path_src, images_folder)

component_path = './src/components'
page_path = './src/pages/'
style_path = "./src/styles/"
public_path = "./public/"
images_path = "./public/images"

def create_paths():
  # ----------------------------------------- Create component directory ----------------------------
  if os.path.exists(component_path):
    print("⭐ Component path exists.")
  else:
    print("✅ Components directory created.")
    os.mkdir(component_path)
    
  # ----------------------------------------- Create pages directory ----------------------------
  if os.path.exists(page_path):
    print("⭐ Page path exists.")
  else:
    print("✅ Page directory created.")
    os.mkdir(page_path)
    
  # ----------------------------------------- Create styles directory ----------------------------
  if os.path.exists(style_path):
    print("⭐ Style path exists.")
  else:
    print("✅ Style directory created.")
    os.mkdir(style_path)
    
  # ----------------------------------------- Create public directory ----------------------------
  if os.path.exists(public_path):
    print("⭐ Public path exists.")
  else:
    print("✅ Public directory created.")
    os.mkdir(public_path)
    
  # ----------------------------------------- Create public directory ----------------------------
  if os.path.exists(images_path):
    print("⭐ Images path exists.")
  else:
    print("✅ Images directory created.")
    os.mkdir(images_path)


def create_pages(page_name):
  # ----------------------------------------- page path and content ----------------------------
  page_style_path = f"{styles_directory}/{page_name}.scss"
  styles_content = f".{page_name}" + "{}"
  page_file_path = f"{page_directory}/{page_name}.js"
  page_content = 'import React from "react"; const '+page_name+' = () => { return ( <div className="'+page_name+'"> <div className="container"> <h1 className="content-header">'+page_name+'</h1> </div> </div> ); }; export default '+page_name+';'
  styles_import = f'import "../styles/{page_name}.scss";'
  
  # ----------------------------------------- Create page if it doesn't exist ------------------
  if os.path.exists(page_file_path):
    print("⭐ This page already exists")
  else:
    print("✅ Page js file created.")
    writeToFile(page_file_path, page_content)
    writeToFile(page_style_path, styles_content)
    print("✅ Scss added to page.")
    writeToBeginningOfFile(f"{current_path}/App.js", styles_import)
    
    
def create_components(folder_name, component_name):
  # ----------------------------------------- Create styles for component ----------------------
  component_style_path = f"{styles_directory}/{component_name}.scss"
  component_style_folder_path = f"{component_directory}/{folder_name}/{component_name}.scss"
  styles_content = f".{component_name}" + "{}"
  styles_import = f'import "../styles/{component_name}.scss";'
  
  # ----------------------------------------- component path and content ----------------------------
  component_file_path = f"{component_directory}/{component_name}.js"
  component_file_folder_path = f"{component_directory}/{folder_name}/{component_name}.js"
  component_content = 'import React from "react"; const '+component_name+' = () => { return ( <div className="'+component_name+'"> <div className="container"> <h1 className="content-header">'+component_name+'</h1> </div> </div> ); }; export default '+component_name+';'
  
  # ----------------------------------------- create component if it doesn't exist ----------------------------
  if os.path.exists(f"{component_directory}/{folder_name}/"):
    print("⭐ The component folder already exists")
  else:
    print("✅ Component folder created.")
    os.mkdir(f"{component_directory}/{folder_name}/")
  
  # ----------------------------------------- put it in page folder if necessary ----------------------------
  if(folder_name != ""):    
    if os.path.exists(component_file_folder_path):
      print("⭐ This component already exists")
    else:
      print("✅ Component js file created.")
      writeToFile(component_file_folder_path, component_content)
      writeToFile(component_style_folder_path, styles_content)
      writeToBeginningOfFile(f"{current_path}/App.js", styles_import)
  else:
    if os.path.exists(component_file_path):
      print("⭐ This component already exists")
    else:
      print("✅ Component js file created.")
      writeToFile(component_file_path, component_content)
      writeToFile(component_style_path, styles_content)
      writeToBeginningOfFile(f"{current_path}/App.js", styles_import)

def create_git_ignore():
  git_ignore_file_path = f"{current_path}/.gitignore"
  git_ignore_content = ".env\n./firebase.js\n/node_modules\n/.pnp\n.pnp.js\n/coverage\n/.next/\n/out/\n/build\n.DS_Store\n*.pem\nnpm-debug.log*\nyarn-debug.log*\nyarn-error.log*\n.pnpm-debug.log*\n.env*.local\n.vercel\n*.tsbuildinfo\nnext-env.d.ts"
  if os.path.exists(f"{current_path}/.gitignore"):
    print("⭐ The git ignore already exists")
  else:
    print("✅ Git ignore file created.")
    writeToFile(git_ignore_file_path, git_ignore_content)
    
def create_package_json():
  package_json_path = f"{current_path}/package.json"
  package_json_content = '{ "name": "client", "version": "0.1.0", "private": true, "dependencies": { "@testing-library/jest-dom": "^5.16.5", "@testing-library/react": "^13.4.0", "@testing-library/user-event": "^13.5.0", "bootstrap": "^5.3.0", "react": "^18.2.0", "react-bootstrap": "^2.8.0", "react-dom": "^18.2.0", "react-router-dom": "^6.14.0", "react-scripts": "5.0.1", "web-vitals": "^2.1.4" }, "scripts": { "start": "react-scripts start", "build": "react-scripts build", "test": "react-scripts test", "eject": "react-scripts eject" }, "eslintConfig": { "extends": [ "react-app", "react-app/jest" ] }, "browserslist": { "production": [ ">0.2%", "not dead", "not op_mini all" ], "development": [ "last 1 chrome version", "last 1 firefox version", "last 1 safari version" ] } } '
  if os.path.exists(f"{current_path}/package.json"):
    print("⭐ The package.json already exists")
  else:
    print("✅ package.json file created.")
    writeToFile(package_json_path, package_json_content)
    
def create_index_page():
  index_style_path = f"{style_path}/index.scss"
  index_style_content = "body { margin: 0; box-sizing: border-box; } "
  index_page_path = f"{page_path}/index.js"
  index_page_content = 'import React from "react"; import ReactDOM from "react-dom/client"; import "./styles/index.css"; import App from "./App"; const root = ReactDOM.createRoot(document.getElementById("root")); root.render( <React.StrictMode> <App /> </React.StrictMode> ); '
  if os.path.exists(f"{page_path}/index.js"):
    print("⭐ The index.js already exists")
  else:
    print("✅ index.js file created.")
    writeToFile(index_page_path, index_page_content)
    print("✅ index.scss file created.")
    writeToFile(index_style_path, index_style_content)
    
def create_app_page():
  app_style_path = f"{style_path}/globals.scss"
  app_style_content = ".Home{}"
  app_page_path = f"{current_path}/App.js"
  app_page_content = 'import React from "react"; import Home from "./pages/Home"; import { BrowserRouter, Routes, Route } from "react-router-dom"; import "bootstrap/dist/css/bootstrap.min.css"; const App = () => { return ( <div className="App"> <BrowserRouter> <Routes> <Route path="/"> <Route index element={<Home />} /> <Route path="Home" element={<Home />} /> </Route> </Routes> </BrowserRouter> </div> ); }; export default App; '
  if os.path.exists(f"{current_path}/App.js"):
    print("⭐ The app.js already exists")
  else:
    print("✅ app.js file created.")
    writeToFile(app_page_path, app_page_content)
    print("✅ app.scss file created.")
    writeToFile(app_style_path, app_style_content)
    
    
    
create_paths()
create_git_ignore()
create_package_json()
create_index_page()
create_app_page()

create_page = input("Would you like to create a page? [Y or N]")
while(create_page.lower() == "y"):
  page_name = input("What would you like to call the page? [String]")
  create_pages(page_name)
  create_page = input("Would you like to create a page? [Y or N]")

create_component = input("Would you like to create a component? [Y or N]")
while(create_component.lower() == "y"):
  component_name = input("What would you like to call the component? [String}")
  create_components("", component_name)
  create_component = input("Would you like to create a component? [Y or N]")

