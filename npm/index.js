const { spawn } = require('child_process')
const path = require('path')

const python = process.platform === 'win32' ? 'python' : 'python3'
const script = path.join(__dirname, 'python', 'splc.py')

const args = process.argv.slice(2)
spawn(python, [script, ...args], { stdio: 'inherit' })
