# VSCode Setup for R Markdown Files

## Overview
This guide shows how to work with R Markdown (.Rmd) files in VSCode while maintaining the R language functionality.

## Required Extensions

1. **R Extension for Visual Studio Code** (by REditorSupport)
   - Extension ID: `REditorSupport.r`
   - Provides R language support, syntax highlighting, and code execution

2. **R Markdown All in One** (by TianyiShi)
   - Extension ID: `TianyiShi.rmarkdown`
   - Provides RMarkdown preview and execution support

3. **R LSP Client** (optional but recommended)
   - Extension ID: `REditorSupport.r-lsp`
   - Provides language server protocol support for better IntelliSense

## Installation Steps

1. Open VSCode
2. Press `Ctrl+Shift+X` (or `Cmd+Shift+X` on Mac) to open Extensions
3. Search for and install the extensions listed above

## Configuration

### 1. R Path Configuration
Add to your VSCode settings.json (`Ctrl+,` then click the {} icon):
```json
{
    "r.rterm.windows": "C:\\Program Files\\R\\R-4.x.x\\bin\\x64\\R.exe",
    "r.rterm.linux": "/usr/bin/R",
    "r.rterm.mac": "/usr/local/bin/R",
    "r.bracketedPaste": true,
    "r.sessionWatcher": true
}
```

### 2. R Markdown Settings
```json
{
    "r.rmarkdown.enableCodeLens": true,
    "r.rmarkdown.chunkBackgroundColor": "#1e1e1e20",
    "r.plot.useHttpgd": true
}
```

## Working with RMD Files

### Running Code Chunks
- **Run current chunk**: `Ctrl+Shift+Enter` (or `Cmd+Shift+Enter` on Mac)
- **Run current line**: `Ctrl+Enter` (or `Cmd+Enter` on Mac)
- **Run all chunks above**: `Ctrl+Alt+Shift+P`

### Knitting/Rendering Documents
1. Open Command Palette: `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
2. Type "R Markdown: Knit" or "R Markdown: Render"
3. Select the output format (PDF, HTML, Word)

Alternative method using terminal:
```bash
# In VSCode terminal
Rscript -e "rmarkdown::render('search-costs-results.Rmd')"
```

### Preview
- **Preview HTML**: Use the built-in Markdown preview (`Ctrl+Shift+V`)
- **Preview PDF**: After knitting, VSCode will automatically open the PDF

## Keyboard Shortcuts

Add these to your keybindings.json for faster workflow:
```json
[
    {
        "key": "ctrl+shift+k",
        "command": "r.knitRmd",
        "when": "editorTextFocus && editorLangId == 'rmd'"
    },
    {
        "key": "ctrl+alt+i",
        "command": "r.rmarkdown.insertChunk",
        "when": "editorTextFocus && editorLangId == 'rmd'"
    }
]
```

## Interactive R Terminal

1. Open integrated terminal: `Ctrl+`` (backtick)
2. Start R session by typing `R`
3. Use the R terminal interactively alongside your RMD file

## Useful Features

### 1. Code Lens
Shows inline buttons above code chunks to run them directly.

### 2. Variable Explorer
View R workspace variables:
- Command Palette → "R: Show Workspace"

### 3. Plot Viewer
Plots appear in a separate pane when using httpgd backend.

### 4. Git Integration
VSCode's built-in Git support works seamlessly with R projects.

## Tips for Your Workflow

1. **Split Editor**: Right-click on the RMD file tab → "Split Right" to view code and PDF side by side
2. **Auto-save**: Enable auto-save (`File → Auto Save`) to automatically save before knitting
3. **Tasks**: Create a VSCode task to automate knitting:

Create `.vscode/tasks.json`:
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Knit RMD to PDF",
            "type": "shell",
            "command": "Rscript",
            "args": [
                "-e",
                "rmarkdown::render('${file}', output_format='pdf_document')"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        }
    ]
}
```

Then use `Ctrl+Shift+B` to knit the current file.

## Troubleshooting

1. **R not found**: Make sure R is in your system PATH
2. **Packages missing**: Install required R packages:
   ```r
   install.packages(c("rmarkdown", "knitr", "tinytex"))
   tinytex::install_tinytex()  # For PDF output
   ```
3. **PDF compilation errors**: Check LaTeX installation with `tinytex::is_tinytex()`

## Benefits Over RStudio

- Integrated terminal for Git operations
- Better multi-file editing
- Extensive extension ecosystem
- Customizable keybindings
- Lighter resource usage
- Better version control integration