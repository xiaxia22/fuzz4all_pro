# Interface SynthConstants

**Source:** `java.desktop\javax\swing\plaf\synth\SynthConstants.html`

### Class Description

```java
public interface
SynthConstants
```

Constants used by Synth. Not all Components support all states. A
Component will at least be in one of the primary states. That is, the
return value from

SynthContext.getComponentState()

will at
least be one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

, and may also contain

FOCUSED

,

SELECTED

or

DEFAULT

.

**All Known Subinterfaces:** SynthUI

---

### Field Details

#### static final int ENABLED

Primary state indicating the component is enabled.

**See Also:**
- Constant Field Values

---

#### static final int MOUSE_OVER

Primary state indicating the mouse is over the region.

**See Also:**
- Constant Field Values

---

#### static final int PRESSED

Primary state indicating the region is in a pressed state. Pressed
does not necessarily mean the user has pressed the mouse button.

**See Also:**
- Constant Field Values

---

#### static final int DISABLED

Primary state indicating the region is not enabled.

**See Also:**
- Constant Field Values

---

#### static final int FOCUSED

Indicates the region has focus.

**See Also:**
- Constant Field Values

---

#### static final int SELECTED

Indicates the region is selected.

**See Also:**
- Constant Field Values

---

#### static final int DEFAULT

Indicates the region is the default. This is typically used for buttons
to indicate this button is somehow special.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface SynthConstants

**All Known Subinterfaces:** SynthUI

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
SynthConstants
```

Constants used by Synth. Not all Components support all states. A
Component will at least be in one of the primary states. That is, the
return value from

SynthContext.getComponentState()

will at
least be one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

, and may also contain

FOCUSED

,

SELECTED

or

DEFAULT

.

**Since:** 1.5

public interface

SynthConstants

Constants used by Synth. Not all Components support all states. A
Component will at least be in one of the primary states. That is, the
return value from

SynthContext.getComponentState()

will at
least be one of

ENABLED

,

MOUSE_OVER

,

PRESSED

or

DISABLED

, and may also contain

FOCUSED

,

SELECTED

or

DEFAULT

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

DEFAULT

Indicates the region is the default.

static int

DISABLED

Primary state indicating the region is not enabled.

static int

ENABLED

Primary state indicating the component is enabled.

static int

FOCUSED

Indicates the region has focus.

static int

MOUSE_OVER

Primary state indicating the mouse is over the region.

static int

PRESSED

Primary state indicating the region is in a pressed state.

static int

SELECTED

Indicates the region is selected.

Field Summary

Fields

Modifier and Type

Field

Description

static int

DEFAULT

Indicates the region is the default.

static int

DISABLED

Primary state indicating the region is not enabled.

static int

ENABLED

Primary state indicating the component is enabled.

static int

FOCUSED

Indicates the region has focus.

static int

MOUSE_OVER

Primary state indicating the mouse is over the region.

static int

PRESSED

Primary state indicating the region is in a pressed state.

static int

SELECTED

Indicates the region is selected.

---

#### Field Summary

Indicates the region is the default.

Primary state indicating the region is not enabled.

Primary state indicating the component is enabled.

Indicates the region has focus.

Primary state indicating the mouse is over the region.

Primary state indicating the region is in a pressed state.

Indicates the region is selected.

============ FIELD DETAIL ===========

- Field Detail

- ENABLED

```java
static final int ENABLED
```

Primary state indicating the component is enabled.

**See Also:** Constant Field Values

- MOUSE_OVER

```java
static final int MOUSE_OVER
```

Primary state indicating the mouse is over the region.

**See Also:** Constant Field Values

- PRESSED

```java
static final int PRESSED
```

Primary state indicating the region is in a pressed state. Pressed
does not necessarily mean the user has pressed the mouse button.

**See Also:** Constant Field Values

- DISABLED

```java
static final int DISABLED
```

Primary state indicating the region is not enabled.

**See Also:** Constant Field Values

- FOCUSED

```java
static final int FOCUSED
```

Indicates the region has focus.

**See Also:** Constant Field Values

- SELECTED

```java
static final int SELECTED
```

Indicates the region is selected.

**See Also:** Constant Field Values

- DEFAULT

```java
static final int DEFAULT
```

Indicates the region is the default. This is typically used for buttons
to indicate this button is somehow special.

**See Also:** Constant Field Values

Field Detail

- ENABLED

```java
static final int ENABLED
```

Primary state indicating the component is enabled.

**See Also:** Constant Field Values

- MOUSE_OVER

```java
static final int MOUSE_OVER
```

Primary state indicating the mouse is over the region.

**See Also:** Constant Field Values

- PRESSED

```java
static final int PRESSED
```

Primary state indicating the region is in a pressed state. Pressed
does not necessarily mean the user has pressed the mouse button.

**See Also:** Constant Field Values

- DISABLED

```java
static final int DISABLED
```

Primary state indicating the region is not enabled.

**See Also:** Constant Field Values

- FOCUSED

```java
static final int FOCUSED
```

Indicates the region has focus.

**See Also:** Constant Field Values

- SELECTED

```java
static final int SELECTED
```

Indicates the region is selected.

**See Also:** Constant Field Values

- DEFAULT

```java
static final int DEFAULT
```

Indicates the region is the default. This is typically used for buttons
to indicate this button is somehow special.

**See Also:** Constant Field Values

---

#### Field Detail

ENABLED

```java
static final int ENABLED
```

Primary state indicating the component is enabled.

**See Also:** Constant Field Values

---

#### ENABLED

static final int ENABLED

Primary state indicating the component is enabled.

MOUSE_OVER

```java
static final int MOUSE_OVER
```

Primary state indicating the mouse is over the region.

**See Also:** Constant Field Values

---

#### MOUSE_OVER

static final int MOUSE_OVER

Primary state indicating the mouse is over the region.

PRESSED

```java
static final int PRESSED
```

Primary state indicating the region is in a pressed state. Pressed
does not necessarily mean the user has pressed the mouse button.

**See Also:** Constant Field Values

---

#### PRESSED

static final int PRESSED

Primary state indicating the region is in a pressed state. Pressed
does not necessarily mean the user has pressed the mouse button.

DISABLED

```java
static final int DISABLED
```

Primary state indicating the region is not enabled.

**See Also:** Constant Field Values

---

#### DISABLED

static final int DISABLED

Primary state indicating the region is not enabled.

FOCUSED

```java
static final int FOCUSED
```

Indicates the region has focus.

**See Also:** Constant Field Values

---

#### FOCUSED

static final int FOCUSED

Indicates the region has focus.

SELECTED

```java
static final int SELECTED
```

Indicates the region is selected.

**See Also:** Constant Field Values

---

#### SELECTED

static final int SELECTED

Indicates the region is selected.

DEFAULT

```java
static final int DEFAULT
```

Indicates the region is the default. This is typically used for buttons
to indicate this button is somehow special.

**See Also:** Constant Field Values

---

#### DEFAULT

static final int DEFAULT

Indicates the region is the default. This is typically used for buttons
to indicate this button is somehow special.

---

