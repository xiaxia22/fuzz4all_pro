# Interface ColorSelectionModel

**Source:** `java.desktop\javax\swing\colorchooser\ColorSelectionModel.html`

### Class Description

```java
public interface
ColorSelectionModel
```

A model that supports selecting a

Color

.

**All Known Implementing Classes:** DefaultColorSelectionModel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Color
getSelectedColor()

Returns the selected

Color

which should be
non-

null

.

**Returns:**
- the selected

Color

**See Also:**
- setSelectedColor(java.awt.Color)

---

#### void setSelectedColor​(
Color
color)

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color.

**Parameters:**
- color

- the new

Color

**See Also:**
- getSelectedColor()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### void addChangeListener​(
ChangeListener
listener)

Adds

listener

as a listener to changes in the model.

**Parameters:**
- listener

- the

ChangeListener

to be added

---

#### void removeChangeListener​(
ChangeListener
listener)

Removes

listener

as a listener to changes in the model.

**Parameters:**
- listener

- the

ChangeListener

to be removed

---

### Additional Sections

#### Interface ColorSelectionModel

**All Known Implementing Classes:** DefaultColorSelectionModel

```java
public interface
ColorSelectionModel
```

A model that supports selecting a

Color

.

**See Also:** Color

public interface

ColorSelectionModel

A model that supports selecting a

Color

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

Color

getSelectedColor

()

Returns the selected

Color

which should be
non-

null

.

void

removeChangeListener

​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

void

setSelectedColor

​(

Color

color)

Sets the selected color to

color

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addChangeListener

​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

Color

getSelectedColor

()

Returns the selected

Color

which should be
non-

null

.

void

removeChangeListener

​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

void

setSelectedColor

​(

Color

color)

Sets the selected color to

color

.

---

#### Method Summary

Adds

listener

as a listener to changes in the model.

Returns the selected

Color

which should be
non-

null

.

Removes

listener

as a listener to changes in the model.

Sets the selected color to

color

.

============ METHOD DETAIL ==========

- Method Detail

- getSelectedColor

```java
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Returns:** the selected

Color
**See Also:** setSelectedColor(java.awt.Color)

- setSelectedColor

```java
void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color.

**Parameters:** color

- the new

Color
**See Also:** getSelectedColor()

,

addChangeListener(javax.swing.event.ChangeListener)

- addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be added

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be removed

Method Detail

- getSelectedColor

```java
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Returns:** the selected

Color
**See Also:** setSelectedColor(java.awt.Color)

- setSelectedColor

```java
void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color.

**Parameters:** color

- the new

Color
**See Also:** getSelectedColor()

,

addChangeListener(javax.swing.event.ChangeListener)

- addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be added

- removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be removed

---

#### Method Detail

getSelectedColor

```java
Color
getSelectedColor()
```

Returns the selected

Color

which should be
non-

null

.

**Returns:** the selected

Color
**See Also:** setSelectedColor(java.awt.Color)

---

#### getSelectedColor

Color

getSelectedColor()

Returns the selected

Color

which should be
non-

null

.

setSelectedColor

```java
void setSelectedColor​(
Color
color)
```

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color.

**Parameters:** color

- the new

Color
**See Also:** getSelectedColor()

,

addChangeListener(javax.swing.event.ChangeListener)

---

#### setSelectedColor

void setSelectedColor​(

Color

color)

Sets the selected color to

color

.
Note that setting the color to

null

is undefined and may have unpredictable results.
This method fires a state changed event if it sets the
current color to a new non-

null

color.

addChangeListener

```java
void addChangeListener​(
ChangeListener
listener)
```

Adds

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be added

---

#### addChangeListener

void addChangeListener​(

ChangeListener

listener)

Adds

listener

as a listener to changes in the model.

removeChangeListener

```java
void removeChangeListener​(
ChangeListener
listener)
```

Removes

listener

as a listener to changes in the model.

**Parameters:** listener

- the

ChangeListener

to be removed

---

#### removeChangeListener

void removeChangeListener​(

ChangeListener

listener)

Removes

listener

as a listener to changes in the model.

---

