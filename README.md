# Glyphs Color Labels

A lightweight floating color label palette for Glyphs 3.

[中文说明](./颜色标签安装说明.md)

## Preview

![Glyphs Color Labels preview](./颜色标签管理窗口.gif)

## Download

Download `Color Label Manager.py` from this repository.

You only need this single script file to use Glyphs Color Labels.

## Features

- Floating color label palette
- Quickly apply Glyphs color labels
- Batch apply labels to selected glyphs
- Hold `Option` to apply labels to selected layers
- Clear color labels with the `×` button
- Simple script-based workflow, no plugin installation required

## Installation

1. Open Glyphs.

2. Choose:

   `Script ➜ Open Scripts Folder ➜ Reveal Glyphs Folder`

3. Place `Color Label Manager.py` inside:

   `Glyphs Folder ➜ Scripts`

4. Restart Glyphs.

5. Open Glyphs again and choose:

   `Script ➜ Color Label Manager`

## Usage

1. Select one or more glyphs or layers in Glyphs.
2. Run `Script ➜ Color Label Manager`.
3. Click a color dot to apply that color label.
4. Click `×` to remove the color label.
5. Hold `Option` while clicking a color to apply the label to selected layers instead of glyphs.

## Behavior

By default, the script applies the selected color label to the selected glyphs.

When multiple glyphs are selected, the selected color label is applied to all of them.

When holding `Option`, the script applies the color label to selected layers instead of glyphs.

## Compatibility

- Glyphs 3
- macOS
- Glyphs Python environment with `vanilla`

## Troubleshooting

### The script does not appear in the Script menu

Make sure `Color Label Manager.py` is placed directly inside the Glyphs `Scripts` folder, then restart Glyphs.

### Clicking a color does nothing

Make sure a font is open and at least one glyph or layer is selected.

### How do I remove a color label?

Click the `×` button in the floating window.

### The window is already open

Running the script again closes the previous floating window and opens a fresh one.

## Notes

This is a Glyphs script, not a Glyphs plugin.

It does not modify glyph outlines, create new color label definitions, or change font data other than the selected glyph or layer color labels.

## License

MIT License
