// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "yz" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable1 = vscode.commands.registerCommand('yz.helloWorldFile', async function () {
		// Create a file in the current folder with the content 'Hello World'
		const folder = vscode.workspace.workspaceFolders[0].uri.fsPath;
		const path = require('path');
		const fs = require('fs');
		const filePath = path.join(folder, 'hello_world.txt');
		await fs.promises.writeFile(filePath, 'Hello World');
	});

	context.subscriptions.push(disposable1);

	let disposable2 = vscode.commands.registerCommand('yz.helloWorldMessageBox', function () {
		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World from yz!');
	});

	context.subscriptions.push(disposable2);
}

// This method is called when your extension is deactivated
function deactivate() {}

module.exports = {
	activate,
	deactivate
}
