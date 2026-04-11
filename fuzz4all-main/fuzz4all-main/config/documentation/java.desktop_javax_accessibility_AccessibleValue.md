# Interface AccessibleValue

**Source:** `java.desktop\javax\accessibility\AccessibleValue.html`

### Class Description

```java
public interface
AccessibleValue
```

The

AccessibleValue

interface should be supported by any object that
supports a numerical value (e.g., a scroll bar). This interface provides the
standard mechanism for an assistive technology to determine and set the
numerical value as well as get the minimum and maximum values. Applications
can determine if an object supports the

AccessibleValue

interface by
first obtaining its

AccessibleContext

(see

Accessible

) and
then calling the

AccessibleContext.getAccessibleValue()

method. If the
return value is not

null

, the object supports this interface.

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

Button.AccessibleAWTButton

,

Checkbox.AccessibleAWTCheckbox

,

CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JInternalFrame.AccessibleJInternalFrame

,

JInternalFrame.JDesktopIcon.AccessibleJDesktopIcon

,

JMenu.AccessibleJMenu

,

JMenuItem.AccessibleJMenuItem

,

JProgressBar.AccessibleJProgressBar

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JScrollBar.AccessibleJScrollBar

,

JSlider.AccessibleJSlider

,

JSpinner.AccessibleJSpinner

,

JSplitPane.AccessibleJSplitPane

,

JToggleButton.AccessibleJToggleButton

,

Menu.AccessibleAWTMenu

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

,

Scrollbar.AccessibleAWTScrollBar

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Number
getCurrentAccessibleValue()

Get the value of this object as a

Number

. If the value has not
been set, the return value will be

null

.

**Returns:**
- value of the object

**See Also:**
- setCurrentAccessibleValue(java.lang.Number)

---

#### boolean setCurrentAccessibleValue​(
Number
n)

Set the value of this object as a

Number

.

**Parameters:**
- n

- the number to use for the value

**Returns:**
- true

if the value was set; else

false

**See Also:**
- getCurrentAccessibleValue()

---

#### Number
getMinimumAccessibleValue()

Get the minimum value of this object as a

Number

.

**Returns:**
- minimum value of the object;

null

if this object does not
have a minimum value

**See Also:**
- getMaximumAccessibleValue()

---

#### Number
getMaximumAccessibleValue()

Get the maximum value of this object as a

Number

.

**Returns:**
- maximum value of the object;

null

if this object does not
have a maximum value

**See Also:**
- getMinimumAccessibleValue()

---

### Additional Sections

#### Interface AccessibleValue

**All Known Implementing Classes:** AbstractButton.AccessibleAbstractButton

,

Button.AccessibleAWTButton

,

Checkbox.AccessibleAWTCheckbox

,

CheckboxMenuItem.AccessibleAWTCheckboxMenuItem

,

JButton.AccessibleJButton

,

JCheckBox.AccessibleJCheckBox

,

JCheckBoxMenuItem.AccessibleJCheckBoxMenuItem

,

JInternalFrame.AccessibleJInternalFrame

,

JInternalFrame.JDesktopIcon.AccessibleJDesktopIcon

,

JMenu.AccessibleJMenu

,

JMenuItem.AccessibleJMenuItem

,

JProgressBar.AccessibleJProgressBar

,

JRadioButton.AccessibleJRadioButton

,

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

,

JScrollBar.AccessibleJScrollBar

,

JSlider.AccessibleJSlider

,

JSpinner.AccessibleJSpinner

,

JSplitPane.AccessibleJSplitPane

,

JToggleButton.AccessibleJToggleButton

,

Menu.AccessibleAWTMenu

,

MenuItem.AccessibleAWTMenuItem

,

PopupMenu.AccessibleAWTPopupMenu

,

Scrollbar.AccessibleAWTScrollBar

```java
public interface
AccessibleValue
```

The

AccessibleValue

interface should be supported by any object that
supports a numerical value (e.g., a scroll bar). This interface provides the
standard mechanism for an assistive technology to determine and set the
numerical value as well as get the minimum and maximum values. Applications
can determine if an object supports the

AccessibleValue

interface by
first obtaining its

AccessibleContext

(see

Accessible

) and
then calling the

AccessibleContext.getAccessibleValue()

method. If the
return value is not

null

, the object supports this interface.

**See Also:** Accessible

,

Accessible.getAccessibleContext()

,

AccessibleContext

,

AccessibleContext.getAccessibleValue()

public interface

AccessibleValue

The

AccessibleValue

interface should be supported by any object that
supports a numerical value (e.g., a scroll bar). This interface provides the
standard mechanism for an assistive technology to determine and set the
numerical value as well as get the minimum and maximum values. Applications
can determine if an object supports the

AccessibleValue

interface by
first obtaining its

AccessibleContext

(see

Accessible

) and
then calling the

AccessibleContext.getAccessibleValue()

method. If the
return value is not

null

, the object supports this interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Number

getCurrentAccessibleValue

()

Get the value of this object as a

Number

.

Number

getMaximumAccessibleValue

()

Get the maximum value of this object as a

Number

.

Number

getMinimumAccessibleValue

()

Get the minimum value of this object as a

Number

.

boolean

setCurrentAccessibleValue

​(

Number

n)

Set the value of this object as a

Number

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Number

getCurrentAccessibleValue

()

Get the value of this object as a

Number

.

Number

getMaximumAccessibleValue

()

Get the maximum value of this object as a

Number

.

Number

getMinimumAccessibleValue

()

Get the minimum value of this object as a

Number

.

boolean

setCurrentAccessibleValue

​(

Number

n)

Set the value of this object as a

Number

.

---

#### Method Summary

Get the value of this object as a

Number

.

Get the maximum value of this object as a

Number

.

Get the minimum value of this object as a

Number

.

Set the value of this object as a

Number

.

============ METHOD DETAIL ==========

- Method Detail

- getCurrentAccessibleValue

```java
Number
getCurrentAccessibleValue()
```

Get the value of this object as a

Number

. If the value has not
been set, the return value will be

null

.

**Returns:** value of the object
**See Also:** setCurrentAccessibleValue(java.lang.Number)

- setCurrentAccessibleValue

```java
boolean setCurrentAccessibleValue​(
Number
n)
```

Set the value of this object as a

Number

.

**Parameters:** n

- the number to use for the value
**Returns:** true

if the value was set; else

false
**See Also:** getCurrentAccessibleValue()

- getMinimumAccessibleValue

```java
Number
getMinimumAccessibleValue()
```

Get the minimum value of this object as a

Number

.

**Returns:** minimum value of the object;

null

if this object does not
have a minimum value
**See Also:** getMaximumAccessibleValue()

- getMaximumAccessibleValue

```java
Number
getMaximumAccessibleValue()
```

Get the maximum value of this object as a

Number

.

**Returns:** maximum value of the object;

null

if this object does not
have a maximum value
**See Also:** getMinimumAccessibleValue()

Method Detail

- getCurrentAccessibleValue

```java
Number
getCurrentAccessibleValue()
```

Get the value of this object as a

Number

. If the value has not
been set, the return value will be

null

.

**Returns:** value of the object
**See Also:** setCurrentAccessibleValue(java.lang.Number)

- setCurrentAccessibleValue

```java
boolean setCurrentAccessibleValue​(
Number
n)
```

Set the value of this object as a

Number

.

**Parameters:** n

- the number to use for the value
**Returns:** true

if the value was set; else

false
**See Also:** getCurrentAccessibleValue()

- getMinimumAccessibleValue

```java
Number
getMinimumAccessibleValue()
```

Get the minimum value of this object as a

Number

.

**Returns:** minimum value of the object;

null

if this object does not
have a minimum value
**See Also:** getMaximumAccessibleValue()

- getMaximumAccessibleValue

```java
Number
getMaximumAccessibleValue()
```

Get the maximum value of this object as a

Number

.

**Returns:** maximum value of the object;

null

if this object does not
have a maximum value
**See Also:** getMinimumAccessibleValue()

---

#### Method Detail

getCurrentAccessibleValue

```java
Number
getCurrentAccessibleValue()
```

Get the value of this object as a

Number

. If the value has not
been set, the return value will be

null

.

**Returns:** value of the object
**See Also:** setCurrentAccessibleValue(java.lang.Number)

---

#### getCurrentAccessibleValue

Number

getCurrentAccessibleValue()

Get the value of this object as a

Number

. If the value has not
been set, the return value will be

null

.

setCurrentAccessibleValue

```java
boolean setCurrentAccessibleValue​(
Number
n)
```

Set the value of this object as a

Number

.

**Parameters:** n

- the number to use for the value
**Returns:** true

if the value was set; else

false
**See Also:** getCurrentAccessibleValue()

---

#### setCurrentAccessibleValue

boolean setCurrentAccessibleValue​(

Number

n)

Set the value of this object as a

Number

.

getMinimumAccessibleValue

```java
Number
getMinimumAccessibleValue()
```

Get the minimum value of this object as a

Number

.

**Returns:** minimum value of the object;

null

if this object does not
have a minimum value
**See Also:** getMaximumAccessibleValue()

---

#### getMinimumAccessibleValue

Number

getMinimumAccessibleValue()

Get the minimum value of this object as a

Number

.

getMaximumAccessibleValue

```java
Number
getMaximumAccessibleValue()
```

Get the maximum value of this object as a

Number

.

**Returns:** maximum value of the object;

null

if this object does not
have a maximum value
**See Also:** getMinimumAccessibleValue()

---

#### getMaximumAccessibleValue

Number

getMaximumAccessibleValue()

Get the maximum value of this object as a

Number

.

---

