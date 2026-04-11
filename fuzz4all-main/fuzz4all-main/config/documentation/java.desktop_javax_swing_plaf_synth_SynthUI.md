# Interface SynthUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthUI.html`

### Class Description

```java
public interface
SynthUI

extends
SynthConstants
```

SynthUI is used to fetch the SynthContext for a particular Component.

**All Superinterfaces:** SynthConstants

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### SynthContext
getContext​(
JComponent
c)

Returns the Context for the specified component.

**Parameters:**
- c

- Component requesting SynthContext.

**Returns:**
- SynthContext describing component.

---

#### void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)

Paints the border.

**Parameters:**
- context

- a component context
- g

-

Graphics

to paint on
- x

- the X coordinate
- y

- the Y coordinate
- w

- width of the border
- h

- height of the border

---

### Additional Sections

#### Interface SynthUI

**All Superinterfaces:** SynthConstants

**All Known Implementing Classes:** SynthButtonUI

,

SynthCheckBoxMenuItemUI

,

SynthCheckBoxUI

,

SynthColorChooserUI

,

SynthComboBoxUI

,

SynthDesktopIconUI

,

SynthDesktopPaneUI

,

SynthEditorPaneUI

,

SynthFormattedTextFieldUI

,

SynthInternalFrameUI

,

SynthLabelUI

,

SynthListUI

,

SynthMenuBarUI

,

SynthMenuItemUI

,

SynthMenuUI

,

SynthOptionPaneUI

,

SynthPanelUI

,

SynthPasswordFieldUI

,

SynthPopupMenuUI

,

SynthProgressBarUI

,

SynthRadioButtonMenuItemUI

,

SynthRadioButtonUI

,

SynthRootPaneUI

,

SynthScrollBarUI

,

SynthScrollPaneUI

,

SynthSeparatorUI

,

SynthSliderUI

,

SynthSpinnerUI

,

SynthSplitPaneUI

,

SynthTabbedPaneUI

,

SynthTableHeaderUI

,

SynthTableUI

,

SynthTextAreaUI

,

SynthTextFieldUI

,

SynthTextPaneUI

,

SynthToggleButtonUI

,

SynthToolBarUI

,

SynthToolTipUI

,

SynthTreeUI

,

SynthViewportUI

```java
public interface
SynthUI

extends
SynthConstants
```

SynthUI is used to fetch the SynthContext for a particular Component.

**Since:** 1.7

public interface

SynthUI

extends

SynthConstants

SynthUI is used to fetch the SynthContext for a particular Component.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SynthContext

getContext

​(

JComponent

c)

Returns the Context for the specified component.

void

paintBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border.

Field Summary

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Field Summary

Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Fields declared in interface javax.swing.plaf.synth. SynthConstants

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SynthContext

getContext

​(

JComponent

c)

Returns the Context for the specified component.

void

paintBorder

​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border.

---

#### Method Summary

Returns the Context for the specified component.

Paints the border.

============ METHOD DETAIL ==========

- Method Detail

- getContext

```java
SynthContext
getContext​(
JComponent
c)
```

Returns the Context for the specified component.

**Parameters:** c

- Component requesting SynthContext.
**Returns:** SynthContext describing component.

- paintBorder

```java
void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border.

**Parameters:** context

- a component context
**Parameters:** g

-

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

Method Detail

- getContext

```java
SynthContext
getContext​(
JComponent
c)
```

Returns the Context for the specified component.

**Parameters:** c

- Component requesting SynthContext.
**Returns:** SynthContext describing component.

- paintBorder

```java
void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border.

**Parameters:** context

- a component context
**Parameters:** g

-

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

---

#### Method Detail

getContext

```java
SynthContext
getContext​(
JComponent
c)
```

Returns the Context for the specified component.

**Parameters:** c

- Component requesting SynthContext.
**Returns:** SynthContext describing component.

---

#### getContext

SynthContext

getContext​(

JComponent

c)

Returns the Context for the specified component.

paintBorder

```java
void paintBorder​(
SynthContext
context,

Graphics
g,
int x,
int y,
int w,
int h)
```

Paints the border.

**Parameters:** context

- a component context
**Parameters:** g

-

Graphics

to paint on
**Parameters:** x

- the X coordinate
**Parameters:** y

- the Y coordinate
**Parameters:** w

- width of the border
**Parameters:** h

- height of the border

---

#### paintBorder

void paintBorder​(

SynthContext

context,

Graphics

g,
int x,
int y,
int w,
int h)

Paints the border.

---

