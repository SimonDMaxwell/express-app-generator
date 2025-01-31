import os
import subprocess
import tkinter
from datetime import date
from tkinter import filedialog


# Main function
def main():
    app_name = "Express API Generator (EAGR) - Simon Maxwell"
    app_version = "v1.2.2"

    author = input("Hello, Author, what is your desired name?")
    name = input("What will this project be named?")
    print("[!] Where should this project be stored? [Hit enter to select location]")
    tkinter.Tk().withdraw()
    gen_directory = filedialog.askdirectory()
    project_dir: str = os.path.normpath(os.path.join(gen_directory, name))
    folders: list[str] = [ "api", "api/v1", "api/v1/middlewares", "api/v1/controllers", "lib", "lib/db", "lib/db/models", ]
    files: list[str] = [ ".env.example", "package.json", ".gitignore" ,"app.js", "api/v1/hub.js", "api/v1/controllers/controller1.js", "lib/json.helper.js", "lib/email.helper.js", "lib/db/db.js", "lib/db/models/model1.js" ]
    os.mkdir(project_dir)

    # Create folders
    for folder in folders:
        depth_1_folder: str = os.path.normpath(os.path.join(project_dir, folder))
        os.mkdir(depth_1_folder)

    # Create files
    for file in files:
        if file == "lib/db/models/model1.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(
                'const db = require("../db.js")\n'
                '\n'
                'let modelSchema = new db.Schema({\n'
                '   modelName: { type: String, required: true }\n'
                '})\n'
                '\n'
                'module.exports = db.model("models", modelSchema)'
            )
            f.close()
            continue
        if file == "lib/email.helper.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(
                'var nodemailer = require(\'nodemailer\')\n'
                'const JSONResponse = require(\'./json.helper\')\n'
                'require("dotenv").config()\n'
                '\n'
                'class Emailer {\n'
                '	transporter = nodemailer.createTransport({\n'
                '		service: \'gmail\',\n'
                '		auth: {\n'
                '			user: process.env.user,\n'
                '			pass: process.env.password,\n'
                '		},\n'
                '	})\n'
                '\n'
                '	constructor() {}\n'
                '	/**\n'
                '	 * Sends an email to the intended recipient.\n'
                '	 * @param {*} to - The recipient or recipient array for the email\n'
                '	 * @param {*} sub - The subject of the email\n'
                '	 * @param {*} body - The body of the email\n'
                '	 */\n'
                '	sendMail(to, sub, body) {\n'
                '		let mailOptions = {\n'
                '			to: to,\n'
                '			from: process.env.user,\n'
                '			subject: sub,\n'
                '			text: body,\n'
                '		}\n'
                '		this.transporter.sendMail(mailOptions, function (error, info) {\n'
                '			if (error) {\n'
                '				console.error(error)\n'
                '			} else {\n'
                '				console.log(\'Email sent: \' + info.response)\n'
                '			}\n'
                '		})\n'
                '	}\n'
                '}\n'
                '\n'
                'module.exports = new Emailer()'
            )
            f.close()
            continue
        if file == "lib/json.helper.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(
                'class JSONResponse {\n'
                '   static success(res, status = 200, message = "success", data = null) {\n'
                '      res.status(status).json({\n'
                '         status: status,\n'
                '         message,\n'
                '         data,\n'
                '      });\n'
                '   }\n'
                '\n'
                '   static error(res, status = 500, message = "error", error = new Error(message)) {\n'
                '      res.status(status).json({\n'
                '         status: status,\n'
                '         message,\n'
                '         error,\n'
                '      });\n'
                '   }\n'
                '}\n'
                '\n'
                'module.exports = { JSONResponse };'
            )
            f.close()
            continue
        if file == "api/v1/controllers/controller1.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(
                'const model1 = require("../../../lib//db/models/model1.js")'
                '\n'
                'class controller1 {\n'
                '   static func1(req, res) {\n'
                '       new model1(req.body).save()\n'
                '       console.log("This is a snippet example.")\n'
                '   }\n'
                '}\n'
                'module.exports = controller1'
            )
            f.close()
            continue
        if file == "api/v1/hub.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(
                'const controller1 = require("./controllers/controller1.js")\n'
                'const router = require("express").Router()\n'
                '\n'
                'router.post("/model1", controller1.func1)\n'
                '\n'
                'module.exports = router'
            );
            f.close()
            continue
        if file == ".env.example":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write(f'NAME={name}\n'
                    'PORT=8080\n'
                    'DBHOST=mongodb://localhost:27017\n'
                    f'SESSION_SECRET=eagr_{date.today().year}{date.today().month}{date.today().day}\n')
            f.close()
            continue
        if file == ".gitignore":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write('# Logs\n'
                    'logs\n'
                    '*.log\n'
                    'npm-debug.log*\n'
                    'yarn-debug.log*\n'
                    'yarn-error.log*\n'
                    'lerna-debug.log*\n'
                    '\n'
                    '# Diagnostic reports (https://nodejs.org/api/report.html)\n'
                    'report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json\n'
                    '\n'
                    '# Runtime data\n'
                    'pids\n'
                    '*.pid\n'
                    '*.seed\n'
                    '*.pid.lock\n'
                    '\n'
                    '# Directory for instrumented libs generated by jscoverage/JSCover\n'
                    'lib-cov\n'
                    '\n'
                    '# Coverage directory used by tools like istanbul\n'
                    'coverage\n'
                    '*.lcov\n'
                    '\n'
                    '# nyc test coverage\n'
                    '.nyc_output\n'
                    '\n'
                    '# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)\n'
                    '.grunt\n'
                    '\n'
                    '# Bower dependency directory (https://bower.io/)\n'
                    'bower_components\n'
                    '\n'
                    '# node-waf configuration\n'
                    '.lock-wscript\n'
                    '\n'
                    '# Compiled binary addons (https://nodejs.org/api/addons.html)\n'
                    'build/Release\n'
                    '\n'
                    '# Dependency directories\n'
                    'node_modules/\n'
                    'jspm_packages/\n'
                    '\n'
                    '# TypeScript v1 declaration files\n'
                    'typings/\n'
                    '\n'
                    '# TypeScript cache\n'
                    '*.tsbuildinfo\n'
                    '\n'
                    '# Optional npm cache directory\n'
                    '.npm\n'
                    '\n'
                    '# Optional eslint cache\n'
                    '.eslintcache\n'
                    '\n'
                    '# Microbundle cache\n'
                    '.rpt2_cache/\n'
                    '.rts2_cache_cjs/\n'
                    '.rts2_cache_es/\n'
                    '.rts2_cache_umd/\n'
                    '\n'
                    '# Optional REPL history\n'
                    '.node_repl_history\n'
                    '\n'
                    '# Output of \'npm pack\'\n'
                    '*.tgz\n'
                    '\n'
                    '# Yarn Integrity file\n'
                    '.yarn-integrity\n'
                    '\n'
                    '# dotenv environment variables file\n'
                    '.env\n'
                    '.env.test\n'
                    '\n'
                    '# parcel-bundler cache (https://parceljs.org/)\n'
                    '.cache\n'
                    '\n'
                    '# Next.js build output\n'
                    '.next\n'
                    '\n'
                    '# Nuxt.js build / generate output\n'
                    '.nuxt\n'
                    'dist\n'
                    '\n'
                    '# Gatsby files\n'
                    '.cache/\n'
                    '# Comment in the public line in if your project uses Gatsby and *not* Next.js\n'
                    '# https://nextjs.org/blog/next-9-1#public-directory-support\n'
                    '# public\n'
                    '\n'
                    '# vuepress build output\n'
                    '.vuepress/dist\n'
                    '\n'
                    '# Serverless directories\n'
                    '.serverless/\n'
                    '\n'
                    '# FuseBox cache\n'
                    '.fusebox/\n'
                    '\n'
                    '# DynamoDB Local files\n'
                    '.dynamodb/\n'
                    '\n'
                    '# TernJS port file\n'
                    '.tern-port\n'
                    '# Environment\n'
                    '.env\n')
            f.close()
            continue
        if file == "package.json":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write('{\n'
                    f'	"name": "{name.lower()}",\n'
                    '	"version": "1.0.1",\n'
                    '	"description": "A standard Express REST API.",\n'
                    '	"main": "app.js",\n'
                    '	"scripts": {\n'
                    '		"start": "node app.js"\n'
                    '       "test": "nodemon app.js"\n'
                    '	},\n'
                    '	"keywords": [],\n'
                    f'	"author": "{author}",\n'
                    '	"license": "ISC",\n'
                    '	"type": "commonjs",\n'
                    '	"dependencies": {\n'
                    '		"cors": "^2.8.5",\n'
                    '		"dotenv": "^16.0.0",\n'
                    '		"express": "^4.18.1",\n'
                    '		"express-session": "^1.17.3",\n'
                    '		"mongoose": "^6.4.6"\n'
                    '	},\n'
                    '	"devDependencies": {\n'
                    '		"concurrently": "^7.2.1",\n'
                    '		"nodemon": "^2.0.16"\n'
                    '	},\n'
                    '	"engines": {\n'
                    '		"node": "^16.13.2",\n'
                    '		"npm": "^8.5.0"\n'
                    '	}\n'
                    '}\n')
            f.close()
            continue
        if file == "app.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write('require(\'dotenv\').config()\n'
                    'const express = require(\'express\')\n'
                    'const session = require(\'express-session\')\n'
                    'const cors = require(\'cors\')\n'
                    'const app = express()\n'
                    'const API_V1 = require(\'./api/v1/hub.js\')'
                    '\n'
                    'const PORT = process.env.PORT || 8080\n'
                    'const APP_NAME = process.env.NAME || \'Express API\'\n'
                    '\n'
                    '// Middlewares\n'
                    'app.use(express.json())\n'
                    'app.use(express.urlencoded({ extended: true }))\n'
                    'app.use(cors([\'*\']))\n'
                    'app.use(\n'
                    '	session({\n'
                    '		secret: process.env.SESSION_SECRET || \'secret8080\',\n'
                    '		resave: false,\n'
                    '		saveUninitialized: false,\n'
                    '		cookie: {\n'
                    '			maxAge: 1000 * 60 * 60 * 24, // day in milliseconds\n'
                    '		},\n'
                    '	})\n'
                    ')\n'
                    '// Establish API\n'
                    'app.get("", (req, res) => {\n'
                    '   res.json({name: process.env.NAME, versions: ["v1"]})\n'
                    '})\n'
                    'app.use("/api/v1", API_V1)\n'
                    '\n'
                    '// Start express app\n'
                    'const _app = app.listen(PORT, require(\'os\').hostname(), () => {\n'
                    '	console.log(`\\n\\t${APP_NAME} listening on http://${_app.address().address}:${_app.address().port}\\n`)\n'
                    '})\n')
            f.close()
            continue
        if file == "lib/db/db.js":
            f = open(os.path.normpath(os.path.join(project_dir, file)), "x")
            f.write('const mongoose = require(\'mongoose\')\n'
                    '\n'
                    'console.log(\'Establishing for database connection...\')\n'
                    'mongoose.connect(process.env.DBHOST, (err) => {\n'
                    '   if (err) {\n'
                    '       console.log(`MongoDB failed to connect @ ${process.env.DBHOST}`)\n'
                    '       console.error(err)\n'
                    '       exit(-1)\n'
                    '   } else {\n'
                    '       console.log("MongoDB succesfully connected...")\n'
                    '   }\n'
                    '})\n'
                    '\n'
                    'module.exports = mongoose'
                    '\n')
            f.close()
            continue

    # Generation completed
    os.system("npm i --save nodemailer")
    completed(os.path.normpath(project_dir))


def banner():
    print('\n'
          '███████ ██   ██ ██████  ██████  ███████ ███████ ███████   ██ █         ██████  ███████ ███    ██ \n'
          '██       ██ ██  ██   ██ ██   ██ ██      ██      ██           ██ █     ██       ██      ████   ██ \n'
          '█████     ███   ██████  ██████  █████   ███████ ███████         ██ █  ██   ███ █████   ██ ██  ██ \n'
          '██       ██ ██  ██      ██   ██ ██           ██      ██      ██ █     ██    ██ ██      ██  ██ ██ \n'
          '███████ ██   ██ ██      ██   ██ ███████ ███████ ███████   ██ █         ██████  ███████ ██   ████ \n'
          '\n')


def completed(generated_app_dir: str):
    # Change generated directory to absolute path if it is in the script's directory
    if "\\" not in generated_app_dir:
        generated_app_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), generated_app_dir))

    print()
    print("*******************************************")
    print("[!] Express App Generated")
    print(f"[!] Directory - {generated_app_dir}")
    print("*******************************************")
    print()

    # Open project directory after app is generated. Windows Only
    # explorer_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
    # subprocess.run([explorer_path, generated_app_dir])

    # Open project directory in VSCode if installed
    cmd_path = os.path.join(os.getenv("WINDIR"), os.path.normpath("/Windows/System32"), "cmd.exe")
    subprocess.run([cmd_path, f"cmd.exe /C cd {generated_app_dir} && code ."])


# Script entry point
if __name__ == "__main__":

    # print(cmd_path)
    try:
        banner()
        main()
    except KeyboardInterrupt:
        print("\033[93m\n\nUnexpected Exit\n\033[0m")
        exit(0)
