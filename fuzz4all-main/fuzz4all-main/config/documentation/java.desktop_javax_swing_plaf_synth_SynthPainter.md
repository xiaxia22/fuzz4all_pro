# Class SynthPainter

**Source:** `java.desktop\javax\swing\plaf\synth\SynthPainter.html`

### Class Description

```java
public abstract class
SynthPainter

extends
Object
```

SynthPainter

is used for painting portions of

JComponent

s. At a minimum each

JComponent

has two paint methods: one for the border and one for the background. Some

JComponent

s have more than one

Region

, and as
a consequence more paint methods.

Instances of

SynthPainter

are obtained from the

SynthStyle.getPainter(javax.swing.plaf.synth.SynthContext)

method.

You typically supply a

SynthPainter

by way of Synth's

file

format. The following
example registers a painter for all

JButton

s that will
render the image

myImage.png

:

```java
<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>
```

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthPainter()

*No description found.*

---

### Method Details

#### public void paintArrowButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintArrowButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintArrowButtonForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int direction)

Paints the foreground of an arrow button. This method is responsible
for drawing a graphical representation of a direction, typically
an arrow. Arrow buttons are created by
some components, such as

JScrollBar

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- direction

- One of SwingConstants.NORTH, SwingConstants.SOUTH
SwingConstants.EAST or SwingConstants.WEST

---

#### public void paintButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintCheckBoxMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a check box menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintCheckBoxMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a check box menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintCheckBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a check box.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintCheckBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a check box.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintColorChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a color chooser.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintColorChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a color chooser.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintComboBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a combo box.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintComboBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a combo box.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintDesktopIconBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a desktop icon.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintDesktopIconBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a desktop icon.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintDesktopPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintDesktopPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintEditorPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of an editor pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintEditorPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of an editor pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintFileChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a file chooser.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintFileChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a file chooser.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintFormattedTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a formatted text field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintFormattedTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a formatted text field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintInternalFrameTitlePaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame title pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintInternalFrameTitlePaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame title pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintInternalFrameBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintInternalFrameBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintLabelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a label.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintLabelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a label.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintListBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a list.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintListBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a list.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a menu bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a menu bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a menu.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a menu.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintOptionPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of an option pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintOptionPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of an option pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPanelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a panel.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPanelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a panel.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPasswordFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a password field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPasswordFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a password field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPopupMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a popup menu.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintPopupMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a popup menu.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a progress bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a progress bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintProgressBarForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

---

#### public void paintRadioButtonMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a radio button menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintRadioButtonMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a radio button menu item.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintRadioButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a radio button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintRadioButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a radio button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintRootPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a root pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintRootPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a root pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a scrollbar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a scrollbar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintScrollBarThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

---

#### public void paintScrollBarThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

---

#### public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the track of a scrollbar. The track contains
the thumb.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the track of a scrollbar. The track contains
the thumb.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintScrollPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a scroll pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintScrollPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a scroll pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a separator.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

**Since:**
- 1.6

---

#### public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a separator.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

**Since:**
- 1.6

---

#### public void paintSeparatorForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a separator.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

---

#### public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

**Since:**
- 1.6

---

#### public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

**Since:**
- 1.6

---

#### public void paintSliderThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

---

#### public void paintSliderThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

---

#### public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the track of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a slider. This implementation invokes
the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

**Since:**
- 1.6

---

#### public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the track of a slider.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

**Since:**
- 1.6

---

#### public void paintSpinnerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a spinner.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSpinnerBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a spinner.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the divider of a split pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the divider of a split pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

**Since:**
- 1.6

---

#### public void paintSplitPaneDividerForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of the divider of a split pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

---

#### public void paintSplitPaneDragDivider​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the divider, when the user is dragging the divider, of a
split pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

---

#### public void paintSplitPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a split pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintSplitPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a split pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the area behind the tabs of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the area behind the tabs of a tabbed pane.
This implementation invokes the method of the same name without the
orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT

**Since:**
- 1.6

---

#### public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the area behind the tabs of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the area behind the tabs of a tabbed pane. This
implementation invokes the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT

**Since:**
- 1.6

---

#### public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the background of a tab of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- tabIndex

- Index of tab being painted.

---

#### public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the background of a tab of a tabbed pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- tabIndex

- Index of tab being painted.
- orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT

**Since:**
- 1.6

---

#### public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the border of a tab of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- tabIndex

- Index of tab being painted.

---

#### public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the border of a tab of a tabbed pane. This implementation invokes
the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- tabIndex

- Index of tab being painted.
- orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT

**Since:**
- 1.6

---

#### public void paintTabbedPaneContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTabbedPaneContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTableHeaderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the header of a table.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTableHeaderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the header of a table.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTableBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a table.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTableBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a table.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a text area.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a text area.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a text pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a text pane.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a text field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a text field.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToggleButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a toggle button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToggleButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a toggle button.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a tool bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a tool bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the tool bar's content area.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the tool bar's content area. This implementation
invokes the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the content area of a tool bar.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the content area of a tool bar. This implementation
invokes the method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to
- orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL

**Since:**
- 1.6

---

#### public void paintToolTipBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a tool tip.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintToolTipBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a tool tip.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTreeBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of a tree.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTreeBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a tree.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTreeCellBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the row containing a cell in a tree.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTreeCellBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of the row containing a cell in a tree.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintTreeCellFocus​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the focus indicator for a cell in a tree when it has focus.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintViewportBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the background of the viewport.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

#### public void paintViewportBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border of a viewport.

**Parameters:**
- context

- SynthContext identifying the

JComponent

and

Region

to paint to
- g

-

Graphics

to paint to
- x

- X coordinate of the area to paint to
- y

- Y coordinate of the area to paint to
- w

- Width of the area to paint to
- h

- Height of the area to paint to

---

### Additional Sections

#### Class SynthPainter

java.lang.Object

- javax.swing.plaf.synth.SynthPainter

javax.swing.plaf.synth.SynthPainter

```java
public abstract class
SynthPainter

extends
Object
```

SynthPainter

is used for painting portions of

JComponent

s. At a minimum each

JComponent

has two paint methods: one for the border and one for the background. Some

JComponent

s have more than one

Region

, and as
a consequence more paint methods.

Instances of

SynthPainter

are obtained from the

SynthStyle.getPainter(javax.swing.plaf.synth.SynthContext)

method.

You typically supply a

SynthPainter

by way of Synth's

file

format. The following
example registers a painter for all

JButton

s that will
render the image

myImage.png

:

```java
<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>
```

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

**Since:** 1.5

public abstract class

SynthPainter

extends

Object

SynthPainter

is used for painting portions of

JComponent

s. At a minimum each

JComponent

has two paint methods: one for the border and one for the background. Some

JComponent

s have more than one

Region

, and as
a consequence more paint methods.

Instances of

SynthPainter

are obtained from the

SynthStyle.getPainter(javax.swing.plaf.synth.SynthContext)

method.

You typically supply a

SynthPainter

by way of Synth's

file

format. The following
example registers a painter for all

JButton

s that will
render the image

myImage.png

:

```java
<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>
```

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

Instances of

SynthPainter

are obtained from the

SynthStyle.getPainter(javax.swing.plaf.synth.SynthContext)

method.

You typically supply a

SynthPainter

by way of Synth's

file

format. The following
example registers a painter for all

JButton

s that will
render the image

myImage.png

:

```java
<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>
```

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

You typically supply a

SynthPainter

by way of Synth's

file

format. The following
example registers a painter for all

JButton

s that will
render the image

myImage.png

:

```java
<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>
```

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

<style id="buttonStyle">
<imagePainter path="myImage.png" sourceInsets="2 2 2 2"
paintCenter="true" stretch="true"/>
<insets top="2" bottom="2" left="2" right="2"/>
</style>
<bind style="buttonStyle" type="REGION" key="button"/>

SynthPainter

is abstract in so far as it does no painting,
all the methods
are empty. While none of these methods are typed to throw an exception,
subclasses can assume that valid arguments are passed in, and if not
they can throw a

NullPointerException

or

IllegalArgumentException

in response to invalid arguments.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthPainter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

paintArrowButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an arrow button.

void

paintArrowButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an arrow button.

void

paintArrowButtonForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int direction)

Paints the foreground of an arrow button.

void

paintButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a button.

void

paintButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a button.

void

paintCheckBoxBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box.

void

paintCheckBoxBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box.

void

paintCheckBoxMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box menu item.

void

paintCheckBoxMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box menu item.

void

paintColorChooserBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a color chooser.

void

paintColorChooserBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a color chooser.

void

paintComboBoxBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a combo box.

void

paintComboBoxBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a combo box.

void

paintDesktopIconBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop icon.

void

paintDesktopIconBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a desktop icon.

void

paintDesktopPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

void

paintDesktopPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

void

paintEditorPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an editor pane.

void

paintEditorPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an editor pane.

void

paintFileChooserBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a file chooser.

void

paintFileChooserBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a file chooser.

void

paintFormattedTextFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a formatted text field.

void

paintFormattedTextFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a formatted text field.

void

paintInternalFrameBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame.

void

paintInternalFrameBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame.

void

paintInternalFrameTitlePaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame title pane.

void

paintInternalFrameTitlePaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame title pane.

void

paintLabelBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a label.

void

paintLabelBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a label.

void

paintListBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a list.

void

paintListBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a list.

void

paintMenuBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu.

void

paintMenuBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu bar.

void

paintMenuBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu bar.

void

paintMenuBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu.

void

paintMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu item.

void

paintMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu item.

void

paintOptionPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an option pane.

void

paintOptionPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an option pane.

void

paintPanelBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a panel.

void

paintPanelBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a panel.

void

paintPasswordFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a password field.

void

paintPasswordFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a password field.

void

paintPopupMenuBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a popup menu.

void

paintPopupMenuBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a popup menu.

void

paintProgressBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a progress bar.

void

paintProgressBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a progress bar.

void

paintProgressBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a progress bar.

void

paintProgressBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a progress bar.

void

paintProgressBarForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

void

paintRadioButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button.

void

paintRadioButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button.

void

paintRadioButtonMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button menu item.

void

paintRadioButtonMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button menu item.

void

paintRootPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a root pane.

void

paintRootPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a root pane.

void

paintScrollBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scrollbar.

void

paintScrollBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a scrollbar.

void

paintScrollBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scrollbar.

void

paintScrollBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a scrollbar.

void

paintScrollBarThumbBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a scrollbar.

void

paintScrollBarThumbBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a scrollbar.

void

paintScrollBarTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a scrollbar.

void

paintScrollBarTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a scrollbar.

void

paintScrollBarTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a scrollbar.

void

paintScrollBarTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a scrollbar.

void

paintScrollPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scroll pane.

void

paintScrollPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scroll pane.

void

paintSeparatorBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a separator.

void

paintSeparatorBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a separator.

void

paintSeparatorBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a separator.

void

paintSeparatorBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a separator.

void

paintSeparatorForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a separator.

void

paintSliderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a slider.

void

paintSliderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a slider.

void

paintSliderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a slider.

void

paintSliderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a slider.

void

paintSliderThumbBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a slider.

void

paintSliderThumbBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a slider.

void

paintSliderTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a slider.

void

paintSliderTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a slider.

void

paintSliderTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a slider.

void

paintSliderTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a slider.

void

paintSpinnerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a spinner.

void

paintSpinnerBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a spinner.

void

paintSplitPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a split pane.

void

paintSplitPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a split pane.

void

paintSplitPaneDividerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the divider of a split pane.

void

paintSplitPaneDividerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the divider of a split pane.

void

paintSplitPaneDividerForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of the divider of a split pane.

void

paintSplitPaneDragDivider

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the divider, when the user is dragging the divider, of a
split pane.

void

paintTabbedPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tabbed pane.

void

paintTabbedPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tabbed pane.

void

paintTabbedPaneContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

void

paintTabbedPaneContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

void

paintTabbedPaneTabAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the background of a tab of a tabbed pane.

void

paintTabbedPaneTabBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the background of a tab of a tabbed pane.

void

paintTabbedPaneTabBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the border of a tab of a tabbed pane.

void

paintTabbedPaneTabBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the border of a tab of a tabbed pane.

void

paintTableBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a table.

void

paintTableBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a table.

void

paintTableHeaderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the header of a table.

void

paintTableHeaderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the header of a table.

void

paintTextAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text area.

void

paintTextAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text area.

void

paintTextFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text field.

void

paintTextFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text field.

void

paintTextPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text pane.

void

paintTextPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text pane.

void

paintToggleButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a toggle button.

void

paintToggleButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a toggle button.

void

paintToolBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool bar.

void

paintToolBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a tool bar.

void

paintToolBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool bar.

void

paintToolBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a tool bar.

void

paintToolBarContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the tool bar's content area.

void

paintToolBarContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the tool bar's content area.

void

paintToolBarContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the content area of a tool bar.

void

paintToolBarContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the content area of a tool bar.

void

paintToolBarDragWindowBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

void

paintToolBarDragWindowBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

void

paintToolBarDragWindowBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

void

paintToolBarDragWindowBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

void

paintToolTipBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool tip.

void

paintToolTipBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool tip.

void

paintTreeBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tree.

void

paintTreeBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tree.

void

paintTreeCellBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the row containing a cell in a tree.

void

paintTreeCellBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the row containing a cell in a tree.

void

paintTreeCellFocus

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the focus indicator for a cell in a tree when it has focus.

void

paintViewportBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the viewport.

void

paintViewportBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a viewport.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SynthPainter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

paintArrowButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an arrow button.

void

paintArrowButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an arrow button.

void

paintArrowButtonForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int direction)

Paints the foreground of an arrow button.

void

paintButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a button.

void

paintButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a button.

void

paintCheckBoxBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box.

void

paintCheckBoxBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box.

void

paintCheckBoxMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box menu item.

void

paintCheckBoxMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box menu item.

void

paintColorChooserBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a color chooser.

void

paintColorChooserBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a color chooser.

void

paintComboBoxBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a combo box.

void

paintComboBoxBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a combo box.

void

paintDesktopIconBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop icon.

void

paintDesktopIconBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a desktop icon.

void

paintDesktopPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

void

paintDesktopPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

void

paintEditorPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an editor pane.

void

paintEditorPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an editor pane.

void

paintFileChooserBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a file chooser.

void

paintFileChooserBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a file chooser.

void

paintFormattedTextFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a formatted text field.

void

paintFormattedTextFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a formatted text field.

void

paintInternalFrameBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame.

void

paintInternalFrameBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame.

void

paintInternalFrameTitlePaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame title pane.

void

paintInternalFrameTitlePaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame title pane.

void

paintLabelBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a label.

void

paintLabelBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a label.

void

paintListBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a list.

void

paintListBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a list.

void

paintMenuBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu.

void

paintMenuBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu bar.

void

paintMenuBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu bar.

void

paintMenuBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu.

void

paintMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu item.

void

paintMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu item.

void

paintOptionPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an option pane.

void

paintOptionPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an option pane.

void

paintPanelBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a panel.

void

paintPanelBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a panel.

void

paintPasswordFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a password field.

void

paintPasswordFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a password field.

void

paintPopupMenuBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a popup menu.

void

paintPopupMenuBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a popup menu.

void

paintProgressBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a progress bar.

void

paintProgressBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a progress bar.

void

paintProgressBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a progress bar.

void

paintProgressBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a progress bar.

void

paintProgressBarForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

void

paintRadioButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button.

void

paintRadioButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button.

void

paintRadioButtonMenuItemBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button menu item.

void

paintRadioButtonMenuItemBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button menu item.

void

paintRootPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a root pane.

void

paintRootPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a root pane.

void

paintScrollBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scrollbar.

void

paintScrollBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a scrollbar.

void

paintScrollBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scrollbar.

void

paintScrollBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a scrollbar.

void

paintScrollBarThumbBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a scrollbar.

void

paintScrollBarThumbBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a scrollbar.

void

paintScrollBarTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a scrollbar.

void

paintScrollBarTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a scrollbar.

void

paintScrollBarTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a scrollbar.

void

paintScrollBarTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a scrollbar.

void

paintScrollPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scroll pane.

void

paintScrollPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scroll pane.

void

paintSeparatorBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a separator.

void

paintSeparatorBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a separator.

void

paintSeparatorBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a separator.

void

paintSeparatorBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a separator.

void

paintSeparatorForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a separator.

void

paintSliderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a slider.

void

paintSliderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a slider.

void

paintSliderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a slider.

void

paintSliderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a slider.

void

paintSliderThumbBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a slider.

void

paintSliderThumbBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a slider.

void

paintSliderTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a slider.

void

paintSliderTrackBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a slider.

void

paintSliderTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a slider.

void

paintSliderTrackBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a slider.

void

paintSpinnerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a spinner.

void

paintSpinnerBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a spinner.

void

paintSplitPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a split pane.

void

paintSplitPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a split pane.

void

paintSplitPaneDividerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the divider of a split pane.

void

paintSplitPaneDividerBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the divider of a split pane.

void

paintSplitPaneDividerForeground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of the divider of a split pane.

void

paintSplitPaneDragDivider

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the divider, when the user is dragging the divider, of a
split pane.

void

paintTabbedPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tabbed pane.

void

paintTabbedPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tabbed pane.

void

paintTabbedPaneContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

void

paintTabbedPaneContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

void

paintTabbedPaneTabAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the area behind the tabs of a tabbed pane.

void

paintTabbedPaneTabBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the background of a tab of a tabbed pane.

void

paintTabbedPaneTabBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the background of a tab of a tabbed pane.

void

paintTabbedPaneTabBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the border of a tab of a tabbed pane.

void

paintTabbedPaneTabBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the border of a tab of a tabbed pane.

void

paintTableBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a table.

void

paintTableBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a table.

void

paintTableHeaderBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the header of a table.

void

paintTableHeaderBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the header of a table.

void

paintTextAreaBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text area.

void

paintTextAreaBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text area.

void

paintTextFieldBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text field.

void

paintTextFieldBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text field.

void

paintTextPaneBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text pane.

void

paintTextPaneBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text pane.

void

paintToggleButtonBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a toggle button.

void

paintToggleButtonBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a toggle button.

void

paintToolBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool bar.

void

paintToolBarBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a tool bar.

void

paintToolBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool bar.

void

paintToolBarBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a tool bar.

void

paintToolBarContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the tool bar's content area.

void

paintToolBarContentBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the tool bar's content area.

void

paintToolBarContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the content area of a tool bar.

void

paintToolBarContentBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the content area of a tool bar.

void

paintToolBarDragWindowBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

void

paintToolBarDragWindowBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

void

paintToolBarDragWindowBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

void

paintToolBarDragWindowBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

void

paintToolTipBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool tip.

void

paintToolTipBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool tip.

void

paintTreeBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tree.

void

paintTreeBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tree.

void

paintTreeCellBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the row containing a cell in a tree.

void

paintTreeCellBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the row containing a cell in a tree.

void

paintTreeCellFocus

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the focus indicator for a cell in a tree when it has focus.

void

paintViewportBackground

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the viewport.

void

paintViewportBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a viewport.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Paints the background of an arrow button.

Paints the border of an arrow button.

Paints the foreground of an arrow button.

Paints the background of a button.

Paints the border of a button.

Paints the background of a check box.

Paints the border of a check box.

Paints the background of a check box menu item.

Paints the border of a check box menu item.

Paints the background of a color chooser.

Paints the border of a color chooser.

Paints the background of a combo box.

Paints the border of a combo box.

Paints the background of a desktop icon.

Paints the border of a desktop icon.

Paints the background of a desktop pane.

Paints the background of an editor pane.

Paints the border of an editor pane.

Paints the background of a file chooser.

Paints the border of a file chooser.

Paints the background of a formatted text field.

Paints the border of a formatted text field.

Paints the background of an internal frame.

Paints the border of an internal frame.

Paints the background of an internal frame title pane.

Paints the border of an internal frame title pane.

Paints the background of a label.

Paints the border of a label.

Paints the background of a list.

Paints the border of a list.

Paints the background of a menu.

Paints the background of a menu bar.

Paints the border of a menu bar.

Paints the border of a menu.

Paints the background of a menu item.

Paints the border of a menu item.

Paints the background of an option pane.

Paints the border of an option pane.

Paints the background of a panel.

Paints the border of a panel.

Paints the background of a password field.

Paints the border of a password field.

Paints the background of a popup menu.

Paints the border of a popup menu.

Paints the background of a progress bar.

Paints the border of a progress bar.

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

Paints the background of a radio button.

Paints the border of a radio button.

Paints the background of a radio button menu item.

Paints the border of a radio button menu item.

Paints the background of a root pane.

Paints the border of a root pane.

Paints the background of a scrollbar.

Paints the border of a scrollbar.

Paints the background of the thumb of a scrollbar.

Paints the border of the thumb of a scrollbar.

Paints the background of the track of a scrollbar.

Paints the border of the track of a scrollbar.

Paints the background of a scroll pane.

Paints the border of a scroll pane.

Paints the background of a separator.

Paints the border of a separator.

Paints the foreground of a separator.

Paints the background of a slider.

Paints the border of a slider.

Paints the background of the thumb of a slider.

Paints the border of the thumb of a slider.

Paints the background of the track of a slider.

Paints the border of the track of a slider.

Paints the background of a spinner.

Paints the border of a spinner.

Paints the background of a split pane.

Paints the border of a split pane.

Paints the background of the divider of a split pane.

Paints the foreground of the divider of a split pane.

Paints the divider, when the user is dragging the divider, of a
split pane.

Paints the background of a tabbed pane.

Paints the border of a tabbed pane.

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

Paints the background of the area behind the tabs of a tabbed pane.

Paints the border of the area behind the tabs of a tabbed pane.

Paints the background of a tab of a tabbed pane.

Paints the border of a tab of a tabbed pane.

Paints the background of a table.

Paints the border of a table.

Paints the background of the header of a table.

Paints the border of the header of a table.

Paints the background of a text area.

Paints the border of a text area.

Paints the background of a text field.

Paints the border of a text field.

Paints the background of a text pane.

Paints the border of a text pane.

Paints the background of a toggle button.

Paints the border of a toggle button.

Paints the background of a tool bar.

Paints the border of a tool bar.

Paints the background of the tool bar's content area.

Paints the border of the content area of a tool bar.

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

Paints the background of a tool tip.

Paints the border of a tool tip.

Paints the background of a tree.

Paints the border of a tree.

Paints the background of the row containing a cell in a tree.

Paints the border of the row containing a cell in a tree.

Paints the focus indicator for a cell in a tree when it has focus.

Paints the background of the viewport.

Paints the border of a viewport.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthPainter

```java
public SynthPainter()
```

============ METHOD DETAIL ==========

- Method Detail

- paintArrowButtonBackground

```java
public void paintArrowButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintArrowButtonBorder

```java
public void paintArrowButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintArrowButtonForeground

```java
public void paintArrowButtonForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int direction)
```

Paints the foreground of an arrow button. This method is responsible
for drawing a graphical representation of a direction, typically
an arrow. Arrow buttons are created by
some components, such as

JScrollBar

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** direction

- One of SwingConstants.NORTH, SwingConstants.SOUTH
SwingConstants.EAST or SwingConstants.WEST

- paintButtonBackground

```java
public void paintButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintButtonBorder

```java
public void paintButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxMenuItemBackground

```java
public void paintCheckBoxMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxMenuItemBorder

```java
public void paintCheckBoxMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxBackground

```java
public void paintCheckBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxBorder

```java
public void paintCheckBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintColorChooserBackground

```java
public void paintColorChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintColorChooserBorder

```java
public void paintColorChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintComboBoxBackground

```java
public void paintComboBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintComboBoxBorder

```java
public void paintComboBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopIconBackground

```java
public void paintDesktopIconBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopIconBorder

```java
public void paintDesktopIconBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopPaneBackground

```java
public void paintDesktopPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopPaneBorder

```java
public void paintDesktopPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintEditorPaneBackground

```java
public void paintEditorPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintEditorPaneBorder

```java
public void paintEditorPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFileChooserBackground

```java
public void paintFileChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFileChooserBorder

```java
public void paintFileChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFormattedTextFieldBackground

```java
public void paintFormattedTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFormattedTextFieldBorder

```java
public void paintFormattedTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameTitlePaneBackground

```java
public void paintInternalFrameTitlePaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameTitlePaneBorder

```java
public void paintInternalFrameTitlePaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameBackground

```java
public void paintInternalFrameBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameBorder

```java
public void paintInternalFrameBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintLabelBackground

```java
public void paintLabelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintLabelBorder

```java
public void paintLabelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintListBackground

```java
public void paintListBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintListBorder

```java
public void paintListBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBarBackground

```java
public void paintMenuBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBarBorder

```java
public void paintMenuBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuItemBackground

```java
public void paintMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuItemBorder

```java
public void paintMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBackground

```java
public void paintMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBorder

```java
public void paintMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintOptionPaneBackground

```java
public void paintOptionPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintOptionPaneBorder

```java
public void paintOptionPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPanelBackground

```java
public void paintPanelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPanelBorder

```java
public void paintPanelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPasswordFieldBackground

```java
public void paintPasswordFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPasswordFieldBorder

```java
public void paintPasswordFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPopupMenuBackground

```java
public void paintPopupMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPopupMenuBorder

```java
public void paintPopupMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

- paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

- paintProgressBarForeground

```java
public void paintProgressBarForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

- paintRadioButtonMenuItemBackground

```java
public void paintRadioButtonMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonMenuItemBorder

```java
public void paintRadioButtonMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonBackground

```java
public void paintRadioButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonBorder

```java
public void paintRadioButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRootPaneBackground

```java
public void paintRootPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRootPaneBorder

```java
public void paintRootPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarThumbBackground

```java
public void paintScrollBarThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

- paintScrollBarThumbBorder

```java
public void paintScrollBarThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

- paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollPaneBackground

```java
public void paintScrollPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollPaneBorder

```java
public void paintScrollPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

- paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

- paintSeparatorForeground

```java
public void paintSeparatorForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

- paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderThumbBackground

```java
public void paintSliderThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

- paintSliderThumbBorder

```java
public void paintSliderThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

- paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a slider. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSpinnerBackground

```java
public void paintSpinnerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSpinnerBorder

```java
public void paintSpinnerBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the divider of a split pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Since:** 1.6

- paintSplitPaneDividerForeground

```java
public void paintSplitPaneDividerForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

- paintSplitPaneDragDivider

```java
public void paintSplitPaneDragDivider​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the divider, when the user is dragging the divider, of a
split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

- paintSplitPaneBackground

```java
public void paintSplitPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneBorder

```java
public void paintSplitPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneBackground

```java
public void paintTabbedPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneBorder

```java
public void paintTabbedPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the area behind the tabs of a tabbed pane.
This implementation invokes the method of the same name without the
orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the area behind the tabs of a tabbed pane. This
implementation invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the background of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

- paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the background of a tab of a tabbed pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the border of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

- paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the border of a tab of a tabbed pane. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneContentBackground

```java
public void paintTabbedPaneContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneContentBorder

```java
public void paintTabbedPaneContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableHeaderBackground

```java
public void paintTableHeaderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableHeaderBorder

```java
public void paintTableHeaderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableBackground

```java
public void paintTableBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableBorder

```java
public void paintTableBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextAreaBackground

```java
public void paintTextAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextAreaBorder

```java
public void paintTextAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextPaneBackground

```java
public void paintTextPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextPaneBorder

```java
public void paintTextPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextFieldBackground

```java
public void paintTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextFieldBorder

```java
public void paintTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToggleButtonBackground

```java
public void paintToggleButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToggleButtonBorder

```java
public void paintToggleButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the tool bar's content area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the tool bar's content area. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the content area of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the content area of a tool bar. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolTipBackground

```java
public void paintToolTipBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolTipBorder

```java
public void paintToolTipBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeBackground

```java
public void paintTreeBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeBorder

```java
public void paintTreeBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellBackground

```java
public void paintTreeCellBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellBorder

```java
public void paintTreeCellBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellFocus

```java
public void paintTreeCellFocus​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the focus indicator for a cell in a tree when it has focus.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintViewportBackground

```java
public void paintViewportBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintViewportBorder

```java
public void paintViewportBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

Constructor Detail

- SynthPainter

```java
public SynthPainter()
```

---

#### Constructor Detail

SynthPainter

```java
public SynthPainter()
```

---

#### SynthPainter

public SynthPainter()

Method Detail

- paintArrowButtonBackground

```java
public void paintArrowButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintArrowButtonBorder

```java
public void paintArrowButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintArrowButtonForeground

```java
public void paintArrowButtonForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int direction)
```

Paints the foreground of an arrow button. This method is responsible
for drawing a graphical representation of a direction, typically
an arrow. Arrow buttons are created by
some components, such as

JScrollBar

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** direction

- One of SwingConstants.NORTH, SwingConstants.SOUTH
SwingConstants.EAST or SwingConstants.WEST

- paintButtonBackground

```java
public void paintButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintButtonBorder

```java
public void paintButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxMenuItemBackground

```java
public void paintCheckBoxMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxMenuItemBorder

```java
public void paintCheckBoxMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxBackground

```java
public void paintCheckBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintCheckBoxBorder

```java
public void paintCheckBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintColorChooserBackground

```java
public void paintColorChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintColorChooserBorder

```java
public void paintColorChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintComboBoxBackground

```java
public void paintComboBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintComboBoxBorder

```java
public void paintComboBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopIconBackground

```java
public void paintDesktopIconBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopIconBorder

```java
public void paintDesktopIconBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopPaneBackground

```java
public void paintDesktopPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintDesktopPaneBorder

```java
public void paintDesktopPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintEditorPaneBackground

```java
public void paintEditorPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintEditorPaneBorder

```java
public void paintEditorPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFileChooserBackground

```java
public void paintFileChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFileChooserBorder

```java
public void paintFileChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFormattedTextFieldBackground

```java
public void paintFormattedTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintFormattedTextFieldBorder

```java
public void paintFormattedTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameTitlePaneBackground

```java
public void paintInternalFrameTitlePaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameTitlePaneBorder

```java
public void paintInternalFrameTitlePaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameBackground

```java
public void paintInternalFrameBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintInternalFrameBorder

```java
public void paintInternalFrameBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintLabelBackground

```java
public void paintLabelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintLabelBorder

```java
public void paintLabelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintListBackground

```java
public void paintListBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintListBorder

```java
public void paintListBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBarBackground

```java
public void paintMenuBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBarBorder

```java
public void paintMenuBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuItemBackground

```java
public void paintMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuItemBorder

```java
public void paintMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBackground

```java
public void paintMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintMenuBorder

```java
public void paintMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintOptionPaneBackground

```java
public void paintOptionPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintOptionPaneBorder

```java
public void paintOptionPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPanelBackground

```java
public void paintPanelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPanelBorder

```java
public void paintPanelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPasswordFieldBackground

```java
public void paintPasswordFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPasswordFieldBorder

```java
public void paintPasswordFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPopupMenuBackground

```java
public void paintPopupMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintPopupMenuBorder

```java
public void paintPopupMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

- paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

- paintProgressBarForeground

```java
public void paintProgressBarForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

- paintRadioButtonMenuItemBackground

```java
public void paintRadioButtonMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonMenuItemBorder

```java
public void paintRadioButtonMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonBackground

```java
public void paintRadioButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRadioButtonBorder

```java
public void paintRadioButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRootPaneBackground

```java
public void paintRootPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintRootPaneBorder

```java
public void paintRootPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarThumbBackground

```java
public void paintScrollBarThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

- paintScrollBarThumbBorder

```java
public void paintScrollBarThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

- paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

- paintScrollPaneBackground

```java
public void paintScrollPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintScrollPaneBorder

```java
public void paintScrollPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

- paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

- paintSeparatorForeground

```java
public void paintSeparatorForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

- paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderThumbBackground

```java
public void paintSliderThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

- paintSliderThumbBorder

```java
public void paintSliderThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

- paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a slider. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

- paintSpinnerBackground

```java
public void paintSpinnerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSpinnerBorder

```java
public void paintSpinnerBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the divider of a split pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Since:** 1.6

- paintSplitPaneDividerForeground

```java
public void paintSplitPaneDividerForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

- paintSplitPaneDragDivider

```java
public void paintSplitPaneDragDivider​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the divider, when the user is dragging the divider, of a
split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

- paintSplitPaneBackground

```java
public void paintSplitPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintSplitPaneBorder

```java
public void paintSplitPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneBackground

```java
public void paintTabbedPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneBorder

```java
public void paintTabbedPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the area behind the tabs of a tabbed pane.
This implementation invokes the method of the same name without the
orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the area behind the tabs of a tabbed pane. This
implementation invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the background of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

- paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the background of a tab of a tabbed pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the border of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

- paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the border of a tab of a tabbed pane. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

- paintTabbedPaneContentBackground

```java
public void paintTabbedPaneContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTabbedPaneContentBorder

```java
public void paintTabbedPaneContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableHeaderBackground

```java
public void paintTableHeaderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableHeaderBorder

```java
public void paintTableHeaderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableBackground

```java
public void paintTableBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTableBorder

```java
public void paintTableBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextAreaBackground

```java
public void paintTextAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextAreaBorder

```java
public void paintTextAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextPaneBackground

```java
public void paintTextPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextPaneBorder

```java
public void paintTextPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextFieldBackground

```java
public void paintTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTextFieldBorder

```java
public void paintTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToggleButtonBackground

```java
public void paintToggleButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToggleButtonBorder

```java
public void paintToggleButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the tool bar's content area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the tool bar's content area. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the content area of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the content area of a tool bar. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

- paintToolTipBackground

```java
public void paintToolTipBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintToolTipBorder

```java
public void paintToolTipBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeBackground

```java
public void paintTreeBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeBorder

```java
public void paintTreeBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellBackground

```java
public void paintTreeCellBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellBorder

```java
public void paintTreeCellBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintTreeCellFocus

```java
public void paintTreeCellFocus​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the focus indicator for a cell in a tree when it has focus.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintViewportBackground

```java
public void paintViewportBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

- paintViewportBorder

```java
public void paintViewportBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### Method Detail

paintArrowButtonBackground

```java
public void paintArrowButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintArrowButtonBackground

public void paintArrowButtonBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

paintArrowButtonBorder

```java
public void paintArrowButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintArrowButtonBorder

public void paintArrowButtonBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an arrow button. Arrow buttons are created by
some components, such as

JScrollBar

.

paintArrowButtonForeground

```java
public void paintArrowButtonForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int direction)
```

Paints the foreground of an arrow button. This method is responsible
for drawing a graphical representation of a direction, typically
an arrow. Arrow buttons are created by
some components, such as

JScrollBar

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** direction

- One of SwingConstants.NORTH, SwingConstants.SOUTH
SwingConstants.EAST or SwingConstants.WEST

---

#### paintArrowButtonForeground

public void paintArrowButtonForeground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int direction)

Paints the foreground of an arrow button. This method is responsible
for drawing a graphical representation of a direction, typically
an arrow. Arrow buttons are created by
some components, such as

JScrollBar

paintButtonBackground

```java
public void paintButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintButtonBackground

public void paintButtonBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a button.

paintButtonBorder

```java
public void paintButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintButtonBorder

public void paintButtonBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a button.

paintCheckBoxMenuItemBackground

```java
public void paintCheckBoxMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintCheckBoxMenuItemBackground

public void paintCheckBoxMenuItemBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box menu item.

paintCheckBoxMenuItemBorder

```java
public void paintCheckBoxMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintCheckBoxMenuItemBorder

public void paintCheckBoxMenuItemBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box menu item.

paintCheckBoxBackground

```java
public void paintCheckBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintCheckBoxBackground

public void paintCheckBoxBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a check box.

paintCheckBoxBorder

```java
public void paintCheckBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a check box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintCheckBoxBorder

public void paintCheckBoxBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a check box.

paintColorChooserBackground

```java
public void paintColorChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintColorChooserBackground

public void paintColorChooserBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a color chooser.

paintColorChooserBorder

```java
public void paintColorChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a color chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintColorChooserBorder

public void paintColorChooserBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a color chooser.

paintComboBoxBackground

```java
public void paintComboBoxBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintComboBoxBackground

public void paintComboBoxBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a combo box.

paintComboBoxBorder

```java
public void paintComboBoxBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a combo box.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintComboBoxBorder

public void paintComboBoxBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a combo box.

paintDesktopIconBackground

```java
public void paintDesktopIconBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintDesktopIconBackground

public void paintDesktopIconBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop icon.

paintDesktopIconBorder

```java
public void paintDesktopIconBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a desktop icon.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintDesktopIconBorder

public void paintDesktopIconBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a desktop icon.

paintDesktopPaneBackground

```java
public void paintDesktopPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintDesktopPaneBackground

public void paintDesktopPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

paintDesktopPaneBorder

```java
public void paintDesktopPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a desktop pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintDesktopPaneBorder

public void paintDesktopPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a desktop pane.

paintEditorPaneBackground

```java
public void paintEditorPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintEditorPaneBackground

public void paintEditorPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an editor pane.

paintEditorPaneBorder

```java
public void paintEditorPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an editor pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintEditorPaneBorder

public void paintEditorPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an editor pane.

paintFileChooserBackground

```java
public void paintFileChooserBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintFileChooserBackground

public void paintFileChooserBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a file chooser.

paintFileChooserBorder

```java
public void paintFileChooserBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a file chooser.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintFileChooserBorder

public void paintFileChooserBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a file chooser.

paintFormattedTextFieldBackground

```java
public void paintFormattedTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintFormattedTextFieldBackground

public void paintFormattedTextFieldBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a formatted text field.

paintFormattedTextFieldBorder

```java
public void paintFormattedTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a formatted text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintFormattedTextFieldBorder

public void paintFormattedTextFieldBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a formatted text field.

paintInternalFrameTitlePaneBackground

```java
public void paintInternalFrameTitlePaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintInternalFrameTitlePaneBackground

public void paintInternalFrameTitlePaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame title pane.

paintInternalFrameTitlePaneBorder

```java
public void paintInternalFrameTitlePaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame title pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintInternalFrameTitlePaneBorder

public void paintInternalFrameTitlePaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame title pane.

paintInternalFrameBackground

```java
public void paintInternalFrameBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintInternalFrameBackground

public void paintInternalFrameBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an internal frame.

paintInternalFrameBorder

```java
public void paintInternalFrameBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an internal frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintInternalFrameBorder

public void paintInternalFrameBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an internal frame.

paintLabelBackground

```java
public void paintLabelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintLabelBackground

public void paintLabelBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a label.

paintLabelBorder

```java
public void paintLabelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a label.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintLabelBorder

public void paintLabelBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a label.

paintListBackground

```java
public void paintListBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintListBackground

public void paintListBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a list.

paintListBorder

```java
public void paintListBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a list.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintListBorder

public void paintListBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a list.

paintMenuBarBackground

```java
public void paintMenuBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuBarBackground

public void paintMenuBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu bar.

paintMenuBarBorder

```java
public void paintMenuBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuBarBorder

public void paintMenuBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu bar.

paintMenuItemBackground

```java
public void paintMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuItemBackground

public void paintMenuItemBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu item.

paintMenuItemBorder

```java
public void paintMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuItemBorder

public void paintMenuItemBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu item.

paintMenuBackground

```java
public void paintMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuBackground

public void paintMenuBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a menu.

paintMenuBorder

```java
public void paintMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintMenuBorder

public void paintMenuBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a menu.

paintOptionPaneBackground

```java
public void paintOptionPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintOptionPaneBackground

public void paintOptionPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of an option pane.

paintOptionPaneBorder

```java
public void paintOptionPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of an option pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintOptionPaneBorder

public void paintOptionPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of an option pane.

paintPanelBackground

```java
public void paintPanelBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPanelBackground

public void paintPanelBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a panel.

paintPanelBorder

```java
public void paintPanelBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a panel.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPanelBorder

public void paintPanelBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a panel.

paintPasswordFieldBackground

```java
public void paintPasswordFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPasswordFieldBackground

public void paintPasswordFieldBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a password field.

paintPasswordFieldBorder

```java
public void paintPasswordFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a password field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPasswordFieldBorder

public void paintPasswordFieldBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a password field.

paintPopupMenuBackground

```java
public void paintPopupMenuBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPopupMenuBackground

public void paintPopupMenuBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a popup menu.

paintPopupMenuBorder

```java
public void paintPopupMenuBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a popup menu.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintPopupMenuBorder

public void paintPopupMenuBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a popup menu.

paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintProgressBarBackground

public void paintProgressBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a progress bar.

paintProgressBarBackground

```java
public void paintProgressBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

---

#### paintProgressBarBackground

public void paintProgressBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a progress bar. This implementation invokes the
method of the same name without the orientation.

paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintProgressBarBorder

public void paintProgressBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a progress bar.

paintProgressBarBorder

```java
public void paintProgressBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a progress bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL
**Since:** 1.6

---

#### paintProgressBarBorder

public void paintProgressBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a progress bar. This implementation invokes the
method of the same name without the orientation.

paintProgressBarForeground

```java
public void paintProgressBarForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- one of

JProgressBar.HORIZONTAL

or

JProgressBar.VERTICAL

---

#### paintProgressBarForeground

public void paintProgressBarForeground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a progress bar. is responsible for
providing an indication of the progress of the progress bar.

paintRadioButtonMenuItemBackground

```java
public void paintRadioButtonMenuItemBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRadioButtonMenuItemBackground

public void paintRadioButtonMenuItemBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button menu item.

paintRadioButtonMenuItemBorder

```java
public void paintRadioButtonMenuItemBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button menu item.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRadioButtonMenuItemBorder

public void paintRadioButtonMenuItemBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button menu item.

paintRadioButtonBackground

```java
public void paintRadioButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRadioButtonBackground

public void paintRadioButtonBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a radio button.

paintRadioButtonBorder

```java
public void paintRadioButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a radio button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRadioButtonBorder

public void paintRadioButtonBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a radio button.

paintRootPaneBackground

```java
public void paintRootPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRootPaneBackground

public void paintRootPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a root pane.

paintRootPaneBorder

```java
public void paintRootPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a root pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintRootPaneBorder

public void paintRootPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a root pane.

paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollBarBackground

public void paintScrollBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scrollbar.

paintScrollBarBackground

```java
public void paintScrollBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

---

#### paintScrollBarBackground

public void paintScrollBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a scrollbar. This implementation invokes the
method of the same name without the orientation.

paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scrollbar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollBarBorder

public void paintScrollBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scrollbar.

paintScrollBarBorder

```java
public void paintScrollBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a scrollbar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

---

#### paintScrollBarBorder

public void paintScrollBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a scrollbar. This implementation invokes the
method of the same name without the orientation.

paintScrollBarThumbBackground

```java
public void paintScrollBarThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

---

#### paintScrollBarThumbBackground

public void paintScrollBarThumbBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

paintScrollBarThumbBorder

```java
public void paintScrollBarThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL

---

#### paintScrollBarThumbBorder

public void paintScrollBarThumbBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a scrollbar. The thumb provides
a graphical indication as to how much of the Component is visible in a

JScrollPane

.

paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollBarTrackBackground

public void paintScrollBarTrackBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a scrollbar. The track contains
the thumb.

paintScrollBarTrackBackground

```java
public void paintScrollBarTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

---

#### paintScrollBarTrackBackground

public void paintScrollBarTrackBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a scrollbar. The track contains
the thumb.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollBarTrackBorder

public void paintScrollBarTrackBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a scrollbar. The track contains
the thumb.

paintScrollBarTrackBorder

```java
public void paintScrollBarTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- Orientation of the JScrollBar, one of

JScrollBar.HORIZONTAL

or

JScrollBar.VERTICAL
**Since:** 1.6

---

#### paintScrollBarTrackBorder

public void paintScrollBarTrackBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a scrollbar. The track contains
the thumb. This implementation invokes the method of the same name without
the orientation.

paintScrollPaneBackground

```java
public void paintScrollPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollPaneBackground

public void paintScrollPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a scroll pane.

paintScrollPaneBorder

```java
public void paintScrollPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a scroll pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintScrollPaneBorder

public void paintScrollPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a scroll pane.

paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSeparatorBackground

public void paintSeparatorBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a separator.

paintSeparatorBackground

```java
public void paintSeparatorBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

---

#### paintSeparatorBackground

public void paintSeparatorBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a separator. This implementation invokes the
method of the same name without the orientation.

paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSeparatorBorder

public void paintSeparatorBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a separator.

paintSeparatorBorder

```java
public void paintSeparatorBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a separator. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL
**Since:** 1.6

---

#### paintSeparatorBorder

public void paintSeparatorBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a separator. This implementation invokes the
method of the same name without the orientation.

paintSeparatorForeground

```java
public void paintSeparatorForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of a separator.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSeparator.HORIZONTAL

or

JSeparator.VERTICAL

---

#### paintSeparatorForeground

public void paintSeparatorForeground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of a separator.

paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSliderBackground

public void paintSliderBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a slider.

paintSliderBackground

```java
public void paintSliderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

---

#### paintSliderBackground

public void paintSliderBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a slider. This implementation invokes the
method of the same name without the orientation.

paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSliderBorder

public void paintSliderBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a slider.

paintSliderBorder

```java
public void paintSliderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

---

#### paintSliderBorder

public void paintSliderBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a slider. This implementation invokes the
method of the same name without the orientation.

paintSliderThumbBackground

```java
public void paintSliderThumbBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

---

#### paintSliderThumbBackground

public void paintSliderThumbBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the thumb of a slider.

paintSliderThumbBorder

```java
public void paintSliderThumbBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the thumb of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL

---

#### paintSliderThumbBorder

public void paintSliderThumbBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the thumb of a slider.

paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSliderTrackBackground

public void paintSliderTrackBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the track of a slider.

paintSliderTrackBackground

```java
public void paintSliderTrackBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the track of a slider. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

---

#### paintSliderTrackBackground

public void paintSliderTrackBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the track of a slider. This implementation invokes
the method of the same name without the orientation.

paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the track of a slider.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSliderTrackBorder

public void paintSliderTrackBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the track of a slider.

paintSliderTrackBorder

```java
public void paintSliderTrackBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the track of a slider. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSlider.HORIZONTAL

or

JSlider.VERTICAL
**Since:** 1.6

---

#### paintSliderTrackBorder

public void paintSliderTrackBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the track of a slider. This implementation invokes the
method of the same name without the orientation.

paintSpinnerBackground

```java
public void paintSpinnerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSpinnerBackground

public void paintSpinnerBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a spinner.

paintSpinnerBorder

```java
public void paintSpinnerBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a spinner.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSpinnerBorder

public void paintSpinnerBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a spinner.

paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSplitPaneDividerBackground

public void paintSplitPaneDividerBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the divider of a split pane.

paintSplitPaneDividerBackground

```java
public void paintSplitPaneDividerBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the divider of a split pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT
**Since:** 1.6

---

#### paintSplitPaneDividerBackground

public void paintSplitPaneDividerBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the divider of a split pane. This implementation
invokes the method of the same name without the orientation.

paintSplitPaneDividerForeground

```java
public void paintSplitPaneDividerForeground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the foreground of the divider of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

---

#### paintSplitPaneDividerForeground

public void paintSplitPaneDividerForeground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the foreground of the divider of a split pane.

paintSplitPaneDragDivider

```java
public void paintSplitPaneDragDivider​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the divider, when the user is dragging the divider, of a
split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JSplitPane.HORIZONTAL_SPLIT

or

JSplitPane.VERTICAL_SPLIT

---

#### paintSplitPaneDragDivider

public void paintSplitPaneDragDivider​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the divider, when the user is dragging the divider, of a
split pane.

paintSplitPaneBackground

```java
public void paintSplitPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSplitPaneBackground

public void paintSplitPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a split pane.

paintSplitPaneBorder

```java
public void paintSplitPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a split pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintSplitPaneBorder

public void paintSplitPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a split pane.

paintTabbedPaneBackground

```java
public void paintTabbedPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneBackground

public void paintTabbedPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tabbed pane.

paintTabbedPaneBorder

```java
public void paintTabbedPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneBorder

public void paintTabbedPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tabbed pane.

paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneTabAreaBackground

public void paintTabbedPaneTabAreaBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area behind the tabs of a tabbed pane.

paintTabbedPaneTabAreaBackground

```java
public void paintTabbedPaneTabAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the area behind the tabs of a tabbed pane.
This implementation invokes the method of the same name without the
orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

---

#### paintTabbedPaneTabAreaBackground

public void paintTabbedPaneTabAreaBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the area behind the tabs of a tabbed pane.
This implementation invokes the method of the same name without the
orientation.

paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area behind the tabs of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneTabAreaBorder

public void paintTabbedPaneTabAreaBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area behind the tabs of a tabbed pane.

paintTabbedPaneTabAreaBorder

```java
public void paintTabbedPaneTabAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the area behind the tabs of a tabbed pane. This
implementation invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

---

#### paintTabbedPaneTabAreaBorder

public void paintTabbedPaneTabAreaBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the area behind the tabs of a tabbed pane. This
implementation invokes the method of the same name without the orientation.

paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the background of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

---

#### paintTabbedPaneTabBackground

public void paintTabbedPaneTabBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the background of a tab of a tabbed pane.

paintTabbedPaneTabBackground

```java
public void paintTabbedPaneTabBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the background of a tab of a tabbed pane. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

---

#### paintTabbedPaneTabBackground

public void paintTabbedPaneTabBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the background of a tab of a tabbed pane. This implementation
invokes the method of the same name without the orientation.

paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex)
```

Paints the border of a tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.

---

#### paintTabbedPaneTabBorder

public void paintTabbedPaneTabBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex)

Paints the border of a tab of a tabbed pane.

paintTabbedPaneTabBorder

```java
public void paintTabbedPaneTabBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)
```

Paints the border of a tab of a tabbed pane. This implementation invokes
the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** tabIndex

- Index of tab being painted.
**Parameters:** orientation

- One of

JTabbedPane.TOP

,

JTabbedPane.LEFT

,

JTabbedPane.BOTTOM

, or

JTabbedPane.RIGHT
**Since:** 1.6

---

#### paintTabbedPaneTabBorder

public void paintTabbedPaneTabBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int tabIndex,
int orientation)

Paints the border of a tab of a tabbed pane. This implementation invokes
the method of the same name without the orientation.

paintTabbedPaneContentBackground

```java
public void paintTabbedPaneContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneContentBackground

public void paintTabbedPaneContentBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the area that contains the content of the
selected tab of a tabbed pane.

paintTabbedPaneContentBorder

```java
public void paintTabbedPaneContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTabbedPaneContentBorder

public void paintTabbedPaneContentBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the area that contains the content of the
selected tab of a tabbed pane.

paintTableHeaderBackground

```java
public void paintTableHeaderBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTableHeaderBackground

public void paintTableHeaderBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the header of a table.

paintTableHeaderBorder

```java
public void paintTableHeaderBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the header of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTableHeaderBorder

public void paintTableHeaderBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the header of a table.

paintTableBackground

```java
public void paintTableBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTableBackground

public void paintTableBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a table.

paintTableBorder

```java
public void paintTableBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a table.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTableBorder

public void paintTableBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a table.

paintTextAreaBackground

```java
public void paintTextAreaBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextAreaBackground

public void paintTextAreaBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text area.

paintTextAreaBorder

```java
public void paintTextAreaBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextAreaBorder

public void paintTextAreaBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text area.

paintTextPaneBackground

```java
public void paintTextPaneBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextPaneBackground

public void paintTextPaneBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text pane.

paintTextPaneBorder

```java
public void paintTextPaneBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text pane.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextPaneBorder

public void paintTextPaneBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text pane.

paintTextFieldBackground

```java
public void paintTextFieldBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextFieldBackground

public void paintTextFieldBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a text field.

paintTextFieldBorder

```java
public void paintTextFieldBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a text field.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTextFieldBorder

public void paintTextFieldBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a text field.

paintToggleButtonBackground

```java
public void paintToggleButtonBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToggleButtonBackground

public void paintToggleButtonBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a toggle button.

paintToggleButtonBorder

```java
public void paintToggleButtonBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a toggle button.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToggleButtonBorder

public void paintToggleButtonBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a toggle button.

paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarBackground

public void paintToolBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool bar.

paintToolBarBackground

```java
public void paintToolBarBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarBackground

public void paintToolBarBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of a tool bar. This implementation invokes the
method of the same name without the orientation.

paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarBorder

public void paintToolBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool bar.

paintToolBarBorder

```java
public void paintToolBarBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of a tool bar. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarBorder

public void paintToolBarBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of a tool bar. This implementation invokes the
method of the same name without the orientation.

paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the tool bar's content area.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarContentBackground

public void paintToolBarContentBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the tool bar's content area.

paintToolBarContentBackground

```java
public void paintToolBarContentBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the tool bar's content area. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarContentBackground

public void paintToolBarContentBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the tool bar's content area. This implementation
invokes the method of the same name without the orientation.

paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the content area of a tool bar.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarContentBorder

public void paintToolBarContentBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the content area of a tool bar.

paintToolBarContentBorder

```java
public void paintToolBarContentBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the content area of a tool bar. This implementation
invokes the method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarContentBorder

public void paintToolBarContentBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the content area of a tool bar. This implementation
invokes the method of the same name without the orientation.

paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarDragWindowBackground

public void paintToolBarDragWindowBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame.

paintToolBarDragWindowBackground

```java
public void paintToolBarDragWindowBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the background of the window containing the tool bar when it
has been detached from its primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarDragWindowBackground

public void paintToolBarDragWindowBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the background of the window containing the tool bar when it
has been detached from its primary frame. This implementation invokes the
method of the same name without the orientation.

paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolBarDragWindowBorder

public void paintToolBarDragWindowBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame.

paintToolBarDragWindowBorder

```java
public void paintToolBarDragWindowBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h,
int orientation)
```

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame. This implementation invokes the
method of the same name without the orientation.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to
**Parameters:** orientation

- One of

JToolBar.HORIZONTAL

or

JToolBar.VERTICAL
**Since:** 1.6

---

#### paintToolBarDragWindowBorder

public void paintToolBarDragWindowBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h,
int orientation)

Paints the border of the window containing the tool bar when it
has been detached from it's primary frame. This implementation invokes the
method of the same name without the orientation.

paintToolTipBackground

```java
public void paintToolTipBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolTipBackground

public void paintToolTipBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tool tip.

paintToolTipBorder

```java
public void paintToolTipBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tool tip.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintToolTipBorder

public void paintToolTipBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tool tip.

paintTreeBackground

```java
public void paintTreeBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTreeBackground

public void paintTreeBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of a tree.

paintTreeBorder

```java
public void paintTreeBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTreeBorder

public void paintTreeBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a tree.

paintTreeCellBackground

```java
public void paintTreeCellBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTreeCellBackground

public void paintTreeCellBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the row containing a cell in a tree.

paintTreeCellBorder

```java
public void paintTreeCellBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of the row containing a cell in a tree.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTreeCellBorder

public void paintTreeCellBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of the row containing a cell in a tree.

paintTreeCellFocus

```java
public void paintTreeCellFocus​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the focus indicator for a cell in a tree when it has focus.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintTreeCellFocus

public void paintTreeCellFocus​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the focus indicator for a cell in a tree when it has focus.

paintViewportBackground

```java
public void paintViewportBackground​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the background of the viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintViewportBackground

public void paintViewportBackground​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the background of the viewport.

paintViewportBorder

```java
public void paintViewportBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border of a viewport.

**Parameters:** context

- SynthContext identifying the

JComponent

and

Region

to paint to
**Parameters:** g

-

Graphics

to paint to
**Parameters:** x

- X coordinate of the area to paint to
**Parameters:** y

- Y coordinate of the area to paint to
**Parameters:** w

- Width of the area to paint to
**Parameters:** h

- Height of the area to paint to

---

#### paintViewportBorder

public void paintViewportBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border of a viewport.

---

